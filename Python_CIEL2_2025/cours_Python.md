# Python

## Introduction

Python est un **langage interprété**, **multiplateforme**, simple à apprendre et très puissant. Il est utilisé à la fois dans **l'industrie** et la **recherche académique**.

### Avantages principaux

* Fonctionne sous **Windows, Linux et MacOS**
* Dispose d'un **vaste écosystème scientifique**
* Idéal pour le **traitement de données**, l’**analyse scientifique**, et le **développement web**

---

### Anaconda : une distribution Python complète

**Anaconda** est une distribution populaire pour les scientifiques et analystes de données.

Elle fournit :

* Python + gestionnaire de paquets `conda`
* Des environnements comme **Spyder** (IDE) ou **Jupyter Notebook**
* Une gestion simplifiée des bibliothèques comme :

  * `numpy` : calcul numérique
  * `pandas` : manipulation de données
  * `matplotlib` : visualisation
  * ...

---

## Démarrer avec Jupyter Notebook

### Lancer Jupyter Notebook

* Depuis **Anaconda Navigator** : cliquer sur `Launch`
* Ou via un **terminal** :

```bash
jupyter notebook
```

---

### Interface des notebooks

* L'interface s'ouvre dans un **navigateur web**
* Un notebook est composé de **cellules**

  * **Cellules de code** : contiennent du code Python
  * **Cellules Markdown** : contiennent du texte formaté (titres, listes, etc.)

---

## Les bibliothèques scientifiques

Une bibliothèque (ou module) contient un ensemble de fonctions prêtes à l'emploi.

### Exemples populaires

* `numpy` : calcul scientifique
* `scipy` : traitement du signal, intégration, optimisation
* `matplotlib` : visualisation de données
* `pandas` : manipulation de données tabulaires

---

### Comment importer une bibliothèque ?

```python
from module import fonction  # Import spécifique (recommandé)
from module import *         # Tout importer (à éviter)
import module as md          # Import avec alias (fréquent)
```

Exemple avec `numpy` :

```python
import numpy as np
np.sqrt(2)  # racine carrée de 2
```

---

## Bases de Python

### Variables et types

```python
a = "Bonjour"
x = 3.14
liste = [1, 2, 3]
liste2 = [[1, 2], [3, 4]]
t = (1, "texte", True)

print(a, x, liste, t)
```

> Les variables sont **dynamiquement typées** : leur type est déterminé automatiquement lors de l'affectation.

---

### Chaînes de caractères

```python
mot = "Python"
print(mot[0], mot[-1])   # P n
print(mot[:2])           # Py
print(len(mot))          # 6
print(mot + " 3.13")
print(f"Nom : {mot}, longueur : {len(mot)}")
```

> Les chaînes sont **immuables** : on ne peut pas modifier un caractère directement.

---

### Entrées / sorties

```python
a = 5
print(f"Résultat : {a/3:.2f}")
```

```python
nom = input("Votre nom : ")
print(f"Bonjour {nom} !")
```

> `input()` retourne toujours une **chaîne de caractères**

#### Conversion de types

```python
x = int(input('Entrer un entier : '))
y = float(input('Entrer un réel : '))
```

### Formatage des chaînes avec `print()`

#### 1. Concaténation

```python
nom = "Carnus"
print("Bonjour " + nom + " !")
```

> Moins lisible, fragile si on mélange types (`int`, `str`, etc.)

---

#### 2. Formatage moderne avec `f-strings` (recommandé)

```python
nom = "Carnus"
age = 25
print(f"Nom : {nom}, âge : {age}")
```

* On peut aussi **formater des nombres** :

```python
pi = 3.14159
print(f"Pi arrondi : {pi:.2f}")    # Pi arrondi : 3.14
```

---

#### 3. Autres formats utiles

```python
x = 42
print(f"{x:04d}")       # 0042 (zéro-padding)
print(f"{x:b}")         # 101010 (binaire)
```

