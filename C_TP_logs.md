# TP – Utiliser les logs en Python

## Objectifs

* Comprendre **à quoi servent les logs**
* Remplacer des `print()` par des logs adaptés
* Utiliser les niveaux `INFO` et `ERROR`
* Écrire des logs dans un **fichier**
* Distinguer **affichage utilisateur** et **suivi développeur**

## 1. Les logs

* `print()` → communication avec l’utilisateur
* `logging` → suivi technique pour le développeur

Les logs permettent de :

* suivre l’exécution d’un programme
* détecter les erreurs
* conserver une trace des événements
* diagnostiquer un problème sans modifier l’affichage utilisateur

## 2. Les niveaux de logs

| Niveau    | Utilisation                              |
| --------- | ---------------------------------------- |
| `DEBUG`   | Détails techniques (pour le développeur) |
| `INFO`    | Fonctionnement normal du programme       |
| `WARNING` | Situation anormale mais non bloquante    |
| `ERROR`   | Erreur empêchant une action              |
| `CRITICAL` | Erreur grave, programme inutilisable    |

>Par défaut, **seuls WARNING et plus sont affichés**.
>
> Dans ce TP, nous utiliserons principalement `INFO` et `ERROR`.

## 3. Configuration des logs

```python
import logging

logging.basicConfig(
    filename="programme.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.debug("Message debug") # Ne sera pas inclus dans le fichier
logging.info("Message info")
logging.warning("Message warning")
logging.error("Message erreur")
logging.critical("Message critique")
```

Cette configuration :

* écrit les logs dans un fichier (`programme.log`)
* ajoute la date et l’heure
* affiche les messages de niveau `INFO` et supérieurs (`ERROR` inclus)

> `basicConfig()` doit être appelé **une seule fois**, au début du programme.

> Sans `filename=`, les logs s’affichent dans la console.
> Avec `filename=`, ils sont écrits dans un fichier.

---

## Exercice 1 – Remplacer des `print()`

Transformer ce code pour utiliser des logs :

```python
print("Programme démarré")
print("Calcul en cours")
print("Erreur : valeur incorrecte")
```

### Attendu

* `INFO` pour les messages normaux
* `ERROR` pour l’erreur

<details open>
<summary>Corrigé</summary>

```python
import logging

logging.basicConfig(level=logging.INFO)

logging.info("Programme démarré")
logging.info("Calcul en cours")
logging.error("Valeur incorrecte")
```

> Ici les logs sont affichés dans la console car aucun fichier n’est précisé.

</details>

---

## Exercice 2 – Choisir le bon niveau

Quel niveau utiliser ?

1. Programme lancé
2. Résultat calculé
3. Division par zéro

<details open>
<summary>Réponses</summary>

1. `INFO`
2. `INFO`
3. `ERROR`

</details>

---

# TP – Partie 1 : Mini-calculatrice avec logs

## Objectif

Ajouter des **logs** à un programme existant **sans modifier son comportement utilisateur**.

* L’utilisateur ne doit voir que les `print()` des résultats.
* Les logs servent uniquement au suivi interne.

## Code `calculatrice.py`

```python
import logging

logging.basicConfig(
    filename="calculatrice.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def addition(a, b):
    return a + b

def division(a, b):
    if b == 0:
        return None
    return a / b

x = float(input("Premier nombre : "))
y = float(input("Second nombre : "))

resultat_addition = addition(x, y)
print("Résultat de l'addition :", resultat_addition)

resultat_division = division(x, y)
if resultat_division is not None:
    print("Résultat de la division :", resultat_division)
else:
    print("Division impossible")
```

## Travail demandé

### 1. Ajouter des logs `INFO`

* au démarrage du programme
* lors de l’addition
* lors de la division
* à la fin du programme

### 2. Ajouter un log `ERROR`

* si une division par zéro est détectée

### 3. Règles importantes

* Pas de `print()` pour le suivi interne
* `print()` uniquement pour afficher les résultats
* Les logs doivent être écrits dans `calculatrice.log`

### Exemple de logs attendus

```
2026-02-10 14:10:02 - INFO - Démarrage du programme
2026-02-10 14:10:05 - INFO - Addition de 10.0 et 2.0
2026-02-10 14:10:05 - INFO - Division de 10.0 par 2.0
2026-02-10 14:10:05 - INFO - Fin du programme
```

