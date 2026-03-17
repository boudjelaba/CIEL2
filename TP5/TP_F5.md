# TP5 – Réseaux Docker et Analyse du trafic

## Contexte

Nous travaillons avec une application composée de **deux conteneurs Docker** :

* `flask_api` → API web
* `postgres_db` → base de données PostgreSQL

Ces conteneurs sont lancés avec **Docker Compose** et communiquent via des **réseaux Docker**.

## Objectifs

* lancer une application avec **Docker Compose**
* comprendre le fonctionnement des **réseaux Docker**
* expliquer comment **les conteneurs communiquent**
* comprendre pourquoi **une base de données n’est pas exposée**
* observer le trafic réseau avec **Wireshark** et **tcpdump**

### Rappel : technologies utilisées par Docker

Docker s’appuie sur plusieurs mécanismes du noyau Linux :

| Technologie   | Rôle                      |
| ------------- | ------------------------- |
| Namespaces    | isolation des processus   |
| cgroups       | limitation des ressources |
| Bridge réseau | communication interne     |
| NAT           | accès vers l’extérieur    |

Chaque conteneur possède :

* sa **propre interface réseau**
* une **adresse IP interne**
* sa **pile TCP/IP**

> Un conteneur **n’est pas une machine virtuelle**.

## Architecture de l’application

Application composée de deux services :

* une **API Flask**
* une **base de données PostgreSQL**

Architecture réseau :

```
                 HOST
           localhost:5000
                 │
        ┌────────┴────────┐
        │  réseau Docker  │
        │                 │
        │   flask_api     │
        │      │          │
        │   backend       │
        │      │          │
        │  postgres_db    │
        └─────────────────┘
```

Principe :

* l’API est **accessible depuis l’extérieur**
* la base de données est **accessible uniquement depuis l’API**

## Arborescence du projet

```text
student_api_project/
│
├── src/
│   └── app/
│       ├── __init__.py
│       ├── routes.py
│       └── models.py
│
├── run.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .env
├── .dockerignore
└── .gitignore
```

## Configuration Docker

### docker-compose.yml

```yaml
version: "3.9" # A commenter pour les versions récentes de Docker

services:

  flask_api:
    build: .
    ports:
      - "5000:5000"

    environment:
      POSTGRES_USER: admin
      POSTGRES_PASSWORD: admin
      POSTGRES_DB: students_db

    depends_on:
      postgres_db:
        condition: service_healthy

    networks:
      - frontend
      - backend

  postgres_db:
    image: postgres:15

    environment:
      POSTGRES_USER: admin
      POSTGRES_PASSWORD: admin
      POSTGRES_DB: students_db

    volumes:
      - pgdata:/var/lib/postgresql/data

    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U admin -d students_db"]
      interval: 5s
      timeout: 5s
      retries: 5

    networks:
      - backend

volumes:
  pgdata:

networks:
  frontend:
  backend:
```

Deux réseaux sont utilisés :

| Réseau   | Rôle                           |
| -------- | ------------------------------ |
| frontend | accès externe à l’API          |
| backend  | communication interne API ↔ DB |

### Dockerfile

```dockerfile
FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY src/ /app/src/
COPY run.py /app/run.py

EXPOSE 5000

CMD ["python", "run.py"]
```

---

# Partie 0 – Lancer l'application

Lancer `Docker Desktop`

Dans un terminal (terminal A), démarrer les conteneurs :

```bash
docker compose down -v
docker compose up -d --build
```

Vérifier les services et l’état des des conteneurs :

```bash
docker ps
docker compose ps
```

Vous devez voir deux conteneurs :

```
SERVICE           STATUS
flask_api         Up ... (running)
postgres_db       Up ... (running)
```

Tester l’API :

Navigateur :

```
http://localhost:5000
```

ou

```bash
curl http://localhost:5000
```

---

# PARTIE 1 – Comprendre les réseaux Docker

```
                 HOST
           localhost:5000
                 │
        ┌────────┴────────┐
        │  docker bridge  │
        │                 │
     flask_api        postgres_db
     172.18.0.3       172.18.0.2
```

Lister les réseaux Docker :

```bash
docker network ls
```

Identifier les réseaux créés pour ce projet.

Exemple :

```
tp5_frontend
tp5_backend
```

## Inspection d'un réseau

Inspecter le réseau frontend :

```bash
docker network inspect tp5_frontend
# OU affichage avec couluers dans le terminal
docker network inspect tp5_frontend | jq
# OU rediriger la sortie vers un fichier
docker network inspect tp5_frontend > frontend.json
```

