# Jupyter Notebook

## 1. Créer le venv

```bash
python -m venv nom_venv
```

> `nom_venv` peut être remplacé par le nom du projet.

### 2. Activer le venv et installer Jupyter

**Windows :**

```bash
nom_venv\Scripts\activate
pip install --upgrade pip
pip install jupyter ipykernel
```

**macOS / Linux :**

```bash
source nom_venv/bin/activate
pip install --upgrade pip
pip install jupyter ipykernel
```

### 3. Ajouter le venv comme kernel Jupyter

```bash
python -m ipykernel install --user --name=nom_venv --display-name "Python NomVenv"
```

> Dans Jupyter Notebook, on pourra maintenant choisir **Python NomVenv** comme kernel.

* On ouvre Jupyter Notebook (`jupyter notebook`), kernel “Python NomVenv” et tout ce qu’on installe reste isolé dans ce venv.
* Pour ajouter des packages supplémentaires (ex : `numpy`, `matplotlib`), juste `pip install numpy` dans ce venv et redémarrer le kernel.

```bash
pip install numpy matplotlib pillow
```

---
