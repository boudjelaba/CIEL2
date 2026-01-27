# Introduction aux tests logiciels avec **pytest** (Python)

## Objectifs

* comprendre l’intérêt des tests logiciels
* écrire des tests simples avec **pytest**
* exécuter une suite de tests
* interpréter les résultats
* tester des fonctions Python courantes

## 1. Tests logiciels

### 1.1 Définition

Un **test logiciel** est un programme qui vérifie automatiquement qu’un autre programme fonctionne correctement.

Objectif :

* détecter les erreurs
* garantir le bon fonctionnement du code
* faciliter la maintenance

### 1.2 Exemple sans test

```python
def addition(a, b):
    return a - b   # erreur !
```

> Sans test, l’erreur peut passer inaperçue.

---

## 2. Présentation de pytest

### 2.1 pytest

**pytest** est un framework de tests pour Python :

* simple à utiliser
* très lisible
* largement utilisé dans l’industrie

### 2.2 Installation

```bash
pip install pytest
```

### 2.3 Organisation des fichiers

Convention pytest :

* les fichiers de test commencent par `test_`
* les fonctions de test commencent par `test_`

Exemple :

```
projet/
 ├── calcul.py
 └── test_calcul.py
```

---

## 3. Test avec pytest

### 3.1 Code à tester

**`calcul.py`**

```python
def addition(a, b):
    return a + b
```

### 3.2 Test associé

**`test_calcul.py`**

```python
from calcul import addition

def test_addition():
    assert addition(2, 3) == 5
```

### 3.3 Lancer les tests

Dans le terminal :

```bash
pytest
```

OK : Si le test passe
NOK: Sinon, pytest affiche une erreur détaillée

---

## 4. Comprendre `assert`

### 4.1 Principe

```python
assert condition
```

* si la condition est vraie → test réussi
* sinon → test échoué

### 4.2 Exemples

```python
assert 3 + 2 == 5
assert "info".upper() == "INFO"
assert len([1, 2, 3]) == 3
```

---

## 5. Tester plusieurs cas

### 5.1 Exemple

```python
def soustraction(a, b):
    return a - b
```

```python
def test_soustraction():
    assert soustraction(5, 2) == 3
    assert soustraction(2, 5) == -3
    assert soustraction(0, 0) == 0
```

---

## 6. Tests paramétrés (optionnel)

```python
import pytest
from calcul import addition

@pytest.mark.parametrize("a,b,resultat", [
    (2, 3, 5),
    (0, 0, 0),
    (-1, 1, 0)
])
def test_addition(a, b, resultat):
    assert addition(a, b) == resultat
```

* Évite la répétition
* Très lisible

---
---

## Exercice 1 — Test simple

### Énoncé

Écrire une fonction `carre(x)` qui retourne le carré d’un nombre, puis écrire les tests associés.

### Corrigé

`math_utils.py`

```python
def carre(x):
    return x * x
```

`test_math_utils.py`

```python
from math_utils import carre

def test_carre():
    assert carre(2) == 4
    assert carre(-3) == 9
    assert carre(0) == 0
```

---

## Exercice 2 — Chaînes de caractères

### Énoncé

Écrire une fonction `est_pair(n)` qui retourne `True` si un nombre est pair, `False` sinon.
Tester plusieurs cas.

---

### Corrigé

```python
def est_pair(n):
    return n % 2 == 0
```

```python
from utils import est_pair

def test_est_pair():
    assert est_pair(2) is True
    assert est_pair(7) is False
    assert est_pair(0) is True
```

---

## Exercice 3 — Listes

### Énoncé

Écrire une fonction `maximum(liste)` qui retourne le plus grand élément d’une liste.

---

### Corrigé

```python
def maximum(liste):
    return max(liste)
```

```python
def test_maximum():
    assert maximum([1, 5, 2]) == 5
    assert maximum([-1, -5, -3]) == -1
```

---

## 7. Remarques

* Un test = une idée
* Tester les cas limites (0, négatif, vide…)
* Nommer clairement les tests
* Lancer les tests souvent

---

## 8. Conclusion

Les tests avec pytest permettent :

* d’améliorer la qualité du code
* de détecter les bugs rapidement
* de programmer de manière plus professionnelle

---
---

# TP — Tester une application Python avec **pytest**

## Organisation du projet

```
tp_pytest/
 ├── app.py
 └── test_app.py
```

## Contexte applicatif

On développe une **mini-application réseau** permettant de vérifier une adresse IP

## Validation d’une adresse IP 

### 1. Fonction

Dans `app.py`, écrire la fonction :

```python
def est_ip_valide(ip):
    parties = ip.split(".")

    if len(parties) != 4:
        return False

    for p in parties:
        if not p.isdigit():
            return False
        if not 0 <= int(p) <= 255:
            return False

    return True
```

* une IP contient 4 nombres séparés par des `.`
* chaque nombre est compris entre 0 et 255

### 2. Tests à écrire

Dans `test_app.py`, écrire les tests pour vérifier :

* IP valide : `"192.168.1.1"`
* IP invalide : `"256.1.1.1"`
* IP invalide : `"192.168.1"`
* IP invalide : `"abc.def.1.2"`

---

### Corrigé

**`test_app.py`**

```python
from app import est_ip_valide

def test_ip_valide():
    assert est_ip_valide("192.168.1.1") is True

def test_ip_invalide():
    assert est_ip_valide("256.1.1.1") is False
    assert est_ip_valide("192.168.1") is False
    assert est_ip_valide("abc.def.1.2") is False
```

---