* Pourcentage :

```python
pourcent = 0.857
print(f"Taux : {pourcent:.1%}")   # Taux : 85.7%
```

---

### Listes

Les **listes** sont des structures de données ordonnées, **muables** (modifiables) et hétérogènes (peuvent contenir plusieurs types).

```python
produits = ["ordinateur", "clavier", "serveur"]
nombres = [1, 2, 3, 4, 5]
```

```python
squares = [1, 4, 9, 16]
squares.append(25)
print(squares)
print(squares[-2:])
```

> Les listes sont **muables** (on peut les modifier)

---

#### Accéder à une liste

```python
print(produits[0])     # "ordinateur"
print(produits[-1])    # "serveur"
print(produits[:2])    # ["ordinateur", "clavier"]
```

> Les indices commencent à 0

---

#### Parcourir et filtrer les valeurs

##### Exemples avec `for` + `if`

```python
nombres = [1, 5, 8, 12, 3, 7]

# Afficher les éléments supérieurs à 5
for n in nombres:
    if n > 5:
        print(n)
```

> Résultat :

```
8
12
7
```

---

#### Créer une nouvelle liste filtrée

```python
# Liste des nombres pairs
pairs = []
for n in nombres:
    if n % 2 == 0:
        pairs.append(n)

print(pairs)  # [8, 12]
```

Ou avec une **compréhension de liste** (plus concis) :

```python
pairs = [n for n in nombres if n % 2 == 0]
```

---

#### Appliquer une fonction à chaque élément

##### Avec une boucle classique

```python
nombres = [1, 2, 3, 4]
carrés = []

for n in nombres:
    carrés.append(n ** 2)

print(carrés)  # [1, 4, 9, 16]
```

---

##### Avec une compréhension de liste

```python
carrés = [n ** 2 for n in nombres]
```

---

##### Avec `map()` et une fonction

```python
def triple(x):
    return 3 * x

resultat = list(map(triple, nombres))
print(resultat)  # [3, 6, 9, 12]
```

> On peut aussi utiliser une **fonction lambda** :

```python
resultat = list(map(lambda x: x * 3, nombres))
```

---

#### Commandes utiles

* `sum(liste)` : somme des éléments
* `min(liste)`, `max(liste)` : minimum / maximum
* `sorted(liste)` : retourne une nouvelle liste triée
* `liste.sort()` : trie la liste en place


---

### Opérateurs

| Symbole | Nom              | Exemple   | Résultat |
| ------: | ---------------- | --------- | -------: |
|     `+` | Addition         | `3 + 2`   |      `5` |
|     `*` | Multiplication   | `3 * "a"` |  `"aaa"` |
|    `**` | Puissance        | `2 ** 3`  |      `8` |
|     `/` | Division réelle  | `7 / 2`   |    `3.5` |
|    `//` | Division entière | `7 // 2`  |      `3` |
|     `%` | Modulo           | `7 % 2`   |      `1` |

Autres opérateurs :

* **Comparaison** : `==`, `!=`, `<`, `>`, `<=`, `>=`
* **Logiques** : `and`, `or`, `not`

---

## Boucles et conditions

### Conditions

```python
x = 5
if x > 0:
    print("Positif")
elif x == 0:
    print("Nul")
else:
    print("Négatif")
```

> Python ne possède pas de structure `switch`.

---

### Boucle `for`

```python
for i in range(5):
    print(i)

for mois in ["juin", "juillet", "août"]:
    print(mois)
```

---

### Boucle `while`

```python
compte = 5
while compte > 0:
    print(compte)
    compte -= 1
```

---

## Fonctions

```python
def triple(x):
    return 3 * x

def somme(*args):
    return sum(args)

print(triple(4))
print(somme(1, 2, 3))
```

## Fonctions avancées

### Paramètres par défaut