<details open>
<summary> Corrigé </summary>

```python
import logging

logging.basicConfig(
    filename="calculatrice.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("Démarrage du programme")

def addition(a, b):
    logging.info(f"Addition de {a} et {b}")
    return a + b

def division(a, b):
    if b == 0:
        logging.error("Division par zéro")
        return None
    logging.info(f"Division de {a} par {b}")
    return a / b

x = float(input("Premier nombre : "))
y = float(input("Second nombre : "))

resultat_addition = addition(x, y)
print("Résultat de l'addition :", resultat_addition)

resultat_division = division(x, y)
if resultat_division is not None:
    print("Résultat de la division :", resultat_division)
else:
    print("Division impossible")

logging.info("Fin du programme")
```

</details>

## Conclusion

* `print()` → communication utilisateur
* `logging` → suivi technique
* les logs sont **indispensables en projet réel**
* ils facilitent le debug, la maintenance et le travail en équipe

---

# TP - Partie 2 : Versionner la calculatrice avec GitHub

## Objectifs

* Créer un dépôt GitHub
* Versionner un projet Python simple
* Comprendre pourquoi les fichiers de logs ne sont **pas versionnés**
* Faire des commits clairs et professionnels

## Rappel

* **Git** = historique du code
* **GitHub** = hébergement et partage du projet

On versionne :

* le **code source**
* la **structure du projet**
* la documentation

On ne versionne pas :

* les fichiers générés automatiquement (`.log`, cache, fichiers temporaires…)

## Structure du projet

```
calculatrice-logs/
├── calculatrice.py
├── README.md
├── .gitignore
├── requirements.txt
└── calculatrice.log   (NON versionné)
```

## Étape 1 – Créer le dépôt GitHub

1. Aller sur github.com
2. Cliquer sur **New repository**
3. Nom :

```
calculatrice-logs
```

4. Décocher *Initialize with README*
5. Créer le dépôt

## Étape 2 – Initialiser Git en local

Dans le dossier du projet :

```bash
git init
git status
```

## Étape 3 – Ajouter le code

```bash
git add calculatrice.py
git status
```

## Étape 4 – Premier commit

```bash
git commit -m "Ajout de la calculatrice avec gestion des logs"
```

Un bon message de commit est :

* clair
* précis
* lié à l’action effectuée
* pas “first commit”

## Étape 5 – Ajouter un README

Créer un fichier `README.md` :

````markdown
# Calculatrice avec logs

Mini-projet Python utilisant le module logging.

## Fonctionnalités
- Addition
- Division
- Gestion des erreurs
- Logs enregistrés dans un fichier

## Lancer le programme
```bash
python calculatrice.py
```
````

Puis :

```bash
git add README.md
git commit -m "Ajout du README du projet"
```

## Étape 6 – Ignorer les logs

Ne pas versionner les logs (`calculatrice.log`) car :

* fichier généré automatiquement
* change à chaque exécution
* pollue l’historique Git
* peut contenir données sensibles

Créer un fichier `.gitignore` :

```gitignore
*.log
__pycache__/
```

Commit :

```bash
git add .gitignore
git commit -m "Ajout du .gitignore pour ignorer les logs"
```

## Étape 7 – Lier le dépôt local à GitHub

```bash
git branch -M main
git remote add origin https://github.com/<user>/calculatrice-logs.git
git push -u origin main
```

## Vérification finale

Sur GitHub :

* `calculatrice.py` présent
* `README.md` présent
* `.gitignore` présent
* `calculatrice.log` absent

## Conclusion

* GitHub sert à **partager le code**
* Les logs servent à **comprendre l’exécution**
* Les fichiers `.log` ne sont pas du code source
* Logs + Git = base du travail en équipe

---

# TP – Partie 3 : Supervision réseau

## Objectifs

* Tester la connectivité réseau (ping)
* Enregistrer des événements système
* Différencier INFO / WARNING / ERROR
* Comprendre le rôle des logs en supervision
* Simuler un mini outil d’administration

## Mise en situation

Vous travaillez dans un service informatique.

On vous demande de créer un petit outil Python capable de :

1. Faire des calculs
2. Tester si un serveur est accessible
3. Enregistrer toutes les actions dans un fichier log

## Nouvelle organisation du projet