Repérer les informations suivantes :

* Subnet
* Gateway
* conteneurs connectés
* adresses IP internes

Faire la même chose pour le réseau backend.

### Questions

1. Quel est le **Subnet** du réseau `frontend` ?
2. Quel est le **Subnet** du réseau `backend` ?
3. Quels conteneurs sont connectés à chaque réseau ?
4. Quelle **adresse IP interne** possède chaque conteneur ?

<details>
<summary><strong>Réponses</strong>
</summary>

**Subnet**

Exemple :

```json
"Subnet": "172.20.0.0/16"
```

→ Docker attribue une plage privée.

**Gateway**

Exemple :

```json
"Gateway": "172.20.0.1"
```

→ C’est l’IP du bridge Linux.

**Liste des conteneurs connectés**

* Backend :

    * flask_api
    * postgres_db

* Frontend :

    * flask_api uniquement

→ Chaque conteneur a :

* une IP interne
* une interface virtuelle (veth)
* un namespace réseau isolé

</details>

---

# PARTIE 2 – Comprendre les interfaces réseau

```bash
docker compose ps
```

Entrer dans le conteneur Flask (terminal A) :

```bash
docker compose exec flask_api bash
```

Installer quelques outils réseau :

Dans le conteneur (prompt `root@xxxxx:/app#`) :

```bash
apt update
apt install iproute2 iputils-ping -y
```

Afficher les interfaces réseau :

```bash
ip a
```

Observation :

Un conteneur connecté à plusieurs réseaux possède **plusieurs interfaces réseau**.

Exemple :

```
eth0
eth1
lo
```

| Interface   | Rôle           |
| ----------- | -------------- |
| eth0 / eth1 | réseaux Docker |
| lo          | loopback       |

Afficher la table de routage du conteneur :

```bash
ip route
```

Exemple :

```
default via 172.19.0.1 dev eth0 
172.18.0.0/16 dev eth1 ...
172.19.0.0/16 dev eth0 ...
```

---

# PARTIE 3 – DNS interne Docker

Docker fournit un **serveur DNS interne**.

Dans le conteneur Flask (prompt `root@xxxxx:/app#`), tester la résolution du service PostgreSQL :

```bash
getent hosts postgres_db
```

Résultat :

```
172.xx.xx.xx postgres_db
```

Cela signifie que les conteneurs peuvent communiquer avec :

```
nom_du_service
```

au lieu d’utiliser une adresse IP.

---

# PARTIE 4 – Communication entre conteneurs

Depuis le conteneur Flask (prompt `root@xxxxx:/app#`) :

```bash
ping postgres_db
```

Arrêter après quelques paquets :

```
CTRL + C
```

Observation :

Les conteneurs communiquent via le **réseau Docker interne**.

### Question

Pourquoi cette communication fonctionne-t-elle ?

<details>
<summary><strong>Réponse</strong>
</summary>

Les deux conteneurs sont connectés au **même réseau Docker `backend`**.
Docker fournit un **DNS interne** qui traduit `postgres_db` en IP du conteneur PostgreSQL, ce qui permet la communication réseau.

Architecture :

```
flask_api  →  Bridge Docker  →  postgres_db
```

Lancer :

```bash
cat /etc/resolv.conf
```

</details>

---

# PARTIE 5 – Connexion PostgreSQL

Dans le conteneur Flask (prompt `root@xxxxx:/app#`)

Installer le client PostgreSQL :

```bash
apt install postgresql-client -y
```

Définir le mot de passe :

```bash
export PGPASSWORD=admin
```

Connexion :

```bash
psql -h postgres_db -U admin -d students_db
```

Si la connexion fonctionne :

```
students_db=#
```

Quitter :

```sql
\q
```

### Question

Pourquoi cette connexion fonctionne **alors que le port 5432 n’est pas exposé ?**

<details>
<summary><strong>Réponse</strong>
</summary>

Parce que la communication se fait **à l’intérieur du réseau Docker `backend`**.
L’exposition de port (`-p`) est uniquement nécessaire pour accéder au conteneur **depuis la machine hôte ou Internet**.

```
Client
   ↓
frontend network
   ↓
flask_api
   ↓
backend network
   ↓
postgres_db
```

</details>

Afficher les connexions TCP :

```bash
ss -tn | grep 5432
```

Exemple :

```
172.19.0.3:xxxxx → 172.19.0.2:5432
```

---

# Partie 6 - Analyse du trafic réseau entre conteneurs Docker

Les conteneurs Docker utilisent la **pile réseau Linux standard**.

Nous allons observer les échanges réseau entre :

