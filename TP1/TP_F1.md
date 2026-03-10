# TP1 – Développement d’un service HTTP avec Flask

## Objectifs

* Comprendre ce qu’est un service réseau
* Identifier processus / port / interface
* Comprendre les codes HTTP principaux
* Utiliser `curl`
* Faire le lien application ↔ TCP

---

## 1. Préparation du projet

### 1.1. Important

> Après chaque modification du code :
>
> 1. Arrêter le serveur (`CTRL + C`)
> 2. Relancer : `python src/app.py`

### 1.2 Arborescence

Créer le dossier suivant :

```
TP_Flask_HTTP/
│
├── requirements.txt
└── src/
    └── app.py
```

### 1.3. Fichier `requirements.txt`

```text
Flask>=3.0.0
```

### 1.4. Fichier `src/app.py`

Créer `src/app.py` :

```python
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Bienvenue sur l'API Flask"

@app.route("/api/status")
def status():
    return jsonify({"status": "OK"})

@app.route("/api/user/<name>")
def user(name):
    return jsonify({
        "name": name,
        "role": "student"
    })

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
```

* `127.0.0.1` = localhost
* `5000` = port du service

### 1.5. Environnement virtuel et installation

```bash
cd TP_Flask_HTTP
python -m venv .venv
```

Activation :

Linux / Mac :

```bash
source .venv/bin/activate
```

Windows :

```bash
.venv\Scripts\activate
```

Installer les dépendances :

```bash
pip install -r requirements.txt
```

Attendu : installation sans erreur.

---

## 1. Lancement du service

Dans le terminal (avec `.venv` activé) :

```bash
python src/app.py
```

Vous devez voir :

```text
Running on http://127.0.0.1:5000
```

> Ne pas fermer ce terminal.

### 1.1. Tester avec le navigateur

Ouvrir un navigateur et aller sur :

```
http://127.0.0.1:5000
```

### 1.2. Tester avec `curl`

Ouvrir un **second terminal** (toujours dans le dossier du projet, avec `.venv` activé) :

```bash
curl http://127.0.0.1:5000
```

**Question 1**

Quelle méthode HTTP est utilisée par défaut ?

<details>
<summary><strong>Réponse</strong>
</summary>

**GET**

* Un navigateur envoie une requête GET lorsqu’on tape une URL.
* `curl` utilise GET par défaut.

</details>

### 1.3. Analyse du fonctionnement réseau

L'application est maintenant :

* Un **processus**
* Écoutant sur le **port TCP 5000**
* Sur l’adresse **127.0.0.1**

Afficher les ports ouverts :

**Linux / Mac :**

```bash
netstat -an | grep 5000
# Ou
ss -ltnp | grep 5000
```

**Windows :**

```bash
netstat -an | findstr 5000
```

**Questions**

1. Quel est le numéro de port ?
2. Quelle est l’adresse IP d’écoute ?
3. Quel processus écoute sur ce port ?

<details>
<summary><strong>Réponses</strong>
</summary>

| Élément    | Réponse   |
| ---------- | --------- |
| Port       | 5000      |
| Adresse IP | 127.0.0.1 |
| Processus  | python    |

Un service réseau =

```text
Processus + Port + Interface réseau
```

Si un des trois manque → pas de service accessible.

</details>

### 1.4. Codes HTTP

Tester :

```bash
curl -i http://127.0.0.1:5000
```

Repérer :

```
HTTP/1.1 200 OK
```

**Question**

Que signifie 200 ?

<details>
<summary><strong>Réponse</strong>
</summary>

Succès. La requête a été traitée correctement.

</details>

Tester une route inexistante :

```bash
curl -i http://127.0.0.1:5000/test
```

**Question**

Pourquoi obtient-on 404 ?

<details>
<summary><strong>Réponse</strong>
</summary>

La route demandée n’existe pas dans l’application.

404 = erreur **applicative**, ce n’est PAS une erreur réseau.

</details>

### 1.5. Route dynamique

Tester :

```bash
curl http://127.0.0.1:5000/api/user/Carnus
```

**Questions**

1. Donner l’URL complète.
2. Que représente `<name>` dans la route ?

<details>
<summary><strong>Réponses</strong>
</summary>

URL complète :

```text
http://127.0.0.1:5000/api/user/Carnus
```

`<name>` représente :

Un **paramètre dynamique** transmis à la fonction.

URL → traitement serveur → réponse

</details>

---

## Conclusion

Un service réseau repose sur :

```
Processus + Port + Interface réseau
```

---
