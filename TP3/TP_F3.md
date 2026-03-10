# TP3 – Conteneurisation avec Docker

On exécute maintenant le même service dans un conteneur.

> Reprendre les fichiers `src/app.py` et `requirements.txt` du TP2.

---

## Partie 1 – Docker : Image et Conteneur

Créer le fichier `Dockerfile` :

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY src/ ./src/

EXPOSE 5000

CMD ["python", "src/app.py"]
```

### 1.1. Construire l’image Docker

> Ouvrir `Docker Desktop` 

* Taper la commande suivante dans le terminal du projet :

```bash
docker build -t flask-api .
```

Vérifier :

```bash
docker images
```

Vous devez voir l’image `flask-api`.

**Question**

Différence entre :

* Image Docker
* Conteneur Docker

<details>
<summary><strong>Réponse</strong>
</summary>

| Image     | Modèle statique               |
| --------- | ----------------------------- |
| Conteneur | Instance en cours d’exécution |

</details>

**Vérifier dans Docker Desktop**

1. Dans Docker Desktop, ouvrir l'Onglet **Images**.
2. Vérifier que `flask-api` apparaît.

### 1.2 Vérifier dans Docker Desktop

1. Dans Docker Desktop, ouvrir l'Onglet **Images**.
2. Vérifier que `flask-api` apparaît.

## Partie 2 – Lancer un conteneur

```bash
docker run -p 5000:5000 flask-api
```

Dans un autre terminal :

```bash
curl http://localhost:5000/api/status
```

**Observer dans Docker Desktop**

Onglet **Containers** → conteneur basé sur `flask-api` :

- le **port mapping** (5000 → 5000),
- le **Container ID**.

**Question**

Où s’exécute maintenant le processus Python ?

* Sur l’hôte ?
* Dans une VM ?
* Dans un conteneur ?

<details>
<summary><strong>Réponse</strong>
</summary>

Dans un **conteneur**,
lui-même isolé via namespaces Linux.

> Ce n’est PAS une VM complète.

```text
Navigateur
    │
    ▼
Machine hôte
Port 5000
    │
    │ NAT Docker
    ▼
Conteneur
Port 5000
    │
    ▼
Processus Flask
```

</details>

### Tester une connexion vers un port fermé

```bash
curl http://127.0.0.1:5999
```

Quel message apparaît ?

## Partie 3 – Mapping de port

Arrêter le conteneur :

```bash
docker ps
# Puis
docker stop <container_id>
```

Relancer l’API dans un conteneur avec un port externe différent :

```bash
docker run -p 8080:5000 flask-api
```

Tester :

```bash
curl http://localhost:8080
```

Puis tester :

```bash
curl http://localhost:5000
```

### Questions

1. Pourquoi utilise-t-on 8080 dans l’URL ?
2. Le service écoute-t-il toujours sur 5000 dans le conteneur ?

<details>
<summary><strong>Réponse</strong>
</summary>

Parce que :

* 8080 = port exposé sur la machine hôte
* 5000 = port interne du conteneur

✖️ Non. Flask écoute toujours sur 5000 dans le conteneur.

</details>

### Observer avec Wireshark

Filtre :

```text
tcp.port == 8080
```

Générer du trafic :

Dans le terminal

```bash
curl http://localhost:8080
```

**Questions**

1.  Dans Wireshark (filtre `tcp.port == 8080`), quel port voyez-vous côté machine ?
2.  Le port interne de Flask a-t-il changé ? 

   * Tester `python src/app.py` puis ouvrir `http://127.0.0.1:5000`
   * Ou vérifier dans l'onglet `Containers` de `Docker Desktop`

<details>
<summary><strong>Réponses</strong>
</summary>

1.  Dans Wireshark (machine hôte), on voit :

    → Port destination = **8080** côté machine.

2.  Le port interne Flask change-t-il ?

    → Non

    Le port interne Flask reste 5000 dans le conteneur.

    Il n’a jamais changé. Seul le port externe change.

```
Navigateur
    │
    ▼
Machine hôte
Port 8080
    │
    │ NAT Docker
    ▼
Conteneur
Port 5000
    │
    ▼
Flask
```

</details>

---

### Identifier l’IP interne du conteneur

Dans un 2ème terminal :

```bash
docker ps
# Puis
docker inspect <container_id>
```

Rechercher :

```
"IPAddress": "172.17.0.X"
```

### Table réseau Docker

Docker crée automatiquement :

* un réseau virtuel nommé `bridge`
* une interface virtuelle
* un sous-réseau interne

Vérifier :

```bash
docker network ls
```

Vous devez voir :

```
bridge
host
none
```

Inspecter le réseau bridge (réseau virtuel interne Docker) :

```bash
docker network inspect bridge
```

Vous verrez :

* le subnet (ex : 172.17.0.0/16)
* la passerelle (ex : 172.17.0.1)
* les conteneurs connectés 
    * IP privée du conteneur (ex : 172.17.0.X)