* l’**hôte (host)**
* le conteneur **Flask**
* le conteneur **PostgreSQL**

## 6.1. Observation du trafic HTTP dans Wireshark

Objectif : observer le trafic HTTP entre l’hôte et l’API Flask.

1. Lancer **Wireshark** sur l’hôte.
2. Démarrer une capture sur l’interface :
   ```
   lo (loopback) ou any
   ```
   > *`lo` :* Docker redirige le trafic depuis `localhost:5000` → NAT docker → docker-proxy / iptables → conteneur.
3. Appliquer le filtre :
   ```
   tcp.port == 5000
   ```
   > Pour isoler le trafic HTTP de l’application Flask.
4. Dans un terminal, générer du trafic :
   ```bash
   curl -v http://localhost:5000
   ```
5. **Observation** :
   Le trafic HTTP passe par `localhost:5000` sur l’hôte, puis Docker le redirige vers le conteneur Flask (mappage de port, `-p 5000:5000`).

Dans Wireshark, observer :

* établissement de la connexion TCP
* requête HTTP
* réponse HTTP

## 6.2. Analyse ICMP avec tcpdump dans le conteneur

Objectif : Vérifier la connectivité réseau entre les conteneurs Flask et PostgreSQL via ICMP.

* Dans le conteneur Flask (`root@xxxxx:/app#`), installer `tcpdump` :
   ```bash
   apt update && apt install tcpdump -y
   ```

### Terminal B — Capture réseau

```bash
docker compose exec flask_api tcpdump -i any -nn -tttt icmp
```

| option   | utilité                       |
| -------- | ----------------------------- |
| `-i any` | capture toutes les interfaces |
| `-nn`    | évite résolution DNS          |
| `-tttt`  | affiche l’heure complète de chaque paquet |
| `icmp`   | filtre protocole                          |

### Terminal C — Génération du trafic

```bash
docker compose exec flask_api ping postgres_db
```

**Observation** :

- `ICMP echo request` : Envoi d’un ping.
- `ICMP echo reply` : Réponse du conteneur PostgreSQL.
> *Interprétation* : La communication réseau entre les conteneurs est fonctionnelle.

> **Arrêter la capture** : `CTRL + C` dans les terminaux B et C.

## 6.3. Observation du trafic PostgreSQL (TCP 5432)

Objectif : Capturer le handshake TCP et les échanges de données entre Flask et PostgreSQL.

### 6.3.1. Analyse directe dans le terminal

#### Terminal B — Capture réseau

```bash
docker compose exec flask_api tcpdump -i any -nn -vv -X port 5432
```

| option      | utilité                     |
| ----------- | --------------------------- |
| `-vv`       | plus de détails             |
| `-X`        | affiche payload hex + ASCII |
| `port 5432` | filtre le trafic PostgreSQL |

#### Terminal C — Connexion PostgreSQL

```bash
docker compose exec flask_api psql -h postgres_db -U admin -d students_db
```

Puis dans PostgreSQL, exécuter :

```sql
SELECT 1;
```

Quitter PostgreSQL :

```sql
\q
```

> **Observation** :
> 
> - Handshake TCP (`SYN`, `SYN ACK`, `ACK`).
> - Échanges de données PostgreSQL (requêtes/réponses PostgreSQL).

> **Arrêter la capture** : `CTRL + C` dans le terminal B.

### 6.3.2. Capture dans un fichier pour Wireshark

#### Terminal B — Capture réseau

```bash
# Écrire la capture dans un fichier
docker compose exec flask_api tcpdump -i any -nn port 5432 -w capture.pcap
# OU docker compose exec flask_api tcpdump -i any -nn port 5432 -w /tmp/capture.pcap
```

- `-w capture.pcap` : Sauvegarde la capture pour une analyse ultérieure dans Wireshark.

#### Terminal C — Connexion PostgreSQL

```bash
docker compose exec flask_api psql -h postgres_db -U admin -d students_db
```

Puis exécuter :

```sql
SELECT 1;
```

Quitter PostgreSQL :

```sql
\q
```

Arrêter `tcpdump` avec `CTRL + C` dans le terminal (B).

Copier le fichier sur l’hôte :

```bash
docker compose cp flask_api:/app/capture.pcap .
# OU docker compose cp flask_api:/tmp/capture.pcap .
```

Sur l’hôte :

- Ouvrir `capture.pcap` avec **Wireshark** pour analyser plus confortablement les paquets (filtre : `tcp.port == 5432`).
- Observer :

  ```
  SYN
  SYN ACK
  ACK
  ```

  Ce mécanisme est appelé :

  **Three-way handshake TCP**.


