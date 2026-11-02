// TP05 - Decodeur de trames de capteurs (fichier de depart a completer)
#include <cstddef>
#include <cstdint>
#include <iomanip>
#include <iostream>
#include <string>
#include <vector>

// A COMPLETER : constantes (en-tete, cle, codes de verification, types de mesure...)

// A COMPLETER : fonctions afficherTrame, calculerSomme, verifierTrame,
//               demasquerDonnees, texteVersDixiemes

int main() {
    // Trames de test. "trames" est un vecteur dont chaque element est
    // lui-meme un vecteur d'octets : trames[0] est la premiere trame,
    // trames[0][1] est le deuxieme octet de la premiere trame.
    const std::vector<std::vector<std::uint8_t>> trames{
        {0xAA, 0x12, 0x01, 0x03, 0x68, 0x0D, 0x90, 0x4F},
        {0xAA, 0x07, 0x02, 0x03, 0x6F, 0x0A, 0x96, 0x5F},
        {0xAA, 0x21, 0x01, 0x03, 0x77, 0x04, 0x90, 0x6A},
        {0xAA, 0x12, 0x01, 0x03, 0x68, 0x0D, 0x90, 0x4E},
        {0xAB, 0x12, 0x01, 0x03, 0x68, 0x0D, 0x90, 0x4E},
        {0xAA, 0x07, 0x02, 0x04, 0x6F, 0x0A, 0x96, 0x58}
    };

    std::cout << trames.size() << " trame(s) a decoder\n";

    // A COMPLETER : boucle de decodage, bilan, tests unitaires de texteVersDixiemes

    return 0;
}