```python
def saluer(nom="inconnu"):
    print(f"Bonjour {nom} !")

saluer()             # Bonjour inconnu !
saluer("Carnus")     # Bonjour Carnus !
```

> Les paramètres avec valeur par défaut doivent être placés **après** les paramètres obligatoires.

---

### Retourner plusieurs valeurs

```python
def min_et_max(liste):
    return min(liste), max(liste)

valeurs = [3, 7, 2, 9]
mini, maxi = min_et_max(valeurs)
print("Min :", mini, "Max :", maxi)
```

> Une fonction peut retourner un **tuple** automatiquement.

---

### `*args` et `**kwargs`

#### `*args` : liste d'arguments non nommés

```python
def somme(*nombres):
    return sum(nombres)

print(somme(1, 2, 3))         # 6
print(somme(10, 20, 30, 40))  # 100
```

#### `**kwargs` : dictionnaire d'arguments nommés

```python
def infos_utilisateur(**kwargs):
    for cle, valeur in kwargs.items():
        print(f"{cle} : {valeur}")

infos_utilisateur(nom="Carnus", age=20)
```

> `kwargs` signifie "keyword arguments", pratique pour passer des options.

---

### Fonctions anonymes (lambda)

Les **fonctions lambda** sont des fonctions simples sans nom.

```python
carre = lambda x: x * x
print(carre(5))  # 25
```

On les utilise souvent avec `map`, `filter`, ou `sorted` :

```python
nombres = [5, 2, 9, 1]
trié = sorted(nombres, key=lambda x: -x)  # tri décroissant
print(trié)  # [9, 5, 2, 1]
```

---

## Courbes avec matplotlib

```python
import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline # Obligatoire dans Jupyter Notebook

X = np.linspace(-2*np.pi, 2*np.pi, 200)

plt.plot(X, np.sin(X), label="sin(x)")
plt.plot(X, np.cos(X), label="cos(x)")
plt.title("Courbes : sin(x) et cos(x)")
plt.xlabel("x")
plt.ylabel("Amplitude")
plt.legend()
plt.grid()
plt.show()
```

---

## Nombres complexes

```python
z = 3 + 4j
print(z.real, z.imag)
print(abs(z))  # module
```

---

## Manipulation de fichiers

### Fichiers texte

```python
with open("donnees.txt", "w") as f:
    f.write("Ligne 1\n")
    f.write("Ligne 2\n")

with open("donnees.txt", "r") as f:
    contenu = f.read()
    print(contenu)
```

---

### Fichiers binaires

```python
import struct

with open("data.bin", "wb") as f:
    f.write(struct.pack("i", 12345))

with open("data.bin", "rb") as f:
    data = struct.unpack("i", f.read())[0]
    print(data)
```

---

## Structures de données avancées

### Dictionnaires

```python
etudiants = {"Alice": 15, "Bob": 12}
etudiants["Claire"] = 17

for nom, note in etudiants.items():
    print(nom, note)
```

### Ensembles (sets)

```python
A = {1, 2, 3}
B = {3, 4, 5}

print(A | B)  # union
print(A & B)  # intersection
print(A - B)  # différence
```

---

## Manipulation de données avec pandas

```python
import pandas as pd

df = pd.DataFrame({
    "Nom": ["Alice", "Bob"],
    "Note": [15, 12]
})
df.to_csv("notes.csv", index=False)

data = pd.read_csv("notes.csv")
print(data)
```

---


### Gestion des erreurs : `try / except / finally`

En Python, on utilise `try / except` pour capturer et gérer les erreurs (aussi appelées **exceptions**) qui pourraient interrompre le programme.

---

#### Exemple

```python
a = 0
b = 5

try:
    b / a
    print("Ok pas d'erreur")
except:
    print("Erreur")
```

> Ce code déclenche une division par zéro (`ZeroDivisionError`) qui est capturée par le bloc `except`.

---

#### Version améliorée : spécifier le type d’erreur