Dans le conteneur Flask (prompt `root@xxxxx:/app#`) (si besoin de vérifier) :

```bash
ls -lh capture.pcap        # vérifier la taille du fichier
tcpdump -r capture.pcap    # relire la capture en mode texte
```

## 6.4. Observation détaillée des requêtes SQL

Objectif : Analyser le contenu des requêtes SQL échangées entre Flask et PostgreSQL, soit directement dans tcpdump, soit via Wireshark (plus lisible).

Selon la configuration PostgreSQL, les requêtes SQL peuvent apparaître :

* **en clair**
* ou sous forme de **protocole PostgreSQL binaire**

### 4.1. Analyse directe avec tcpdump

#### Terminal B

```bash
docker compose exec flask_api tcpdump -i any -nn -tttt -s 0 -X port 5432
# OU -A (option moins pertinente ici ?)
```

| option | rôle                                |
| ------ | ----------------------------------- |
| `-s 0` | capture le paquet complet (payload) |

#### Terminal C

```bash
docker compose exec flask_api psql -h postgres_db -U admin -d students_db
```

Exécuter quelques requêtes :

```sql
SELECT 1;
SELECT NOW();
```

Quitter PostgreSQL :

```sql
\q
```

Puis arrêter la capture (terminal B) :

```
CTRL + C
```

Remarque : le protocole PostgreSQL est binaire, le contenu n’est pas aussi lisible qu’une requête HTTP, mais on peut identifier les échanges requête/réponse et la structure des paquets.

### 4.2. Capture pour analyse avec Wireshark

Une analyse est souvent plus facile dans **Wireshark**.

#### Terminal B — Capture

```bash
docker compose exec flask_api tcpdump -i any -s 0 -w postgres.pcap port 5432
```

Cette commande enregistre les paquets dans un fichier :

```
postgres.pcap
```

#### Terminal C — Génération du trafic

```bash
docker compose exec flask_api psql -h postgres_db -U admin -d students_db
```

Exécuter :

```sql
SELECT 1;
```

Quitter PostgreSQL :

```sql
\q
```

Puis arrêter la capture (terminal B) avec `CTRL + C`.

#### Copier le fichier de capture sur l’hôte

```bash
docker compose cp flask_api:/app/postgres.pcap .
```

Ouvrir **postgres.pcap** avec **Wireshark** et :

- Filtrer sur `tcp.port == 5432`.
- Reconstituer un flux TCP.
- Observer la séquence handshake TCP, authentification PostgreSQL, requête, réponse.

---

# PARTIE 7 – Isolation réseau

Depuis la machine hôte, couper la connexion au réseau backend :

```bash
docker compose ps
# Puis docker network disconnect tp5_backend <container_name>
docker network disconnect tp5_backend tp5-flask_api-1
# OU directement
docker network disconnect tp5_backend $(docker compose ps -q flask_api)
```

Dans le conteneur Flask (prompt `root@xxxxx:/app#`) Terminal A :

```bash
ping postgres_db
```

La communication échoue.

Reconnecter le réseau :

```bash
docker network connect tp5_backend tp5-flask_api-1
# OU
docker network connect tp5_backend $(docker compose ps -q flask_api)
```

Dans le conteneur Flask (prompt `root@xxxxx:/app#`) Terminal A :

```bash
ping postgres_db
```

La communication OK.

---

# PARTIE 8 – Isolation du système de fichiers (filesystem)

Entrer dans le conteneur (ou utiliser le Terminal A) :

```bash
docker compose exec flask_api bash
```

Créer un fichier :

```bash
touch test.txt
```

Vérifier :

```bash
ls
```

Sortir :

```bash
exit
```

Sur la machine hôte :

```bash
ls
```

Le fichier **n’existe pas**.

Chaque conteneur possède **son propre système de fichiers**.

---

## Arrêt des conteneurs

Quitter le conteneur Flask (prompt `root@xxxxx:/app#`) si ce n'est pas déjà fait :

```bash
exit
```

```bash
docker compose down
```

Vérifier :

```bash
docker ps
```

Aucun conteneur ne doit rester actif.

```bash
docker compose down -v
```

---

## Synthèse

Docker s’appuie sur plusieurs mécanismes Linux.

| mécanisme    | rôle                    |
| ------------ | ----------------------- |
| namespaces   | isolation               |
| veth         | interfaces virtuelles   |
| bridge Linux | commutation             |
| iptables     | NAT                     |
| DNS interne  | résolution des services |

Un conteneur fonctionne donc comme **une mini machine isolée**.

---
