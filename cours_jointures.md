# SQL – Les jointures

## 1. Introduction

> Dans une base de données, *“Les infos sont souvent séparées en plusieurs tables.”*

Exemple :

* Table `Etudiants` → noms
* Table `Notes` → notes
* on veut **nom + note**

➡ Une jointure permet d’afficher **le nom + la note**

> Jointure = relier des lignes

---

## 2. Tables d’exemple

<img src="t06.png" width="200px">

* `PK = clé primaire`
* `FK = clé étrangère, référence une autre table`

* Cardinalité (1 → N) 
* Schéma relationnel : 1 étudiant → N notes (clé étrangère Notes.id_etudiant)

```sql
CREATE TABLE Etudiants (
    id INT PRIMARY KEY,
    nom VARCHAR(100) NOT NULL
);

CREATE TABLE Notes (
    id INT PRIMARY KEY,
    id_etudiant INT NOT NULL,
    note INT NOT NULL,
    CONSTRAINT fk_notes_etudiants
        FOREIGN KEY (id_etudiant)
        REFERENCES Etudiants(id)
);
```

<div style="display:grid; grid-template-columns:1fr 1fr; gap:20px;">

<div>

**Etudiants**

| id | nom |
|----|-----|
| 1 | Alice |
| 2 | Bob |
| 3 | Charlie |

</div>

<div>

**Notes**

| id_etudiant | note |
|-------------|------|
| 1 | 15 |
| 1 | 12 |
| 3 | 18 |

</div>

</div>

Lien :

```
Etudiants.id = Notes.id_etudiant
```

* **Etudiants** → table parent
* **Notes** → table enfant
* Relation **1 étudiant – N notes**

> Une jointure relie des **lignes compatibles**, pas des tables entières.

---

## 3. INNER JOIN – seulement ce qui correspond

**INNER JOIN = intersection** *“Seulement ce qui existe des deux côtés”*

```
INNER JOIN = zone commune
```

> **Pas de correspondance → pas de ligne**

```sql
SELECT e.nom, n.note
FROM Etudiants e
INNER JOIN Notes n
ON e.id = n.id_etudiant;
```

<div style="display:grid; grid-template-columns:1fr 1fr 1fr; gap:20px;">

<div>

**Etudiants**

| id | nom |
|----|-----|
| 1 | Alice |
| 2 | Bob |
| 3 | Charlie |

</div>

<div>

**Notes**

| id_etudiant | note |
|-------------|------|
| 1 | 15 |
| 1 | 12 |
| 3 | 18 |

</div>

<div>

**Résultat (INNER JOIN)**

| nom | note |
|-----|------|
| Alice | 15 |
| Alice | 12 |
| Charlie | 18 |

</div>

</div>

➡ **Bob n’apparaît pas**
➡ Pas de correspondance → pas de ligne (pas de note)

> Une ligne dans `Etudiants` peut produire **plusieurs lignes** dans le résultat

> **INNER JOIN = ce qui existe dans les deux tables**

---

## 4. LEFT JOIN – tout de la table de gauche

**LEFT JOIN = table de gauche prioritaire**

```
LEFT JOIN = TOUT à gauche
```

> S’il n’y a rien à droite → `NULL`
> **L’ordre des tables est important**

```sql
SELECT e.nom, n.note
FROM Etudiants e
LEFT JOIN Notes n
ON e.id = n.id_etudiant;
```

<div style="display:grid; grid-template-columns:1fr 1fr 1fr; gap:20px;">

<div>

**Etudiants**

| id | nom |
|----|-----|
| 1 | Alice |
| 2 | Bob |
| 3 | Charlie |

</div>

<div>

**Notes**

| id_etudiant | note |
|-------------|------|
| 1 | 15 |
| 1 | 12 |
| 3 | 18 |

</div>

<div>

**Résultat (LEFT JOIN)**

| nom | note |
|-----|------|
| Alice | 15 |
| Alice | 12 |
| Bob | NULL |
| Charlie | 18 |

</div>

</div>

➡ **Bob apparaît**
➡ `NULL` = aucune correspondance trouvée

> `NULL` ne vient **pas de la table**, mais du **résultat de la jointure**

