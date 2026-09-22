# CIEL2



# ⬇️ <cite><font color="(0,68,88)">CIEL-2 : Informatique</font></cite>

<a href="https://carnus.fr"><img src="https://img.shields.io/badge/Carnus%20Enseignement Supérieur-F2A900?style=for-the-badge" /></a>
<a href="https://carnus.fr"><img src="https://img.shields.io/badge/BTS%20CIEL-2962FF?style=for-the-badge" /></a>

    Professeur - K. B.

### Contact : [Mail](mailto:lycee@carnus.fr)

---

## Annexe — Rappels SQL généraux

### A.1 Gestion des bases et tables

| Commande          | Description            | Exemple                                              |
| ------------------ | ----------------------- | ----------------------------------------------------- |
| `CREATE DATABASE` | Créer une base          | `CREATE DATABASE ma_base;`                            |
| `DROP DATABASE`   | Supprimer une base       | `DROP DATABASE ma_base;`                              |
| `USE`             | Sélectionner une base    | `USE ma_base;`                                         |
| `CREATE TABLE`    | Créer une table          | `CREATE TABLE etudiants (id INT, nom VARCHAR(50));`    |
| `ALTER TABLE`     | Modifier une table       | `ALTER TABLE etudiants ADD age INT;`                   |
| `DROP TABLE`      | Supprimer une table      | `DROP TABLE etudiants;`                                |

### A.2 Manipulation des données (CRUD)

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

### A.3 Fonctions d'agrégation et regroupements

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

### A.4 Administration SQL

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

### A.5 Jointures

| Commande SQL  | Description                        | Exemple                                               |
|---------------|------------------------------------|-------------------------------------------------------|
| `JOIN`        | Joindre deux tables                | `SELECT * FROM A JOIN B ON A.id = B.a_id;`            |
| `JOIN`        | Rassembler des infos sur plusieurs tables | `SELECT ... FROM a JOIN b ON ...;`            |
| `INNER JOIN`  | Jointure interne                   | `SELECT etudiants.nom, cours.nom FROM etudiants INNER JOIN inscriptions ON etudiants.id = inscriptions.etudiant_id INNER JOIN cours ON inscriptions.cours_id = cours.id;` |
| `LEFT JOIN`   | Jointure à gauche                  | `SELECT etudiants.nom, cours.nom FROM etudiants LEFT JOIN inscriptions ON etudiants.id = inscriptions.etudiant_id LEFT JOIN cours ON inscriptions.cours_id = cours.id;` |
| `RIGHT JOIN`  | Jointure à droite                  | `SELECT etudiants.nom, cours.nom FROM etudiants RIGHT JOIN inscriptions ON etudiants.id = inscriptions.etudiant_id RIGHT JOIN cours ON inscriptions.cours_id = cours.id;` |
| `FULL JOIN`   | Jointure complète                  | `SELECT etudiants.nom, cours.nom FROM etudiants FULL JOIN inscriptions ON etudiants.id = inscriptions.etudiant_id FULL JOIN cours ON inscriptions.cours_id = cours.id;` |

### A.6 Résumé

* Les clés définissent la relation
* `JOIN` définit le lien
* `LEFT` / `RIGHT` définissent ce qu'on conserve
* Une jointure = **1 `JOIN` + 1 `ON`**
* N—N ⇒ table de liaison


---

### Création d’un environnement virtuel

1. **Créer un environnement virtuel** :

   ```bash
   python3 -m venv env
   ```

   Cela crée un sous-dossier `env/` contenant une installation isolée de Python.

3. **Activer l’environnement** :

   ```bash
   source env/bin/activate
   ```

   Le prompt change, par exemple : `(env) pi@raspberrypi:~/monprojet $`

## Pour sortir de l’environnement :

```bash
deactivate
```

Cela revient au Python système, sans rien casser.

---
---

# TP 24/03

## index.html

```html
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <title>TP Fetch CSV</title>
</head>
<body>

    <h2>Diagnostic Fetch</h2>

    <button onclick="chargerCSV()">Tester chargement CSV</button>

    <div id="status"></div>
    <pre id="resultat"></pre>

    <script>
        
        function chargerCSV() {
            fetch("data.csv")
                .then(res => {
                    // Vérification du statut HTTP
                    if (!res.ok) {
                        throw new Error(`Erreur HTTP : ${res.status} (${res.statusText})`);
                    }
                    return res.text();
                })
                .then(data => traiterCSV(data))
                .catch(err => {
                    afficherErreur(err.message);
                });

            // Observation de l'origine
            console.log("Origin :", window.location.origin);
        }

        // Affiche le contenu du CSV (version simple)
        function traiterCSV(data) {
            document.getElementById("resultat").textContent = data;
        }

        // Affichage des erreurs
        function afficherErreur(message) {
            let div = document.createElement("div");
            div.style.color = "red";
            div.textContent = "Erreur : " + message;
            document.body.appendChild(div);
        }

    </script>

</body>
</html>
```

