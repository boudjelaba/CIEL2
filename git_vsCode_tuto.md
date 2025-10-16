# Git avec VS Code

*(Basé sur le tutoriel en ligne de commande `git_bash_tuto1.md`)*

Ce TP permet de :

* Voir les changements en temps réel (dans l'interface graphique de Git intégrée à VS Code),
* Utiliser Git **sans retenir toutes les commandes tout de suite**.

---

## Extensions Git à installer dans VS Code

### 1. **GitLens — Git supercharged**

[GitLens sur Marketplace](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens)

#### Fonctions principales :

* Voir **qui a modifié chaque ligne** (blame)
* Voir l’**historique détaillé** d’un fichier ou d’un commit
* Naviguer dans les **branches, commits, tags, remotes**
* Visualiser facilement les **diffs**
* Explorer visuellement l’**historique de projet**
* Suivre les **auteurs des modifications**

#### Utilité :

* Renforcer la compréhension de l’**historique de modification**
* Aider à visualiser les effets des commits et merges
* Aider à se repérer dans le projet

---

### 2. **Git Graph**

[Git Graph sur Marketplace](https://marketplace.visualstudio.com/items?itemName=mhutchie.git-graph)

#### Fonctions principales :

* Visualiser l’**arborescence complète des branches**
* Voir les **fusions, commits, tags** de manière graphique
* Faire du **drag & drop** pour merge, rebase, etc.
* Afficher les détails d’un commit ou d’un fichier modifié

#### Utilité :

* Montrer de manière **visuelle et immédiate** ce qu’est une branche, un merge, etc.
* Idéal pour les **exercices sur les branches et fusions**
* Rendre visible les conflits éventuels et l’évolution du projet

---

### 3. **Git History**

[Git History sur Marketplace](https://marketplace.visualstudio.com/items?itemName=donjayamanne.githistory)

#### Fonctions principales :

* Voir l’**historique des commits** fichier par fichier
* Restaurer un fichier à une version précise
* Parcourir les commits et leurs contenus

#### Utilité :

* Permet de **voir ce qu’on a fait** à chaque étape
* Outil simple et efficace pour les TP de restauration

---

### 4. **.gitignore Generator** *(optionnel)*

[Gitignore Generator](https://marketplace.visualstudio.com/items?itemName=codezombiech.gitignore)

* Permet de **générer automatiquement un `.gitignore`**
* Choix par langage (ex : Node.js, Python, Java, etc.)

---

## Objectifs :

* Créer un dépôt Git local dans VS Code
* Gérer des fichiers et voir leur état (modifiés, suivis, supprimés)
* Faire des commits à travers l’interface
* Utiliser les branches dans VS Code
* Comprendre les notions de staging, historique, restauration

---

## Prérequis :

* Ouvrir VS Code dans le bon dossier de projet

---

## TP : Git avec VS Code

---

### Étape 1 – Création du projet

1. **Ouvrir VS Code**
2. Dans le menu : `Fichier > Ouvrir un dossier...` ➜ Créer un dossier `mon-projet`
3. Dans l’explorateur VS Code, cliquer sur l’icône `+` pour créer ces fichiers :

   * `accueil.html`
   * `style.css`
   * `image.png` (crée un fichier vide pour l’exemple)
   * `readme.md`

> On peut écrire un petit texte dans `readme.md` dès maintenant.

---

### Étape 2 – Initialiser un dépôt Git

1. Cliquer sur l’icône **Source Control** dans la barre latérale (sorte de branche)
2. Cliquer sur **"Initialiser le dépôt"** ➜ Git commence à suivre le projet.

---

### Étape 3 – Faire un premier commit

1. On voit que les 4 fichiers apparaissent comme **"modifiés"** (U = untracked)
2. Cliquer sur le "+" à côté de chaque fichier pour les ajouter au staging (ou cliquer sur "Tout ajouter")
3. En haut, écrire un message de commit :

   > `Premier commit : ajout des fichiers de base`
4. Cliquer sur la coche ✔️ pour valider le commit

---

### Étape 4 – Modifier un fichier et committer

1. Modifier `readme.md` (ajouter un titre, par exemple `# Mon Projet Git`)
2. On verra le fichier repasser en "modifié" dans Git
3. Cliquer sur `+` ➜ Écrire un message de commit ➜ Cliquer sur ✔️

---

### Étape 5 – Restaurer un fichier modifié

1. Modifier `style.css` : ajouter une ligne comme `body { background: lightblue; }`
2. Clic droit sur le fichier dans l'onglet Git ➜ Sélectionner **"Discard Changes"**
3. Confirmer ➜ Le fichier revient à son état précédent (non modifié)

> Attention, cette action **efface la modification sans possibilité d’annulation**

---

### Étape 6 – Supprimer un fichier et le restaurer

1. Supprimer `readme.md` depuis l’explorateur

2. On verra que Git détecte la suppression (D)

3. Faire un commit :

   > `Suppression de readme.md`

4. Pour le restaurer :

   * Aller dans l'onglet **Source Control**
   * Cliquer sur les `…` (trois points en haut à droite) ➜ `View Commit History` *(ou installer l’extension Git History si elle n'est pas installée)*
   * Trouver le commit où `readme.md` existait ➜ Clic droit ➜ `Checkout file` (ou `Revert this commit` selon l’outil utilisé)

---

### Étape 7 – Créer et utiliser une branche

1. Cliquer en bas à gauche sur le nom de la branche actuelle (ex : `master` ou `main`)
2. Choisir **Créer une nouvelle branche** ➜ Nom : `nouvelle-fonctionnalite`
3. On est maintenant sur cette branche
4. Modifier `accueil.html` ➜ Ajouter un `<h1>` ➜ Committer

---

### Étape 8 – Revenir à `master` (ou `main`) et fusionner

1. Cliquer en bas à gauche pour revenir à la branche `master`
2. Cliquer sur les `…` ➜ `Merge Branch...` ➜ Choisir `nouvelle-fonctionnalite`
3. Git fusionne automatiquement les modifications
4. Supprimer la branche si on veut : `… > Delete Branch`

---

## Résumé du TP VS Code

| Action                        | Méthode dans VS Code                         |
| ----------------------------- | -------------------------------------------- |
| Initialiser Git               | Onglet Git > "Initialiser le dépôt"          |
| Ajouter au staging            | Clic sur "+" à côté du fichier               |
| Faire un commit               | Saisir un message + clic sur `✔️`            |
| Créer une branche             | Barre du bas > Cliquer sur le nom de branche |
| Changer de branche            | Idem                                         |
| Fusionner une branche         | Onglet Git > `…` > Merge                     |
| Restaurer un fichier supprimé | Via l’historique ou extension Git History    |

---

## Vérification : GitLens et Git Graph

> 1. Ouvrir GitLens ➜ clic droit sur un fichier ➜ `Show File History`
> 2. Utiliser Git Graph pour visualiser les branches
> 3. Merger une branche et observer le résultat dans le graphe



