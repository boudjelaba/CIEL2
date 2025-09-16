
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
