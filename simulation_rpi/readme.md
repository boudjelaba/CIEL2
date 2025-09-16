# **TP : Simulation d’un système d’alerte avec Flask et GPIO (Mock)**

*Mock : Objet simulé qui imite le comportement d'un objet réel dans un but de test.* 

**Matériel requis :** Un ordinateur, Python installé, accès à Internet
**Aucun Raspberry Pi requis dans cette partie.**

---

## Objectifs

* Déclencher une alerte en appuyant sur un bouton simulé (Touche `Entrée`)
* Transmettre des données d’alerte via HTTP (POST)
* Visualiser les alertes reçues sur une interface web locale
* Séparer la logique matérielle de la logique logicielle (via Mock)

---

## Partie 1 – Mise en place de l’environnement

**Structure des fichiers**

```
systeme_alerte_simulation/
├── MockGPIO.py
├── test_composants.py
├── systeme_alerte.py
└── serveur_alertes.py
```

**Instructions** :

1. Créer un dossier de projet :
   `systeme_alerte_simulation/`

2. Créer les fichiers suivants avec les contenus donnés :

   * `MockGPIO.py`
   * `test_composants.py`
   * `serveur_alertes.py`
   * `systeme_alerte.py`

3. Vérifier que Python est installé (3.8 ou +) :

   ```bash
   python --version
   ```

4. Installer Flask (si nécessaire) :

   ```bash
   pip install flask
   ```

---

## Partie 2 – Lancer le serveur d’alertes

**But :** Démarrer un serveur web capable de recevoir des alertes

1. Lancer `serveur_alertes.py` :

   ```bash
   python serveur_alertes.py
   ```

2. Ouvrir dans un navigateur :

   ```
   http://localhost:5000
   ```

   Ou `http://localhost:5000/alertes`

3. Test (facultatif) : envoyer une alerte manuellement avec `curl` :

   ```bash
   curl -X POST http://localhost:5000/alertes \
     -H "Content-Type: application/json" \
     -d '{"message": "Test manuel", "source": "poste1"}'
   ```

**Résultat attendu** : L’alerte est affichée sur `/alertes`

---

## Partie 3 – Déclencher une alerte via bouton simulé

**But :** Simuler un bouton d’alerte qui envoie une requête POST au serveur

1. Ouvrir un second terminal et lancer le fichier `systeme_alerte.py` :

   ```bash
   python systeme_alerte.py
   ```

2. Appuyer sur la touche `Entrée` (dans le terminal) dès que le programme est lancé pour simuler un appui sur le bouton.


**Résultat attendu** :

* Le script envoie une alerte avec un message
* L’alerte est visible sur le serveur `/alertes`

---

## Partie 4 – Questions / Débrief

1. À quoi sert `MockGPIO` dans cette simulation ?
2. Que se passe-t-il si le serveur est arrêté ? (relancer et tester)
3. Proposez une amélioration visuelle sur `/alertes` (ex : couleur selon type)
4. Quelle serait la différence si on utilisait un vrai Raspberry Pi ?

---