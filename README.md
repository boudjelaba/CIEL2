# CIEL2

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
* <a href="#RT">Répartition des tâches </a>
    * <a href="#MP1">Mini-Projet 1</a>
    * <a href="#MP2">Mini-Projet 2 </a>
* <a href="#PR">Prérequis</a>
* <a href="#OB">Objectifs </a>
* <a href="#PDL">Processus de développement logiciel </a>
    * <a href="#PDLE">Exemples d’étapes</a>

---

<a id="PP"></a>
## <cite><font color="#F2A900"> Présentation : </font></cite>

✍🏼 Le projet consiste à réaliser un système de contrôle d'accès et de surveillance dynamique contrôlable par l’outil informatique. Ce système est composé de plusieurs points de contrôle répartis dans des endroits clé de la salle 215. Des informations peuvent être affichées ainsi que des vidéos et des images pour prévenir d’événements spéciaux.

<a id="CC"></a>
## <cite><font color="#F2A900"> Cahier des charges et expression du besoin : </font></cite>

Le lycée désire se doter d'un système de contrôle d'accès dynamique, installé dans la salle 215.

Le projet se voudra évolutif, il sera possible dans l'avenir d'ajouter des points de contrôle (en fonction des besoins, du budget et de la structure réseau mise en place).

Les points de contrôle seront utilisés afin de renseigner les étudiants et les enseignants sur l'état d'occupation de la salle 215, ainsi que des valeurs fournies par des capteurs connectés à une carte Raspberry Pi (Badge RFID, détecteur de mouvement, caméra de surveillance).

Les capteureurs de présence (caméra, détecteur de mouvement) permettront l’extinction automatique des lumières personne n'est présente dans la salle (temporisé 2mn).

<a id="RT"></a>
## <cite><font color="#F2A900"> Répartition des tâches : </font></cite>

<a id="MP1"></a>
### <cite><font color="#F2A900"> Mini-Projet 1 : </font></cite>

| Tâche-1 (E.F. ~~et M.D.~~) | Fonctions à développer et tâches à effectuer |
| -------------- |:----------------------------------------|
| Vidéo surveillance | Installation de la caméra (logiciel)|
|  | Développement en Python du programme de surveillance  |
|  |Sauvegarde des données dans la base de données         |
|  |Documentation logicielle                               |
|  |Rédaction d'un rapport                                 |


|Tâche-2 (R.R. et Y.F.)| Fonctions à développer et tâches à effectuer|
| -------------- |:----------------------------------------|
| Détection de mouvement | Installation du module          |
|  |Développement en C++ (Arduino) du programme de détection|
|  |Sauvegarde des données dans la base de données         |
|  |Documentation logicielle                               |
|  |Rédaction d'un rapport                                 |

|Tâche-3 (V.M.)| Fonctions à développer et tâches à effectuer|
| -------------- |:----------------------------------------|
| Réseaux | Installation du serveur Linux virtualisé       |
|  | Services Web sur serveur                              |
|  | Services SGBD                                         |
|  | Configuration des serveurs Linux, Web, MySQL          |
|  |Documentation logicielle                               |
|  |Rédaction d'un rapport                                 |


<a id="MP2"></a>
### <cite><font color="#F2A900"> Mini-Projet 2 : </font></cite>

| Tâche-1 (A.G. et C.M.) | Fonctions à développer et tâches à effectuer |
| -------------- |:----------------------------------------|
| Contrôle d'accès | Installation du module                |
|  | Développement en C++ (Arduino) du programme de contrôle d'accès  |
|  |Sauvegarde des données dans la base de données         |
|  |Documentation logicielle                               |
|  |Rédaction d'un rapport                                 |


|Tâche-2 (R.C. et H.P.)| Fonctions à développer et tâches à effectuer|
| -------------- |:----------------------------------------|
| QR code et authentification | Développement en PHP du logiciel d'identification |
|  |Développement du logiciel de réservation               |
|  |Sauvegarde des données dans la base de données         |
|  |Documentation logicielle                               |
|  |Rédaction d'un rapport                                 |

|Tâche-3 (M.A.-B.)| Fonctions à développer et tâches à effectuer|
| -------------- |:----------------------------------------|
| Réseaux | Installation du serveur Linux virtualisé       |
|  | Services Web sur serveur                              |
|  | Services SGBD                                         |
|  | Configuration des serveurs Linux, Web, MySQL          |
|  |Documentation logicielle                               |
|  |Rédaction d'un rapport                                 |



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
