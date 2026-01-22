# TP - ÉVALUATION SQL

**Thème : Supervision d’un réseau informatique**

### DOCUMENTS AUTORISÉS

* Documentation Technique (annexe)
* Ordinateur autorisé uniquement pour les vérifications

### CONSIGNES GÉNÉRALES

* Les requêtes SQL doivent être :

  * syntaxiquement correctes
  * cohérentes avec le schéma fourni

## CONTEXTE

La société **NetCarnus** supervise le réseau informatique du Lycée Carnus afin de détecter les problèmes de performance.

Elle gère :

* les **équipements réseau** (routeurs, switches, serveurs),
* les **interfaces réseau**,
* les **mesures de performance** (débit, latence).

La base de données permet d’analyser l’état et les performances du réseau.

## SCHÉMA DE LA BASE DE DONNÉES

```sql
CREATE TABLE EQUIPEMENT (
    id_equipement INT PRIMARY KEY NOT NULL,
    nom VARCHAR(50),
    type VARCHAR(30),
    adresse_ip VARCHAR(15)
);

CREATE TABLE INTERFACE (
    id_interface INT PRIMARY KEY NOT NULL,
    nom_interface VARCHAR(20),
    id_equipement INT,
    FOREIGN KEY (id_equipement) REFERENCES EQUIPEMENT(id_equipement)
);

CREATE TABLE MESURE_RESEAU (
    id_mesure INT PRIMARY KEY NOT NULL,
    date_mesure DATETIME,
    debit_mbps DECIMAL(6,2),
    latence_ms INT,
    id_interface INT,
    FOREIGN KEY (id_interface) REFERENCES INTERFACE(id_interface)
);
```

### Schéma relationnel

<img src="imA1.png" width="480px">


---

## TRAVAIL DEMANDÉ

### Partie A – Insertion de données (5 points)

1. **(1,5 pt)**
   Ajouter l’équipement suivant :

   * id_equipement : 1
   * nom : Routeur-Principal
   * type : Routeur
   * adresse_ip : 192.168.1.1

2. **(1,5 pt)**
   Ajouter deux interfaces pour cet équipement :

    * (id_interface = 1, nom_interface = eth0, id_equipement = 1)
    * (id_interface = 2, nom_interface = eth1, id_equipement = 1)

3. **(2 pts)**
   Ajouter une mesure réseau :

   * id_mesure : 1
   * date : 20/03/2025 à 10h00
   * débit : 100.5 Mbps
   * latence : 12 ms
   * interface : 1 (interface eth0)

### Partie B – Requêtes de sélection simples (3 points)

1. **(1 pt)** Afficher tous les équipements.
2. **(1 pt)** Afficher le nom et l’adresse IP des équipements.
3. **(1 pt)** Afficher les mesures dont la latence est supérieure à 20 ms.

### Partie C – Requêtes avec jointures (5 points)

1. **(2 pts)**
   Afficher la date de mesure, le débit et le **nom de l’équipement** concerné.

2. **(1,5 pt)**
   Afficher les mesures avec le **nom de l’interface** associée.

3. **(1,5 pt)**
   Afficher toutes les mesures réalisées sur l’interface **eth0**.

### Partie D – Mise à jour et suppression (4 points)

1. **(1,5 pt)**
   Modifier l’adresse IP du routeur principal en `192.168.1.254`.

2. **(1 pt)**
   Augmenter de **5 ms** la latence de toutes les mesures.

3. **(1,5 pt)**
   Supprimer la mesure dont l’identifiant est 1.

### Partie E – Requêtes avancées (GROUP BY) (5 points)

1. **(2 pts)**
   Afficher, pour chaque interface, le **nombre de mesures enregistrées**.

2. **(1,5 pt)**
   Afficher la **latence moyenne** par interface.

3. **(1,5 pt)**
   Afficher les interfaces ayant **plus d’une mesure**.

### Partie F – Question de réflexion (3 points)

1. **(2 pts)**
   Expliquer l’intérêt des **clés étrangères** dans cette base de données.

2. **(1 pt)**
   Expliquer la différence entre `WHERE` et `HAVING`.