```python
try:
    b / a
except ZeroDivisionError:
    print("Erreur : division par zéro")
```

> Il est **recommandé** de spécifier le type d'erreur pour ne pas masquer d'autres erreurs potentielles.

---

#### Utiliser `finally`

Le bloc `finally` est **toujours exécuté**, que l’erreur ait lieu ou non. Il est souvent utilisé pour :

* Fermer un fichier
* Libérer une ressource
* Nettoyer des variables temporaires

```python
try:
    b / a
except ZeroDivisionError:
    print("Division par zéro détectée")
finally:
    print("Bloc finally exécuté")
```

---

#### Exemple avec plusieurs types d’erreurs

```python
try:
    val = int(input("Entrez un entier : "))
    print(10 / val)
except ValueError:
    print("Ce n'est pas un entier valide.")
except ZeroDivisionError:
    print("Division par zéro interdite.")
except Exception as e:
    print("Erreur inattendue :", e)
finally:
    print("Terminé.")
```

---

#### Résumé

| Bloc      | Rôle                                             |
| --------- | ------------------------------------------------ |
| `try`     | Contient le code susceptible de lever une erreur |
| `except`  | Gère les erreurs si elles se produisent          |
| `finally` | Toujours exécuté (utile pour le nettoyage)       |


---

## Exercices avec corrigés

### Exercice : Variables et types

#### Énoncé

Créer trois variables :

* `nom` (str)
* `age` (int)
* `notes` (liste de trois nombres)

Afficher :

```
Nom : <nom>, âge : <age>, moyenne : <moyenne des notes>
```

#### **Correction**

```python
nom = "Alice"
age = 20
notes = [12, 14, 15]

moyenne = sum(notes) / len(notes)
print(f"Nom : {nom}, âge : {age}, moyenne : {moyenne}")
```

---

### Exercice : Chaînes de caractères

#### Énoncé

Demander un mot à l’utilisateur et afficher :

* le premier caractère
* le dernier caractère
* le mot en majuscules

#### Correction

```python
mot = input("Mot : ")
print("Premier :", mot[0])
print("Dernier :", mot[-1])
print("Majuscules :", mot.upper())
```

---

### Exercice : Entrées / sorties et conversions

#### Énoncé

Demander deux nombres à l'utilisateur, les convertir en `float`, et afficher leur somme arrondie à 2 décimales.

#### Correction

```python
a = float(input("Nombre 1 : "))
b = float(input("Nombre 2 : "))
print(f"Somme : {a + b:.2f}")
```

---

### Exercice : Boucles

#### Énoncé

Afficher la table de multiplication de 7.

#### Correction

```python
for i in range(1, 11):
    print(f"7 x {i} = {7 * i}")
```

---

### Exercice : Listes

#### Énoncé

Soit la liste `L = [2, 5, 8, 1, 9, 3]`.
Créer :

1. une liste contenant les nombres pairs
2. une liste contenant les carrés
3. la même chose mais avec des compréhensions de listes

#### Correction

```python
L = [2, 5, 8, 1, 9, 3]

# 1. pairs
pairs = []
for x in L:
    if x % 2 == 0:
        pairs.append(x)

# 2. carrés
carres = []
for x in L:
    carres.append(x ** 2)

# Versions compréhensions
pairs2 = [x for x in L if x % 2 == 0]
carres2 = [x*x for x in L]

print(pairs, carres)
print(pairs2, carres2)
```

---

### Exercice : Boucles et conditions

#### Énoncé

Écrire un programme qui affiche tous les nombres de 1 à 50, mais :

* affiche "D3" si le nombre est divisible par 3
* "D5" s’il est divisible par 5
* "D3D5" s’il est divisible par 3 et 5

#### Correction

```python
for i in range(1, 51):
    if i % 15 == 0:
        print("D3D5")
    elif i % 3 == 0:
        print("D3")
    elif i % 5 == 0:
        print("D5")
    else:
        print(i)
```