---

# Partie 4 – 127.0.0.1 dans un conteneur

```bash
docker ps
# Puis
docker stop <container_id>
```

Modifier `src/app.py` :

```python
app.run(host="127.0.0.1", port=5000)
```

Rebuild l’image :

```bash
docker build -t flask-api .
```

Relancer :

```bash
docker run -p 5000:5000 flask-api
```

Tester :

```bash
curl http://localhost:5000
```

### Question

Pourquoi cela ne fonctionne-t-il plus ?

Expliquer ce que représente 127.0.0.1 dans un conteneur.

<details>
<summary><strong>Réponse</strong>
</summary>

Dans un conteneur :

```text
127.0.0.1 = loopback du conteneur
```

Donc :

* Le service écoute uniquement à l’intérieur
* Docker ne peut pas rediriger vers lui

</details>

### Règle fondamentale

Dans un conteneur, toujours utiliser :

```python
host="0.0.0.0"
```

Sinon le service est inaccessible.

**Arrêter avant correction**

```bash
docker ps
# Puis
docker stop <container_id>
```

Corriger `src/app.py` en remettant :

```python
app.run(host="0.0.0.0", port=5000)
```

## Partie 5 – Volume Docker

Modifier `src/app.py` pour écrire un log simple :

```python
from flask import Flask, jsonify
from datetime import datetime
import logging
import os

# Création du dossier logs
os.makedirs("/app/logs", exist_ok=True)

# On écrit dans /app/logs
logging.basicConfig(
    filename="/app/logs/log.txt",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)

app = Flask(__name__)

@app.route("/")
def home():
    logging.info("Route appelée")
    return jsonify({
        "message": "API Flask opérationnelle",
        "timestamp": datetime.now().isoformat()
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
```

Rebuild :

```bash
docker build -t flask-api .
```

Créer le dossier local :

```bash
mkdir logs
```

Lancer avec volume :

```bash
docker run -p 5000:5000 -v $(pwd)/logs:/app/logs flask-api
```

Appeler plusieurs fois l’API (4 ou 5 fois) :

```bash
curl http://localhost:5000
```

Arrêter le conteneur.

```bash
docker ps
# Puis
docker stop <container_id>
```

Vérifier :

```bash
cat logs/log.txt
```

Ou ouvrir directement le fichier `logs/log.txt`

**Question**

Pourquoi le fichier log est-il toujours présent ?

<details>
<summary><strong>Réponse</strong>
</summary>

Car le dossier local est monté dans le conteneur.

Le volume :

* persiste les données
* sépare code et données

</details>

## Partie 6 – Deux conteneurs

Lancer 2 conteneurs :

```bash
docker run -p 8080:5000 flask-api
docker run -p 8081:5000 flask-api
```

Puis :

```bash
curl http://localhost:8080
curl http://localhost:8081
```

**Question**

Comment deux serveurs peuvent-ils utiliser le port 5000 en même temps ?

<details>
<summary><strong>Réponse</strong>
</summary>

Chaque conteneur possède :

* son propre namespace réseau
* son propre port 5000 interne

Les ports externes sont différents :

* 8080 → conteneur 1
* 8081 → conteneur 2

</details>

**Arrêter les deux conteneurs**

```bash
docker ps
# Puis
docker stop <container_id_1>
# Puis
docker stop <container_id_2>
```

## Synthèse finale à compléter

| Notion         | Définition |
| -------------- | ---------- |
| Service réseau |            |
| Image Docker   |            |
| Conteneur      |            |
| -p             |            |
| 127.0.0.1      |            |
| 0.0.0.0        |            |
| Volume Docker  |            |

<details>
<summary><strong>Réponses</strong>
</summary>

| Notion         | Définition correcte                             |
| -------------- | ----------------------------------------------- |
| Service réseau | Processus écoutant sur un port et une interface |
| Image Docker   | Modèle immuable servant à créer des conteneurs  |
| Conteneur      | Instance isolée d’une image en exécution        |
| -p             | Règle de redirection de port (DNAT)             |
| 127.0.0.1      | Loopback local (relatif au namespace)           |
| 0.0.0.0        | Toutes les interfaces réseau                    |
| Volume         | Mécanisme de persistance des données            |

```
Image ≠ Conteneur ≠ VM
```

</details>

## Conclusion

* Un service réseau = processus + port + interface réseau
* HTTP repose sur TCP
* Docker isole processus et réseau
* Docker utilise du DNAT pour exposer un port
* Un conteneur n’est pas une VM
* Les données doivent être externalisées via des volumes

> Un conteneur n’est pas visible directement depuis l’extérieur.
> Docker crée un réseau privé.
> Le mapping de port (-p) agit comme un routeur miniature.
> Le volume agit comme un disque dur externe branché au conteneur.

---
