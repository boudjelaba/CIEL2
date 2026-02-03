# TP C++ — Du diagramme de classes UML au code

**Passer de l’UML au code C++**

### Objectif

Être capable de traduire un diagramme de classes UML simple en code C++ **compilable**, en respectant **strictement** le diagramme fourni.

## 1. Lire un diagramme UML

En UML, une classe est représentée par un **rectangle à 3 compartiments** :

```
-------------------------
|       Classe          |  <-- Nom de la classe
-------------------------
| attributs             |  <-- Attributs / propriétés
-------------------------
| méthodes              |  <-- Méthodes / comportements
-------------------------
```

## 2. Attributs

Les attributs représentent les **données internes** de la classe.

### Visibilité UML

| UML | Signification | C++         |
| --- | ------------- | ----------- |
| `+` | public        | `public`    |
| `-` | private       | `private`   |
| `#` | protected     | `protected` |

Exemple UML :

`- nom : string` → attribut privé `nom` de type `string`

## 3. Méthodes

Les méthodes représentent les **actions** réalisées par la classe.

Exemple UML :

`+ afficher() : void` → méthode publique ne retournant rien

## 4. UML → C++

> En C++, les membres d’une `classe` sont **private par défaut**.
> Il faut donc déclarer explicitement les sections `public:`, `private:` ou `protected:`.

## 5. Traduire une classe simple

### UML

```
-------------------------
|       Personne        |  <-- Nom de la classe
-------------------------
| - nom : string        |  <-- Attributs / propriétés
| - age : int           |
-------------------------
| + Personne(nom:string, age:int) |  <-- Méthodes / comportements
| + afficher() : void   | 
-------------------------
```

### C++ (`Personne.h`)

```cpp
#ifndef PERSONNE_H
#define PERSONNE_H

#include <string>

class Personne {
private:
    std::string nom;
    int age;

public:
    Personne(std::string nom, int age);
    void afficher();
};

#endif
```

## 6. Types UML → Types C++

| UML      | C++           |
| -------- | ------------- |
| `string` | `std::string` |
| `int`    | `int`         |
| `float`  | `float`       |
| `bool`   | `bool`        |
| `void`   | `void`        |

> Ne pas oublier :

```cpp
#include <string>
```

## 7. Méthode UML → Fonction membre

### UML

```
+ afficher() : void
```

### Dans le `.h`

```cpp
void afficher();
```

### Dans le `.cpp`

```cpp
#include "Personne.h"
#include <iostream>

void Personne::afficher() {
    std::cout << nom << " (" << age << " ans)" << std::endl;
}
```

## 8. Constructeur UML → Constructeur C++

### UML

```
+ Personne(nom : string, age : int)
```

### C++

```cpp
Personne(std::string nom, int age);
```

> Le constructeur :

* n’a **pas de type de retour**
* porte exactement le **nom de la classe**

## 9. Séparer `.h` et `.cpp`

| Fichier | Contenu                     |
| ------- | --------------------------- |
| `.h`    | déclaration de la classe    |
| `.cpp`  | implémentation des méthodes |

Le fichier `.h` contient :

* le nom de la classe
* les attributs
* les prototypes des méthodes

Le fichier `.cpp` contient :

* le code des méthodes

> Tous les fichiers `.h` doivent être protégés contre les inclusions multiples.

## 10. Relations entre classes

> Dans un programme réel, une classe n’est généralement pas seule.
> Les classes peuvent être liées entre elles par des relations UML.

### 10.1 Association simple

* Lien « utilise » ou « possède »
* Ligne simple entre classes
* Peut avoir une **cardinalité**

Exemple UML :

```
Personne 1 ---- * Voiture
```

> Une personne peut posséder plusieurs voitures.
> Une voiture appartient à une seule personne.

> En C++, une association peut être représentée par un objet, une référence ou un pointeur, selon le contexte.

### 10.2 Agrégation (relation faible)

* Relation « partie de » **faible**
* Représentée par un **losange vide**
* Les objets existent indépendamment

UML :

```
Equipe <>---- Joueur
```

Traduction courante en C++ :

```cpp
std::vector<Joueur*> joueurs;
```

> Les joueurs existent indépendamment de l’équipe.
> L’équipe ne gère pas leur destruction.

### 10.3 Composition (relation forte)

* Relation « partie de » **forte**
* Représentée par un **losange plein**
* Les objets n’existent pas sans le tout

