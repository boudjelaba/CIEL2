# TP : Visualisation et analyse de données (CSV & logs)

## Objectifs

* lire des fichiers (`CSV`, `logs`)
* Extraire et transformer des données
* Afficher des données dans une page web
* Tracer une courbe
* Analyser des données et détecter des anomalies

## Structure du projet

```
tp-courbes/
│── index.html
│── style.css
│── script.js
│── data.csv
│── logs.txt
```

---

## PARTIE 0 : Diagnostic d’un bug (fetch et serveur)

### Objectif 

Comprendre pourquoi `fetch()` ne fonctionne pas sur des fichiers locaux (`file://`) et comment diagnostiquer les erreurs réseau.

### `index.html`

```html
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <title>TP Fetch CSV</title>
</head>
<body>

    <h1>Test chargement CSV</h1>

    <button onclick="chargerCSV()">Charger CSV</button>
    <button onclick="chargerLogs()">Charger Logs</button>

    <pre id="resultat"></pre>

    <ul id="liste"></ul>

    <div id="incidents"></div>

    <div id="logs"></div>

    <canvas id="graphique" width="500" height="300"></canvas>

    <canvas id="myChart"></canvas>

    <script src="script.js"></script>

</body>
</html>
```

### `script.js`

```javascript
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
```

### Test 1 : Sans serveur (échec attendu)

1. Ouvrir `index.html` en double-cliquant (sans serveur)
2. Cliquer sur **"Charger CSV"**

> Résultat attendu

* Rien ne fonctionne
* Ouvrir la console (F12)

On voit une erreur du type :

```
Access to fetch at 'data.csv' from origin 'null' has been blocked by CORS policy
```

**Remarques :**

* En ouvrant un fichier local :

```
file://
```

Le navigateur utilise une origine spéciale :

```
origin = null
```

> Pour des raisons de sécurité, les requêtes `fetch()` sont bloquées.


Dans ce cas :

* La requête est **bloquée avant même d’atteindre le serveur**
* Le code `.then(res => ...)` **n’est jamais exécuté**
* C’est directement `.catch()` qui s’exécute

### Solutions : utiliser un serveur local

**Option 1 — Live Server (VS Code)**

* Installer l'Extension **Live Server** (si non installée)
* Clic droit → **Open with Live Server**
* URL devient : `http://127.0.0.1:5500/index.html` 

> On passe de `file://` à `http://` → Le navigateur autorise maintenant `fetch()` car la requête passe par HTTP.

**Option 2 — Serveur Python**

```bash
python -m http.server 8000
```

Puis dans le navigateur : `http://localhost:8000`

> Python agit comme serveur HTTP simple. Toutes les requêtes fetch seront acceptées.

### Test 2 : Avec serveur (fonctionnel)

* Le fichier CSV s’affiche dans la page
* Aucune erreur dans la console

### Test 3 : Provoquer une erreur HTTP

1. Renommer `data.csv` → `data2.csv`
2. Recharger la page
3. Cliquer sur **"Charger CSV"**

Erreur :

```
Erreur HTTP : 404 (Not Found)
```

### Analyse avec les outils navigateur

**Onglet **Network** (F12)**

Permet de voir :

* Les requêtes envoyées
* Les réponses du serveur
* Les codes HTTP (200, 404, 500)

**(Optionnel) Analyse réseau avancée**

Avec **Wireshark**, on peut observer :

* Les paquets réseau
* Les requêtes HTTP
* Les réponses du serveur

Filtre utile :

```
http || tcp.port == 80 || tcp.port == 443
```

* Lancer le TP (`index.html` + `fetch`)


