# TP 4 - Déployer une API professionnelle multi-conteneurs

## Objectifs

* Déployer une API multi-conteneurs avec Docker Compose
* Comprendre le réseau interne Docker
* Utiliser des variables d’environnement
* Mettre en place un volume PostgreSQL persistant
* Tester une API avec `curl`
* Comprendre des notions de sécurité d’infrastructure

## Contexte professionnel

Vous devez déployer une API de gestion d’étudiants.

Contraintes :

* Exposer un service HTTP
* Stocker les données en base PostgreSQL
* Fonctionner dans un environnement isolé
* Être redémarrable sans perte de données
* Sécuriser l’architecture réseau

Architecture cible :

```
Client
   ↓
Service HTTP (API Flask)
   ↓
Base PostgreSQL
   ↓
Volume persistant
   ↓
Réseau Docker isolé
```
---

## 1. Structure du projet

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
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── .dockerignore
└── .gitignore
```

### `requirements.txt`

```text
Flask==3.0.0
Flask-SQLAlchemy==3.1.1
psycopg2-binary==2.9.9
SQLAlchemy==2.0.20
```

### `src/app/__init__.py`

```python
import os
from flask import Flask
from .routes import student_bp
from .models import db

def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = (
        f"postgresql://{os.getenv('POSTGRES_USER')}:{os.getenv('POSTGRES_PASSWORD')}"
        f"@postgres_db:5432/{os.getenv('POSTGRES_DB')}"
    )

    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)
    app.register_blueprint(student_bp)

    @app.route("/")
    def home():
        return {"status": "ok", "message": "API Student Running"}

    with app.app_context():
        db.create_all()
        # En projet, on utiliserait Flask-Migrate.

    return app
```

### `src/app/routes.py`

```python
from flask import Blueprint, jsonify, request
from .models import db, Student

student_bp = Blueprint("student_bp", __name__, url_prefix="/students")

@student_bp.route("", methods=["GET"])
def list_students():
    students = Student.query.all()
    result = [
        {"id": s.id, "name": s.name, "email": s.email}
        for s in students
    ]
    return jsonify(result)

@student_bp.route("", methods=["POST"])
def add_student():
    data = request.get_json()

    if not data or not data.get("name") or not data.get("email"):
        return jsonify({"error": "Invalid data"}), 400

    student = Student(name=data["name"], email=data["email"])
    db.session.add(student)
    db.session.commit()

    return jsonify({"message": "Student added"}), 201
```

### `src/app/models.py`

```python
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Student(db.Model):
    __tablename__ = "students"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), nullable=False)
```

### `run.py`

```python
import os
from src.app import create_app

app = create_app()

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=os.getenv("FLASK_DEBUG", "False") == "True"
    )
```

### `Dockerfile`

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

### `docker-compose.yml`

```yaml
version: "3.9" # Commenter cette ligne pour les versions récentes de Docker

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
    depends_on:
      postgres_db:
        condition: service_healthy

  postgres_db:
    image: postgres:15
    container_name: postgres_db
    environment:
      POSTGRES_USER: admin
      POSTGRES_PASSWORD: admin
      POSTGRES_DB: students_db
    volumes:
      - pgdata:/var/lib/postgresql/data
    # Exposé uniquement pour test local
    ports:
      - "5432:5432"
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U admin -d students_db"]
      interval: 5s
      timeout: 5s
      retries: 5

volumes:
  pgdata:
```

### `.dockerignore`

```
.venv
__pycache__
.git
.gitignore
logs
```

### `.gitignore`

```
.venv
__pycache__
*.pyc
*.pyo
*.pyd
*.sqlite3
*.log
```

---

## 2. Environnement virtuel (Optionnel) 

Créer un environnement Python local pour tester le projet hors Docker :

```bash
python -m venv .venv
source .venv/bin/activate   # Linux/macOS
.venv\Scripts\activate      # Windows

# Installer les dépendances du projet
pip install -r requirements.txt
```

* `flask` → pour l’API web
* `psycopg2-binary` → pour se connecter à PostgreSQL

> Vérifier :
>
> ```bash
> pip list | grep -E "Flask|psycopg2"
> ```

## 3. Lancement

Ouvrir `Docker Desktop`

Vérifications Docker / Compose (dans un terminal) :

```bash
docker info
```

* Construire l’image et lancer les conteneurs test (Lancer Docker / PostgreSQL / Flask) :

```bash
docker compose down -v
docker compose up --build
```

* Vérifier les conteneurs actifs :

```bash
docker ps
```

* Vérifier la persistance de PostgreSQL (volume `pgdata`) :

```bash
docker volume ls
```

* API Flask disponible sur `http://localhost:5000`
* Endpoint étudiants : `http://localhost:5000/students`
* PostgreSQL : port `5432` (local pour test)

## 4. Test API :

### Vérifier API

```bash
curl http://localhost:5000
# Renvoie : {"status": "ok", "message": "API Student Running"}
```

### Lister étudiants

```bash
curl http://localhost:5000/students
# Renvoie : [] renvoie un tableau JSON (vide au départ)
```

### Ajouter étudiant

```bash
curl -X POST http://localhost:5000/students \
     -H "Content-Type: application/json" \
     -d '{"name":"Carnus","email":"lycee@carnus.fr"}'
```

* Vérifier ajout :

```bash
curl http://localhost:5000/students
# [{"id":1,"name":"Carnus","email":"lycee@carnus.fr"}]
```

* **Vérifier les logs et volumes PostgreSQL**

    ```bash
    docker logs flask_api
    docker logs postgres_db
    ```

* **Tester la base (Vérifier PostgreSQL)**

    * Se connecter depuis un autre conteneur :

    ```bash
    docker exec -it postgres_db psql -U admin -d students_db
    ```

        * Tester les commandes suivantes :
            * `\dt` : pour voir les tables
            * `SELECT * FROM students;` : pour voir les enregistrements
            * ou une autre commande

## 5. Exercice : Persistance

1. Ajouter un étudiant

    ```bash
    curl -X POST http://localhost:5000/students \
         -H "Content-Type: application/json" \
         -d '{"name":"Exercice","email":"exercice@carnus.fr"}'
    ```

    ```bash
    curl http://localhost:5000/students
    ```

2. Faire :

    ```bash
    docker compose down # Arrêter SANS supprimer le volume
    docker compose up   # Relancer
    ```

3. Vérifier que l’étudiant existe toujours. Expliquer pourquoi.

    ```bash
    curl http://localhost:5000/students
    ```

4. Vérifier que le volume existe

    ```bash
    docker volume ls
    ```

    Résultat :

    ```text
    tp4_pgdata
    ```

    Inspecter :

    ```bash
    docker volume inspect tp4_pgdata
    ```

## 6. Remarques

* `.gitignore` pour `.venv`, fichiers logs
* `.dockerignore` pour `.venv`, `__pycache__`
* Volumes pour persistance PostgreSQL
* Variables d’environnement pour credentials

```bash
docker compose down -v
```

> Le `-v` supprime le volume `pgdata`.

* volume supprimé
* base recréée
* table vide

---

## 7. Notions sécurité

1. Pourquoi ne pas exposer le port PostgreSQL à l’internet public ?
2. Que se passe-t-il si l’on change `0.0.0.0` pour `127.0.0.1` dans Flask ?
3. Quel est l’intérêt d’un volume pour la DB ?

<details>
<summary><strong>Réponses</strong>
</summary>

* Exposition publique → risque de piratage
* `127.0.0.1` → service accessible seulement localement
* Volume → persistance des données
* 
</details>

---