UML :

```
Maison ◆---- Piece
```

C++ :

```cpp
Piece piece;
```

> Si la maison disparaît, les pièces disparaissent aussi.

### 10.4 Héritage (généralisation)

UML :

```
Etudiant ---|> Personne
```

C++ :

```cpp
class Etudiant : public Personne {
public:
    Etudiant(std::string nom, int age);
    void afficher() override;
};
```

```cpp
Etudiant::Etudiant(std::string nom, int age)
    : Personne(nom, age) {
}
```

> `Etudiant` est une `Personne` et hérite de ses attributs et méthodes.

### 10.5. Les **cardinalités**

| Notation UML  | Signification     |
| ------------- | ----------------- |
| `1`           | exactement un     |
| `0..1`        | zéro ou un        |
| `0..*` ou `*` | zéro ou plusieurs |
| `1..*`        | au moins un       |

Exemple :

```
Bibliotheque 1 ---- * Livre
```

> Une bibliothèque contient **au moins 1 livre et potentiellement plusieurs**.

## 11. Erreurs fréquentes à éviter

* Ajouter des méthodes absentes du diagramme UML
* Oublier `#include <string>`
* Confondre `.h` et `.cpp`
* Mettre tous les membres en `public`
* Ne pas respecter exactement les noms UML

## 12. Méthode de travail conseillée

1. Lire le diagramme UML
2. Lister :

   * les classes
   * les attributs
   * les méthodes
3. Écrire les fichiers `.h`
4. Écrire les fichiers `.cpp`
5. Tester avec un `main.cpp`

---

## Conclusion

> En BTS, **le diagramme UML est la référence**.
> Le code C++ doit le traduire **fidèlement**, sans ajout ni modification.

---
---

## TP : Modélisation UML et Programmation Orientée Objet (C++)

### Contexte général

Vous travaillez au sein d’une entreprise de services numériques spécialisée dans les systèmes embarqués et applicatifs.
On vous demande de **traduire des diagrammes UML en structures C++**, en respectant **strictement** les diagrammes fournis.

## Exercice 1 — Lecture de diagramme UML

### Diagramme UML

```
-------------------------
|        Voiture        |
-------------------------
| - marque : string     |
| - vitesse : int       |
-------------------------
| + accelerer() : void  |
-------------------------
```

### Questions

1. Indiquer le nombre d’attributs de la classe `Voiture`.
2. Préciser le type de chaque attribut.
3. Donner la visibilité de l’attribut `vitesse`.
4. Indiquer le nombre de méthodes publiques.

### Réponses

1. **Nombre d’attributs** :
   → **2**

2. **Types des attributs** :
   → `marque : string`
   → `vitesse : int`

3. **Visibilité de `vitesse`** :
   → **privée** (`-` en UML)

4. **Nombre de méthodes publiques** :
   → **1** (`accelerer()`)

## Exercice 2 — Traduction UML vers C++

### Diagramme UML

```
-------------------------
|        Capteur        |
-------------------------
| - valeur : float      |
-------------------------
| + lire() : float      |
-------------------------
```

### Travail demandé

Écrire **uniquement le fichier `Capteur.h`**, en respectant :

* les visibilités UML
* les types
* les conventions C++

### Réponses `Capteur.h`

```cpp
#ifndef CAPTEUR_H
#define CAPTEUR_H

class Capteur {
private:
    float valeur;

public:
    float lire();
    // Ou float lire() const;
};

#endif
```

## Exercice 3 — Classe avec constructeur

### Diagramme UML

```
-------------------------
|        Produit        |
-------------------------
| - nom : string        |
| - prix : float        |
-------------------------
| + Produit(nom:string, prix:float) |
-------------------------
```

### Travail demandé

* Écrire **le fichier `Produit.h`** correspondant au diagramme UML.

### Réponses

#### `Produit.h`

```cpp
#ifndef PRODUIT_H
#define PRODUIT_H

#include <string>

class Produit {
private:
    std::string nom;
    float prix;

public:
    Produit(std::string nom, float prix);
};

#endif
```

## Exercice 4 — Relation entre classes (agrégation)

### Diagramme UML

```
-------------------------            -------------------------
|       Ordinateur       |<>--------|         Ecran          |
-------------------------            -------------------------
| - marque : string      |          | - taille : int         |
| - ecran : Ecran*       |           -------------------------
-------------------------
```

