# Git : Travailler avec un fork + push GitHub

## Objectifs

* **Cloner un dépôt GitHub** pour travailler dessus localement. 
* **Lien entre GitHub et Git local**
* Comprendre ce qu’est un **fork**
* Travailler sur une **copie distante personnelle** d’un projet
* **Pousser** les modifications sur GitHub
* **Simuler un travail collaboratif** (projet, en équipe ou projet open source)

## Contexte

> Forker un dépôt GitHub, c’est comme **faire une copie** dans notre propre compte.
> On peut y faire toutes les modifications qu'on veut sans toucher à l’original.
> Ensuite, on peut proposer nos changements via une **pull request**, ou simplement garder le projet modifié.

## TP Git avec VS Code – Fork + clone + modification + push

### Prérequis

Avoir un compte Github (ou créer un compte si nécessaire)

### 1. Fork du dépôt (depuis GitHub)

1. Aller sur mon github (`https://github.com/boudjelaba/atelier-git-vscode`)
2. Cliquer sur le bouton **Fork** en haut à droite
3. GitHub crée une copie du dépôt dans votre compte (ex : `https://github.com/etudiant/atelier-git-vscode`)

---

### 2. Cloner votre fork sur votre machine

Dans VS Code ou dans Git Bash :

```bash
git clone https://github.com/etudiant/atelier-git-vscode.git
```

Puis :

```bash
cd atelier-git-vscode
code .
```

---

### 3. Créer une branche personnelle

Avant de modifier les fichiers, créer une branche dédiée à votre travail :

```bash
git switch -c ajout-bio
```

---

### 4. Modifier un fichier

Par exemple, dans `accueil.html`, ajouter une section :

```html
<section>
  <h2>À propos de moi</h2>
  <p>Je m'appelle [nom prénom]</p>
</section>
```

---

### 5. Ajout et commit

Une fois la modification terminée, sauvegarder et dans le terminal :

```bash
git add accueil.html
git commit -m "Ajout d'une section bio"
```

---

### 6. Pousser votre branche sur GitHub

Pour envoyer votre branche sur votre dépôt distant (fork) :

```bash
git push origin ajout-bio
```

---

### 6. (Optionnel) Faire une pull request

* Aller sur votre dépôt GitHub forké
* GitHub détecte automatiquement qu'on a poussé une branche et propose de créer une Pull Request (PR).
* Cliquer sur **"Compare & Pull Request"**
* Ajouter un message, puis cliquer sur **Create pull request**.

> Cela simule la proposition de modifications à un projet existant.

* Faire une **pull request** vers mon dépôt

---

## ✅ Résumé des commandes utiles

```bash
# Cloner son propre fork
git clone https://github.com/moi/atelier-git.git
cd atelier-git

# Créer une branche
git switch -c nom-de-branche

# Modifier des fichiers, puis :
git add .
git commit -m "message"
git push origin nom-de-branche
```

---

