```cmd
git config --global color.diff auto
git config --global color.status auto
git config --global color.branch auto
```


https://www.elektormagazine.fr/articles/micropython-pour-l-esp32-et-ses-copains-partie-1

# CIEL2

[![Développement Web](https://img.shields.io/badge/HTML-CSS-yellow)](https://www.w3.org/)
[![PHP SQL](https://img.shields.io/badge/PHP-MySQL-8A2BE2)](https://www.php.net/)

[![Robot NAO](https://img.shields.io/badge/Robot%20NAO-f2003c)](https://www.aldebaran.com/fr/nao)
[![C++ Arduino](https://img.shields.io/badge/Arduino-teal)](https://docs.arduino.cc/)
[![ESP32](https://img.shields.io/badge/ESP32-green)](https://www.espressif.com/en/products/socs/esp32)
[![RPi](https://img.shields.io/badge/Paspberry%20Pi-1b4d3e)](https://www.raspberrypi.com/)

[![C CPP](https://img.shields.io/badge/C-C++-7b68ee)](https://www.cpp.org/)
[![Python Versions](https://img.shields.io/badge/Python-3-blue)](https://www.python.org/)
[![PS CMD](https://img.shields.io/badge/>__ps->\__cmd-bebebe)](https://www.carnus.fr/)
[![JS JSON](https://img.shields.io/badge/JS-JSON-cb410b)](https://www.carnus.fr/)

[![GitHub git](https://img.shields.io/badge/GitHub-git-fd5800)](https://www.carnus.fr/)
[![Markdown](https://img.shields.io/badge/M%20⬇-191970)](https://www.carnus.fr/)

[![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-2a52be)](https://www.carnus.fr/)
[![Code Blocks](https://img.shields.io/badge/Code::Blocks-008000)](https://www.carnus.fr/)
[![Jupyter](https://img.shields.io/badge/Jupyter%20NoteBook-ff8c00)](https://www.carnus.fr/)

# ⬇️ <cite><font color="(0,68,88)">Mini-Projets CIEL-2</font></cite>

<a href="https://carnus.fr"><img src="https://img.shields.io/badge/Carnus%20Enseignement Supérieur-F2A900?style=for-the-badge" /></a>
<a href="https://carnus.fr"><img src="https://img.shields.io/badge/BTS%20CIEL-2962FF?style=for-the-badge" /></a>

    Professeur - K. B.

### Contact : [Mail](mailto:lycee@carnus.fr)
---

<a id="LOG"></a>
## <cite><font color="blue"> Logiciels et supports : </font></cite>

[![C++ Arduino](https://img.shields.io/badge/C++-Arduino-teal)](https://docs.arduino.cc/)
[![Développement Web](https://img.shields.io/badge/HTML-CSS-yellow)](https://www.w3.org/)
[![PHP SQL](https://img.shields.io/badge/PHP-MySQL-8A2BE2)](https://www.php.net/)
[![Python Versions](https://img.shields.io/badge/Python-3-blue)](https://www.python.org/)
[![RPi](https://img.shields.io/badge/Paspberry%20Pi-red)](https://www.raspberrypi.com/)
[![ESP32](https://img.shields.io/badge/ESP32-green)](https://www.espressif.com/en/products/socs/esp32)

---

### Table des matières :

* <a href="#LOG">Logiciels et supports</a>
* <a href="#PP">Présentation </a>
* <a href="#CC">Cahier des charges et expression du besoin</a>
* <a href="#PR">Prérequis</a>
* <a href="#OB">Objectifs </a>
* <a href="#PDL">Processus de développement logiciel </a>
    * <a href="#PDLE">Exemples d’étapes</a>
* <a href="#POO">Classes C++ </a>

---

<a id="PP"></a>
## <cite><font color="#F2A900"> Présentation : </font></cite>

✍🏼 Le projet consiste à réaliser une interface de gestion (dashboard) dynamique contrôlable par l’outil informatique. Ce système est composé de plusieurs points de contrôle répartis dans des endroits clé de la salle 215.

<a id="CC"></a>
## <cite><font color="#F2A900"> Cahier des charges et expression du besoin : </font></cite>

Le lycée désire se doter d'un système de gestion des capteurs installés dans la salle 215.

Le projet se voudra évolutif, il sera possible dans l'avenir d'ajouter des points de contrôle et de gestion (en fonction des besoins, du budget et de la structure réseau mise en place).

Les points de contrôle seront utilisés afin de renseigner les étudiants et les enseignants sur les valeurs fournies par des capteurs connectés à une carte Raspberry Pi.

<a id="PR"></a>
## <cite><font color="blue"> Prérequis : </font></cite>

* Des connaissances en programmation 
* Des connaissances en développement Web
* Des conaissances en réseaux


<a id="OB"></a>
## <cite><font color="blue"> Objectifs : </font></cite>

* Travailler en équipe et gérer un projet
* Produire de la documentation technique
* Approfondir les connaissances en programmation et en réseaux


---

<a id="PDL"></a>
## Processus de développement logiciel
* Un processus de développement décrit une méthode qui permet de construire, déployer et éventuellement maintenir ou faire évoluer un logiciel. ✌🏼

<a id="PDLE"></a>
### Exemples d’étapes :
- Exigences, Analyse, Conception, Mise en œuvre (implémentation), Test
- Besoin/Faisabilité, Élaboration, Fabrication, Transition/Test

---
---

<a id="POO"></a>
## Programmation Orientée Objet (C++)

[![C CPP](https://img.shields.io/badge/C-C++-7b68ee)](https://www.cpp.org/)

[![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-2a52be)](https://www.carnus.fr/)
[![Code Blocks](https://img.shields.io/badge/Code::Blocks-008000)](https://www.carnus.fr/)


# C++ : Programmation orientée objet

- **Classe** : structure rassemblant à la fois les données (*attributs*) et les méthodes pour les manipuler.
    + un ensemble d’attributs (données membres) décrivant sa structure.
    + un ensemble d’opérations (méthodes, ou fonctions membres) qui lui sont applicables.
- **Objet** : un objet est une instance de classe (variable).
- **Constructeur/Destructeur** : ce sont deux méthodes appelées systématiquement lors de la création (instanciation) d'un objet et de sa destruction (libération). Le constructeur porte le même nom que la classe, le destructeur également, mais précédé du signe `~`.

> L'encapsulation consiste à masquer l'accès à certains attributs et méthodes d'une classe. Elle est réalisée à l'aide des mots clés :
>
>- `private` : les membres privés ne sont accessibles que par les fonctions membres de la classe. La partie privée est aussi appelée réalisation.
>- `protected` : les membres protégés sont comme les membres privés. Mais ils sont aussi accessibles par les fonctions membres des classes dérivées (voir l'héritage).
>- `public` : les membres publics sont accessibles par tous. La partie publique est appelée interface.
Les mots réservés private, protected et public peuvent figurer plusieurs fois dans la déclaration de la classe.


```cpp
#include <iostream>
using namespace std;

class MaClasse {       // La classe
  public:              // Spécifieur d'accès
    int nombre;        // Attribut (int variable)
    string chaine;     // Attribut (string variable)
};

int main() {
  MaClasse objet;  // Créer un objet de MaClasse

  // Accès aux attributs et définition des valeurs
  objet.nombre = 12; 
  objet.chaine = "BTS CIEL";

  // Affichage des valeurs des attributs
  cout << objet.nombre<< "\n"; 
  cout << objet.chaine; 
  return 0;
}
```

## Exemple 1

```cpp
#include <iostream>
using namespace std;

class Ordinateur {
    public:
    string marque;
    int annee;
    int prix;

    public:
    void printDetails(){
        cout << "Marque : " << marque << endl;
        cout << "Année de sortie : " << annee << endl;
        cout << "Prix : " << prix << endl;
    }
};

int main() {
   //création d'un objet de la classe
   Ordinateur ordi_1;

   //modification des attributs de l'objet
   ordi_1.marque = "Apple";
   ordi_1.annee = 2025;
   ordi_1.prix = 2300;

   //Appel de la fonction
   ordi_1.printDetails();
}
```

## Exemple 1 : avec constructeur

```cpp
#include <iostream>
using namespace std;

class Ordinateur {
   public:
   string marque;
   int annee;
   int prix;

   //constructeur
   Ordinateur(string x, int y, int z) {
      marque = x;
      annee = y;
      prix = z;
   }

   public:
   void printDetails(){
      cout << "Marque : " << marque << endl;
      cout << "Année de sortie : " << annee << endl;
      cout << "Prix : " << prix << endl;
   }
};

int main() {
   //créer un objet de classe avec un appel au constructeur
   Ordinateur ordi_1("Apple", 2025, 2300);

   //Appel de la fonction
   ordi_1.printDetails();
}
```


# Diagramme de classe (UML)

La classe est définie par son nom, ses attributs et ses opérations (méthodes). Étant donné que les classes vont être utilisées pour générer le code, il est souhaitable d'utiliser une règle de nommage qui respecte les syntaxes des langages informatiques :

- Les noms des classes commencent par des majuscules et tous les autres éléments par des minuscules.
- Séparer les mots composés par des majuscules.
- Ne pas utiliser de caractères spéciaux ou accentués qui pourraient ne pas être acceptés dans les langages informatiques.

<table>
<tr>
  <th></th>
  </tr>
  <tr>
    <th>NomDeLaClasse</th>
  </tr>

  <tr style="color:#4488EE">
    <td>-nomAttribut1</td>
  </tr>
  <tr style="color:#4488EE">
    <td>-nomAttribut2: type</td>
  </tr>
  <tr>
    <td style="color:#4488EE">-nomAttribut2: type = valeur</td>
  </tr>

  <tr>
  <th></th>
  </tr>
  <tr style="color:#EE8844">
    <td>+nomOperation1()</td>
  </tr>
  <tr style="color:#EE8844">
    <td>#nomOperation2(parametre1)</td>
  </tr>
  <tr style="color:#EE8844">
    <td>-nomOperation3(parametre2: type,parametre3: type)</td>
  </tr>
  <tr style="color:#EE8844">
    <td>#nomOperation4(): typeRetour</td>
  </tr>
  <tr style="color:#EE8844">
    <td>-nomOperation5(parametre2: type, parametre3: type): typeRerour2:typeRetour</td>
  </tr>
  <tr>
  <th></th>
  </tr>
 </table>

### Attributs de classe :

- Les attributs sont affichés dans la deuxième partie.
- Le type d’attribut est affiché après les deux-points.

### Opérations de classe (méthodes) :

- Les opérations sont présentées dans la troisième partie. Ce sont des services que la classe fournit.
- Le type de retour d’une méthode est affiché après les deux-points à la fin de la signature de la méthode.
- Le type de retour des paramètres de méthode est affiché après les deux-points suivant le nom du paramètre.

---

### Programme : Attribut privé ("private")

```cpp
#include <iostream>
using namespace std;
 
class Rectangle {
   public:
      double longueur;
      //! La largeur du rectangle est "privée (private)"
      //! Il est nécessaire d'utiliser un "setter" et un "getter" pour accéder à la largeur
      void setLargeur( double lar ); // Fonction pour : définir (fixer) la largeur
      double getLargeur( void ); // Fonction pour : obtenir (récupérer) la largeur
 
   private:
      double largeur;
};
 
// Définitions des fonctions memebres
double Rectangle::getLargeur(void) {
   return largeur ;
}
 
void Rectangle::setLargeur( double lar ) {
   largeur = lar;
}
 
// fonction main() du programme
int main() {
   Rectangle rectangle1; // Objet rectangle1
 
   // définir la longueur ("public") du rectangle sans fonction membre
   rectangle1.longueur = 12.0; // Juste : parce que la longueur est publique
   cout << "Longueur du rectangle : " << rectangle1.longueur <<endl;
 
   // définir la largeur ("private") de la boîte sans fonction membre : impossible
   // rectangle1.largeur = 10.0; // Erreur : car la largeur est privée
   rectangle1.setLargeur(10.0);  // Utiliser la fonction membre "setter" pour la définir.
   cout << "Largeur du rectangle : " << rectangle1.getLargeur() <<endl;
 
   return 0;
}
```

### Programme : Objet statique

```cpp
#include <iostream>
using namespace std;

class Rectangle {
   public:
    static int objetCount;

    // Définition du constructeur
    Rectangle(double L = 2.0, double l = 3.0) {
      cout <<"Constructeur appelé." << endl;
      longueur = L;
      largeur = l;

      // Incrémenter à chaque fois qu'un objet est créé
      objetCount++;
    }
    double Surface() {
      return longueur * largeur;
    }
      
   private:
    double longueur;   // Longueur du rectangle
    double largeur;    // Largeur du rectangle
};

// Initialiser le membre statique de la classe Rectangle
int Rectangle::objetCount = 0;

int main(void) {
  Rectangle Rectangle1(3.14, 2.5);   // Déclarer Rectangle1
  Rectangle Rectangle2(4.9, 6.2);    // Déclarer Rectangle2

  // Afficher le nombre total d'objets.
  cout << "Total des objets: " << Rectangle::objetCount << endl;

  return 0;
}
```

### Exemple (Constructeur)

```cpp
#include <iostream>
using namespace std;
 
class Rectangle {
   public:
      double longueur;
      double largeur;
      // Constructeur par défaut vide
      //Rectangle() {}
      //

     // Constructeur par défaut
      //Rectangle() {
      //   longueur = 0;
      //   largeur = 0;
      //}


      // Constructeur paramétré     
      Rectangle(double L, double l) {
        longueur = L;
        largeur = l;
      }

      void AffichageResultat() {
        cout << "La longueur du rectangle est : " << longueur << endl;
        cout << "La largeur du rectangle est : " << largeur << endl;
        cout << "La surface du rectangle est : " << longueur*largeur << endl;
      }
};
 
// fonction main() du programme
int main() {
   Rectangle rectangle1(12,10); // Objet rectangle1
   rectangle1.AffichageResultat();
 
   return 0;
}
```

### Exemple (Destructeur)

```cpp
#include <iostream>
using namespace std;
 
class Rectangle {
   public:
      double longueur;
      double largeur;

      // Constructeur   
      Rectangle(double L, double l) {
        longueur = L;
        largeur = l;
        cout << "Le constructeur du rectangle " << longueur << "x" << largeur << " est appelé" <<endl;
      }
      // Destructeur
      ~Rectangle() {
         cout << "Le destructeur du rectangle " << longueur << "x" << largeur << " est appelé" <<endl;
      }
      // Copie constructeur
      Rectangle(const Rectangle& original) {
         longueur = original.longueur;
         largeur = original.largeur;
      }

      void AffichageResultat() {
        cout << "La longueur du rectangle est : " << longueur << endl;
        cout << "La largeur du rectangle est : " << largeur << endl;
        cout << "La surface du rectangle est : " << longueur*largeur << endl;
      }
};
 
// fonction main() du programme
int main() {
   Rectangle rectangle1(12,10); // Objet rectangle1
   rectangle1.AffichageResultat();
   Rectangle rectangle2(212,210); // Objet rectangle2
   rectangle2.AffichageResultat();

   Rectangle rectangle3(rectangle1); // Objet rectangle3
   rectangle3.AffichageResultat();
 
   return 0;
}
```

---

# Héritage

L’héritage est un mécanisme clé de la programmation orientée objet qui permet de créer des relations hiérarchiques entre les classes.

Lorsqu'une relation d'héritage est définie entre deux classes, la sous-classe hérite de tous les attributs et méthodes de la classe mère. C'est à dire que tout se passe comme si les attributs et méthodes de la classe mère avaient été explicitement définies pour la sous-classe. 

Une sous-classe d'une classe donnée représente donc une sorte de cas particulier de cette classe qui possède des attributs et méthodes supplémentaires et spécifiques.

L'héritage évite d'avoir à réécrire le même code à plusieurs reprises. Un ancêtre peut transmettre des propriétés à tous ses descendants. En termes de codage, cela peut nous faire économiser beaucoup de temps et de travail.


- Classe de base - La classe dont les propriétés et les fonctionnalités sont utilisées par une autre classe est appelée la classe de base (super-classe, classe mère ...).
- Classe dérivée - La classe qui reprend les propriétés et les fonctionnalités d’une autre classe est appelée la classe dérivée. (sous-classe ...).

<center>
<img width="300" alt="Diagramme" src="d.png">
</center>

### Programme : Attribut protégé ("protected")

```cpp
#include <iostream>
using namespace std;
 
class Rectangle {
   protected:
      double largeur;
};
 
class Carre:Rectangle { // Carre est la classe dérivée.
   public:
      void setCarreLargeur( double lar );
      double getCarreLargeur( void );
};
 
// Fonctions membres de la classe enfant (dérivée)
double Carre::getCarreLargeur(void) {
   return largeur ;
}
 
void Carre::setCarreLargeur( double lar ) {
   largeur = lar;
}

int main() {
   Carre carre1;
 
   // définir la largeur du rectangle (carré) à l'aide de la fonction membre
   carre1.setCarreLargeur(5.0);
   cout << "Largeur du carré : "<< carre1.getCarreLargeur() << endl;
 
   return 0;
}
```

### Constructeur par défaut

```cpp
#include <iostream>
using namespace std;
 
class Base {
  int x;
  public:
    // Constructeur par défaut
    Base() {
      cout << "Constructeur par défaut de la classe de base" << endl;
    }
};
 
class Herite : public Base {
  int y;
  public:
    // Constructeur par défaut
    Herite() {
      cout << "Constructeur par défaut de la classe derivée" << endl;
    }
    // Constructeur paramétré
    Herite(int i) {
      cout << "Constructeur paramétré de la classe derivée\n";
    }
};
 
int main()
{
    Herite d1;
    Herite d2(12);
}
```

```cpp
#include <iostream>
#include <string>
using namespace std;

class Rectangle {
 public:
  int L;
  int l;
};
class Carre : public Rectangle {
 public:
  int surface() { return L * L; }
};
int main() {
  Carre c;
  c.L = 5;
  cout << "Area: " << s.surface() << endl;
  return 0;
}
```


---

<kbd>cmd + shift + p</kbd>

<kbd> [GitHub](https://github.com/boudjelaba) ↗️ </kbd>

[:arrow_up:](#top)

:exclamation: test

:question: test

:bust_in_silhouette: test

:mag: test

:date: test

:arrow_down: test

:arrow_left: test 

:arrow_right: test

:ok: test

:cl: test

:negative_squared_cross_mark: test