> **LEFT JOIN = TOUJOURS tout de la table de gauche**

---

## 5. ON vs WHERE

### ON

**Comment relier les tables**

```sql
ON e.id = n.id_etudiant
```

### WHERE

**Quelles lignes garder après la jointure**

```sql
WHERE n.note >= 15
```

Règle :

| Clause | Rôle    |
| ------ | ------- |
| ON     | relier  |
| WHERE  | filtrer |

> **ON relie, WHERE filtre**
> **ON fabrique les couples, WHERE élimine après**

### Exemple de requête

```sql
SELECT e.nom, n.note
FROM Etudiants e
LEFT JOIN Notes n
ON e.id = n.id_etudiant
WHERE n.note >= 15;
```

<div style="display:grid; grid-template-columns:1fr 1fr 1fr; gap:20px;">

<div>

**Etudiants**

| id | nom |
|----|-----|
| 1 | Alice |
| 2 | Bob |
| 3 | Charlie |

</div>

<div>

**Notes**

| id_etudiant | note |
|-------------|------|
| 1 | 15 |
| 1 | 12 |
| 3 | 18 |

</div>

<div>

**Résultat**

| nom | note |
|-----|------|
| Alice | 15 |
| Charlie | 18 |

</div>

</div>


➡ Bob disparaît
➡ Les lignes avec `NULL` sont éliminées par le `WHERE`

**Règle**

| Clause  | Effet                                       |
| ------- | ------------------------------------------- |
| `ON`    | décide **quelles lignes peuvent se relier** |
| `WHERE` | supprime des lignes **après la jointure**   |

> Un `WHERE` sur la table de droite peut **annuler l’effet du LEFT JOIN**

---

## 6. Résumé

```
INNER JOIN → seulement les correspondances
LEFT JOIN  → tout de la table de gauche
NULL       → absence de correspondance
ON         → comment relier
WHERE      → quoi garder
```

* RIGHT JOIN = LEFT JOIN en inversant les tables
* FULL JOIN = tout, même sans correspondance
* > Mettre une condition sur la table de droite dans le `WHERE` transforme un `LEFT JOIN` en `INNER JOIN`

---

## 7. Exercice d'application

### Objectif 

* Voir concrètement :

  * disparition avec INNER
  * apparition de NULL avec LEFT
  * différence ON / WHERE

### Mise en place

Tables fournies :

**Table `Etudiants`**

| id | nom    | age |
|----|--------|-----|
| 1  | Alice  | 20  |
| 2  | Bob    | 21  |
| 3  | Charlie| 22  |

**Table `Notes`**

| id_etudiant | matiere | note |
|-------------|---------|------|
| 1           | Maths   | 15   |
| 1           | Physique| 12   |
| 3           | Maths   | 18   |

```sql
CREATE TABLE Etudiants (
  id INT PRIMARY KEY,
  nom VARCHAR(20),
  age INT
);

CREATE TABLE Notes (
  id_etudiant INT,
  matiere VARCHAR(20),
  note INT
);
```

### INNER JOIN

```sql
SELECT e.nom, n.note
FROM Etudiants e
INNER JOIN Notes n
ON e.id = n.id_etudiant;
```

<div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 20px;">

<div>

**Etudiants**

| id | nom     |
|----|---------|
| 1  | Alice   |
| 2  | Bob     |
| 3  | Charlie |

</div>

<div>

**Notes**

| id_etudiant | note |
|-------------|------|
| 1           | 15   |
| 1           | 12   |
| 3           | 18   |

</div>

<div>

**Résultat (INNER JOIN)**

| nom     | note |
|---------|------|
| Alice   | 15   |
| Alice   | 12   |
| Charlie | 18   |

</div>

</div>

* Qui manque ?
* Pourquoi Bob n’apparaît pas ?

> **Une ligne dans `Etudiants` peut produire plusieurs lignes dans le résultat**

### LEFT JOIN

```sql
SELECT e.nom, n.note
FROM Etudiants e
LEFT JOIN Notes n
ON e.id = n.id_etudiant;
```

<div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 20px;">

<div>

**Etudiants**

