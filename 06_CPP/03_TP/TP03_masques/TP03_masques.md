# TP06 — Commander des voyants avec des masques

**Durée indicative :** 30 à 45 minutes  
**Prérequis :** chapitre 6 — opérations bit à bit et masques

## Objectif

Écrire un programme C++ qui teste, active, désactive et inverse des bits pour commander quatre voyants.

## Situation

Les quatre bits de poids faible d’un entier représentent l’état des voyants. Un bit à `1` signifie que le voyant est allumé.

| Bit | Voyant |
|---:|---|
| 0 | Alimentation |
| 1 | Capteur |
| 2 | Communication |
| 3 | Alarme |

L’état initial est `0b1001` : l’alimentation et l’alarme sont allumées.

## Travail demandé

### 1. Prévoir les états à la main

Complétez le tableau en écrivant chaque état sur quatre bits.

| Étape | Opération | État |
|---|---|---|
| Départ | — | `1001` |
| 1 | Activer le voyant Capteur | |
| 2 | Vérifier si le voyant Alarme est allumé | |
| 3 | Éteindre le voyant Alarme | |
| 4 | Inverser l’état du voyant Communication | |

Pour chaque changement d’état, posez l’opération bit à bit et indiquez le masque utilisé.

### 2. Compléter le programme

Complétez les parties marquées `À compléter`. L’affichage binaire utilise `std::bitset<4>`.

```cpp
#include <bitset>
#include <iostream>

int main()
{
    constexpr unsigned int ALIMENTATION{1u << 0};
    constexpr unsigned int CAPTEUR{1u << 1};
    constexpr unsigned int COMMUNICATION{1u << 2};
    constexpr unsigned int ALARME{1u << 3};

    unsigned int etat{0b1001};

    std::cout << "Depart       : " << std::bitset<4>{etat} << '\n';

    // 1. Activer le voyant Capteur.
    // À compléter
    std::cout << "Capteur actif: " << std::bitset<4>{etat} << '\n';

    // 2. Tester si le voyant Alarme est allumé.
    // À compléter : afficher "Alarme allumee" ou "Alarme eteinte".

    // 3. Éteindre le voyant Alarme.
    // À compléter
    std::cout << "Alarme eteinte: " << std::bitset<4>{etat} << '\n';

    // 4. Inverser l’état du voyant Communication.
    // À compléter
    std::cout << "Communication inversee: "
              << std::bitset<4>{etat} << '\n';

    return 0;
}
```

### 3. Vérifier le résultat

1. Comparez l’affichage du programme avec votre tableau.
2. Indiquez quels voyants sont allumés à la fin.
3. Expliquez pourquoi les autres bits ne changent pas lorsqu’on utilise un masque.

## Livrables

- Le tableau de calcul complété.
- Le fichier C++ complété.
- Une courte réponse à la question 3.

## Barème indicatif

| Critère | Points |
|---|---:|
| Calcul manuel des états et des masques | 6 |
| Activation, test, désactivation et inversion en C++ | 8 |
| Affichage et comparaison avec les calculs | 4 |
| Explication et qualité du code | 2 |
| **Total** | **20** |
