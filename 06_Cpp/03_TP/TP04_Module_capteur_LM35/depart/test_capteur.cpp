// TP04 - Tests unitaires du module capteur (fichier de depart a completer)
// Compilation : g++ -std=c++17 -Wall -Wextra test_capteur.cpp capteur.cpp -o test_capteur
#include <cmath>
#include <iostream>
#include <string>
#include <vector>
#include "capteur.h"

constexpr double TOLERANCE{1e-6};

// Affiche le verdict d'un test ; renvoie 1 en cas d'echec, 0 sinon
int verdict(const std::string& nomDuTest, bool reussi) {
    std::cout << (reussi ? "OK     " : "ECHEC  ") << nomDuTest << '\n';
    return reussi ? 0 : 1;
}

// Vrai si deux double sont egaux a TOLERANCE pres
bool proches(double obtenu, double attendu) {
    return std::fabs(obtenu - attendu) < TOLERANCE;
}

int main() {
    int nbEchecs{0};

    // Exemple de test : a conserver
    nbEchecs += verdict("valeurCanValide(0) = true", valeurCanValide(0));

    // A COMPLETER : un appel a verdict() par cas du tableau de l'enonce

    std::cout << nbEchecs << " test(s) en echec\n";
    return nbEchecs == 0 ? 0 : 1;
}