### Travail demandé

1. Identifier le **type de relation UML** entre `Ordinateur` et `Ecran`.
2. Écrire le fichier `Ordinateur.h` correspondant.

### Réponses

1. Relation : `<>` : **agrégation**
    * `Ordinateur` *a un* `Ecran`
    * L’écran peut exister indépendamment de l’ordinateur.
2. `Ordinateur.h`

```cpp
#ifndef ORDINATEUR_H
#define ORDINATEUR_H

#include <string>
#include "Ecran.h"

class Ordinateur {
private:
    std::string marque;
    Ecran* ecran; // agrégation
};

#endif
```

## Exercice 5 — Héritage

### Diagramme UML

```
        ---------------------
        |      Animal       |
        ---------------------
        | - nom : string    |
        ---------------------
        | + parler() : void |
        ---------------------
                 ▲
                 |
        ---------------------
        |       Chien       |
        ---------------------
        | + parler() : void |
        ---------------------
```

### Travail demandé

1. Écrire la déclaration des classes `Animal` et `Chien` en C++
   *(fichiers `.h` uniquement)*.
2. Indiquer le mot-clé C++ utilisé pour mettre en œuvre l’héritage.

### Réponses (`Animal.h` et `Chien.h`)

1. Déclarations :

```cpp
#ifndef ANIMAL_H
#define ANIMAL_H

#include <string>

class Animal {
private:
    std::string nom;

public:
    void parler();
};

#endif
```

```cpp
#ifndef CHIEN_H
#define CHIEN_H

#include "Animal.h"

class Chien : public Animal {
public:
    void parler();
};

#endif
```

* `Chien` **hérite** de `Animal`
* `Chien` peut redéfinir la méthode `parler()`

2. Mot-clé C++ pour l’héritage
    → **`public`**

## Exercice 6 — Analyse Vrai / Faux

Indiquer si les affirmations suivantes sont **VRAIES ou FAUSSES**.
Justifier brièvement votre réponse.

| Affirmation                                 | Vrai / Faux |
| ------------------------------------------- | ----------- |
| Le symbole `-` en UML correspond à `public` |             |
| Une méthode UML devient une fonction membre |             |
| Une relation UML se traduit par un attribut |             |
| Un constructeur possède un type de retour   |             |

### Réponses

| Affirmation                   | Réponse | Justification attendue |
| ----------------------------- | ------- | ---------------------- |
| `-` signifie public           |  Faux  | `-` = private         |
| Méthode UML → fonction membre |  Vrai | Correspondance directe |
| Relation UML → attribut       |  Vrai | Cas général            |
| Constructeur a un type        |  Faux  | Aucun type de retour  |

## Exercice 7 — Repérer les erreurs UML / C++

### UML

```
-------------------------
|        Compte         |
-------------------------
| - solde : float       |
-------------------------
| + Compte()            |
| + debiter(montant:int)|
-------------------------
```

### Code C++ (erroné)

```cpp
class Compte {
public:
    float solde;

    Compte();
    void debiter(float montant);
};
```

### Travail demandé

- Identifier **au moins trois erreurs** entre le diagramme UML et le code C++ proposé.

### Réponses

### Erreurs possibles (au moins 3) :

1. `solde` est **public** alors qu’il doit être **private**
2. Type du paramètre `montant` incorrect (`float` au lieu de `int`)
3. Non-respect des visibilités UML

## Exercice 8 — Synthèse UML → C++ (.h)

### UML

```
-------------------------
|        Livre          |
-------------------------
| - titre : string      |
| - auteur : string     |
-------------------------
| + Livre(titre:string, |
|         auteur:string)|
| + afficher() : void   |
-------------------------
```

### Travail demandé

1. Écrire **le fichier `Livre.h`** correspondant au diagramme UML.

### Réponses

### `Livre.h`

```cpp
#ifndef LIVRE_H
#define LIVRE_H

#include <string>

class Livre {
private:
    std::string titre;
    std::string auteur;

public:
    Livre(std::string titre, std::string auteur);
    void afficher();
};

#endif
```

---

## Conclusion

> En programmation orientée objet, le diagramme UML est un **contrat**.
> Le code C++ doit respecter :

* les **noms**
* les **types**
* les **visibilités**
* les **relations**

Toute divergence est considérée comme une **erreur de conception**.
