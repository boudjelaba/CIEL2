// TP07 - Gestion d'un parc de capteurs (fichier de depart a completer)
#include <iostream>
#include <string>
#include <vector>

struct Capteur {
    std::string identifiant{};
    std::string type{};        // "temperature", "humidite" ou "pression"
    double valeur{};
    double seuilMin{};
    double seuilMax{};
    bool actif{};
};

// A COMPLETER : fonctions estEnAlarme, afficherCapteur, afficherParc, chercherCapteur,
//               basculerActivation, moyenneParType, lireReel

int main() {
    std::vector<Capteur> parc{
        {"T1", "temperature", 21.5, 15.0, 27.0, true},
        {"T2", "temperature", 29.0, 15.0, 27.0, true},
        {"H1", "humidite", 45.0, 30.0, 60.0, true},
        {"H2", "humidite", 72.0, 30.0, 60.0, false},
        {"P1", "pression", 1013.0, 950.0, 1050.0, true}
    };

    std::cout << parc.size() << " capteur(s) dans le parc\n";

    // A COMPLETER : menu en boucle

    return 0;
}