| id | nom     |
|----|---------|
| 1  | Alice   |
| 2  | Bob     |
| 3  | Charlie |

</div>

<div>

**Notes**

| id_etudiant | note |
|-------------|------|
| 1           | 15   |
| 1           | 12   |
| 3           | 18   |

</div>

<div>

**Résultat (LEFT JOIN)**

| nom     | note |
|---------|------|
| Alice   | 15   |
| Alice   | 12   |
| Bob     | NULL |
| Charlie | 18   |

</div>

</div>

* Qui est revenu ? → **Bob**
* Pourquoi `NULL` ? → aucune ligne correspondante dans `Notes`

> `NULL` ne vient **pas de la table**, mais du **résultat de la jointure**

### ON vs WHERE

**Version A (correcte)**

```sql
SELECT e.nom, n.note
FROM Etudiants e
LEFT JOIN Notes n
ON e.id = n.id_etudiant
AND n.note >= 15;
```

<div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 20px;">

<div>

**Etudiants**

| id | nom     |
|----|---------|
| 1  | Alice   |
| 2  | Bob     |
| 3  | Charlie |

</div>

<div>

**Notes (note ≥ 15)**

| id_etudiant | note |
|-------------|------|
| 1           | 15   |
| 3           | 18   |

</div>

<div>

**Résultat (LEFT JOIN + condition dans ON)**

| nom     | note |
|---------|------|
| Alice   | 15   |
| Bob     | NULL |
| Charlie | 18   |

</div>

</div>

* La condition est appliquée **pendant la jointure**
* Bob est conservé (LEFT JOIN respecté)

**Version B (piège)**

```sql
SELECT e.nom, n.note
FROM Etudiants e
LEFT JOIN Notes n
ON e.id = n.id_etudiant
WHERE n.note >= 15;
```

<div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 20px;">

<div>

**Etudiants**

| id | nom     |
|----|---------|
| 1  | Alice   |
| 2  | Bob     |
| 3  | Charlie |

</div>

<div>

**Notes**

| id_etudiant | note |
|-------------|------|
| 1           | 15   |
| 1           | 12   |
| 3           | 18   |

</div>

<div>

**Résultat (LEFT JOIN + WHERE)**

| nom     | note |
|---------|------|
| Alice   | 15   |
| Charlie | 18   |

</div>

</div>

> Pourquoi Bob disparaît dans la version B ?

* Le `WHERE` s’applique **après la jointure**
* Les lignes avec `NULL` sont supprimées
* **Bob disparaît**

> Un `WHERE` sur la table de droite peut **annuler l’effet du LEFT JOIN**

---
---

# TP SQL – Jointures

**Gestion d’un parc informatique**

## Objectifs

* relier des tables avec une **jointure**
* choisir entre **INNER JOIN** et **LEFT JOIN**
* comprendre la différence entre **ON** et **WHERE**
* interpréter les valeurs **NULL**

## Rappel

* `INNER JOIN` → seulement les correspondances
* `LEFT JOIN` → tout de la table de gauche
* `ON` → relier
* `WHERE` → filtrer
* `NULL` → pas de correspondance

## Contexte

Parc informatique d’un établissement :

* **Salles**
* **Équipements**
* **Techniciens**

Les données sont réparties → **jointures nécessaires**.

## Schéma de la base de données - tables et données

<img src="t4.png" width="320px">

### Table `Salles`

| id  | nom_salle | batiment | capacite |
|-----|-----------|----------|----------|
| 1   | A101      | A        | 20       |
| 2   | B202      | B        | 15       |
| 3   | C303      | C        | 25       |

### Table `Equipements`

| id  | nom_equipement | type          | adresse_ip   | id_salle [FK] |
|-----|----------------|---------------|---------------|---------------|
| 101 | PC-Prof        | Ordinateur    | 192.168.1.1   | 1             |
| 102 | Switch-Central | Switch        | 192.168.1.254 | 1             |
| 103 | Imprimante     | Imprimante    | 192.168.2.1   | 2             |
| 104 | Routeur        | Routeur       | 192.168.1.253 | 3             |

### Table `Techniciens`

