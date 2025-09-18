
```cmd
git config --global color.diff auto
git config --global color.status auto
git config --global color.branch auto
```


# CIEL2



# ⬇️ <cite><font color="(0,68,88)">CIEL-2 : Informatique</font></cite>

<a href="https://carnus.fr"><img src="https://img.shields.io/badge/Carnus%20Enseignement Supérieur-F2A900?style=for-the-badge" /></a>
<a href="https://carnus.fr"><img src="https://img.shields.io/badge/BTS%20CIEL-2962FF?style=for-the-badge" /></a>

    Professeur - K. B.

### Contact : [Mail](mailto:lycee@carnus.fr)
---




# Étapes du TP

## Préparation matérielle

* Vérifier les Raspberry Pi à jour (avec accès réseau)
* Installer `requests` : `pip3 install requests`
* Installer Flask : `pip3 install flask`
* Code de base fourni

---

## 1. Lancer un mini serveur Flask de test

*1.1. Exécuter ce serveur Python `serveur.py` :*

```python
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/alerte", methods=["POST"])
def recevoir_alerte():
    data = request.get_json(silent=True)
    if data is None:
        return jsonify({"error": "Données JSON invalides"}), 400
    print("Alerte reçue :", data)
    print("Traitement de l'alerte...")
    return "", 200
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
```

Puis :

*1.2. Exécuter ce code Python simulant un appui sur un bouton `bouton_simu.py` :*

```python
import requests

print("Appuyez sur Entrée pour déclencher l’alerte (Ctrl+C pour quitter).")

try:
    while True:
        input(">>> ")
        print("ALERTE : Bouton pressé !")
        data = {"message": "Alerte déclenchée depuis bouton.py"}
        try:
            response = requests.post("http://127.0.0.1:5000/alerte", json=data)
            print("Réponse du serveur :", response.status_code, response.text)
        except Exception as e:
            print("Erreur lors de l'envoi :", e)
        print()
except KeyboardInterrupt:
    print("\nArrêt du programme.")
```

---
---


## Environnements virtuels Python sur Raspberry Pi

Utiliser des **environnements virtuels (venv)** est **la meilleure pratique** pour isoler les projets et éviter les problèmes de droits, de dépendances ou de conflits entre bibliothèques.

---

### Objectif

Créer un environnement Python isolé pour travailler avec `requests`, `flask`, etc., **sans interférer avec le système global**.

---

### Prérequis

Python 3 est préinstallé sur les Raspberry Pi. Assurez-vous que les paquets suivants sont là :

```bash
sudo apt update
sudo apt install python3 python3-venv python3-pip -y
```

*Remarques*

* Si le Raspberry Pi a **une installation propre** et **récente**, il est possible que ces paquets soient déjà présents.
* Pour **vérifier** :

```bash
python3 -m venv --help
```

Si cette commande fonctionne sans erreur, cela signifie que `python3-venv` est installé.

De même pour `pip` :

```bash
pip3 --version
```

Cela permettra de confirmer si `pip` est déjà installé.

---

### Création d’un environnement virtuel

1. **Se placer dans le dossier du projet** :

   ```bash
   mkdir ~/monprojet
   cd ~/monprojet
   ```

2. **Créer un environnement virtuel** :

   ```bash
   python3 -m venv env
   ```

   Cela crée un sous-dossier `env/` contenant une installation isolée de Python.

3. **Activer l’environnement** :

   ```bash
   source env/bin/activate
   ```

   Le prompt change, par exemple : `(env) pi@raspberrypi:~/monprojet $`

---

## Installer les bibliothèques (dans le venv)

Par exemple :

```bash
pip install flask requests
```

Les paquets sont installés **localement dans le projet**, pas globalement.

---

## Pour sortir de l’environnement :

```bash
deactivate
```

Cela revient au Python système, sans rien casser.

---

## Vérifier que tout fonctionne

Test avec Flask :

```python
# app.py
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Bonjour depuis Flask sur le RPi !"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
```

Puis lancer :

```bash
python app.py
```

Et accéder depuis un navigateur à l’adresse :
`http://<ip-du-RPi>:5000`

---

## Notes : pour éviter les erreurs fréquentes

* Toujours **activer le venv** avant de faire `pip install` ou `python`.
* Ajouter un fichier `requirements.txt` au projet :

```bash
pip freeze > requirements.txt
```

> On reviendra sur ça dans les prochains cours

Et pour restaurer sur un autre RPi ou utilisateur :

```bash
pip install -r requirements.txt
```

---
# Suppression d'utilisateurs sur RPI

## Remarques (importantes)

* Ne **supprimez jamais l'utilisateur root**.
* Ne supprimez pas l'utilisateur avec lequel vous êtes connecté avant d’avoir **créé et testé un nouveau compte avec droits sudo**.

---

## Étapes pour supprimer tous les utilisateurs sauf `root`

### 1. Créer un nouvel utilisateur

Connectez-vous avec l’utilisateur actuel (par défaut c’est souvent `pi`), puis dans le terminal :

```bash
sudo adduser ciel
```

Suivez les instructions pour lui attribuer un mot de passe.

### 2. Ajouter l'utilisateur au groupe sudo (pour avoir les droits administrateurs)

```bash
sudo usermod -aG sudo ciel
```

> Vous pouvez vérifier avec `groups ciel`.

---

### 3. Se connecter avec le nouvel utilisateur

Avant de supprimer les autres, **ouvrez une nouvelle session (terminal ou SSH)** avec le nouvel utilisateur pour vérifier que tout fonctionne :

```bash
su - ciel
```

Vérifiez que vous avez bien les droits sudo :

```bash
sudo whoami
```

Cela doit renvoyer :

```bash
root
```

---

### 4. Lister tous les utilisateurs normaux

Commande pour lister tous les comptes avec UID ≥ 1000 (utilisateurs normaux) :

```bash
awk -F: '$3 >= 1000 && $1 != "nobody" {print $1}' /etc/passwd
```

Cela vous donnera une liste comme :

```text
pi
autreutilisateur
ciel
```

---

### 5. Supprimer les autres utilisateurs

**Ne supprimez pas** `ciel`. Par exemple, pour supprimer l’utilisateur `pi` :

```bash
sudo deluser --remove-home pi
```

Faites de même pour chaque utilisateur à supprimer (sauf votre nouveau compte).

---
---