```text
                ┌────────────────────────────┐
                │       NAVIGATEUR           │
                │     (index.html + JS)      │
                └────────────┬───────────────┘
                             │
                             │ fetch("data.csv")
                             ▼

        ✖️ CAS 1 : PAS DE SERVEUR (file://)
        ─────────────────────────────────────
                origin = null
                             │
                             ▼
                ✖️ BLOQUÉ (CORS)
                "Access blocked by CORS policy"

────────────────────────────────────────────────────────────

        ✔️ CAS 2 : SERVEUR ACTIF (http://localhost)
        ─────────────────────────────────────────────

                             │
                             ▼
                ┌────────────────────────────┐
                │       SERVEUR LOCAL        │
                │   (python / live server)   │
                └────────────┬───────────────┘
                             │
               cherche "data.csv"
                             │

        ┌────────────────────┼────────────────────┐
        │                    │                    │

   ✖️ CAS 2A            ✖️ CAS 2B             ✔️ CAS 2C
   FICHIER ABSENT       ERREUR SERVEUR        SUCCÈS
   (404)                (500)                 (200)

        │                    │                    │
        ▼                    ▼                    ▼

  404 Not Found      500 Internal Error      200 OK
        │                    │                    │
        ▼                    ▼                    ▼

 JS reçoit erreur     JS reçoit erreur       JS reçoit données
        │                    │                    │
        ▼                    ▼                    ▼

.catch() exécuté   .catch() exécuté     .then() exécuté

        │                    │                    │
        ▼                    ▼                    ▼

✖️ message erreur    ✖️ message erreur     ✔️ affichage CSV
```

```mermaid
flowchart LR
    style A fill:#cce5ff,stroke:#3399ff,stroke-width:2px
    style B fill:#d4edda,stroke:#28a745,stroke-width:2px
    style C fill:#fff3cd,stroke:#ffc107,stroke-width:2px
    style D fill:#f8d7da,stroke:#dc3545,stroke-width:2px
    style E fill:#e2e3e5,stroke:#6c757d,stroke-width:2px,stroke-dasharray: 5 5

    A[Navigateur<br>(fetch JS)]
    B[Réseau / Paquets TCP<br>(Wireshark)]
    C[Serveur<br>(local / dev)]
    D[Console JS<br>Affiche données ou erreurs]
    E[Analyse finale Wireshark<br>Paquets et statuts]

    %% Flux normal
    A -- Requête HTTP/HTTPS --> B
    B -- Trafic visible : URL, méthode, headers --> C
    C -- 200 OK / JSON / CSV --> B
    B -- Paquets reçus --> D

    %% Erreurs
    C -- 404 Not Found --> B
    C -- 500 Server Error --> B
    C -- Headers CORS manquants --> B
    B -- Bloqué côté navigateur (CORS) --> D
    B -- Erreur fetch() 404/500 --> D

    %% Wireshark final
    D --> E
```

* **Bleu clair** → Navigateur / client
* **Vert** → Réseau / capture Wireshark (normal)
* **Jaune** → Serveur / attention erreurs potentielles
* **Rouge** → Erreurs visibles dans la console JS
* **Gris** → Analyse finale / récapitulatif Wireshark

---

## PARTIE 1 : 

* Lire un fichier CSV 
* Affichage HTML 
* Tracer une courbe (Canvas) 
* Lecture de logs 
* Graphique avancé (Chart.js)

### `script.js`