| id  | nom_technicien | specialite   | id_salle_affectee [FK] |
|-----|----------------|--------------|------------------------|
| 1   | Jean Dupont    | Réseau       | 1                      |
| 2   | Marie Martin   | Matériel     | 2                      |
| 3   | Paul Durand    | Sécurité     | NULL                   |

> `[FK] = clé étrangère, référence une autre table`

---

## Partie 1 — Relier deux tables

### 1. Équipements et salles

**Afficher la liste des équipements avec le nom de la salle associée.**

* Colonnes : `nom_equipement`, `type`, `nom_salle`
* Nombre de lignes attendu : **4**

Indice :

> Tous les équipements sont dans une salle.

### 2. Techniciens et salles (affectation)

**Afficher tous les techniciens avec le nom de leur salle (si affectés).**

* Colonnes : `nom_technicien`, `specialite`, `nom_salle`
* Nombre de lignes attendu : **3**
* Les techniciens sans salle doivent apparaître avec `NULL`

Indice :

> Certains techniciens ne sont pas affectés.

---

## Partie 2 — INNER vs LEFT

### 3. Différence INNER / LEFT

a) Afficher les **techniciens affectés à une salle**
b) Afficher **tous les techniciens**, même sans salle

> Deux requêtes différentes
> Comparer les résultats

> Qui disparaît avec INNER JOIN ? Pourquoi ?

### 4. Salles et équipements (LEFT JOIN)

**Afficher toutes les salles avec leurs équipements (s’il y en a).**

* Colonnes : `nom_salle`, `nom_equipement`, `type`
* Une salle sans équipement doit apparaître avec `NULL`

Indice :

> Quelle table doit être à gauche ?

---

## Partie 3 — ON vs WHERE

### 5. Filtrer les équipements

**Afficher uniquement les équipements de type `Ordinateur` ou `Switch`, avec le nom de la salle.**

* Colonnes : `nom_equipement`, `type`, `nom_salle`
* Nombre de lignes attendu : **2**

### 6. ON vs WHERE 

**Objectif :**

Afficher **toutes les salles**, mais seulement les équipements de type `Ordinateur`.

#### Version A

Filtrage dans `ON`

#### Version B

Filtrage dans `WHERE`

> Comparer les résultats
> Repérer :

* apparition/disparition de lignes
* impact sur les `NULL`

> Pourquoi une version fait disparaître certaines salles ?

---

## Partie 4 — Cas concrets

### 7. Équipements d’une salle gérée par un technicien Réseau

**Afficher les équipements situés dans une salle affectée à un technicien spécialisé en `Réseau`.**

* Colonnes : `nom_equipement`, `type`, `nom_salle`
* Nombre de lignes attendu : **2**

Indice :

> Plusieurs jointures nécessaires, mais toujours la même logique.

### 8. Salles sans technicien

**Afficher les salles qui n’ont aucun technicien affecté.**

* Colonne : `nom_salle`
* Nombre de lignes attendu : **1**

Indice :

> `LEFT JOIN` + `IS NULL`

---

## Corrigé – TP SQL : Jointures

## 1. Équipements et salles

**Afficher la liste des équipements avec le nom de la salle associée.**

```sql
SELECT e.nom_equipement, e.type, s.nom_salle
FROM Equipements e
INNER JOIN Salles s
ON e.id_salle = s.id;
```

<div style="display:grid; grid-template-columns:1fr 1fr 1fr 1fr; gap:20px;">

<div>

**Salles**

| id | nom_salle |
|----|-----------|
| 1  | A101 |
| 2  | B202 |
| 3  | C303 |

</div>

<div>

**Equipements**

| id | nom_equipement | id_salle |
|----|---------------|----------|
|101 | PC-Prof | 1 |
|102 | Switch-Central | 1 |
|103 | Imprimante | 2 |
|104 | Routeur | 3 |

</div>

<div>

**Techniciens**

| id | nom |
|----|-----|
| 1  | Jean |
| 2  | Marie |
| 3  | Paul |

</div>

<div>

**Résultat**

| nom_equipement | type | nom_salle |
|----------------|------|-----------|
| PC-Prof | Ordinateur | A101 |
| Switch-Central | Switch | A101 |
| Imprimante | Imprimante | B202 |
| Routeur | Routeur | C303 |

