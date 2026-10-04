# Annexe — Rappels SQL généraux

## A.1 Gestion des bases et tables

| Commande          | Description            | Exemple                                              |
| ------------------ | ----------------------- | ----------------------------------------------------- |
| `CREATE DATABASE` | Créer une base          | `CREATE DATABASE ma_base;`                            |
| `DROP DATABASE`   | Supprimer une base       | `DROP DATABASE ma_base;`                              |
| `USE`             | Sélectionner une base    | `USE ma_base;`                                         |
| `CREATE TABLE`    | Créer une table          | `CREATE TABLE etudiants (id INT, nom VARCHAR(50));`    |
| `ALTER TABLE`     | Modifier une table       | `ALTER TABLE etudiants ADD age INT;`                   |
| `DROP TABLE`      | Supprimer une table      | `DROP TABLE etudiants;`                                |

## A.2 Manipulation des données (CRUD)

| Commande      | Description          | Exemple                                                    |
| ------------- | ---------------------- | ------------------------------------------------------------ |
| `INSERT INTO` | Ajouter des données     | `INSERT INTO etudiants (nom, age) VALUES ('Alice', 20);`     |
| `SELECT`      | Lire des données        | `SELECT * FROM etudiants;`                                   |
| `WHERE`       | Filtrer                 | `SELECT * FROM etudiants WHERE age > 18;`                    |
| `ORDER BY`    | Trier                   | `SELECT * FROM etudiants ORDER BY nom ASC;`                  |
| `LIMIT`       | Limiter                 | `SELECT * FROM etudiants LIMIT 10;`                           |
| `UPDATE`      | Modifier                | `UPDATE etudiants SET age = 21 WHERE nom = 'Alice';`          |
| `DELETE`      | Supprimer               | `DELETE FROM etudiants WHERE age < 18;`                       |

Types de données courants : `INT`, `FLOAT`, `VARCHAR`, `BOOLEAN`, `DATE`, `NULL`.

```sql
INSERT INTO commandes (client, quantite, commentaire)
VALUES ('ClientA', 3, NULL);
```

## A.3 Fonctions d'agrégation et regroupements

| Fonction   | Rôle                  | Exemple                                               |
| ---------- | ----------------------| ------------------------------------------------------|
| `COUNT()`  | Compter               | `SELECT COUNT(*) FROM etudiants;`                     |
| `SUM()`    | Somme                 | `SELECT SUM(age) FROM etudiants;`                     |
| `AVG()`    | Moyenne               | `SELECT AVG(age) FROM etudiants;`                     |
| `MIN()`    | Minimum               | `SELECT MIN(age) FROM etudiants;`                     |
| `MAX()`    | Maximum               | `SELECT MAX(age) FROM etudiants;`                     |
| `GROUP BY` | Regrouper             | `SELECT age, COUNT(*) FROM etudiants GROUP BY age;`   |
| `HAVING`   | Filtrer les groupes   | `HAVING COUNT(*) > 1;`                                |

> `WHERE` filtre **avant** regroupement — `HAVING` filtre **après** regroupement

`COUNT(colonne)` ignore automatiquement les `NULL` : combiné à un `LEFT JOIN`, c'est la technique standard pour compter "y compris les 0" (ex : nombre de commandes par client, y compris ceux qui n'en ont aucune).

## A.4 Administration SQL

| Commande            | Description                | Exemple                                                          |
| -------------------- | ---------------------------- | ------------------------------------------------------------------ |
| `CREATE USER`       | Créer un utilisateur          | `CREATE USER 'user'@'localhost' IDENTIFIED BY 'mdp';`             |
| `DROP USER`         | Supprimer un utilisateur       | `DROP USER 'user'@'localhost';`                                   |
| `GRANT`             | Donner des droits              | `GRANT ALL PRIVILEGES ON ma_base.* TO 'user'@'localhost';`        |
| `REVOKE`            | Retirer des droits             | `REVOKE ALL PRIVILEGES ON ma_base.* FROM 'user'@'localhost';`     |
| `SHOW DATABASES`    | Lister les bases                | `SHOW DATABASES;`                                                  |
| `SHOW TABLES`       | Lister les tables               | `SHOW TABLES;`                                                     |
| `DESCRIBE`          | Structure d'une table            | `DESCRIBE etudiants;`                                              |
| `EXPLAIN`           | Plan d'exécution                 | `EXPLAIN SELECT * FROM etudiants;`                                 |
| `SHOW PROCESSLIST`  | Requêtes en cours                | `SHOW PROCESSLIST;`                                                |
| `FLUSH PRIVILEGES`  | Appliquer les droits             | `FLUSH PRIVILEGES;`                                                |

**Sauvegarde / restauration (dans le terminal, pas dans l'éditeur SQL)**

```bash
mysqldump -u user -p ma_base > sauvegarde.sql
mysql -u user -p ma_base < sauvegarde.sql
```

## A.5 Jointures

| Commande SQL  | Description                        | Exemple                                               |
|---------------|------------------------------------|-------------------------------------------------------|
| `JOIN`        | Joindre deux tables                | `SELECT * FROM A JOIN B ON A.id = B.a_id;`            |
| `JOIN`        | Rassembler des infos sur plusieurs tables | `SELECT ... FROM a JOIN b ON ...;`            |
| `INNER JOIN`  | Jointure interne                   | `SELECT etudiants.nom, cours.nom FROM etudiants INNER JOIN inscriptions ON etudiants.id = inscriptions.etudiant_id INNER JOIN cours ON inscriptions.cours_id = cours.id;` |
| `LEFT JOIN`   | Jointure à gauche                  | `SELECT etudiants.nom, cours.nom FROM etudiants LEFT JOIN inscriptions ON etudiants.id = inscriptions.etudiant_id LEFT JOIN cours ON inscriptions.cours_id = cours.id;` |
| `RIGHT JOIN`  | Jointure à droite                  | `SELECT etudiants.nom, cours.nom FROM etudiants RIGHT JOIN inscriptions ON etudiants.id = inscriptions.etudiant_id RIGHT JOIN cours ON inscriptions.cours_id = cours.id;` |
| `FULL JOIN`   | Jointure complète                  | `SELECT etudiants.nom, cours.nom FROM etudiants FULL JOIN inscriptions ON etudiants.id = inscriptions.etudiant_id FULL JOIN cours ON inscriptions.cours_id = cours.id;` |

## A.6 Résumé

* Les clés définissent la relation
* `JOIN` définit le lien
* `LEFT` / `RIGHT` définissent ce qu'on conserve
* Une jointure = **1 `JOIN` + 1 `ON`**

---

* N—N ⇒ table de liaison

