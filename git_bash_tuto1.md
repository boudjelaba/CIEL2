# Tutoriel Git – Git Bash

## Objectif :

Apprendre à utiliser **Git en ligne de commande** avec **Git Bash**, à partir de zéro.
Nous allons :

1. Créer un dossier de projet avec quelques fichiers simples
2. Initialiser un dépôt Git
3. Suivre les étapes de base : `git add`, `git commit`, etc.

## Pré-requis : Installer Git Bash
- Télécharger Git Bash depuis le site officiel : [git-scm.com](https://git-scm.com).[5]
- Savoir naviguer un peu dans l’arborescence des dossiers (cd, ls, dir...)

### Étape 1 : Créer le dossier du projet

Ouvrir Git Bash et taper les commandes suivantes :
```bash
# 1. Aller dans le dossier où on veut créer le projet (ex. sur le Bureau)
cd ~/Desktop

# 2. Créer un dossier nommé "mon-projet-web"
mkdir mon-projet-web

# 3. Entrer dans ce dossier
cd mon-projet-web
```

### Étape 2 : Créer les fichiers de base

Dans le terminal, taper :
```bash
touch accueil.html
touch style.css
touch image.png
touch readme.md
```
- Chaque ligne crée un fichier vide correspondant (HTML, CSS, image, README).

Vérifier que les fichiers ont bien été créés :

```bash
dir # ls
```

### Étape 3 : Initialiser le dépôt Git

Toujours dans le dossier, taper :
```bash
git init
```
- Cette commande crée un dépôt Git local, permettant de suivre les modifications des fichiers.

**Vérifier l’état du dépôt**

```bash
git status
```

Git nous dira qu'on a des fichiers **non suivis**

### Résumé des commandes utilisées

| Commande               | Explication                                                          |
|------------------------|-----------------------------------------------------------------------|
| mkdir mon-projet-web   | Crée un dossier nommé "mon-projet-web"                       |
| cd mon-projet-web      | Entre dans le dossier créé                                    |
| touch accueil.html       | Crée un fichier accueil.html vide                               |
| touch style.css        | Crée un fichier style.css vide                                |
| touch image.png        | Crée un fichier image.png vide                                |
| touch readme.md        | Crée un fichier readme.md vide                               |
| git init               | Initialise le dépôt Git dans le dossier                       |

---

### Ajouter les fichiers à Git

Dans le terminal, taper :
```bash
git add accueil.html style.css image.png readme.md
```
- Cette commande ajoute ces fichiers à l’index (zone de préparation).

Si vous souhaitez ajouter tous les fichiers du dossier, on peut utiliser :
```bash
git add .
```
- Cela sélectionne tous les fichiers et dossiers présents dans le répertoire courant.

### Vérifier les fichiers suivis

Pour voir quels fichiers sont suivis (ou non suivis), utiliser :
```bash
git status
```
- Les fichiers marqués « nouveaux fichiers » ont été ajoutés à l’index mais pas encore validés.

### Valider (commit) les fichiers

Pour enregistrer ces fichiers dans l’historique du projet :
```bash
git commit -m "Initialisation du projet web avec 4 fichiers"
```
- « -m » permet d’ajouter un message décrivant votre commit.

**Vérifier l’historique**

```bash
git log
```

### Récapitulatif du workflow

Voici un résumé des commandes utilisées pour l'ajout et le suivi des fichiers :

| Commande                                | Explication                                                  |
|------------------------------------------|--------------------------------------------------------------|
| git add nom_du_fichier                   | Ajoute un fichier spécifique à l’index       |
| git add .                                | Ajoute tous les fichiers et dossiers à l’index       |
| git status                               | Affiche le statut des fichiers et du dépôt   |
| git commit -m "Message de commit"        | Valide les changements dans l’historique Git |

---

## `.gitignore`

Pour ignorer un fichier config.txt contenant des données sensibles, il faut créer et configurer le fichier `.gitignore` à la racine du projet.

### Étape 1 : Créer le fichier config.txt

Dans Git Bash, taper :
```bash
touch config.txt
```
- Cette commande crée le fichier destiné à contenir des données sensibles (identifiant, mot de passe, etc.).
- Ajouter ces lignes dans le fichier `config.txt` :
    ```text
    login : carnus_bts_ciel
    mdp : Git_CIEL@BTS#12
   ``` 
- Juste pour vérifier : 
    ```bash
    git add config.txt
    ```

    ```bash
    git status
    ```

    ```bash
    git commit -m "Ajout de config.txt dans le suivi"
    ```

    ```bash
    git status
    ```

    ```bash
    git ls # dir
    ```

    ```bash
    git rm --cached config.txt
    ```

### Étape 2 : Créer le fichier .gitignore

Toujours dans le terminal :
```bash
touch .gitignore
```
- Cela crée un fichier spécial servant à indiquer à Git quels fichiers doivent être ignorés.

### Étape 3 : Configurer .gitignore pour ignorer config.txt

Ouvrir le fichier `.gitignore` avec un éditeur de texte (par exemple : `nano .gitignore` ou `notepad .gitignore` sur Windows) et ajouter :
```
# Ignorer les infos sensibles
config.txt
```
- Cette ligne ordonne à Git d’ignorer le fichier config.txt lors du suivi des modifications.

### Étape 4 : Vérifier l’ignorance par Git

Pour vérifier :
```bash
git status
```
- Le fichier "config.txt" ne doit plus apparaître dans la liste des fichiers non suivis ou à suivre par Git.

### Astuce : Si le fichier était déjà suivi par Git

S’il avait été ajouté avant la règle .gitignore, il faut l’enlever du suivi en tapant :
```bash
git rm --cached config.txt
```
- Cela supprime le suivi tout en gardant le fichier localement.

---

### Étape 1 : Modifier un fichier

Ouvrir et modifier l’un des fichiers (ex : accueil.html) avec un éditeur de texte comme Notepad, Visual Studio Code ou directement dans le terminal (nano/vim par exemple).

```bash
notepad accueil.html    # Windows
# ou code accueil.html  # Windows
```

**Ajouter ceci dans le fichier :**

```
<p>Ce site est utilisé dans un projet d'exemple pour apprendre à utiliser Git.</p>
```

**Puis enregistrer**

### Étape 2 : Vérifier les modifications

Dans Git Bash, taper :
```bash
git status
```
- Cette commande indique quels fichiers ont été modifiés depuis le dernier commit.

### Étape 3 : Ajouter les fichiers modifiés à l’index (au commit)

Pour enregistrer les modifications faites sur le fichier `accueil.html` :
```bash
git add accueil.html
```
- Pour ajouter tous les fichiers modifiés :
```bash
git add .
```
- Ces commandes placent les modifications dans la zone de préparation (staging area).

- Puis vérifier :

    ```bash
    git status
    ```

### Étape 4 : Commit des modifications

Valider (= commit) les modifications avec un message explicatif :

```bash
git commit -m "Modifications apportées à accueil.html"
```
- Choisir un message de commit clair et explicite.

Git enregistre maintenant cette modification dans l’historique du projet.

### Étape optionnelle : Visualiser les modifications

Pour voir les différences avant de valider :
```bash
git diff
```
- Affiche les modifications faites dans les fichiers avant l’ajout (git add).

### Tableau récapitulatif

| Commande                  | Explication                                                |
|---------------------------|------------------------------------------------------------|
| git status                | Voir les fichiers modifiés ou en attente    |
| git diff                  | Afficher les différences non indexées              |
| git add nom_du_fichier    | Ajouter un fichier modifié à l’index        |
| git add .                 | Ajouter tous les fichiers modifiés          |
| git commit -m "Message"   | Valider les modifications et ajouter un commentaire |

Ce cycle (modification → ajout → commit) permet de bien suivre toutes les évolutions du projet dans Git.

---

## Afficher l'historique des commits

Pour visualiser tous les commits réalisés dans le projet avec Git Bash, utiliser la commande suivante dans le terminal :

```bash
git log
```
- Cette commande affiche la liste de tous les **commits** du plus récent au plus ancien, avec pour chaque commit : l'identifiant unique (hash), l'auteur, la date et le message de commit.
- Naviguer dans la liste en utilisant les flèches, et quitter avec la touche `q`.

Pour un aperçu plus condensé (chaque commit sur une seule ligne) :
```bash
git log --oneline
```
- C'est très utile pour avoir une vision globale du projet.

***

## Cycle de base Git (schématisé en étapes simples)

1. **Modification du/des fichier(s)** (dans le dossier du projet)
2. **Ajout à l'index** (avec `git add <fichier>`)
3. **Commit** (avec `git commit -m "Message"`)
4. **Historique consultable** (avec `git log`)

```
[Modifications] --> git add --> [Index] --> git commit --> [Historique]
```

Ce cycle « Modification → Ajout → Commit → Historique » constitue le cœur du travail avec Git. Toute nouvelle modification commence ce cycle à nouveau.

On peut réutiliser ces commandes à chaque fois qu'on ajoute ou modifie des fichiers dans le projet.

---

Pour comparer les modifications apportées à un ou plusieurs fichiers dans un dépôt Git, il existe des commandes essentielles à connaître.

### Modifier un fichier

- Utiliser un éditeur de texte (exemple : Visual Studio Code, Notepad ou nano dans le terminal) pour apporter des modifications à un ou plusieurs fichiers du projet.
- Sauvegarder ensuite les changements.

### Comparer les modifications avec la commande `git diff`

La commande `git diff` permet de visualiser ce qui a changé :

- Pour afficher les modifications non encore ajoutées à l’index (staging area) :
  ```bash
  git diff
  ```
  Cette commande montre les différences entre les fichiers du répertoire de travail et l’index, c’est-à-dire toutes les modifications en attente d’ajout.

- Pour afficher les changements déjà ajoutés à l’index (mais pas encore validés avec commit) :
  ```bash
  git diff --cached
  ```
  Cela permet de vérifier précisément ce qui va être inclus dans le prochain commit.

- Pour comparer un fichier en particulier :
  ```bash
  git diff nom_du_fichier
  ```
  On obtient les différences dans ce fichier seulement.
- ```bash
  git status
  ```
- ```bash
  git add accueil.html style.css # fichiers modifiés
  ```
- ```bash
  git status
  ```
- ```bash
  git commit -m "Ajout des modifications à accueil.html et style.css"
  ```
- ```bash
  git status
  ```

### Résumé de la comparaison

| Commande                     | Utilité                                                        |
|------------------------------|---------------------------------------------------------------|
| git diff                     | Différence entre répertoire actuel et index (avant git add)  |
| git diff --cached            | Différence entre index et dernier commit (avant commit)   |
| git diff nom_du_fichier      | Différence sur un fichier précis                           |

L’utilisation de `git diff` permet de contrôler chaque étape du cycle de modifications, d’éviter les erreurs et d’améliorer la compréhension des changements apportés au projet.

---

### Suppression et restauration de fichiers dans Git

#### Supprimer un fichier suivi par Git

**A. Supprimer un seul fichier**

1. Supprimer le fichier **du dossier ET de Git** :

   ```bash
   git rm accueil.html
   ```

2. Vérifier que Git a bien détecté la suppression :

   ```bash
   git status
   ```

   On verra :

   ```
   deleted:    accueil.html
   ```

3. Enregistrer la suppression :

   ```bash
   git commit -m "Suppression de accueil.html"
   ```

**B. Supprimer plusieurs fichiers**

1. Supprimer plusieurs fichiers d’un coup :

   ```bash
   git rm fichier1 fichier2 fichier3
   ```

2. Puis :

   ```bash
   git commit -m "Suppression de plusieurs fichiers"
   ```

**C. Supprimer un fichier **du suivi seulement** (mais le garder sur le disque)

1. Retirer le fichier du suivi Git :

   ```bash
   git rm --cached nom_du_fichier
   ```

2. Puis valider la modification :

   ```bash
   git commit -m "Retrait de nom_du_fichier du suivi Git"
   ```

> Cela est utile pour un fichier qu’on veut garder localement (ex. : un fichier de config perso), mais ne pas versionner.

#### Restaurer un fichier supprimé

**Cas 1 : La suppression **n’a pas encore été commitée**

1. Annuler simplement la suppression :

   ```bash
   git restore nom_du_fichier
   ```

> Le fichier revient à l’état dans lequel il était avant la suppression.

---

**Cas 2 : Le fichier a été supprimé et commit**

##### Étape 1 : Trouver le commit de suppression

1. Chercher le commit qui a supprimé le fichier :

- Afficher l’historique des commits pour identifier le commit ayant encore le fichier :

   ```bash
   git log --oneline
   ```

- Noter l’identifiant (hash) du commit où « `nom_du_fichier` » existe encore (par exemple : dfa88af).

##### Étape 2 : Restaurer le fichier depuis ce commit

2. Revenir à l’état **avant suppression** :

   ```bash
   git restore --source dfa88af nom_du_fichier
   ```

   * Le fichier sera restauré dans le dossier de travail, comme à l’état du commit choisi.

---

##### Étape 3 : Ajouter et valider la restauration

3. Réintégrer le fichier dans le suivi Git :

   ```bash
   git add nom_du_fichier
   git commit -m "Restauration de nom_du_fichier  depuis le commit dfa88af"
   ```

#### Exemple : restauration de `style.css`

1. **Trouver un commit où le fichier existe encore** :

   ```bash
   git log --oneline
   ```

   → Repérer un commit avant la suppression (ex. : `dfa88af`)

2. **Restaurer le fichier à partir de ce commit** :

   ```bash
   git restore --source cfa88af style.css
   ```

3. **Enregistrer la restauration (si souhaité)** :

   ```bash
   git add style.css
   git commit -m "Restauration de style.css depuis le commit cfa88af"
   ```

---

#### Résumé

| Action                                    | Commande principale                          |
| ----------------------------------------- | -------------------------------------------- |
| Supprimer un fichier                      | `git rm nom_du_fichier`                      |
| Supprimer du suivi mais garder local      | `git rm --cached nom_du_fichier`             |
| Restaurer avant commit                    | `git restore nom_du_fichier`                 |
| Valider la suppression(commit)            | `git commit -m "Suppression..." `            |
| Restaurer après commit                    | `git checkout <commit>^ -- nom_du_fichier`   |
| Restaurer depuis un commit précis         | `git restore --source <hash> nom_du_fichier` |
| Trouver le commit où le fichier existe    | `git log --oneline`                          |
| Restaurer le fichier à l’état de ce commit précis |  `git restore --source <commit> <fichier>` |
| Ajouter le fichier restauré à l’index     | `git add <fichier>`                          |
| Valider la restauration du fichier        |   `git commit -m "Message"`                  |

---

### Renommer un fichier

- Pour renommer (déplacer) un fichier (ex : accueil.html vers accueil.html) :
  ```bash
  git mv accueil.html accueil2.html
  ```
  Cette commande effectue le renommage et prépare la modification pour le commit.

- Valider le changement avec :
  ```bash
  git commit -m "Renommage de accueil.html en accueil2.html"
  ```

| Commande                        | Explication                                 |
|-------------------------------- |---------------------------------------------|
| `git mv ancien_nom nouveau_nom` | Renommer/déplacer un fichier suivi par Git  |
| `git commit -m "Renommage..."`  | Valider le renommage                        |


#### Note

On peut utiliser la commande pour voir **comment un fichier a évolué** :

```bash
git log -- readme.md
```

Elle montre uniquement les commits liés à ce fichier, ce qui est très pratique pour naviguer dans son historique.

---
---

## Créer et utiliser une branche avec Git Bash

### Branche

Une **branche Git** est comme une **version parallèle** de notre projet.
On peut y faire des modifications, des tests, des ajouts **sans impacter la version principale (`main` ou `master`)**.

Créer une branche permet de travailler sur des fonctionnalités ou des modifications spécifiques sans modifier la branche principale (souvent nommée `main` ou `master`). 

**Vérifier sur quelle branche on est :**

```bash
git branch
```

Résultat :

```
* master
```

L’astérisque `*` indique qu'on est actuellement sur la branche `master`.

### 1. Créer une nouvelle branche

Il y a deux manières principales :
- **Créer la branche sans changer de branche :**
  ```bash
  git branch ma-nouvelle-branche
  ```

  * Puis, on bascule sur la nouvelle branche :

    ```bash
    git checkout nouvelle-fonctionnalite
    ```

- **Créer et basculer directement sur la nouvelle branche :**
  ```bash
  git checkout -b ma-nouvelle-branche
  ```
  ou avec les versions récentes de Git :
  ```bash
  git switch -c ma-nouvelle-branche
  ```

### 2. Lister les branches existantes
```bash
git branch
```
- La branche courante s'affiche avec un astérisque `*` devant son nom.

### 3. Passer sur une autre branche
```bash
git checkout nom-de-la-branche
```
- Avec les versions récentes de Git, tu peux aussi faire :
```bash
git switch nom-de-la-branche
```

### 4. Travailler sur la branche

Après avoir créé et basculé sur la nouvelle branche, on peut :
- Modifier des fichiers ou en créer de nouveaux (ex : ajouter une nouvelle fonctionnalité ou corriger une erreur).
- Ajouter ces modifications à l’index avec :
  ```bash
  git add nom_du_fichier
  ```
- Valider les changements avec :
  ```bash
  git commit -m "Description de cette modification"
  ```

Chaque modification effectuée sera enregistrée uniquement sur cette branche tant qu'on n’effectue pas de fusion avec la branche principale. Cela permet de développer ou tester librement sans impacter le travail sur la branche principale.

### 5. Fusionner les changements dans la branche principale
Quand on a terminé, passer sur la branche principale puis fusionner la nouvelle branche :
```bash
git checkout main  # ou master selon le nom de la branche principale
git merge ma-nouvelle-branche
```

**Astuce : Visualiser les branches avec `git log`**

Pour voir les commits par branche (mode graphique simple) :

```bash
git log --oneline --graph --all
```

Cela montre un historique clair des branches et des fusions.

### 6. Supprimer la branche (optionnel)

Une fois fusionnée, on peut supprimer la branche :

```bash
git branch -d ma-nouvelle-branche
```

***

### Résumé des commandes
| Commande                             | Action                              |
|--------------------------------------|-------------------------------------|
| `git branch nouvelle-branche`        | Crée une nouvelle branche           |
| `git checkout -b nouvelle-branche`   | Crée ET bascule sur la nouvelle     |
| `git switch -c nouvelle-branche`     | (Nouvelle syntaxe) Crée et bascule  |
| `git branch`                         | Affiche la liste des branches       |
| `git switch nom-de-la-branche`       | Bascule sur une branche             |
| `git checkout nom-de-la-branche`     | (Ancienne syntaxe) Bascule aussi    |
| `git merge nom-de-la-branche`        | Fusionne une branche sur l'actuelle |


### Documentation

* Commandes Git officielles : [https://education.github.com/git-cheat-sheet-education.pdf](https://education.github.com/git-cheat-sheet-education.pdf)

---
---


## Exercice pratique Git Bash : gestion d’un petit projet

## Objectif 
Apprendre à utiliser Git en ligne de commande pour créer un dépôt, suivre des fichiers, gérer des commits, branches et interactions courantes.

***

## Étapes à réaliser

### 1. Initialisation du projet

- Ouvrir Git Bash.
- Créer un dossier `mon-projet-git` :
  ```bash
  mkdir mon-projet-git
  cd mon-projet-git
  ```
- Initialiser un dépôt Git :
  ```bash
  git init
  ```

### 2. Création et ajout de fichiers

- Créer un fichier `accueil.html` avec du contenu simple (exemple : une page HTML vide).
- Créer un fichier `style.css` avec un style basique.
- Vérifier l’état des fichiers avec `git status`.
- Ajouter les fichiers à l’index :
  ```bash
  git add accueil.html style.css
  ```
- Checker leur statut (`git status`).
- Réaliser un commit avec un message clair :
  ```bash
  git commit -m "Ajout initial des fichiers html et css"
  ```

### 3. Modifications et suivi

- Modifier `accueil.html` en ajoutant un titre ou du texte.
- Vérifier les modifications avec `git status` et `git diff`.
- Ajouter le fichier modifié et réaliser un commit.

### 4. Gestion des fichiers ignorés

- Créer un fichier `config.txt` contenant des données sensibles.
- Créer un fichier `.gitignore`.
- Ajouter `config.txt` dans `.gitignore`.
- Vérifier que `config.txt` n'est pas pris en compte par Git (`git status`).

### 5. Travail en branches

- Créer une nouvelle branche appelée `feature`.
  ```bash
  git checkout -b feature
  ```
- Modifier un fichier sur cette branche, ajouter et "commit" les changements.
- Revenir à la branche principale `main`.
- Fusionner la branche `feature` dans `main`.

### Résumé des commandes clés à utiliser

- `git init`
- `git status`
- `git add <fichiers>`
- `git commit -m "message"`
- `git diff`
- `git checkout -b <branche>`
- `git checkout <branche>`
- `git merge <branche>`

---

## TP Git Bash – Initiation complète pour débutants

### Durée estimée : 2h à 2h30

---

### Objectifs :

- Créer un dépôt Git local
- Suivre l’évolution de leurs fichiers
- Utiliser les commandes de base : `git add`, `commit`, `status`, `log`, `restore`, etc.
- Créer et manipuler des branches
- Fusionner une branche
- Restaurer un fichier depuis l’historique
- Lire l’historique du projet

---

### Plan du TP

#### Partie 1 : Initialisation (20 min)

**Objectifs :**

* Comprendre ce qu’est Git et pourquoi on l’utilise
* Créer un dépôt local

**TP 1** :

> Crée un dépôt local contenant 4 fichiers. Ajouter-les et faire le premier commit.

**Étapes :**

1. Créer un dossier de projet
2. Créer les fichiers initiaux (`accueil.html`, `style.css`, `readme.md`, `image.png`)
3. Initialiser Git avec `git init`
4. Faire un premier commit

---

#### Partie 2 : Suivi des changements (25 min)

**Objectifs :**

* Comprendre le cycle Git : **modification ➜ staging ➜ commit**
* Voir l’état du dépôt à tout moment
* Annuler ou restaurer des changements

**Commandes clés** :
`git status`, `git diff`, `git add`, `git commit`, `git restore`

**TP 2** :

> 1. Modifier `readme.md` en ajoutant une phrase.
> 2. Vérifier les changements avec `git diff`
> 3. Committer la modification.
> 4. Faire une autre modification, puis l'annuler **avant** de faire un commit.

---

#### Partie 3 : Historique et restauration (20 min)

**Objectifs :**

* Consulter l’historique des commits
* Restaurer un fichier depuis un commit antérieur

**Commandes clés** :
`git log`, `git checkout <commit> -- fichier`, `git restore`

**TP 3** :

> 1. Supprimer `readme.md`
> 2. Committer la suppression
> 3. Utiliser `git log` pour retrouver l’ancien commit contenant le fichier
> 4. Restaurer `readme.md` tel qu’il était dans ce commit

---

#### Partie 4 : Les branches (30 min)

**Objectifs :**

* Comprendre le fonctionnement des branches
* Travailler sur une fonctionnalité dans une branche dédiée
* Fusionner les branches

**Commandes clés** :
`git branch`, `git switch -c`, `git merge`, `git branch -d`

**TP 4** :

> 1. Créer une branche `nouvelle-section`
> 2. Ajouter une nouvelle section dans `accueil.html`
> 3. Committer le changement
> 4. Revenir sur `master`, vérifier que le changement n’y est pas
> 5. Merger la branche
> 6. Supprimer la branche

---