---

### Exercice : Fonctions

#### Énoncé

Créer une fonction `est_pair(n)` qui retourne `True` si le nombre est pair, sinon `False`.
Tester la fonction dans une boucle de 0 à 10.

#### Correction

```python
def est_pair(n):
    return n % 2 == 0

for i in range(11):
    print(i, est_pair(i))
```

---

### Exercice : Fonctions avancées (`*args`, `**kwargs`)

#### Énoncé

Créer une fonction `moyenne(*notes)` qui retourne la moyenne de tous les nombres passés en argument.
Exemple : `moyenne(10, 12, 15, 18)`

#### Correction

```python
def moyenne(*notes):
    return sum(notes) / len(notes)

print(moyenne(10, 12, 15, 18))
```

---

### Exercice : `**kwargs`

#### Énoncé

Créer une fonction `decrire(**infos)` qui affiche chaque clé et valeur sous la forme :

```
clé : valeur
```

#### Correction

```python
def decrire(**infos):
    for cle, valeur in infos.items():
        print(f"{cle} : {valeur}")

decrire(nom="Alice", age=22, ville="Paris")
```

---

### Exercice : Dictionnaires et ensembles

#### Énoncé

On a le dictionnaire :

```python
notes = {"Alice": 15, "Bob": 12, "Claire": 17}
```

Afficher uniquement les étudiants ayant une note ≥ 15.

#### Correction

```python
notes = {"Alice": 15, "Bob": 12, "Claire": 17}

for nom, note in notes.items():
    if note >= 15:
        print(nom, note)
```

---

### Exercice : Sets

#### Énoncé

Étant donné :

```python
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
```

Afficher :

* union
* intersection
* éléments de A qui ne sont pas dans B

#### Correction

```python
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print("Union :", A | B)
print("Intersection :", A & B)
print("Différence A - B :", A - B)
```

---

### Exercice : Fichiers

#### Énoncé

Écrire une ligne de texte dans un fichier, puis la relire et l'afficher.

#### Correction

```python
with open("test.txt", "w") as f:
    f.write("Bonjour\n")

with open("test.txt", "r") as f:
    print(f.read())
```

---

### Exercice : Manipulation de fichiers

#### Énoncé

Créer un fichier `test.txt`, écrire trois lignes, puis relire le fichier et afficher son contenu.

#### Correction

```python
with open("test.txt", "w") as f:
    f.write("Ligne 1\n")
    f.write("Ligne 2\n")
    f.write("Ligne 3\n")

with open("test.txt", "r") as f:
    print(f.read())
```

---

### Exercice : Try / Except

#### Énoncé

Écrire un programme qui demande à l’utilisateur un entier et affiche son inverse.
Gérer les erreurs suivantes :

* valeur non entière
* division par zéro

#### Correction

```python
try:
    x = int(input("Entrez un entier : "))
    print("Inverse =", 1 / x)

except ValueError:
    print("Erreur : vous devez entrer un entier.")
except ZeroDivisionError:
    print("Erreur : division par zéro interdite.")
```

---

### Exercice : Matplotlib

#### Énoncé

Tracer la fonction ( f(x) = x^2 - 3x + 2 ) sur l’intervalle [-5, 5].

#### Correction

```python
import numpy as np
import matplotlib.pyplot as plt

X = np.linspace(-5, 5, 200)
Y = X**2 - 3*X + 2

plt.plot(X, Y)
plt.title("f(x) = x^2 - 3x + 2")
plt.grid()
plt.show()
```

---

### Exercice : Représenter deux courbes sur le même graphique

#### Énoncé

Tracer sur l’intervalle ([-4, 4]) :

* ( f(x) = x^2 )
* ( g(x) = x^3 )

Ajouter :

* un titre
* une légende
* une grille

---

#### Correction

