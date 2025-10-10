# **Git avec Visual Studio Code**

Visual Studio Code (VS Code) intègre nativement un client Git puissant, qui permet de gérer ses dépôts sans quitter l’éditeur.

---

## **1. Prérequis**
- Avoir [VS Code installé](https://code.visualstudio.com/).
- Avoir [Git installé](https://git-scm.com/) et configuré (voir séance précédente).
- Ouvrir un dossier déjà initialisé avec Git (`git init`) ou cloner un dépôt existant.

1.  **Ouvrir le Terminal Intégré de VS Code** : Aller dans `Terminal > New Terminal` (ou utiliser le raccourci ` Ctrl + Shift +  `).
2.  **Vérifier votre configuration Git** :
    ```bash
    git config --global user.name
    git config --global user.email
    ```
    Si ces informations ne sont pas configurées, faites-le :
    ```bash
    git config --global user.name "Votre Nom"
    git config --global user.email "votre.email@carnus.fr"
    ```
3.  **Définir VS Code comme éditeur par défaut pour Git (optionnel mais recommandé) :**
    ```bash
    git config --global core.editor "code --wait"
    ```

---

## **2. Ouvrir un dépôt Git dans VS Code**
- Ouvrir VS Code.
- `Fichier > Ouvrir le dossier...` et sélectionner le dossier de votre projet Git.
- VS Code détecte automatiquement le dépôt Git et affiche l’icône Git dans la barre latérale.

---

## **3. Interface Git de VS Code**

| Élément | Description |
|---------|-------------|
| **Icône Git** (barre latérale) | Ouvre le panneau Git. |
| **Liste des fichiers modifiés** | Affiche les fichiers modifiés, ajoutés, supprimés. |
| **Zone de staging** | Permet d’ajouter/supprimer des fichiers avant commit. |
| **Zone de commit** | Champ pour entrer le message de commit. |
| **Bouton Commit** | Valide les modifications en staging. |
| **Bouton Synchronisation** | Push/Pull avec le dépôt distant. |
| **Branches** | Liste et gestion des branches. |

---

## **4. Workflow de base**

### **a. Voir les modifications**
- Ouvrir le panneau Git (icône Git).
- Les fichiers modifiés s’affichent sous **Changes**.
- Cliquer sur un fichier pour voir les différences (diff) directement dans l’éditeur.

### **b. Ajouter des fichiers au staging**
- Cliquer sur le "+" à côté d’un fichier pour l’ajouter au staging.
- Ou utiliser la commande `Ctrl+Enter` (Windows/Linux) ou `Cmd+Enter` (Mac) sur le fichier sélectionné.

### **c. Faire un commit**
- Entrer un message de commit dans le champ prévu.
- Cliquer sur le bouton **Commit** (icône de validation).
- Pour commiter tous les fichiers modifiés en une fois : cocher l’option **Always show staging changes** et utiliser le bouton **Commit All**.

### **d. Pousser vers un dépôt distant**
- Cliquer sur l’icône de synchronisation (flèches circulaires) en bas à gauche.
- Ou utiliser le menu **... > Push**.

---

## **5. Gestion des branches**

### **a. Créer une nouvelle branche**
- Cliquer sur le nom de la branche actuelle (en bas à gauche).
- Sélectionner **Create new branch...**.
- Entrer le nom de la nouvelle branche et valider.

### **b. Changer de branche**
- Cliquer sur le nom de la branche actuelle.
- Sélectionner la branche souhaitée dans la liste.

### **c. Fusionner des branches**
- Se placer sur la branche de destination (ex: `main`).
- Cliquer sur l’icône Git, puis sur les `...` (plus d’options).
- Sélectionner **Merge Branch...** et choisir la branche à fusionner.

---

## **6. Résolution de conflits**
- Si un conflit survient lors d’un merge ou d’un pull, VS Code le signale dans le panneau Git et dans les fichiers concernés.
- Ouvrir le fichier en conflit : VS Code affiche des boutons **Current Changes**, **Incoming Changes**, et **Both Changes**.
- Choisir la version à garder ou éditer manuellement.
- Sauvegarder le fichier, puis faire un commit pour valider la résolution.

---

## **7. Intégration avec GitHub (distant) dans VS Code**

Pour interagir avec GitHub (push, pull, clone), vous utiliserez les fonctionnalités intégrées de VS Code et potentiellement l'extension "GitHub Pull Requests and Issues".

1.  **Cloner un Dépôt GitHub Existant** :

      * Ouvrir la palette de commandes (`Ctrl+Shift+P` ou `Cmd+Shift+P`).
      * Taper "Git: Clone" et sélectionner-le.
      * Entrer l'URL du dépôt GitHub (par exemple, `https://github.com/CharlesCarnus/mon_depot.git`).
      * Choisir un répertoire local où cloner le dépôt. VS Code l'ouvrira automatiquement une fois cloné.

2.  **Pousser (Push) votre Dépôt Local vers GitHub** :

      * **Si votre dépôt local n'est pas encore lié à GitHub :**
          * Créer un nouveau dépôt vide sur GitHub (sans README ni .gitignore).
          * Dans VS Code, ouvrir la palette de commandes (`Ctrl + Shift + P`).
          * Taper "Git: Add Remote" et sélectionner-le.
          * Coller l'URL de votre dépôt GitHub et donner-lui un nom (par exemple, `origin`).
      * **Pour pousser vos commits locaux :**
          * Dans la vue "Source Control", cliquer sur les trois points `...` (More Actions) en haut.
          * Sélectionner `Push` (Pousser) ou `Push To...` (Pousser vers...).
          * Si c'est le premier push d'une branche, VS Code vous demandera de confirmer de "publish" la branche (ce qui équivaut à `git push -u origin <branche>`). Confirmer.
          * Vous devrez peut-être vous authentifier avec vos identifiants GitHub via un navigateur web.

3.  **Tirer (Pull) les Modifications de GitHub** :

      * Pour récupérer et fusionner les dernières modifications du dépôt distant :
          * Dans la vue "Source Control", cliquer sur les trois points `...` (More Actions).
          * Sélectionner `Pull` (Tirer).
          * Si un conflit survient, VS Code vous guidera pour le résoudre (voir "Résolution des Conflits").

4.  **Publier une Branche (Publish Branch)** :

      * Si vous avez créé une nouvelle branche locale et que vous souhaitez la rendre disponible sur GitHub :
          * Cliquer sur le bouton "Publish Branch" dans la barre d'état en bas à gauche (icône de nuage avec une flèche montante) ou dans la vue "Source Control", sous les trois points `...` `> Push To... > Publish Branch`.

## **8. Extensions utiles pour Git dans VS Code**

| Extension | Description |
|-----------|-------------|
| [GitLens](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens) | Superpose des informations Git directement dans le code (auteur, date, commit, etc.). |
| [Git Graph](https://marketplace.visualstudio.com/items?itemName=mhutchie.git-graph) | Visualise l’historique des commits sous forme de graphe. |
| [Git History](https://marketplace.visualstudio.com/items?itemName=donjayamanne.githistory) | Affiche l’historique des commits et des diffs pour un fichier. |

---

## **9. Bonnes pratiques avec Git dans VS Code**
- **Commits réguliers** : Commiter souvent avec des messages clairs.
- **Pull avant push** : Toujours faire un `Pull` avant un `Push` pour éviter les conflits.
- **Branches courtes** : Une branche = une fonctionnalité ou un correctif.
- **Vérifier les diffs** : Toujours vérifier les modifications avant de commiter.
- **Utiliser GitLens** : Pour une meilleure visibilité de l’historique et des changements.

### **petits scénarios d’erreurs**

- *J’ai ajouté un fichier par erreur → git restore --staged*  
- *J’ai supprimé un fichier → git restore*  
- *Je veux revenir à hier → git checkout commit_id chemin* 

### ➕ **Git Stash (sauvegarder sans commit)**
```bash
git stash        # Sauvegarde les modifs en cours
git stash list   # Voir les stash
git stash apply  # Récupérer les modifs
```
> Si vous commencez directement par modifier `index.html`, puis vous devez rapidement pull → Solution : stash.

### ➕ Ajouter une section **Tags (versions officielles)**
```bash
git tag v1.0     # Poser un tag
git tag          # Lister les tags
git checkout v1.0  # Se placer sur le tag
```
> Utile pour comprendre comment on "fige" une version logicielle.


### ➕ Bonnes pratiques en équipe (introduction)
- Faire souvent `git pull` sur main avant de créer une branche.
- Préférer `git log --oneline --graph --decorate` pour visualiser.
- Push petits et réguliers → éviter le "commit monstrueux".

---

## **10. Résumé des commandes clés via VS Code**

| Action | Méthode |
|--------|---------|
| Ouvrir le panneau Git | Cliquer sur l’icône Git ou `Ctrl+Shift+G` |
| Ajouter un fichier au staging | Cliquer sur le "+" ou `Ctrl+Enter` |
| Commiter | Entrer un message et cliquer sur **Commit** |
| Pousser les changements | Cliquer sur l’icône de synchronisation |
| Créer une branche | Cliquer sur le nom de la branche > **Create new branch...** |
| Fusionner une branche | **... > Merge Branch...** |
| Résoudre un conflit | Éditer le fichier, choisir les changements, commiter |

---

# **TP : Git avec Visual Studio Code**

## **Objectifs**
- Utiliser l’interface Git de VS Code.
- Maîtriser les branches, commits et fusions via l’IDE.
- Savoir résoudre des conflits dans VS Code.

---

## **Prérequis**
- VS Code installé.
- Git installé et configuré.
- Avoir cloner ou initialisé un dépôt Git.

---

## **Introduction**

- Le **menu contextuel "GitLens → Show Commit History for this File"** → rend Git "vivant", et vous pouvez voir quand un fichier a évolué.

---

## **Énoncé**

### **1. Cloner un dépôt (optionnel)**
1. Clonez ce dépôt d’exemple : [https://github.com/boudjelaba/Git_Versions.git](https://github.com/boudjelaba/Git_Versions.git) ou [https://github.com/boudjelaba/template-depot-git.git](https://github.com/boudjelaba/template-depot-git.git) (ou utilisez un dépôt local existant)
2. Ouvrez le dossier dans VS Code.





---

### **2. Premier commit via VS Code**
1. Ouvrez le panneau Git (icône Git).
2. Créez un fichier `README.md` avec le contenu suivant :
   ```markdown
   # TP Git avec VS Code
   Ce dépôt sert à s’entraîner avec Git dans VS Code.
   ```
3. Ajoutez le fichier au staging via l’interface.
4. Commitez avec le message `"Ajout du README"`.

---

### **3. Modification et visualisation des diffs**
1. Modifiez le `README.md` en ajoutant une ligne :
   ```markdown
   - Première modification.
   ```
2. Visualisez les modifications dans VS Code (clic sur le fichier modifié).
3. Commitez avec le message `"Mise à jour du README"`.

---

### **4. Gestion des branches**
1. Créez une branche `ajout-licence` via VS Code.
2. Basculez sur cette branche.
3. Créez un fichier `LICENSE` avec le texte `"MIT License"`.
4. Commitez avec le message `"Ajout de la licence"`.
5. Revenez sur `main`.
6. Fusionnez `ajout-licence` dans `main` via l’interface.

---

### **5. Résolution de conflit**
1. Créez une branche `modif-readme`.
2. Modifiez le `README.md` :
   ```markdown
   # TP Git avec VS Code
   Ce dépôt sert à s’entraîner avec Git dans VS Code.
   - Première modification.
   - Ajout d'une licence MIT.
   ```
3. Commitez avec le message `"Ajout info licence"`.
4. Revenez sur `main` et modifiez le même fichier :
   ```markdown
   # TP Git avec VS Code
   Ce dépôt est un TP pour apprendre Git.
   - Première modification.
   ```
5. Commitez avec le message `"Modification de la description"`.
6. Fusionnez `modif-readme` dans `main`. Un conflit apparaît.
7. Résolvez le conflit dans VS Code en gardant les deux modifications.
8. Commitez la résolution.

---

### **6. Utilisation de GitLens**
1. Installez l’extension GitLens.
2. Ouvrez le fichier `README.md` et visualisez l’historique des modifications (clic sur la ligne ou l’icône GitLens).
3. Explorez les fonctionnalités de GitLens (blame, historique, etc.).

---

### **7. Push vers un dépôt distant (optionnel)**
1. Créez un dépôt vide sur GitHub.
2. Ajoutez l’URL du dépôt distant via VS Code.
3. Poussez vos modifications avec l’icône de synchronisation.

---

## **Solution attendue**
- Un dépôt Git avec un historique propre, visible dans VS Code.
- Les fichiers `README.md` et `LICENSE` correctement versionnés.
- Aucun conflit non résolu.

---

## **Documentation et partage (les deux TP)**
- Ajoutez une section dans le `README.md` expliquant ce que vous avez appris.
- Partagez votre dépôt sur GitHub et envoyez le lien à votre professeur.

---

### **Questions** :  
  - "Quelle commande sert à voir l’état du dépôt ?"
  - "Quelle différence entre `git add` et `git commit` ?"
  - "Que fait `git merge` ?"

### **Bonus** : 
- travaillez à deux → un étudiant modifie `index.html`, l’autre `style.css` → pull/push → merge sans conflit.
- **Cas difficile** : les deux modifient la même ligne → montrer le conflit.

---

## **Informations utiles**
- **Durée** : 1h30 par TP.
- **Évaluation** : Vérification de l’historique Git, de la résolution des conflits, et de la propreté du dépôt.
- **Optionnel** : Pour aller plus loin, vous pouvez ajouter des étapes avec `git rebase`, `git stash`, ou la gestion de tags.