```
calculatrice-logs/
├── calculatrice.py
├── supervision.py      ← nouveau
├── README.md
├── .gitignore
├── requirements.txt
└── calculatrice.log    ← (NON versionné)
```

## Ajouter un module de supervision

Créer `supervision.py`

### Fonction demandée

Ce code contient la fonction `verifier_connectivite()` qui doit :

* tester si l’hôte répond au ping
* écrire un log :

  * INFO si OK
  * WARNING si pas de réponse

```python
import os
import logging
import datetime

# Configuration du logging
logging.basicConfig(
    filename="calculatrice.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def verifier_connectivite(hote):
    logging.info(f"Test de connectivité vers {hote}")

    # -c pour Linux / -n pour Windows
    param = "-n" if os.name == "nt" else "-c"
    commande = f"ping {param} 1 {hote}"

    reponse = os.system(commande)

    if reponse == 0:
        logging.info(f"{hote} est accessible")
        return True
    else:
        logging.warning(f"{hote} ne répond pas")
        return False

def verifier_charge_cpu():
    logging.info("Simulation vérification charge CPU")
    charge = 30  # valeur fictive
    if charge > 80:
        logging.warning("Charge CPU élevée")
    return charge


if __name__ == "__main__":
    verifier_connectivite("127.0.0.1")
```

On simule un outil de monitoring.

### Exploitation des logs

Après plusieurs exécutions :

```bash
python calculatrice.py
```

Ouvrir :

```
calculatrice.log
```

Observer :

* horodatage
* niveau
* message

## Variante (bonus)

Remplacer le ping par un test de port :

```python
import socket

def verifier_port(hote, port):
    logging.info(f"Test du port {port} sur {hote}")

    s = socket.socket()
    s.settimeout(2)

    try:
        s.connect((hote, port))
        logging.info("Port ouvert")
        return True
    except:
        logging.warning("Port fermé ou inaccessible")
        return False
    finally:
        s.close()
```

Exemple :

```python
verifier_port("google.com", 80)
```

---

# TP – Partie 4 : Simulation Capteur IoT Réseau

## Objectifs

* Simuler un capteur IoT
* Envoyer des données via le réseau (socket TCP)
* Recevoir et traiter des données
* Logger des événements réseau
* Tester une communication simple

## Mise en situation

Vous devez simuler un capteur industriel qui :

* mesure une température
* l’envoie à un serveur
* le serveur enregistre les données dans un log

## Nouvelle structure du projet

```
calculatrice-logs/
├── calculatrice.py
├── supervision.py
├── capteur.py          ← nouveau
├── serveur_iot.py      ← nouveau
├── README.md
├── .gitignore
├── requirements.txt
└── calculatrice.log    ← (NON versionné)
```

## Étape 1 – Créer le serveur IoT

### `serveur_iot.py`

```python
import socket
import logging

logging.basicConfig(
    filename="calculatrice.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

HOST = "127.0.0.1"
PORT = 5000

def lancer_serveur():
    serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serveur.bind((HOST, PORT))
    serveur.listen()

    logging.info("Serveur IoT démarré")
    print("Serveur en attente de connexion...")

    while True:
        conn, addr = serveur.accept()
        with conn:
            logging.info(f"Connexion reçue de {addr}")
            data = conn.recv(1024)

            if data:
                message = data.decode()
                logging.info(f"Donnée reçue : {message}")
                print("Message reçu :", message)

                valeur = float(message.split(":")[1])

                if valeur > 28:
                    logging.warning("ALERTE : Température élevée")


if __name__ == "__main__":
    lancer_serveur()
```

## Étape 2 – Créer le capteur

### `capteur.py`

```python
import socket
import random
import logging
import time

logging.basicConfig(
    filename="calculatrice.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

HOST = "127.0.0.1"
PORT = 5000

def generer_temperature():
    return round(random.uniform(15, 30), 2)

def envoyer_donnee():
    temperature = generer_temperature()
    message = f"temperature:{temperature}"

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))

    client.sendall(message.encode())
    client.close()

    logging.info(f"Donnée envoyée : {message}")

while True:
    envoyer_donnee()
    time.sleep(3)
```

## Test manuel

### Terminal 1 :

```bash
python serveur_iot.py
```

### Terminal 2 :

```bash
python capteur.py
```

Résultat :