</div>

</div>

* Chaque équipement est lié à une salle
* `INNER JOIN` suffit
* `ON` indique **comment relier** les lignes

**Résultat : 4 lignes**

## 2. Techniciens et salles

**Afficher tous les techniciens avec le nom de leur salle (si affectés).**

```sql
SELECT t.nom_technicien, t.specialite, s.nom_salle
FROM Techniciens t
LEFT JOIN Salles s
ON t.id_salle_affectee = s.id;
```

<div style="display:grid; grid-template-columns:1fr 1fr 1fr 1fr; gap:20px;">

<div>

**Salles**

| id | nom_salle |
|----|-----------|
| 1 | A101 |
| 2 | B202 |
| 3 | C303 |

</div>

<div>

**Equipements**

| id | nom |
|----|-----|
| …  | … |

</div>

<div>

**Techniciens**

| nom_technicien | id_salle |
|----------------|----------|
| Jean Dupont | 1 |
| Marie Martin | 2 |
| Paul Durand | NULL |

</div>

<div>

**Résultat (LEFT JOIN)**

| nom_technicien | specialite | nom_salle |
|----------------|------------|-----------|
| Jean Dupont | Réseau | A101 |
| Marie Martin | Matériel | B202 |
| Paul Durand | Sécurité | NULL |

</div>

</div>

* `LEFT JOIN` conserve **tous les techniciens**
* `NULL` signifie *pas de salle affectée*

**Résultat : 3 lignes**

## 3. Différence INNER JOIN / LEFT JOIN

### a) Techniciens affectés à une salle

```sql
SELECT t.nom_technicien, s.nom_salle
FROM Techniciens t
INNER JOIN Salles s
ON t.id_salle_affectee = s.id;
```

➡ Paul Durand disparaît (pas de salle)

### b) Tous les techniciens

```sql
SELECT t.nom_technicien, s.nom_salle
FROM Techniciens t
LEFT JOIN Salles s
ON t.id_salle_affectee = s.id;
```

➡ Paul Durand apparaît avec `NULL`

## 4. Salles et équipements

**Afficher toutes les salles avec leurs équipements (s’il y en a).**

```sql
SELECT s.nom_salle, e.nom_equipement, e.type
FROM Salles s
LEFT JOIN Equipements e
ON s.id = e.id_salle;
```

<div style="display:grid; grid-template-columns:1fr 1fr 1fr 1fr; gap:20px;">

<div>

**Salles**

| id | nom_salle |
|----|-----------|
| 1 | A101 |
| 2 | B202 |
| 3 | C303 |

</div>

<div>

**Equipements**

| nom_equipement | id_salle |
|----------------|----------|
| PC-Prof | 1 |
| Switch-Central | 1 |
| Imprimante | 2 |
| Routeur | 3 |

</div>

<div>

**Techniciens**

| id | nom |
|----|-----|
| …  | … |

</div>

<div>

**Résultat**

| nom_salle | nom_equipement | type |
|-----------|----------------|------|
| A101 | PC-Prof | Ordinateur |
| A101 | Switch-Central | Switch |
| B202 | Imprimante | Imprimante |
| C303 | Routeur | Routeur |

</div>

</div>

* La table prioritaire est `Salles`
* Les salles sans équipement auraient `NULL`

## 5. Filtrer les équipements

**Afficher les équipements de type Ordinateur ou Switch avec leur salle.**

```sql
SELECT e.nom_equipement, e.type, s.nom_salle
FROM Equipements e
INNER JOIN Salles s
ON e.id_salle = s.id
WHERE e.type IN ('Ordinateur', 'Switch');
```

* Le filtrage se fait dans `WHERE`
* La jointure reste intacte

**Résultat : 2 lignes**

## 6. ON vs WHERE 

### Version A — Filtrage dans ON

```sql
SELECT s.nom_salle, e.nom_equipement, e.type
FROM Salles s
LEFT JOIN Equipements e
ON s.id = e.id_salle
AND e.type = 'Ordinateur';
```