```javascript
// =========================
// CHARGEMENT CSV
// =========================
function chargerCSV() {
    fetch("data.csv")
        .then(res => {
            if (!res.ok) {
                throw new Error(`Erreur HTTP : ${res.status}`);
            }
            return res.text();
        })
        .then(data => traiterCSV(data))
        .catch(err => afficherErreur(err.message));
}

function traiterCSV(data) {

    let lignes = data.trim().split("\n");
    lignes.shift(); // enlever en-tête

    let timestamps = [];
    let latence = [];
    let debit = [];

    lignes.forEach(ligne => {
        if (ligne.trim() === "") return;

        let val = ligne.split(",");

        // sécurité
        if (val.length < 3) return;

        timestamps.push(val[0].trim());
        latence.push(parseFloat(val[1]));
        debit.push(parseFloat(val[2]));
    });

    let incidents = detecterIncidents(latence, debit);

    afficherListe(timestamps, latence, debit);
    tracerGraphique(timestamps, latence, debit, incidents);
    afficherIncidents(timestamps, latence, debit, incidents);
}

// =========================
// AFFICHAGE LISTE
// =========================
function afficherListe(timestamps, latence, debit) {
    let ul = document.getElementById("liste");
    ul.innerHTML = "";

    for (let i = 0; i < timestamps.length; i++) {
        let li = document.createElement("li");
        li.textContent = `Temps: ${timestamps[i]} - Latence: ${latence[i]} ms - Débit: ${debit[i]} Mbps`;
        ul.appendChild(li);
    }
}

// =========================
// GRAPH (Chart.js)
// =========================
let chart;

function tracerGraphique(timestamps, latence, debit, incidents) {
    let ctx = document.getElementById("myChart").getContext("2d");

    if (chart) chart.destroy();

    let pointsIncidents = latence.map((val, i) => {
        return incidents[i] ? val : null;
    });

    chart = new Chart(ctx, {
        type: "line",
        data: {
            labels: timestamps,
            datasets: [
                {
                    label: "Latence (ms)",
                    data: latence,
                    borderColor: "red",
                    tension: 0.2
                },
                {
                    label: "Débit (Mbps)",
                    data: debit,
                    borderColor: "green",
                    tension: 0.2
                },
                {
                    label: "Incidents",
                    data: pointsIncidents,
                    borderColor: "transparent",
                    backgroundColor: "red",
                    pointRadius: 6,
                    showLine: false
                }
            ]
        }
    });
}

// =========================
// INCIDENTS
// =========================
function detecterIncidents(latence, debit) {
    return latence.map((l, i) => l > 80 || debit[i] < 50);
}

function afficherIncidents(timestamps, latence, debit, incidents) {
    let div = document.getElementById("incidents");
    div.innerHTML = "<h2>Incidents détectés</h2>";

    let nb = 0;

    incidents.forEach((isIncident, i) => {
        if (isIncident) {
            nb++;

            let type = latence[i] > 80
                ? "Latence élevée"
                : "Débit faible";

            let p = document.createElement("p");
            p.textContent = `${timestamps[i]} → ${type}`;
            div.appendChild(p);
        }
    });

    div.innerHTML += nb === 0
        ? "<p>Aucun incident</p>"
        : `<p><strong>Total : ${nb}</strong></p>`;
}

// =========================
// CHARGEMENT LOGS
// =========================
function chargerLogs() {
    fetch("logs.txt")
        .then(res => {
            if (!res.ok) {
                throw new Error(`Erreur HTTP : ${res.status}`);
            }
            return res.text();
        })
        .then(data => {
            let resultats = traiterLogs(data);
            console.log(resultats);
        })
        .catch(err => afficherErreur(err.message));
}

function traiterLogs(data) {
    let lignes = data.split("\n");
    let resultats = [];

    let regex = /(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) \w+ (PC\d+) \(([\d.]+)\) LATENCE=(\d+)ms DEBIT=(\d+)Mbps STATUS=(\w+)/;

    lignes.forEach(ligne => {
        let match = ligne.match(regex);

        if (!match) return;

        let latence = parseInt(match[4]);
        let debit = parseInt(match[5]);

        resultats.push({
            timestamp: match[1],
            pc: match[2],
            ip: match[3],
            latence: latence,
            debit: debit,
            status: match[6]
        });
    });

    return resultats;
}

// =========================
// ERREUR
// =========================
function afficherErreur(message) {
    let div = document.createElement("div");
    div.style.color = "red";
    div.textContent = "Erreur : " + message;
    document.body.appendChild(div);
}
```

### `index.html`

```html
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <title>TP CSV & Logs</title>
</head>
<body>

    <h1>Analyse réseau</h1>

    <button onclick="chargerCSV()">Charger CSV</button>
    <button onclick="chargerLogs()">Charger Logs</button>

    <pre id="resultat"></pre>

    <ul id="liste"></ul>

    <div id="incidents"></div>

    <canvas id="myChart"></canvas>

    <script src="script.js"></script>

</body>
</html>
```

---
