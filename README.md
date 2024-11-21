```python
"""
Example script for testing the Azure ttk theme
Author: rdbende
License: MIT license
Source: https://github.com/rdbende/ttk-widget-factory
"""


import tkinter as tk
from tkinter import ttk


class App(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self)

        # Make the app responsive
        for index in [0, 1, 2]:
            self.columnconfigure(index=index, weight=1)
            self.rowconfigure(index=index, weight=1)

        # Create value lists
        self.option_menu_list = ["", "OptionMenu", "Option 1", "Option 2"]
        self.combo_list = ["Combobox", "Editable item 1", "Editable item 2"]
        self.readonly_combo_list = ["Readonly combobox", "Item 1", "Item 2"]

        # Create control variables
        self.var_0 = tk.BooleanVar()
        self.var_1 = tk.BooleanVar(value=True)
        self.var_2 = tk.BooleanVar()
        self.var_3 = tk.IntVar(value=2)
        self.var_4 = tk.StringVar(value=self.option_menu_list[1])
        self.var_5 = tk.DoubleVar(value=75.0)

        # Create widgets :)
        self.setup_widgets()

    def setup_widgets(self):
        # Create a Frame for the Checkbuttons
        self.check_frame = ttk.LabelFrame(self, text="Checkbuttons", padding=(20, 10))
        self.check_frame.grid(
            row=0, column=0, padx=(20, 10), pady=(20, 10), sticky="nsew"
        )

        # Checkbuttons
        self.check_1 = ttk.Checkbutton(
            self.check_frame, text="Unchecked", variable=self.var_0
        )
        self.check_1.grid(row=0, column=0, padx=5, pady=10, sticky="nsew")

        self.check_2 = ttk.Checkbutton(
            self.check_frame, text="Checked", variable=self.var_1
        )
        self.check_2.grid(row=1, column=0, padx=5, pady=10, sticky="nsew")

        self.check_3 = ttk.Checkbutton(
            self.check_frame, text="Third state", variable=self.var_2
        )
        self.check_3.state(["alternate"])
        self.check_3.grid(row=2, column=0, padx=5, pady=10, sticky="nsew")

        self.check_4 = ttk.Checkbutton(
            self.check_frame, text="Disabled", state="disabled"
        )
        self.check_4.state(["disabled !alternate"])
        self.check_4.grid(row=3, column=0, padx=5, pady=10, sticky="nsew")

        # Separator
        self.separator = ttk.Separator(self)
        self.separator.grid(row=1, column=0, padx=(20, 10), pady=10, sticky="ew")

        # Create a Frame for the Radiobuttons
        self.radio_frame = ttk.LabelFrame(self, text="Radiobuttons", padding=(20, 10))
        self.radio_frame.grid(row=2, column=0, padx=(20, 10), pady=10, sticky="nsew")

        # Radiobuttons
        self.radio_1 = ttk.Radiobutton(
            self.radio_frame, text="Unselected", variable=self.var_3, value=1
        )
        self.radio_1.grid(row=0, column=0, padx=5, pady=10, sticky="nsew")
        self.radio_2 = ttk.Radiobutton(
            self.radio_frame, text="Selected", variable=self.var_3, value=2
        )
        self.radio_2.grid(row=1, column=0, padx=5, pady=10, sticky="nsew")
        self.radio_4 = ttk.Radiobutton(
            self.radio_frame, text="Disabled", state="disabled"
        )
        self.radio_4.grid(row=3, column=0, padx=5, pady=10, sticky="nsew")

        # Create a Frame for input widgets
        self.widgets_frame = ttk.Frame(self, padding=(0, 0, 0, 10))
        self.widgets_frame.grid(
            row=0, column=1, padx=10, pady=(30, 10), sticky="nsew", rowspan=3
        )
        self.widgets_frame.columnconfigure(index=0, weight=1)

        # Entry
        self.entry = ttk.Entry(self.widgets_frame)
        self.entry.insert(0, "Entry")
        self.entry.grid(row=0, column=0, padx=5, pady=(0, 10), sticky="ew")

        # Spinbox
        self.spinbox = ttk.Spinbox(self.widgets_frame, from_=0, to=100, increment=0.1)
        self.spinbox.insert(0, "Spinbox")
        self.spinbox.grid(row=1, column=0, padx=5, pady=10, sticky="ew")

        # Combobox
        self.combobox = ttk.Combobox(self.widgets_frame, values=self.combo_list)
        self.combobox.current(0)
        self.combobox.grid(row=2, column=0, padx=5, pady=10, sticky="ew")

        # Read-only combobox
        self.readonly_combo = ttk.Combobox(
            self.widgets_frame, state="readonly", values=self.readonly_combo_list
        )
        self.readonly_combo.current(0)
        self.readonly_combo.grid(row=3, column=0, padx=5, pady=10, sticky="ew")

        # Menu for the Menubutton
        self.menu = tk.Menu(self)
        self.menu.add_command(label="Menu item 1")
        self.menu.add_command(label="Menu item 2")
        self.menu.add_separator()
        self.menu.add_command(label="Menu item 3")
        self.menu.add_command(label="Menu item 4")

        # Menubutton
        self.menubutton = ttk.Menubutton(
            self.widgets_frame, text="Menubutton", menu=self.menu, direction="below"
        )
        self.menubutton.grid(row=4, column=0, padx=5, pady=10, sticky="nsew")

        # OptionMenu
        self.optionmenu = ttk.OptionMenu(
            self.widgets_frame, self.var_4, *self.option_menu_list
        )
        self.optionmenu.grid(row=5, column=0, padx=5, pady=10, sticky="nsew")

        # Button
        self.button = ttk.Button(self.widgets_frame, text="Button")
        self.button.grid(row=6, column=0, padx=5, pady=10, sticky="nsew")

        # Accentbutton
        self.accentbutton = ttk.Button(
            self.widgets_frame, text="Accent button", style="Accent.TButton"
        )
        self.accentbutton.grid(row=7, column=0, padx=5, pady=10, sticky="nsew")

        # Togglebutton
        self.togglebutton = ttk.Checkbutton(
            self.widgets_frame, text="Toggle button", style="Toggle.TButton"
        )
        self.togglebutton.grid(row=8, column=0, padx=5, pady=10, sticky="nsew")

        # Switch
        self.switch = ttk.Checkbutton(
            self.widgets_frame, text="Switch", style="Switch.TCheckbutton"
        )
        self.switch.grid(row=9, column=0, padx=5, pady=10, sticky="nsew")

        # Panedwindow
        self.paned = ttk.PanedWindow(self)
        self.paned.grid(row=0, column=2, pady=(25, 5), sticky="nsew", rowspan=3)

        # Pane #1
        self.pane_1 = ttk.Frame(self.paned, padding=5)
        self.paned.add(self.pane_1, weight=1)

        # Scrollbar
        self.scrollbar = ttk.Scrollbar(self.pane_1)
        self.scrollbar.pack(side="right", fill="y")

        # Treeview
        self.treeview = ttk.Treeview(
            self.pane_1,
            selectmode="browse",
            yscrollcommand=self.scrollbar.set,
            columns=(1, 2),
            height=10,
        )
        self.treeview.pack(expand=True, fill="both")
        self.scrollbar.config(command=self.treeview.yview)

        # Treeview columns
        self.treeview.column("#0", anchor="w", width=120)
        self.treeview.column(1, anchor="w", width=120)
        self.treeview.column(2, anchor="w", width=120)

        # Treeview headings
        self.treeview.heading("#0", text="Column 1", anchor="center")
        self.treeview.heading(1, text="Column 2", anchor="center")
        self.treeview.heading(2, text="Column 3", anchor="center")

        # Define treeview data
        treeview_data = [
            ("", 1, "Parent", ("Item 1", "Value 1")),
            (1, 2, "Child", ("Subitem 1.1", "Value 1.1")),
            (1, 3, "Child", ("Subitem 1.2", "Value 1.2")),
            (1, 4, "Child", ("Subitem 1.3", "Value 1.3")),
            (1, 5, "Child", ("Subitem 1.4", "Value 1.4")),
            ("", 6, "Parent", ("Item 2", "Value 2")),
            (6, 7, "Child", ("Subitem 2.1", "Value 2.1")),
            (6, 8, "Sub-parent", ("Subitem 2.2", "Value 2.2")),
            (8, 9, "Child", ("Subitem 2.2.1", "Value 2.2.1")),
            (8, 10, "Child", ("Subitem 2.2.2", "Value 2.2.2")),
            (8, 11, "Child", ("Subitem 2.2.3", "Value 2.2.3")),
            (6, 12, "Child", ("Subitem 2.3", "Value 2.3")),
            (6, 13, "Child", ("Subitem 2.4", "Value 2.4")),
            ("", 14, "Parent", ("Item 3", "Value 3")),
            (14, 15, "Child", ("Subitem 3.1", "Value 3.1")),
            (14, 16, "Child", ("Subitem 3.2", "Value 3.2")),
            (14, 17, "Child", ("Subitem 3.3", "Value 3.3")),
            (14, 18, "Child", ("Subitem 3.4", "Value 3.4")),
            ("", 19, "Parent", ("Item 4", "Value 4")),
            (19, 20, "Child", ("Subitem 4.1", "Value 4.1")),
            (19, 21, "Sub-parent", ("Subitem 4.2", "Value 4.2")),
            (21, 22, "Child", ("Subitem 4.2.1", "Value 4.2.1")),
            (21, 23, "Child", ("Subitem 4.2.2", "Value 4.2.2")),
            (21, 24, "Child", ("Subitem 4.2.3", "Value 4.2.3")),
            (19, 25, "Child", ("Subitem 4.3", "Value 4.3")),
        ]

        # Insert treeview data
        for item in treeview_data:
            self.treeview.insert(
                parent=item[0], index="end", iid=item[1], text=item[2], values=item[3]
            )
            if item[0] == "" or item[1] in {8, 21}:
                self.treeview.item(item[1], open=True)  # Open parents

        # Select and scroll
        self.treeview.selection_set(10)
        self.treeview.see(7)

        # Notebook, pane #2
        self.pane_2 = ttk.Frame(self.paned, padding=5)
        self.paned.add(self.pane_2, weight=3)

        # Notebook, pane #2
        self.notebook = ttk.Notebook(self.pane_2)
        self.notebook.pack(fill="both", expand=True)

        # Tab #1
        self.tab_1 = ttk.Frame(self.notebook)
        for index in [0, 1]:
            self.tab_1.columnconfigure(index=index, weight=1)
            self.tab_1.rowconfigure(index=index, weight=1)
        self.notebook.add(self.tab_1, text="Tab 1")

        # Scale
        self.scale = ttk.Scale(
            self.tab_1,
            from_=100,
            to=0,
            variable=self.var_5,
            command=lambda event: self.var_5.set(self.scale.get()),
        )
        self.scale.grid(row=0, column=0, padx=(20, 10), pady=(20, 0), sticky="ew")

        # Progressbar
        self.progress = ttk.Progressbar(
            self.tab_1, value=0, variable=self.var_5, mode="determinate"
        )
        self.progress.grid(row=0, column=1, padx=(10, 20), pady=(20, 0), sticky="ew")

        # Label
        self.label = ttk.Label(
            self.tab_1,
            text="Azure theme for ttk",
            justify="center",
            font=("-size", 15, "-weight", "bold"),
        )
        self.label.grid(row=1, column=0, pady=10, columnspan=2)

        # Tab #2
        self.tab_2 = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_2, text="Tab 2")

        # Tab #3
        self.tab_3 = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_3, text="Tab 3")

        # Sizegrip
        self.sizegrip = ttk.Sizegrip(self)
        self.sizegrip.grid(row=100, column=100, padx=(0, 5), pady=(0, 5))


if __name__ == "__main__":
    root = tk.Tk()
    root.title("")

    # Simply set the theme
    root.tk.call("source", "azure.tcl")
    root.tk.call("set_theme", "dark")

    app = App(root)
    app.pack(fill="both", expand=True)

    # Set a minsize for the window, and place it in the middle
    root.update()
    root.minsize(root.winfo_width(), root.winfo_height())
    x_cordinate = int((root.winfo_screenwidth() / 2) - (root.winfo_width() / 2))
    y_cordinate = int((root.winfo_screenheight() / 2) - (root.winfo_height() / 2))
    root.geometry("+{}+{}".format(x_cordinate, y_cordinate-20))

    root.mainloop()

```


