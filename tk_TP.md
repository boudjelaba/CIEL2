# **TP Tkinter (Python)**

**Tkinter / CustomTkinter / Widgets / Tableaux / Graphiques**

**Objectif :** Créer une interface graphique

**Approche :** Apprentissage par construction progressive

--- 

## **PARTIE 1 — Découverte & Installation**

### 1. Installer les dépendances

```bash
pip install customtkinter pillow matplotlib numpy
```

### 2. Créer un premier fichier : `tp_interface.py`

**Objectif** : comprendre comment démarrer une application CustomTkinter.

```python
import customtkinter

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.title("TP Tkinter")
app.geometry("600x400")

app.mainloop()
```

---

## **PARTIE 2 — Navigation avec Menu Latéral**

**Objectif** : comprendre la logique des `frames` et du changement d'écran.

### Étape 2.1 — Créer un menu latéral

```python
import customtkinter

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("TP Tkinter")
        self.geometry("900x500")

        # Frame menu
        self.menu = customtkinter.CTkFrame(self, width=150)
        self.menu.grid(row=0, column=0, sticky="ns")

        # Boutons navigation
        self.btn_home = customtkinter.CTkButton(self.menu, text="Home", command=self.show_home)
        self.btn_data = customtkinter.CTkButton(self.menu, text="Données", command=self.show_data)

        self.btn_home.pack(pady=10)
        self.btn_data.pack(pady=10)

        # Frames de contenu
        self.home = customtkinter.CTkFrame(self)
        self.data = customtkinter.CTkFrame(self)

        self.show_home()

    def show_home(self):
        self.data.grid_forget()
        self.home.grid(row=0, column=1, sticky="nsew")

    def show_data(self):
        self.home.grid_forget()
        self.data.grid(row=0, column=1, sticky="nsew")


app = App()
app.mainloop()
```

---

## **PARTIE 3 — Widgets interactifs**

### Étape 3.1 — Champ de saisie + Bouton

Ajouter dans `self.home` :

```python
self.entry = customtkinter.CTkEntry(self.home, placeholder_text="Angle en degrés")
self.entry.pack(pady=10)

self.btn_convert = customtkinter.CTkButton(self.home, text="Convertir", command=self.convert)
self.btn_convert.pack()

self.label_result = customtkinter.CTkLabel(self.home, text="")
self.label_result.pack(pady=10)
```

Fonction :

```python
def convert(self):
    try:
        angle = float(self.entry.get())
        rad = angle * 3.14159 / 180
        self.label_result.configure(text=f"{angle}° = {rad:.3f} rad")
    except:
        self.label_result.configure(text="Erreur : nombre invalide")
```

---

### Étape 3.2 — LED animée (Canvas)

**Objectif** : comprendre l’utilisation de Canvas + animation simple.

```python
self.canvas = customtkinter.CTkCanvas(self.home, width=100, height=100)
self.canvas.pack()

self.led = self.canvas.create_oval(20, 20, 80, 80, fill="grey")

self.btn_led = customtkinter.CTkButton(self.home, text="Start LED", command=self.run_led)
self.btn_led.pack()
```

Fonction :

```python
import time

def run_led(self):
    colors = ["red", "yellow", "green"]
    for c in colors:
        self.canvas.itemconfig(self.led, fill=c)
        self.update()
        time.sleep(1)
```

---
