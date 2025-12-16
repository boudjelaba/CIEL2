# **TP – Programmation Orientée Objet : Rectangle & Carré**

[![C CPP](https://img.shields.io/badge/C-C++-7b68ee)](https://www.cpp.org/)
[![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-2a52be)](https://www.vscode.fr/)

## Sommaire

* Rappel : Fichier *header* et classe

* Partie 0 : notion de classe + constructeur + méthodes
	- `Classe Rectangle simple`
* Partie 1 : héritage simple
	- `Ajout de l'héritage (Carre)`

---

## **Rappel - Fichier *header* et classe**

Le but d’un fichier header est de **déclarer** :

* les classes
* les structures
* les prototypes de fonctions
* les constantes, etc.

Ainsi, plusieurs fichiers `.cpp` peuvent utiliser la même classe simplement en faisant :

```cpp
#include "MaClasse.h"
```

---

### Structure typique : un fichier `.h` + un fichier `.cpp`

#### **MaClasse.h** (déclaration de la classe)

```cpp
#ifndef MA_CLASSE_H
#define MA_CLASSE_H

class MaClasse {
public:
    MaClasse();               // constructeur
    void afficher() const;    // méthode

private:
    int valeur;               // attribut
};

#endif
```

#### **MaClasse.cpp** (implémentation des méthodes)

```cpp
#include "MaClasse.h"
#include <iostream>

MaClasse::MaClasse() : valeur(0) {}

void MaClasse::afficher() const {
    std::cout << "Valeur = " << valeur << std::endl;
}
```

---

### Utilisation dans un programme

```cpp
#include "MaClasse.h"

int main() {
    MaClasse obj;
    obj.afficher();
    return 0;
}
```

---

### Utilité de la séparation en `.h` et `.cpp` 

- meilleure organisation
- compilation plus rapide
- réutilisation de la classe dans plusieurs fichiers
- évite les doubles définitions

---

### Conclusion

* **.h** → **déclaration** (interface)
* **.cpp** → **définition** (implémentation du code)

C’est une bonne pratique fondamentale en C++ (déjà abordée dans la compilation séparée).

---
---

## **PARTIE 0 — Classe `Rectangle` (sans héritage) avec séparation des codes**

### Objectif 

> Les attributs sont laissés `public` **volontairement**, car :
>
> * la version `protected` + getters/setters a déjà été étudiée (dans la version initiale)
> * l’objectif principal de cette partie est :
>
>   * la **séparation `.h / .cpp`**
>   * l’**organisation d’un projet C++ multi-dossiers**
>   * la **compilation avec chemins d’inclusion**

### Arborescence

```
partie0/
│── Rectangle.h
│── Rectangle.cpp
│── main.cpp
```

---

### **Rectangle.h**

```cpp
#ifndef RECTANGLE_H
#define RECTANGLE_H

class Rectangle {
public:
    double longueur;
    double largeur;

    Rectangle(double l = 0, double L = 0);

    double surface() const;
    double perimetre() const;
};

#endif
```

---


### **Rectangle.cpp**

```cpp
#include "Rectangle.h"
#include <iostream>

Rectangle::Rectangle(double l, double L) : longueur(l), largeur(L) {
    if (l < 0 || L < 0) {
        std::cerr << "Erreur : dimensions négatives !" << std::endl;
        longueur = largeur = 0;
    }
}

double Rectangle::surface() const {
    return longueur * largeur;
}

double Rectangle::perimetre() const {
    return 2 * (longueur + largeur);
}
```

---

### **main.cpp**

```cpp
#include <iostream>
#include "Rectangle.h"

int main() {
    Rectangle rect(3, 4);

    std::cout << "Longueur : " << rect.longueur << std::endl;
    std::cout << "Largeur : " << rect.largeur << std::endl;

    std::cout << "Surface : " << rect.surface() << std::endl;
    std::cout << "Perimetre : " << rect.perimetre() << std::endl;

    return 0;
}
```

---

### **Compilation**

Dans le dossier *partie0* :

**Sous Linux / macOS / MinGW**

```bash
g++ main.cpp Rectangle.cpp -o prog0
```

- Si on veut compiler **tous les fichiers .cpp** dans le dossier :

```bash
g++ *.cpp -o prog0
```

---

**Diagramme de dépendances**

```
main.cpp
   │
   └──> Rectangle.h
            │
            └──> Rectangle.cpp
```

**Remarques :**

* `main.cpp` inclut `Rectangle.h`
* `Rectangle.cpp` inclut aussi `Rectangle.h` (car il doit connaître la classe qu’il implémente)
* `Rectangle.h` n’inclut que `<iostream>`

---

### Nouvelle arborescence

```
partie0/
├── include/
│   └── Rectangle.h
├── src/
│   ├── Rectangle.cpp
│   └── main.cpp
└── build/
```

>Le dossier `build/` contiendra **uniquement les exécutables** (et plus tard les `.o`).

### Compilation avec sous-dossiers

#### Depuis le dossier `partie0`

```bash
g++ -I include src/main.cpp src/Rectangle.cpp -o build/prog0
```

#### Remarques

* `-I include` → indique au compilateur **où chercher les fichiers `.h`**
* Les `.cpp` sont compilés explicitement
* L’exécutable est placé dans `build/`

>**les `.h` ne sont jamais compilés**.

---
---

## **PARTIE 1 — Classe `Rectangle`  + héritage + classe `Carre` avec sparation des codes**

### Arborescence

```
partie1/
│── Rectangle.h
│── Rectangle.cpp
│── Carre.h
│── Carre.cpp
│── main.cpp
```

---

### **Rectangle.h**

```cpp
#ifndef RECTANGLE_H
#define RECTANGLE_H

class Rectangle {
public:
    double longueur;
    double largeur;

    Rectangle(double l = 0, double L = 0);
    double surface() const;
    double perimetre() const;
};

#endif
```

---

### **Rectangle.cpp**

```cpp
#include "Rectangle.h"
#include <iostream>

Rectangle::Rectangle(double l, double L) : longueur(l), largeur(L) {
    if (l < 0 || L < 0) {
        std::cerr << "Erreur : dimensions négatives !" << std::endl;
        longueur = largeur = 0;
    }
}

double Rectangle::surface() const {
    return longueur * largeur;
}

double Rectangle::perimetre() const {
    return 2 * (longueur + largeur);
}
```

---

### **Carre.h**

```cpp
#ifndef CARRE_H
#define CARRE_H

#include "Rectangle.h"

class Carre : public Rectangle {
public:
    Carre(double cote = 0);

    // surcharge des méthodes de Rectangle
    double surface() const;
    double perimetre() const;
};

#endif
```

---

### **Carre.cpp**

```cpp
#include "Carre.h"
#include <cmath>

Carre::Carre(double cote) : Rectangle(cote, cote) {}

double Carre::surface() const {
    return std::pow(longueur, 2);
}

double Carre::perimetre() const {
    return 4 * longueur;
}
```

---

### **main.cpp**

```cpp
#include <iostream>
#include "Rectangle.h"
#include "Carre.h"

int main() {
    Rectangle rect(3, 4);
    std::cout << "Surface rectangle : " << rect.surface() << std::endl;
    std::cout << "Perimetre rectangle : " << rect.perimetre() << std::endl;

    Carre carre(5);
    std::cout << "Surface carre : " << carre.surface() << std::endl;
    std::cout << "Perimetre carre : " << carre.perimetre() << std::endl;

    return 0;
}
```

---

### **Compilation**

Dans le dossier *partie1* :

**Linux / macOS / MinGW**

```bash
g++ main.cpp Rectangle.cpp Carre.cpp -o prog1
```

---

**Diagramme de dépendances (avec héritage)**

```
main.cpp
 ├──> Rectangle.h
 └──> Carre.h
         │
         └──> Rectangle.h   (héritage)
 
Carre.cpp
   └──> Carre.h
          └──> Rectangle.h

Rectangle.cpp
   └──> Rectangle.h
```

**Remarques :**

* `Carre.h` dépend de `Rectangle.h` (héritage → `#include "Rectangle.h"`)
* `main.cpp` inclut les deux classes car il les utilise
* Chaque `.cpp` inclut **son propre .h**

---

### **UML – Partie 1 : `Rectangle` + `Carre` (héritage)**

```
                +-----------------------------+
                |          Rectangle          |
                +-----------------------------+
                | + longueur : double         |
                | + largeur  : double         |
                +-----------------------------+
                | + Rectangle(l=0, L=0)       |
                | + surface() : double        |
                | + perimetre() : double      |
                +-----------------------------+
                           ^
                           |
                           | inherits
                           |
                +-----------------------------+
                |            Carre            |
                +-----------------------------+
                |  (pas d'attributs propres)  |
                +-----------------------------+
                | + Carre(cote=0)             |
                | + surface() : double        |
                | + perimetre() : double      |
                +-----------------------------+
```

* `Carre` n’a **aucun attribut** : il exploite ceux hérités de `Rectangle`.
* `Carre` **redéfinit** `surface()` et `perimetre()`.

---

### Nouvelle arborescence

```
partie1/
├── include/
│   ├── Rectangle.h
│   └── Carre.h
├── src/
│   ├── Rectangle.cpp
│   ├── Carre.cpp
│   └── main.cpp
└── build/
```

>Le dossier `build/` contiendra **uniquement les exécutables** (et plus tard les `.o`).

### Compilation

```bash
g++ -I include \
    src/main.cpp src/Rectangle.cpp src/Carre.cpp \
    -o build/prog1
```

(Sur une seule ligne et sans "\" de fin de ligne)

---

### Remarques

> Les attributs sont laissés `public` volontairement pour simplifier l’accès et se concentrer sur :
>
> * la séparation `.h / .cpp`
> * l’organisation d’un projet en dossiers
>
> En programmation orientée objet stricte, on préférera des attributs `private` ou `protected` (voir la version initiale).

---
---
