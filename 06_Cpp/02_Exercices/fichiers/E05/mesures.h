// mesures.h - fourni, ne pas modifier
#ifndef MESURES_H
#define MESURES_H

#include <string>
#include <vector>

struct Mesure {
    std::string capteur{};
    double valeur{};
};

// Moyenne des valeurs ; 0.0 si le vecteur est vide
double moyenne(const std::vector<Mesure>& mesures);

// Copie dans resultat la mesure de plus grande valeur ; false si le vecteur est vide
bool chercherMaximum(const std::vector<Mesure>& mesures, Mesure& resultat);

// Nombre de mesures hors de la plage [min ; max]
int compterHorsPlage(const std::vector<Mesure>& mesures, double min, double max);

#endif
