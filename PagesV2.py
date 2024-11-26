import os
import customtkinter
import tkinter.ttk as ttk
import tkinter as tk
from PIL import Image

# Définition des différentes fonctions
# ------------------------------------
## - Fonction pour naviguer entre les pages
def selection_frame(name):
    accueil_btn.configure(fg_color=("gray75", "gray25") if name == "Accueil" else "transparent")
    page1_btn.configure(fg_color=("gray75", "gray25") if name == "Page_1" else "transparent")
    page2_btn.configure(fg_color=("gray75", "gray25") if name == "Page_2" else "transparent")

    # Afficher la frame sélectionnée
    if name == "Accueil":
        home_frame.grid(row=0, column=1, sticky="nsew")
    else:
        home_frame.grid_forget()
    if name == "Page_1":
        second_frame.grid(row=0, column=1, sticky="nsew")
    else:
        second_frame.grid_forget()
    if name == "Page_2":
        third_frame.grid(row=0, column=1, sticky="nsew")
    else:
        third_frame.grid_forget()

def accueil_btn_event():
    selection_frame("Accueil")

def page1_btn_event():
    selection_frame("Page_1")

def page2_btn_event():
    selection_frame("Page_2")

### --- Important (remplacer "pass" par le code adéquat) --- ###
## - Définition des fonctions à coder
def valider():
    pass

def mode():
    pass

def ouvrir():
    pass

def fermer():
   App.destroy()

App = customtkinter.CTk()
    
# Titre et taille de l'interface
App.title("BTS CIEL - IR")
App.geometry("1000x562")

# grid layout 1x2
App.grid_rowconfigure(0, weight=1)
App.grid_columnconfigure(1, weight=1)

# Images avec mode light et dark
image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "")

## --- Menu : Boutons de navigation
### --- A répéter pour tous les boutons (ici icone réglage)
btn_icone = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "c_settings.png")),
                                        dark_image=Image.open(os.path.join(image_path, "c_settings.png")),
                                        size=(30, 30))

# Colonne (frame) de navigation
navigation_frame = customtkinter.CTkFrame(App,corner_radius=0)
navigation_frame.grid(row=0, column=0, sticky="nsew")
navigation_frame.grid_rowconfigure(3, weight=1)

## --- Accueil
accueil_btn = customtkinter.CTkButton(navigation_frame, corner_radius=0, 
                                      height=40, 
                                      border_spacing=10, 
                                      text="Accueil",
                                      fg_color="transparent", 
                                      text_color=("gray10", "gray90"), 
                                      hover_color=("gray70", "gray30"),
                                      image=btn_icone, 
                                      anchor="w", 
                                      command=accueil_btn_event)
accueil_btn.grid(row=0, column=0, sticky="ew")

## --- Page 1
page1_btn = customtkinter.CTkButton(navigation_frame, 
                                    corner_radius=0, 
                                    height=40, 
                                    border_spacing=10, 
                                    text="Page 1",
                                    fg_color="transparent", 
                                    text_color=("gray10", "gray90"), 
                                    hover_color=("gray70", "gray30"),
                                    image=btn_icone, 
                                    anchor="w", 
                                    command=page1_btn_event)
page1_btn.grid(row=1, column=0, sticky="ew")

## --- Page 2
page2_btn = customtkinter.CTkButton(navigation_frame, 
                                    corner_radius=0, 
                                    height=40, 
                                    border_spacing=10, 
                                    text="Page 2",
                                    fg_color="transparent", 
                                    text_color=("gray10", "gray90"), 
                                    hover_color=("gray70", "gray30"),
                                    image=btn_icone, 
                                    anchor="w", 
                                    command=page2_btn_event)
page2_btn.grid(row=2, column=0, sticky="ew")

# Autre Menu (Light et Dark par exemple)
t_mode_menu = customtkinter.CTkOptionMenu(navigation_frame, 
                                          values=["Light", "Dark", "System"],
                                          command=mode
                                          )
t_mode_menu.grid(row=3, column=0, padx=20, pady=20, sticky="s")

# Bouton Quitter 
exit_btn = customtkinter.CTkButton(navigation_frame,
                                   text="Quitter",
                                   fg_color="#DC143C",
                                   hover_color="#ec3642", 
                                   font=("Montserrat", 16), 
                                   corner_radius=10, width=100,
                                   command=fermer) 
exit_btn.grid(row=4, column=0, padx=20, pady=20, sticky="ew") 


# création colonne (frame) Accueil
home_frame = customtkinter.CTkFrame(App, corner_radius=0, fg_color="transparent")
home_frame.grid_columnconfigure(0, weight=1)
home_frame.grid_rowconfigure(2, weight=1)

## --- Zone de saisie
entree_texte = customtkinter.CTkEntry(home_frame, width=320, placeholder_text="Veuillez saisir du texte")
entree_texte.grid(row=1, column=0, padx=100, pady=50, sticky="w")


# créate de la seconde frame
second_frame = customtkinter.CTkFrame(App, corner_radius=0, fg_color="transparent")
second_frame.grid_columnconfigure(0, weight=1)

## --- Bouton
bouton_p1 = customtkinter.CTkButton(second_frame, text="Valider",
                                    image=btn_icone, compound="left",
                                    fg_color="#006400",
                                    hover_color="#AAA662",
                                    font=("Montserrat", 16),
                                    corner_radius=10, width=160,
                                    command=valider)
bouton_p1.grid(row=2, column=0, padx=155, pady=100, sticky="w")


# création de la 3ème frame
third_frame = customtkinter.CTkFrame(App, corner_radius=0, fg_color="transparent")
third_frame.grid_columnconfigure(0, weight=1)

## --- Bouton
open_btn = customtkinter.CTkButton(third_frame, text="Ouvrir", command=ouvrir)
open_btn.grid(row=1, column=0, padx=120, pady=40)

## --- Label
p2_label = customtkinter.CTkLabel(third_frame, text="Titre de la section",
                                  font=("Montserrat", 26, "bold"), 
                                  text_color = "red",
                                  padx=20, pady=10)
p2_label.grid(row=2, column=0, padx=20, pady=10)


# sélection de la frame "accueil" comme frame par défaut
selection_frame("Accueil")


App.mainloop()