https://raspberry-pi.fr/activer-connexion-distance-mysql/

# CIEL2

# ⬇️ <cite><font color="(0,68,88)">Mini-Projets CIEL-2</font></cite>

<a href="https://carnus.fr"><img src="https://img.shields.io/badge/Carnus%20Enseignement Supérieur-F2A900?style=for-the-badge" /></a>
<a href="https://carnus.fr"><img src="https://img.shields.io/badge/BTS%20CIEL-2962FF?style=for-the-badge" /></a>

    Professeur - K. B.

### Contact : [Mail](mailto:lycee@carnus.fr)
---

<a id="LOG"></a>
## <cite><font color="blue"> Logiciels et supports : </font></cite>

[![C++ Arduino](https://img.shields.io/badge/C++-Arduino-teal)](https://docs.arduino.cc/)
[![Développement Web](https://img.shields.io/badge/HTML-CSS-yellow)](https://www.w3.org/)
[![PHP SQL](https://img.shields.io/badge/PHP-MySQL-8A2BE2)](https://www.php.net/)
[![Python Versions](https://img.shields.io/badge/Python-3-blue)](https://www.python.org/)
[![RPi](https://img.shields.io/badge/Paspberry%20Pi-red)](https://www.raspberrypi.com/)
[![ESP32](https://img.shields.io/badge/ESP32-green)](https://www.espressif.com/en/products/socs/esp32)

---

### Table des matières :

* <a href="#LOG">Logiciels et supports</a>
* <a href="#PP">Présentation </a>
* <a href="#CC">Cahier des charges et expression du besoin</a>
* <a href="#RT">Répartition des tâches </a>
    * <a href="#MP1">Mini-Projet 1</a>
    * <a href="#MP2">Mini-Projet 2 </a>
* <a href="#PR">Prérequis</a>
* <a href="#OB">Objectifs </a>
* <a href="#PDL">Processus de développement logiciel </a>
    * <a href="#PDLE">Exemples d’étapes</a>

---

<a id="PP"></a>
## <cite><font color="#F2A900"> Présentation : </font></cite>

✍🏼 Le projet consiste à réaliser un système de contrôle d'accès et de surveillance dynamique contrôlable par l’outil informatique. Ce système est composé de plusieurs points de contrôle répartis dans des endroits clé de la salle 215. Des informations peuvent être affichées ainsi que des vidéos et des images pour prévenir d’événements spéciaux.

<a id="CC"></a>
## <cite><font color="#F2A900"> Cahier des charges et expression du besoin : </font></cite>

Le lycée désire se doter d'un système de contrôle d'accès dynamique, installé dans la salle 215.

Le projet se voudra évolutif, il sera possible dans l'avenir d'ajouter des points de contrôle (en fonction des besoins, du budget et de la structure réseau mise en place).

Les points de contrôle seront utilisés afin de renseigner les étudiants et les enseignants sur l'état d'occupation de la salle 215, ainsi que des valeurs fournies par des capteurs connectés à une carte Raspberry Pi (Badge RFID, détecteur de mouvement, caméra de surveillance).

Les capteureurs de présence (caméra, détecteur de mouvement) permettront l’extinction automatique des lumières personne n'est présente dans la salle (temporisé 2mn).

<a id="RT"></a>
## <cite><font color="#F2A900"> Répartition des tâches : </font></cite>

<a id="MP1"></a>
### <cite><font color="#F2A900"> Mini-Projet 1 : </font></cite>

| Tâche-1 (E.F. ~~et M.D.~~) | Fonctions à développer et tâches à effectuer |
| -------------- |:----------------------------------------|
| Vidéo surveillance | Installation de la caméra (logiciel)|
|  | Développement en Python du programme de surveillance  |
|  |Sauvegarde des données dans la base de données         |
|  |Documentation logicielle                               |
|  |Rédaction d'un rapport                                 |


|Tâche-2 (R.R. et Y.F.)| Fonctions à développer et tâches à effectuer|
| -------------- |:----------------------------------------|
| Détection de mouvement | Installation du module          |
|  |Développement en C++ (Arduino) du programme de détection|
|  |Sauvegarde des données dans la base de données         |
|  |Documentation logicielle                               |
|  |Rédaction d'un rapport                                 |

|Tâche-3 (V.M.)| Fonctions à développer et tâches à effectuer|
| -------------- |:----------------------------------------|
| Réseaux | Installation du serveur Linux virtualisé       |
|  | Services Web sur serveur                              |
|  | Services SGBD                                         |
|  | Configuration des serveurs Linux, Web, MySQL          |
|  |Documentation logicielle                               |
|  |Rédaction d'un rapport                                 |


<a id="MP2"></a>
### <cite><font color="#F2A900"> Mini-Projet 2 : </font></cite>

| Tâche-1 (A.G. et C.M.) | Fonctions à développer et tâches à effectuer |
| -------------- |:----------------------------------------|
| Contrôle d'accès | Installation du module                |
|  | Développement en C++ (Arduino) du programme de contrôle d'accès  |
|  |Sauvegarde des données dans la base de données         |
|  |Documentation logicielle                               |
|  |Rédaction d'un rapport                                 |


|Tâche-2 (R.C. et H.P.)| Fonctions à développer et tâches à effectuer|
| -------------- |:----------------------------------------|
| QR code et authentification | Développement en PHP du logiciel d'identification |
|  |Développement du logiciel de réservation               |
|  |Sauvegarde des données dans la base de données         |
|  |Documentation logicielle                               |
|  |Rédaction d'un rapport                                 |

|Tâche-3 (M.A.-B.)| Fonctions à développer et tâches à effectuer|
| -------------- |:----------------------------------------|
| Réseaux | Installation du serveur Linux virtualisé       |
|  | Services Web sur serveur                              |
|  | Services SGBD                                         |
|  | Configuration des serveurs Linux, Web, MySQL          |
|  |Documentation logicielle                               |
|  |Rédaction d'un rapport                                 |



<a id="PR"></a>
## <cite><font color="blue"> Prérequis : </font></cite>

* Des connaissances en programmation 
* Des connaissances en développement Web
* Des conaissances en réseaux


<a id="OB"></a>
## <cite><font color="blue"> Objectifs : </font></cite>

* Travailler en équipe et gérer un projet
* Produire de la documentation technique
* Approfondir les connaissances en programmation et en réseaux


---

<a id="PDL"></a>
## Processus de développement logiciel
* Un processus de développement décrit une méthode qui permet de construire, déployer et éventuellement maintenir ou faire évoluer un logiciel. ✌🏼

<a id="PDLE"></a>
### Exemples d’étapes :
- Exigences, Analyse, Conception, Mise en œuvre (implémentation), Test
- Besoin/Faisabilité, Élaboration, Fabrication, Transition/Test


---
---

```cpp
#include <stdio.h>
#include <stdlib.h>
 
int main()
{
 
    char trame[500];
    char T[500];
 
int i,s;
 
 
s=0;
    do
    {
 
 
    printf("Entrer la trame:     ");
     gets(trame);
 
     if (strlen(trame)< 144)
        {
        printf("\nVeuillez saisir une trame valide!\n\n");
        }
else
{
 
 
        for (i=0; i<strlen(trame); i++)
 
{
    T[i]=trame[i];
}
 
for (i=44; i<=strlen(trame)-9; i++)
{
    s=s+1;
}
 
 
if (s<92)
{
     printf(" Le data ip de cette trame n'est pas valide    ");
}
 
}
    }
 
 
while (strlen(trame)<144);
 
 
 
 
 
for (i=0; i<strlen(trame); i++)
 
{
    T[i]=trame[i];
}
printf("\n------------------------------------------------------------------------------------------- ");
printf("\nLe Preambule de cette trame est:  ");
 
for (i=0; i<=13; i++)
{
    printf("%c",T[i]);
}
printf("\n------------------------------------------------------------------------------------------- ");
 
printf("\nLe SFD de cette trame est:    ");
 
for (i=14; i<=15; i++)
{
    printf("%c",T[i]);
}
printf("\n------------------------------------------------------------------------------------------- ");
 
printf("\nL'Adresse MAC Destination de cette trame est: ");
 
 
for (i=16; i<=27; i++)
{
    printf("%c",T[i]);
}
printf("\n------------------------------------------------------------------------------------------- ");
 
printf("\nL'Adresse MAC Source de cette trame est:  ");
 
 
for (i=28; i<=39; i++)
{
    printf("%c",T[i]);
}
printf("\n------------------------------------------------------------------------------------------- ");
 
printf("\nLe Ether Type de cette trame est:   ");
 
for (i=40; i<=43; i++)
{
    printf("%c",T[i]);
}
 
printf("\n------------------------------------------------------------------------------------------- ");
 
 
printf("\nLe data ip de cette trame est:  ");
for (i=44; i<=strlen(trame)-9; i++)
{
    printf("%c",T[i]);
}
printf("\n------------------------------------------------------------------------------------------- ");
 
printf("\nLe FCS de cette trame est:  ");
 
for (i=strlen(trame)-8; i<=strlen(trame)-1; i++)
{
    printf("%c",T[i]);
}
printf("\n------------------------------------------------------------------------------------------- ");
 
 
 
 
 
 
s=0;
i=strlen(trame)-9;
int b=0;
int bourr=0;
 
for (i=44; i<=strlen(trame)-9; i++)
{
    s=s+1;
}
 
 
if (s==92)
    printf("\n\nLa taille de la DATA IP de cette trame est 46 Octets");
{
while ( (i>=44) && (bourr==0) )
{
 
    if ( (T[i]=='0') && (T[i-1]=='0')  )
    {
 
             b=b+1;
    }
 
    else
    {
        bourr=1;
    }
 
 
           i=i-2;
 
}
 
 
if (b!=0)
{
printf(" et elle contient %d Octet(s) de bourrage\n\n",b);
}
 else if ((s==92) && (b==0))
 {
printf(" mais elle ne contient pas des Octets de bourrage\n\n");
 
 }
}
 
 
/*
Ex de trame valide
000573a00000e06995d85a1386dd60000000009b06402607530000602abc00000000badec0de200141d000024233000000000000000496740050bcea7db800c1d703801800e1cfa000000101080a093e69b917a17ed3474554202f20485454502f312e310d0a417574686f72697a6174696f6e3a20426173696320593239755a6d6b365a47567564476c6862413d3d0d0a557365722d4167656e743a20496e73616e6542726f777365720d0a486f73743a207777772e6d79697076362e6f72670d0a4163636570743a202a2f2a0d0a0d0a
Ex de trame avec bourrage
000573a00000e06995d85a1386dd60000000009b064023616e6542726f777365720d0a486f73743a207777772e6d79697076362e6f72670d0a4163636570743a000000000d0a0d0a
Ex de trame sans bourrage
000573a00000e06995d85a1386dd60000000009b064023616e6542726f777365720d0a486f73743a207777772e6d79697076362e6f72670d0a4163636570743abdhehdgs0d0a0d0a
*/
 
 
 
 
 
    return 0;
}
```