<div style="display:grid; grid-template-columns:1fr 1fr 1fr 1fr; gap:20px;">

<div>

**Salles**

| id | nom_salle |
|----|-----------|
| 1 | A101 |
| 2 | B202 |
| 3 | C303 |

</div>

<div>

**Equipements**

| nom | type | id_salle |
|-----|------|----------|
| PC-Prof | Ordinateur | 1 |
| Switch-Central | Switch | 1 |
| Imprimante | Imprimante | 2 |
| Routeur | Routeur | 3 |

</div>

<div>

**Techniciens**

| id | nom |
|----|-----|
| …  | … |

</div>

<div>

**Résultat (filtre dans ON)**

| nom_salle | nom_equipement | type |
|-----------|----------------|------|
| A101 | PC-Prof | Ordinateur |
| B202 | NULL | NULL |
| C303 | NULL | NULL |

</div>

</div>

➡ Toutes les salles apparaissent
➡ Les salles sans ordinateur → `NULL`

### Version B — Filtrage dans WHERE

```sql
SELECT s.nom_salle, e.nom_equipement, e.type
FROM Salles s
LEFT JOIN Equipements e
ON s.id = e.id_salle
WHERE e.type = 'Ordinateur';
```

<div style="display:grid; grid-template-columns:1fr 1fr 1fr 1fr; gap:20px;">

<div>

**Salles**

| nom_salle |
|-----------|
| A101 |
| B202 |
| C303 |

</div>

<div>

**Equipements**

| nom | type |
|-----|------|
| PC-Prof | Ordinateur |
| Switch-Central | Switch |
| … | … |

</div>

<div>

**Techniciens**

| … |
|---|

</div>

<div>

**Résultat (WHERE)**

| nom_salle | nom_equipement | type |
|-----------|----------------|------|
| A101 | PC-Prof | Ordinateur |

</div>

</div>

➡ Les salles (B202 et C303) sans ordinateur disparaissent

**Conclusion :**

> `ON` influence la jointure
> `WHERE` filtre le résultat final

## 7. Équipements d’une salle gérée par un technicien Réseau

```sql
SELECT e.nom_equipement, e.type, s.nom_salle
FROM Techniciens t
INNER JOIN Salles s
ON t.id_salle_affectee = s.id
INNER JOIN Equipements e
ON e.id_salle = s.id
WHERE t.specialite = 'Réseau';
```

<div style="display:grid; grid-template-columns:1fr 1fr 1fr 1fr; gap:20px;">

<div>

**Techniciens**

| nom | specialite | id_salle |
|-----|------------|----------|
| Jean Dupont | Réseau | 1 |

</div>

<div>

**Salles**

| id | nom_salle |
|----|-----------|
| 1 | A101 |

</div>

<div>

**Equipements**

| nom_equipement | type | id_salle |
|----------------|------|----------|
| PC-Prof | Ordinateur | 1 |
| Switch-Central | Switch | 1 |

</div>

<div>

**Résultat**

| nom_equipement | type | nom_salle |
|----------------|------|-----------|
| PC-Prof | Ordinateur | A101 |
| Switch-Central | Switch | A101 |

</div>

</div>

* technicien → salle → équipements
* `INNER JOIN` car on cherche des correspondances existantes

**Résultat : 2 lignes**

## 8. Salles sans technicien

```sql
SELECT s.nom_salle
FROM Salles s
LEFT JOIN Techniciens t
ON s.id = t.id_salle_affectee
WHERE t.id IS NULL;
```

<div style="display:grid; grid-template-columns:1fr 1fr 1fr 1fr; gap:20px;">

<div>

**Salles**

| id | nom_salle |
|----|-----------|
| 1 | A101 |
| 2 | B202 |
| 3 | C303 |

</div>

<div>

**Techniciens**

| nom | id_salle |
|-----|----------|
| Jean | 1 |
| Marie | 2 |

</div>

<div>

**Equipements**

| … |
|---|

</div>

<div>

**Résultat**

| nom_salle |
|-----------|
| C303 |

</div>

</div>

* `LEFT JOIN` conserve toutes les salles
* `IS NULL` repère l’absence de correspondance

---
