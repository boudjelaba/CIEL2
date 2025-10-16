# Git distant avec GitHub (collaboration en ligne) -- V0

Git est conçu pour la collaboration, et les dépôts distants (ou "remotes") sont essentiels pour partager votre travail et collaborer avec d'autres. GitHub est une plateforme populaire qui héberge des dépôts Git.

## Pré-requis

1. Avoir un compte GitHub : [https://github.com](https://github.com)
2. Se connecter et créer un **nouveau dépôt (repository)** sur le site (bouton "New repository").

   * Ne pas cocher "Initialize with a README" (sinon conflit possible avec le dépôt local)
   * Copier l’URL du dépôt (ex : `https://github.com/CharlesCarnus/mon-projet.git`)

---

## Associer son dépôt local à GitHub (dépôt distant)

Une fois le projet initialisé en local ou dans votre terminal Git Bash (situé dans votre répertoire `Exp_Git` local):

```bash
$ git remote add origin https://github.com/CharlesCarnus/mon-projet.git
```

> `origin` est un **nom par défaut** pour le dépôt distant. On pourrait l'appeler autrement, mais "origin" est la convention.

Vérifiez que le lien est bien établi :

```bash
$ git remote -v
```

* Si vous utilisez le protocole SSH (recommandé pour la sécurité et la commodité après configuration de clés SSH) :
```bash
git remote add origin git@github.com:CharlesCarnus/mon-projet.git
```
---

## Envoyer son projet sur GitHub (push)

Si votre branche locale s’appelle `main` :

```bash
$ git push -u origin main
```

> Le "-u" (ou `--set-upstream`) permet de lier votre branche locale à celle sur GitHub. Ensuite, un simple `git push` suffira.

---

## Récupérer les modifications (pull)

Si vous ou vos camarades avez modifié le dépôt sur GitHub :

```bash
$ git pull
```

Git fusionnera les changements distants avec votre version locale.

---

## Cloner un projet GitHub

Depuis GitHub, pour **télécharger un projet distant** :

```bash
$ git clone https://github.com/AutreUtilisateur/le-projet.git
```

Cela crée automatiquement un dossier avec un dépôt Git lié au GitHub distant.

---

## Remarques

* Toujours faire un `git pull` avant un `git push` pour éviter les conflits.
* Faire des **commits fréquents et clairs**.
* Utiliser les **branches** pour travailler à plusieurs sans tout casser (ça cassera quand même, mais gentiment).
* Ajouter un fichier `README.md` et un `.gitignore`.


```
Ordinateur de l'étudiant         GitHub
         |                         |
     Dépôt local  <------------> Dépôt distant
         ^            push/pull      ^
         |___________________________|
                  git clone
```

---

## TP 1 : Créer et publier un projet personnel sur GitHub

### Objectif :

Créer un petit projet HTML/CSS local, l’initialiser avec Git, suivre son évolution et le publier sur GitHub.

### Énoncé :

1. Créer un dossier appelé `MonSiteWeb`.
2. Ajouter un fichier `index.html` contenant un squelette HTML basique.
3. Initialiser le dépôt Git localement :

   ```bash
   git init
   git add .
   git commit -m "Initial commit: ajout du fichier index.html"
   ```
4. Créer un dépôt sur GitHub (nom : `MonSiteWeb`).
5. Lier le dépôt local à GitHub :

   ```bash
   git remote add origin https://github.com/votre-pseudo/MonSiteWeb.git
   git push -u origin main
   ```
6. Ajouter un fichier `style.css` et modifie `index.html` pour le lier.
7. Faire les commits nécessaires puis pousser les changements :

   ```bash
   git add .
   git commit -m "Ajout de style.css et lien dans index.html"
   git push
   ```

### Bonus :

Ajoute un fichier `.gitignore` pour ignorer tous les fichiers `*.log` et `node_modules/`.

---

## **TP 2 : Travailler avec les branches et résoudre un conflit**

### Objectif :

Simuler un développement en équipe avec deux branches qui modifient la même ligne.

### Énoncé :

1. Cloner un dépôt GitHub (ou utiliser le précédent).

2. Créer une nouvelle branche :

   ```bash
   git switch -c modif-texte
   ```

3. Dans `index.html`, modifier le titre (`<title>`) en `"Bienvenue sur mon site"`.
   Commit :

   ```bash
   git commit -am "modification du titre"
   ```

4. Revenir sur `main` :

   ```bash
   git switch main
   ```

5. Modifier aussi le même titre, mais différemment : `"Mon site officiel"`.
   Commit :

   ```bash
   git commit -am "autre modification du titre"
   ```

6. Tenter un merge :

   ```bash
   git merge modif-texte
   ```

   > Cela devrait provoquer un **conflit**.

7. Ouvrir le fichier concerné, résoudre le conflit **à la main**, puis :

   ```bash
   git add index.html
   git commit -m "résolution du conflit"
   ```

8. Vérifier l’historique avec :

   ```bash
   git log --oneline --graph
   ```

---

## **TP 3 : Exemple de Dépôt GitHub**

**Nom du Dépôt :** `mon-site-web-simple`

**Structure des Fichiers :**

```
mon-site-web-simple/
├── index.html
├── style.css
├── script.js
└── README.md
```
---

### Contenu de chaque fichier :

1.  **`index.html`** (La page principale du site)

    ```html
    <!DOCTYPE html>
    <html lang="fr">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Mon Site Web Simple</title>
        <link rel="stylesheet" href="style.css">
    </head>
    <body>
        <header>
            <h1>Bienvenue sur mon site Web</h1>
        </header>
        <main>
            <p>Ceci est un exemple de page pour mon site web. Je suis étudiant en BTS CIEL - IR</p>
            <button id="monBouton">Valider</button>
        </main>
        <footer>
            <p>&copy; 2025 Mon Site Web</p>
        </footer>
        <script src="script.js"></script>
    </body>
    </html>
    ```

2.  **`style.css`** (Les styles CSS pour le site)

    ```css
    body {
        font-family: Arial, sans-serif;
        line-height: 1.6;
        margin: 0;
        padding: 0;
        background: #f4f4f4;
        color: #333;
    }

    header {
        background: #333;
        color: #fff;
        padding: 1rem 0;
        text-align: center;
    }

    main {
        padding: 20px;
        text-align: center;
    }

    button {
        background-color: #007bff;
        color: white;
        padding: 10px 15px;
        border: none;
        cursor: pointer;
        border-radius: 5px;
        margin-top: 15px;
    }

    footer {
        text-align: center;
        padding: 1rem 0;
        background: #333;
        color: #fff;
        position: fixed;
        width: 100%;
        bottom: 0;
    }
    ```

3.  **`script.js`** (Script JavaScript)

    ```javascript
    document.addEventListener('DOMContentLoaded', () => {
        const monBouton = document.getElementById('monBouton');

        if (monBouton) {
            monBouton.addEventListener('click', () => {
                alert('Bouton cliqué ! Votre requête est enregistrée');
            });
        }
    });
    ```

4.  **`README.md`** (Description du projet, affichée sur la page principale du dépôt GitHub)

    ```markdown
    # Mon site web Simple

    Ce dépôt contient un exemple simple de site web personnel avec des fichiers HTML, CSS et JavaScript basiques.

    ## Contenu

    - `index.html`: La structure principale de la page web.
    - `style.css`: Les styles visuels pour le site.
    - `script.js`: Un petit script interactif (alerte au clic sur un bouton).
    - `README.md`: Ce fichier, décrivant le projet.

    ## Comment l'utiliser

    1. Clonez ce dépôt sur votre machine locale.
    2. Ouvrez `index.html` dans votre navigateur web.

    ---

    **Note :** Ce dépôt est conçu pour servir d'exemple lors de l'apprentissage de Git et GitHub, notamment pour les opérations de clonage, de push et de pull.
    ```

-----

### Étapes pour créer ce dépôt sur GitHub :

1.  **Créer les fichiers localement :**

      * Créer un dossier nommé `mon-site-web-simple` sur l'ordinateur.
      * À l'intérieur de ce dossier, créer les quatre fichiers (`index.html`, `style.css`, `script.js`, `README.md`) et copier-coller le contenu ci-dessus dans chacun d'eux.

2.  **Initialiser le dépôt Git local :**

      * Ouvrir le terminal (Git Bash ou le terminal intégré de VS Code).
      * Naviguer jusqu'à votre dossier `mon-site-web-simple` :
        ```bash
        cd mon-site-web-simple
        ```
      * Initialiser Git :
        ```bash
        git init
        ```
      * Ajouter tous les fichiers :
        ```bash
        git add .
        ```
      * Faire le premier commit :
        ```bash
        git commit -m "Initial commit: Ajout des fichiers HTML, CSS, JS et README"
        ```

3.  **Créer un dépôt sur GitHub :**

      * Allez sur [GitHub.com](https://github.com/) et connectez-vous.
      * Cliquez sur l'icône "+" en haut à droite, puis sur `New repository`.
      * Donnez le nom `mon-site-web-simple`.
      * Laissez-le Public (ou Private si vous préférez).
      * **Important :** Ne cochez pas "Add a README file", "Add .gitignore" ou "Choose a license" car vous avez déjà créé ces fichiers localement.
      * Cliquez sur `Create repository`.

4.  **Lier le dépôt local au dépôt GitHub et pousser :**

      * Sur la page GitHub de votre nouveau dépôt vide, vous verrez des instructions. Copiez la ligne pour `git remote add origin ...` (celle qui ressemble à `https://github.com/VotreNomUtilisateur/mon-site-web-simple.git`).
      * Dans votre terminal (toujours dans le dossier `mon-site-web-simple`), collez et exécutez cette commande :
        ```bash
        git remote add origin https://github.com/VotreNomUtilisateur/mon-site-web-simple.git
        ```
        *(Remplacez `VotreNomUtilisateur` par votre vrai nom d'utilisateur GitHub.)*
      * Poussez vos fichiers vers GitHub :
        ```bash
        git push -u origin main
        ```
        (Si votre branche par défaut est `master`, utilisez `git push -u origin master`.)
      * Vous devrez peut-être vous authentifier via votre navigateur.

Maintenant, si vous rafraîchissez la page de votre dépôt sur GitHub, vous verrez tous vos fichiers et le contenu du `README.md` affiché.

### **Modification de `index.html` dans VS Code après un push initial**

1.  **Modifiez le fichier `index.html` dans VS Code :**
    * Ouvrez votre fichier `index.html` dans l'éditeur de VS Code.
    * Apportez les modifications souhaitées (par exemple, changez un texte, ajoutez un élément, etc.).
    * Enregistrez le fichier (`Ctrl + S` ou `File > Save`).

2.  **Ouvrez la vue "Source Control" (Contrôle de Source) :**
    * Cliquez sur l'icône "Source Control" (trois cercles reliés) dans la barre d'activités à gauche de VS Code. Vous pouvez aussi utiliser le raccourci `Ctrl + Shift + G`.

3.  **Visualisez les modifications :**
    * Dans la vue "Source Control", vous verrez `index.html` listé sous la section "CHANGES" (Modifications).
    * Si vous cliquez sur `index.html` dans cette liste, VS Code ouvrira une vue de comparaison (diff) montrant les lignes que vous avez modifiées par rapport à la dernière version commitée.

4.  **Stager (Ajouter à l'index) les modifications :**
    * Passez la souris sur `index.html` dans la section "CHANGES".
    * Cliquez sur l'icône "+" (Stage Changes) à côté du nom du fichier.
    * Le fichier `index.html` se déplacera de la section "CHANGES" vers la section "STAGED CHANGES" (Modifications préparées). Cela signifie que Git est maintenant prêt à enregistrer ces modifications dans le prochain commit.

5.  **Committer les modifications :**
    * Dans la zone de texte sous "Message" (en haut de la vue "Source Control"), entrez un message de commit concis et descriptif pour vos modifications (par exemple : "Mise à jour du texte d'accueil sur index.html" ou "Ajout d'un nouveau paragraphe dans index.html").
    * Cliquez sur le bouton "Commit" (l'icône de coche) situé juste au-dessus de la zone de message.

    *Alternative : Si vous avez plusieurs fichiers modifiés et que vous voulez tout commiter d'un coup sans les stager un par un, vous pouvez cliquer sur la flèche déroulante à côté de "Commit" et choisir "Commit All". Dans ce cas, l'étape 4 n'est pas nécessaire.*

6.  **Pousser (Push) les modifications vers GitHub :**
    * Une fois le commit effectué, vous verrez que votre branche locale est "en avance" sur la branche distante. VS Code vous indiquera généralement cela avec une icône de nuage avec une flèche montante dans la barre d'état en bas à gauche, ou un indicateur numérique (par exemple, "↑ 1" signifiant 1 commit à pousser).
    * Pour pousser ces commits vers GitHub :
        * Cliquez sur les trois points `...` (More Actions) en haut à droite de la vue "Source Control".
        * Sélectionnez `Push` (Pousser).
        * Si c'est la première fois que vous poussez des modifications après avoir lié votre dépôt local à un dépôt GitHub, VS Code peut vous demander de vous authentifier via votre navigateur. Suivez les instructions.

Vos modifications seront alors envoyées vers votre dépôt GitHub, et vous pourrez les voir sur la page web de votre dépôt.

---

- La documentation officielle Git et GitHub.[1]

[1 Documentation](https://docs.github.com/fr/get-started/start-your-journey/git-and-github-learning-resources)