## data.csv

```csv
timestamp,latence_ms,debit_mbps,etat
2025-01-01 00:00,27,96,OK
2025-01-01 02:00,126,95,ALERTE
2025-01-01 04:00,18,78,OK
2025-01-01 06:00,15,100,OK
2025-01-01 08:00,25,73,OK
2025-01-01 10:00,16,95,OK
2025-01-01 12:00,30,70,OK
2025-01-01 14:00,29,86,OK
2025-01-01 16:00,29,98,OK
2025-01-01 18:00,15,37,ALERTE
2025-01-01 20:00,10,83,OK
2025-01-01 22:00,14,77,OK
2025-01-02 00:00,28,80,OK
2025-01-02 02:00,24,96,OK
2025-01-02 04:00,10,42,ALERTE
2025-01-02 06:00,13,26,ALERTE
2025-01-02 08:00,120,98,ALERTE
2025-01-02 10:00,10,99,OK
2025-01-02 12:00,17,91,OK
2025-01-02 14:00,12,70,OK
2025-01-02 16:00,11,87,OK
2025-01-02 18:00,22,82,OK
2025-01-02 20:00,23,98,OK
2025-01-02 22:00,27,98,OK
2025-01-03 00:00,19,71,OK
2025-01-03 02:00,14,87,OK
2025-01-03 04:00,13,92,OK
2025-01-03 06:00,25,87,OK
2025-01-03 08:00,19,85,OK
2025-01-03 10:00,23,73,OK
2025-01-03 12:00,20,97,OK
2025-01-03 14:00,25,82,OK
2025-01-03 16:00,17,39,ALERTE
2025-01-03 18:00,93,71,ALERTE
2025-01-03 20:00,29,71,OK
2025-01-03 22:00,19,97,OK
2025-01-04 00:00,27,95,OK
2025-01-04 02:00,22,99,OK
2025-01-04 04:00,20,91,OK
2025-01-04 06:00,12,86,OK
2025-01-04 08:00,17,83,OK
2025-01-04 10:00,28,77,OK
2025-01-04 12:00,15,79,OK
2025-01-04 14:00,25,76,OK
2025-01-04 16:00,21,87,OK
2025-01-04 18:00,93,97,ALERTE
2025-01-04 20:00,18,89,OK
2025-01-04 22:00,22,100,OK
2025-01-05 00:00,24,70,OK
2025-01-05 02:00,28,99,OK
2025-01-05 04:00,24,96,OK
2025-01-05 06:00,30,74,OK
2025-01-05 08:00,19,77,OK
2025-01-05 10:00,27,97,OK
2025-01-05 12:00,27,46,ALERTE
2025-01-05 14:00,20,93,OK
2025-01-05 16:00,26,75,OK
2025-01-05 18:00,95,90,ALERTE
2025-01-05 20:00,29,97,OK
2025-01-05 22:00,20,85,OK

```

## logs.txt