```python
import numpy as np
import matplotlib.pyplot as plt

X = np.linspace(-4, 4, 200)
Y1 = X**2
Y2 = X**3

plt.plot(X, Y1, label="x²")
plt.plot(X, Y2, label="x³")
plt.title("Comparaison entre x² et x³")
plt.legend()
plt.grid()
plt.show()
```

---

### Exercice : Tracer plusieurs courbes trigonométriques

#### Énoncé

Sur l’intervalle ([0, 2\pi]), tracer :

* (\sin(x))
* (\cos(x))
* (\tan(x)) (avec prudence : limiter l’axe des y entre -3 et 3)

Affiche une légende, un titre et modifie les limites de l’axe Y.

---

#### Correction

```python
import numpy as np
import matplotlib.pyplot as plt

X = np.linspace(0, 2*np.pi, 400)

plt.plot(X, np.sin(X), label="sin(x)")
plt.plot(X, np.cos(X), label="cos(x)")
plt.plot(X, np.tan(X), label="tan(x)")

plt.ylim(-3, 3)    # éviter les valeurs infinies
plt.title("Fonctions trigonométriques")
plt.legend()
plt.grid()
plt.show()
```

---

### Exercice : Courbe d’une fonction exponentielle et logarithmique

#### Énoncé

Tracer sur ([0.1, 5]) :

* (f(x) = e^x)
* (g(x) = \ln(x))

Afficher :

* un titre
* une légende
* un style différent pour chaque courbe (ex : ligne pointillée)

---

#### Correction

```python
import numpy as np
import matplotlib.pyplot as plt

X = np.linspace(0.1, 5, 300)

plt.plot(X, np.exp(X), label="exp(x)", linestyle="--")
plt.plot(X, np.log(X), label="ln(x)", linestyle="-.")

plt.title("Courbes de exp(x) et ln(x)")
plt.legend()
plt.grid()
plt.show()
```

---

### Exercice : Analyse simple d’un tableau de données avec pandas

On dispose du tableau suivant contenant les noms et notes d’étudiants :

| Nom    | Note |
| ------ | ---- |
| Alice  | 15   |
| Bob    | 12   |
| Claire | 17   |
| David  | 9    |
| Emma   | 14   |

#### **Travail demandé :**

1. Créer un DataFrame pandas à partir des données.
2. Afficher :

   * les 3 premières lignes
   * la note moyenne
3. Afficher uniquement les étudiants ayant une note **≥ 14**.
4. Sauvegarder ce sous-tableau dans un fichier `bons_etudiants.csv`.

---

#### Correction

```python
import pandas as pd

# 1. Création du DataFrame
df = pd.DataFrame({
    "Nom": ["Alice", "Bob", "Claire", "David", "Emma"],
    "Note": [15, 12, 17, 9, 14]
})

# 2. Affichage des trois premières lignes et moyenne
print(df.head(3))
print("Moyenne des notes :", df["Note"].mean())

# 3. Étudiants avec note >= 14
bons = df[df["Note"] >= 14]
print("\nÉtudiants ayant une bonne note :")
print(bons)

# 4. Sauvegarde dans un fichier CSV
bons.to_csv("bons_etudiants.csv", index=False)
```

---
---

## Créer un environnement virtuel Python (Windows, Linux, macOS)

### 0. Prérequis

Les machines doivent avoir **Python 3 installé**.
Pour vérifier :

```
python --version
```

ou

```
python3 --version
```

---

### 1. Windows

#### Étape 1 — Ouvrir un terminal

Ouvrir **Invite de commandes** (CMD) ou **PowerShell**.

#### Étape 2 — Aller dans votre dossier de travail

Par exemple :

```
cd C:\Users\<votre_nom>\Documents
```

#### Étape 3 — Créer l’environnement virtuel

```
python -m venv env
```

