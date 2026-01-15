# TP d’évaluation - Bases de données SQL

## DOCUMENTS AUTORISÉS

* **Documentation technique SQL fournie en annexe**
* **Aucun ordinateur autorisé** (travail sur feuille uniquement)

**CONSIGNES GÉNÉRALES**

* Les requêtes SQL doivent être :

  * **syntaxiquement correctes**,
  * **logiquement cohérentes** au regard de la base de données fournie.
* Les réponses doivent être **justifiées** lorsque cela est demandé.
* Une **syntaxe SQL standard** est attendue.
  Des variantes mineures sont acceptées si la logique est correcte.

*Le schéma relationnel et les tables SQL sont fournis. Les réponses porteront uniquement sur les requêtes demandées.*

---

## CONTEXTE

La société **TechRepair** est une entreprise de maintenance informatique pour les PME.
Elle gère :

* ses **clients**
* les **techniciens**
* les **interventions** réalisées chez les clients

La direction souhaite exploiter la base de données afin d’obtenir des informations de suivi et de gestion.

---

## SCHÉMA DE LA BASE DE DONNÉES

### Diagramme entité–association (MCD)

<img src="im1.png" width="420px">

> **Légende – cardinalités des relations : (Rappel)**
>
> * `|` : un
> * `o` : zéro (optionnel)
> * `<` (patte de corbeau (d'oie)) : plusieurs
>
> Exemple :
>
> * `||—o<` signifie : *un élément peut être associé à zéro ou plusieurs éléments*
> * une relation se lit dans les deux sens entre les entités reliées

---

### Schéma relationnel de référence

> Les tables relationnelles correspondant au diagramme sont fournies ci-dessous à titre de référence.
> Il n’est pas demandé de créer ni de modifier ces tables.

```sql
CREATE TABLE CLIENT (
    id_client INT PRIMARY KEY NOT NULL,
    nom VARCHAR(50),
    adresse VARCHAR(100),
    telephone VARCHAR(15)
);

CREATE TABLE TECHNICIEN (
    id_technicien INT PRIMARY KEY NOT NULL,
    nom VARCHAR(50),
    specialite VARCHAR(50)
);

CREATE TABLE INTERVENTION (
    id_intervention INT PRIMARY KEY NOT NULL,
    date_intervention DATE,
    description VARCHAR(100),
    duree INT,
    id_client INT,
    id_technicien INT,
    FOREIGN KEY (id_client) REFERENCES CLIENT(id_client),
    FOREIGN KEY (id_technicien) REFERENCES TECHNICIEN(id_technicien)
);
```

---

## 4. Travail demandé

### Partie A – Insertion de données (5 points)

1. (1,5 pt) Ajouter le client suivant : 

   * id_client : 1
   * nom : Dupont
   * adresse : Avenue de Bourran, 12000 Rodez
   * téléphone : 0601020304

2. (1,5 pt) Ajouter deux techniciens : 

   * (1, Martin, Réseaux)
   * (2, Bernard, Systèmes)

3. (2 pts) Ajouter une intervention réalisée le 15/03/2025 chez le client Dupont, par le technicien Martin, durée 120 minutes, description : « Maintenance serveur ».
    > *On considère que l’identifiant de l’intervention ajoutée est 1.*

### Partie B – Requêtes de sélection simples (3 points)

1. (1 pt) Afficher la liste de tous les clients.
2. (1 pt) Afficher le nom et la spécialité de tous les techniciens.
3. (1 pt) Afficher toutes les interventions dont la durée est supérieure à 60 minutes.

### Partie C – Requêtes avec jointures (5 points)

> L’utilisation de `JOIN … ON …` est recommandée.

1. (2 pts) Afficher la date et la description des interventions avec le **nom du client** concerné.
2. (1,5 pt) Afficher les interventions avec le **nom du technicien** qui les a réalisées.
3. (1,5 pt) Afficher les interventions réalisées par le technicien « Martin ».

### Partie D – Mise à jour et suppression (4 points)

1.  (1,5 pt) Modifier le numéro de téléphone du client Dupont en `0611223344`.
2.  (1 pt) Augmenter de 30 minutes la durée de toutes les interventions.
3.  (1,5 pt) Supprimer l’intervention dont l’identifiant est 1.

### Partie E – Question de réflexion (2 points)

1.  (2 pts) Expliquer l’intérêt des **clés étrangères** dans la table INTERVENTION.

### Partie F – Lecture du diagramme (5 points)

1.  (1 pt) Identifier les **entités** présentes dans le diagramme.

2.  (1 pt) Pour chaque entité, indiquer :

    * la **clé primaire**
    * son rôle dans la base de données

3.  (1 pt) À partir du diagramme :
    a. Combien d’interventions maximum un client peut-il avoir ?
    b. Une intervention peut-elle concerner plusieurs clients ? Justifier.
    c. Combien d’interventions un technicien peut-il réaliser ?

4.  (1 pt) Indiquer :

    * dans quelle table se trouvent les **clés étrangères**
    * à quelles tables elles font référence

5.  (1 pt) Expliquer ce qui se passerait si :

    * on tente d’ajouter une intervention avec un `id_client` inexistant
    * on supprime un client ayant des interventions associées

---