```text
2025-01-01 00:00:00 INFO PC01 (192.168.1.11) LATENCE=30ms DEBIT=78Mbps STATUS=OK
2025-01-01 00:00:00 INFO PC02 (192.168.1.12) LATENCE=27ms DEBIT=79Mbps STATUS=OK
2025-01-01 00:00:00 ERROR Timeout réseau
2025-01-01 02:00:00 INFO PC01 (192.168.1.11) LATENCE=27ms DEBIT=100Mbps STATUS=OK
2025-01-01 02:00:00 INFO PC02 (192.168.1.12) LATENCE=25ms DEBIT=83Mbps STATUS=OK
2025-01-01 04:00:00 INFO PC01 (192.168.1.11) LATENCE=19ms DEBIT=79Mbps STATUS=OK
2025-01-01 04:00:00 INFO PC02 (192.168.1.12) LATENCE=22ms DEBIT=77Mbps STATUS=OK
2025-01-01 06:00:00 INFO PC01 (192.168.1.11) LATENCE=11ms DEBIT=86Mbps STATUS=OK
2025-01-01 06:00:00 INFO PC02 (192.168.1.12) LATENCE=10ms DEBIT=76Mbps STATUS=OK
2025-01-01 06:00:00 DEBUG Ping envoyé vers 192.168.1.12
2025-01-01 08:00:00 WARNING PC01 (192.168.1.11) LATENCE=92ms DEBIT=96Mbps STATUS=ALERTE
2025-01-01 08:00:00 INFO PC02 (192.168.1.12) LATENCE=26ms DEBIT=96Mbps STATUS=OK
2025-01-01 10:00:00 INFO PC01 (192.168.1.11) LATENCE=13ms DEBIT=78Mbps STATUS=OK
2025-01-01 10:00:00 INFO PC02 (192.168.1.12) LATENCE=22ms DEBIT=70Mbps STATUS=OK
2025-01-01 12:00:00 INFO PC01 (192.168.1.11) LATENCE=13ms DEBIT=72Mbps STATUS=OK
2025-01-01 12:00:00 INFO PC02 (192.168.1.12) LATENCE=21ms DEBIT=99Mbps STATUS=OK
2025-01-01 12:00:00 DEBUG Analyse paquet en cours
2025-01-01 14:00:00 INFO PC01 (192.168.1.11) LATENCE=26ms DEBIT=86Mbps STATUS=OK
2025-01-01 14:00:00 ERROR PC02 (192.168.1.12) LATENCE=29ms DEBIT=48Mbps STATUS=ALERTE
2025-01-01 16:00:00 INFO PC01 (192.168.1.11) LATENCE=21ms DEBIT=78Mbps STATUS=OK
2025-01-01 16:00:00 ERROR PC02 (192.168.1.12) LATENCE=14ms DEBIT=35Mbps STATUS=ALERTE
2025-01-01 18:00:00 ERROR PC01 (192.168.1.11) LATENCE=14ms DEBIT=42Mbps STATUS=ALERTE
2025-01-01 18:00:00 INFO PC02 (192.168.1.12) LATENCE=24ms DEBIT=77Mbps STATUS=OK
2025-01-01 20:00:00 INFO PC01 (192.168.1.11) LATENCE=22ms DEBIT=86Mbps STATUS=OK
2025-01-01 20:00:00 INFO PC02 (192.168.1.12) LATENCE=14ms DEBIT=77Mbps STATUS=OK
2025-01-01 22:00:00 INFO PC01 (192.168.1.11) LATENCE=11ms DEBIT=75Mbps STATUS=OK
2025-01-01 22:00:00 INFO PC02 (192.168.1.12) LATENCE=26ms DEBIT=82Mbps STATUS=OK
2025-01-02 00:00:00 INFO PC01 (192.168.1.11) LATENCE=17ms DEBIT=84Mbps STATUS=OK
2025-01-02 00:00:00 DEBUG Analyse paquet en cours
2025-01-02 00:00:00 INFO PC02 (192.168.1.12) LATENCE=28ms DEBIT=71Mbps STATUS=OK
2025-01-02 02:00:00 INFO PC01 (192.168.1.11) LATENCE=21ms DEBIT=78Mbps STATUS=OK
2025-01-02 02:00:00 WARNING PC02 (192.168.1.12) LATENCE=30ms DEBIT=34Mbps STATUS=ALERTE
2025-01-02 04:00:00 INFO PC01 (192.168.1.11) LATENCE=17ms DEBIT=99Mbps STATUS=OK
2025-01-02 04:00:00 INFO PC02 (192.168.1.12) LATENCE=18ms DEBIT=79Mbps STATUS=OK
2025-01-02 06:00:00 INFO PC01 (192.168.1.11) LATENCE=16ms DEBIT=77Mbps STATUS=OK
2025-01-02 06:00:00 ERROR PC02 (192.168.1.12) LATENCE=11ms DEBIT=39Mbps STATUS=ALERTE
2025-01-02 08:00:00 INFO PC01 (192.168.1.11) LATENCE=11ms DEBIT=89Mbps STATUS=OK
2025-01-02 08:00:00 INFO PC02 (192.168.1.12) LATENCE=16ms DEBIT=86Mbps STATUS=OK
2025-01-02 10:00:00 INFO PC01 (192.168.1.11) LATENCE=ms DEBIT=90Mbps STATUS=OK
2025-01-02 10:00:00 INFO PC02 (192.168.1.12) LATENCE=26ms DEBIT=99Mbps STATUS=OK
2025-01-02 12:00:00 INFO PC01 (192.168.1.11) LATENCE=18ms DEBIT=96Mbps STATUS=OK
2025-01-02 12:00:00 INFO PC02 (192.168.1.12) LATENCE=24ms DEBIT=100Mbps STATUS=OK
2025-01-02 14:00:00 INFO PC01 (192.168.1.11) LATENCE=11ms DEBIT=87Mbps STATUS=OK
2025-01-02 14:00:00 INFO PC02 (192.168.1.12) LATENCE=ms DEBIT=90Mbps STATUS=OK
2025-01-02 16:00:00 ERROR PC01 (192.168.1.11) LATENCE=18ms DEBIT=25Mbps STATUS=ALERTE
2025-01-02 16:00:00 INFO PC02 (192.168.1.12) LATENCE=30ms DEBIT=96Mbps STATUS=OK
2025-01-02 18:00:00 INFO PC01 (192.168.1.11) LATENCE=19ms DEBIT=84Mbps STATUS=OK
2025-01-02 18:00:00 INFO PC02 (192.168.1.12) LATENCE=20ms DEBIT=93Mbps STATUS=OK
2025-01-02 20:00:00 WARNING PC01 (192.168.1.11) LATENCE=21ms DEBIT=34Mbps STATUS=ALERTE
2025-01-02 20:00:00 INFO PC02 (192.168.1.12) LATENCE=23ms DEBIT=95Mbps STATUS=OK
2025-01-02 22:00:00 INFO PC01 (192.168.1.11) LATENCE=14ms DEBIT=93Mbps STATUS=OK
2025-01-02 22:00:00 INFO PC02 (192.168.1.12) LATENCE=21ms DEBIT=85Mbps STATUS=OK
2025-01-03 00:00:00 INFO PC01 (192.168.1.11) LATENCE=14ms DEBIT=95Mbps STATUS=OK
2025-01-03 00:00:00 INFO PC02 (192.168.1.12) LATENCE=27ms DEBIT=85Mbps STATUS=OK
2025-01-03 02:00:00 INFO PC01 (192.168.1.11) LATENCE=17ms DEBIT=73Mbps STATUS=OK
2025-01-03 02:00:00 INFO PC02 (192.168.1.12) LATENCE=ms DEBIT=82Mbps STATUS=OK
2025-01-03 04:00:00 INFO PC01 (192.168.1.11) LATENCE=28ms DEBIT=77Mbps STATUS=OK
2025-01-03 04:00:00 DEBUG Ping envoyé vers 192.168.1.11
2025-01-03 04:00:00 ERROR PC02 (192.168.1.12) LATENCE=119ms DEBIT=82Mbps STATUS=ALERTE
2025-01-03 06:00:00 INFO PC01 (192.168.1.11) LATENCE=13ms DEBIT=99Mbps STATUS=OK
2025-01-03 06:00:00 INFO PC02 (192.168.1.12) LATENCE=13ms DEBIT=79Mbps STATUS=OK
2025-01-03 08:00:00 INFO PC01 (192.168.1.11) LATENCE=17ms DEBIT=74Mbps STATUS=OK
2025-01-03 08:00:00 INFO PC02 (192.168.1.12) LATENCE=15ms DEBIT=96Mbps STATUS=OK
2025-01-03 10:00:00 WARNING PC01 (192.168.1.11) LATENCE=138ms DEBIT=80Mbps STATUS=ALERTE
2025-01-03 10:00:00 ERROR PC02 (192.168.1.12) LATENCE=81ms DEBIT=100Mbps STATUS=ALERTE
2025-01-03 12:00:00 INFO PC01 (192.168.1.11) LATENCE=13ms DEBIT=98Mbps STATUS=OK
2025-01-03 12:00:00 INFO PC02 (192.168.1.12) LATENCE=13ms DEBIT=77Mbps STATUS=OK
2025-01-03 14:00:00 INFO PC01 (192.168.1.11) LATENCE=27ms DEBIT=84Mbps STATUS=OK
2025-01-03 14:00:00 INFO PC02 (192.168.1.12) LATENCE=18ms DEBIT=98Mbps STATUS=OK
2025-01-03 14:00:00 DEBUG Analyse paquet en cours
2025-01-03 16:00:00 ERROR PC01 (192.168.1.11) LATENCE=110ms DEBIT=72Mbps STATUS=ALERTE
2025-01-03 16:00:00 INFO PC02 (192.168.1.12) LATENCE=10ms DEBIT=94Mbps STATUS=OK
2025-01-03 18:00:00 INFO PC01 (192.168.1.11) LATENCE=24ms DEBIT=82Mbps STATUS=OK
2025-01-03 18:00:00 ERROR PC02 (192.168.1.12) LATENCE=148ms DEBIT=74Mbps STATUS=ALERTE
2025-01-03 20:00:00 ERROR PC01 (192.168.1.11) LATENCE=30ms DEBIT=33Mbps STATUS=ALERTE
2025-01-03 20:00:00 ERROR Timeout réseau
2025-01-03 20:00:00 INFO PC02 (192.168.1.12) LATENCE=18ms DEBIT=74Mbps STATUS=OK
2025-01-03 20:00:00 INFO Connexion établie PC02
2025-01-03 22:00:00 INFO PC01 (192.168.1.11) LATENCE=22ms DEBIT=70Mbps STATUS=OK
2025-01-03 22:00:00 DEBUG Ping envoyé vers 192.168.1.11
2025-01-03 22:00:00 INFO PC02 (192.168.1.12) LATENCE=27ms DEBIT=71Mbps STATUS=OK
```