Cela crée un dossier **env/** contenant l’environnement Python isolé.

#### Étape 4 — Activer l’environnement

```
env\Scripts\activate
```

Vous devriez voir :

```
(env) C:\Users\...
```

- Vous êtes maintenant *dans* l’environnement virtuel.

#### Étape 5 — Installer des librairies (exemple)

```
pip install numpy pandas matplotlib
```

#### Désactiver l’environnement

```
deactivate
```

---

### 2. Linux / macOS

#### Étape 1 — Terminal

Ouvrir un terminal.

#### Étape 2 — Aller dans votre dossier

```
cd ~/Documents
```

#### Étape 3 — Créer l’environnement virtuel

```
python3 -m venv env
```

#### Étape 4 — Activer l’environnement

```
source env/bin/activate
```

Vous devriez voir :

```
(env) user@machine:~
```

#### Étape 5 — Installer des librairies (exemple)

```
pip install numpy pandas matplotlib
```

#### Désactiver l’environnement

```
deactivate
```

---

### Vérifier que tout fonctionne

Une fois l’environnement activé (Windows ou Linux/macOS), lancez :

```
python -c "import numpy; print(numpy.__version__)"
```

Si cela affiche un numéro de version, c’est réussi.

---

### Travailler dans VSCode

1. Ouvrir VSCode
2. Explorer → ouvrir le dossier contenant l’environnement
3. Appuyer sur `Ctrl+Shift+P` → “Python: Select Interpreter”
4. Choisir :

   ```
   .\env\Scripts\python.exe  (Windows)
   ./env/bin/python          (Linux/macOS)
   ```

---

### Résumé

| OS              | Créer                 | Activer                   | Désactiver   |
| --------------- | --------------------- | ------------------------- | ------------ |
| **Windows**     | `python -m venv env`  | `env\Scripts\activate`    | `deactivate` |
| **Linux/macOS** | `python3 -m venv env` | `source env/bin/activate` | `deactivate` |

---
---

## Procédure (Jupyter Notebook) : créer un venv et l’utiliser dans Jupyter

### Remarque :

> Vous pouvez utiliser le document fourni : `doc_venv.ipynb`
> Sinon, suivez les étapes ci-dessous.

### Créer l’environnement virtuel

Dans un notebook Jupyter :

```python
!python -m venv env
```

(ou `!python3` selon le système)

Cela crée un dossier `env/`.

---

### Installer ipykernel dans ce venv

L’objectif est d’ajouter un **kernel Jupyter** correspondant à l’environnement virtuel.

#### Étape très importante

Installer ipykernel dans le venv :

```python
!env/Scripts/python -m pip install ipykernel
```

--> Sur Linux / macOS :

```python
!env/bin/python -m pip install ipykernel
```

---

### Ajouter un kernel Jupyter correspondant au venv

Toujours dans le notebook :

#### Windows :

```python
!env/Scripts/python -m ipykernel install --user --name env --display-name "Python (env)"
```

#### Linux / macOS :

```python
!env/bin/python -m ipykernel install --user --name env --display-name "Python (env)"
```

--> Cela crée un nouveau kernel “Python (env)” que vous pourrez sélectionner.

---

### Dans Jupyter, changer de kernel

Menu :
**Kernel → Change Kernel → Python (env)**

--> **À partir de ce moment, tout ce que vous installez ira dans le venv**.

---

## Installer des bibliothèques dans le venv, mais depuis Jupyter

Exemples :

```python
!pip install numpy pandas matplotlib
```

ou si vous voulez être *absolument sûr* d’utiliser le bon interpréteur :

```python
import sys
!{sys.executable} -m pip install numpy pandas matplotlib
```

---

## Résultat

* Le venv apparaît comme un kernel normal dans Jupyter Notebook
* Les installations de packages se font **dans l’environnement virtuel**, pas dans le système

---

## Ce qui n’est pas possible

- **Installer Python systématiquement depuis Jupyter**
- Modifier des dossiers système
- Installer des extensions Jupyter qui nécessitent des droits admin