* Le serveur affiche la température
* Le fichier `calculatrice.log` contient les traces
* Dans le fichier log : Ex. `49846` port source (éphémère) utilisé par le client** (script `capteur.py`) lors de la connexion au serveur. Cela permet :

    * d’avoir plusieurs connexions simultanées
    * de distinguer les différentes communications

| Rôle    | Adresse   | Port                             |
| ------- | --------- | -------------------------------- |
| Serveur | 127.0.0.1 | **5000** (fixe)                  |
| Client  | 127.0.0.1 | **49846, 49850, ...** (variable) |

### Notes

Ici on utilise :

* TCP
* Adresse IP locale (127.0.0.1)
* Port 5000

### Test depuis une autre machine du réseau

Remplacer :

```
HOST = "127.0.0.1"
```

par l’adresse IP locale.

---

# TP – Partie 5 : Détection d’intrusion simple

## Objectifs

* Comprendre le principe d’un IDS (Intrusion Detection System - système de détection d'intrusion)
* Surveiller des connexions réseau
* Détecter un comportement suspect
* Utiliser les niveaux de logs (INFO / WARNING / ERROR)
* Simuler une alerte sécurité

## Mise en situation

Vous administrez un petit serveur IoT.

Vous devez :

* Autoriser les connexions normales
* Détecter trop de tentatives de connexion
* Générer une alerte si activité suspecte

C’est le principe d’un :

* pare-feu intelligent
* IDS réseau
* système de détection brute-force

## Nouvelle structure du projet

```
calculatrice-logs/
├── calculatrice.py
├── supervision.py
├── capteur.py 
├── serveur_iot.py 
├── serveur_securise.py   ← nouveau
├── attaquant.py          ← nouveau
├── README.md
├── .gitignore
├── requirements.txt
└── calculatrice.log    ← (NON versionné)
```

## Créer un serveur sécurisé

### `serveur_securise.py`

```python
import socket
import logging
import time

logging.basicConfig(
    filename="calculatrice.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

HOST = "0.0.0.0"
PORT = 6000

# Dictionnaire pour compter les tentatives par IP
tentatives_connexion = {}

SEUIL_TENTATIVES = 5
INTERVALLE = 10  # secondes

def lancer_serveur():
    serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serveur.bind((HOST, PORT))
    serveur.listen()

    print("Serveur sécurisé en écoute...")
    logging.info("Serveur sécurisé démarré")

    while True:
        conn, addr = serveur.accept()
        ip_client = addr[0]
        moment = time.time()

        logging.info(f"Tentative de connexion depuis {ip_client}")

        # Initialisation si nouvelle IP
        if ip_client not in tentatives_connexion:
            tentatives_connexion[ip_client] = []

        # Ajouter la tentative actuelle
        tentatives_connexion[ip_client].append(moment)

        # Supprimer les anciennes tentatives
        tentatives_connexion[ip_client] = [
            t for t in tentatives_connexion[ip_client]
            if moment - t < INTERVALLE
        ]

        #print(f"Nombre de tentatives récentes : {len(tentatives_connexion[ip_client])}")

        # Vérifier dépassement seuil
        if len(tentatives_connexion[ip_client]) >= SEUIL_TENTATIVES:
            logging.warning(f"ALERTE : Trop de connexions depuis {ip_client}")
            print("Alerte intrusion détectée !")

        conn.close()

if __name__ == "__main__":
    lancer_serveur()
```

On surveille :

* combien de connexions une IP fait
* dans un intervalle de temps donné

Si une IP dépasse le seuil → alerte.

> C’est le principe de détection brute-force.

## Simuler un attaquant

### `attaquant.py`

```python
import socket
import time

HOST = "127.0.0.1"
PORT = 6000

def attaquer(nb_tentatives):
    for i in range(nb_tentatives):
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            client.connect((HOST, PORT))
        except:
            pass
        client.close()
        time.sleep(1)

if __name__ == "__main__":
    attaquer(10)
```

## Test manuel

### Terminal 1 :

```bash
python serveur_securise.py
```

### Terminal 2 :

```bash
python attaquant.py
```

Résultat :

* Le serveur détecte trop de connexions
* Une alerte apparaît
* Le log contient un WARNING

## Analyse du log

Dans `calculatrice.log` :

```
INFO - Tentative de connexion depuis 127.0.0.1
WARNING - ALERTE : Trop de connexions depuis 127.0.0.1
```

