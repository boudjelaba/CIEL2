import os
import customtkinter
import tkinter.ttk as ttk
import tkinter as tk
from PIL import Image


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        
        # Titre et taille de l'interface
        self.title("BTS CIEL - IR")
        self.geometry("1000x562")

        # grid layout 1x2
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # Images avec mode light et dark
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "")

        ## --- Menu : Boutons de navigation
        ### --- A répéter pour tous les boutons (ici icone réglage)
        self.btn_icone = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "c_settings.png")),
                                                dark_image=Image.open(os.path.join(image_path, "c_settings.png")),
                                                size=(30, 30))

        # Colonne (frame) de navigation
        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(3, weight=1)

        ## --- Accueil
        self.accueil_btn = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, 
                                                   height=40, 
                                                   border_spacing=10, 
                                                   text="Accueil",
                                                   fg_color="transparent", 
                                                   text_color=("gray10", "gray90"), 
                                                   hover_color=("gray70", "gray30"),
                                                   image=self.btn_icone, 
                                                   anchor="w", 
                                                   command=self.accueil_btn_event)
        self.accueil_btn.grid(row=0, column=0, sticky="ew")

        ## --- Page 1
        self.page1_btn = customtkinter.CTkButton(self.navigation_frame, 
                                                 corner_radius=0, 
                                                 height=40, 
                                                 border_spacing=10, 
                                                 text="Page 1",
                                                 fg_color="transparent", 
                                                 text_color=("gray10", "gray90"), 
                                                 hover_color=("gray70", "gray30"),
                                                 image=self.btn_icone, 
                                                 anchor="w", 
                                                 command=self.page1_btn_event)
        self.page1_btn.grid(row=1, column=0, sticky="ew")

        ## --- Page 2
        self.page2_btn = customtkinter.CTkButton(self.navigation_frame, 
                                                      corner_radius=0, 
                                                      height=40, 
                                                      border_spacing=10, 
                                                      text="Page 2",
                                                      fg_color="transparent", 
                                                      text_color=("gray10", "gray90"), 
                                                      hover_color=("gray70", "gray30"),
                                                      image=self.btn_icone, 
                                                      anchor="w", 
                                                      command=self.page2_btn_event)
        self.page2_btn.grid(row=2, column=0, sticky="ew")

        # Autre Menu (Light et Dark par exemple)
        self.t_mode_menu = customtkinter.CTkOptionMenu(self.navigation_frame, 
                                                       values=["Light", "Dark", "System"],
                                                       command=self.mode
                                                       )
        self.t_mode_menu.grid(row=3, column=0, padx=20, pady=20, sticky="s")

        # Bouton Quitter 
        self.exit_btn = customtkinter.CTkButton(self.navigation_frame, 
                                                text="Quitter",
                                                fg_color="#DC143C",
                                                hover_color="#ec3642", 
                                                font=("Montserrat", 16), 
                                                corner_radius=10, width=100,
                                                command=self.destroy) 
        self.exit_btn.grid(row=4, column=0, padx=20, pady=20, sticky="ew") 


        # création colonne (frame) Accueil
        self.home_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.home_frame.grid_columnconfigure(0, weight=1)
        self.home_frame.grid_rowconfigure(2, weight=1)

        ## --- Zone de saisie
        self.entree_texte = customtkinter.CTkEntry(self.home_frame, width=320, placeholder_text="Veuillez saisir du texte")
        self.entree_texte.grid(row=1, column=0, padx=100, pady=50, sticky="w")


        # créate de la seconde frame
        self.second_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.second_frame.grid_columnconfigure(0, weight=1)

        ## --- Bouton
        self.bouton_p1 = customtkinter.CTkButton(self.second_frame, text="Valider", 
                                                 image=self.btn_icone, compound="left",
                                                 fg_color="#006400",
                                                 hover_color="#AAA662",
                                                 font=("Montserrat", 16),
                                                 corner_radius=10, width=160,
                                                 command=self.valider)
        self.bouton_p1.grid(row=2, column=0, padx=155, pady=100, sticky="w")


        # création de la 3ème frame
        self.third_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.third_frame.grid_columnconfigure(0, weight=1)

        ## --- Bouton
        self.open_btn = customtkinter.CTkButton(self.third_frame, text="Ouvrir", command=self.ouvrir)
        self.open_btn.grid(row=1, column=0, padx=120, pady=40)

        ## --- Label
        self.p2_label = customtkinter.CTkLabel(self.third_frame, text="Titre de la section", 
                                               font=("Montserrat", 26, "bold"), 
                                               text_color = "red",
                                               padx=20, pady=10)
        self.p2_label.grid(row=2, column=0, padx=20, pady=10)


        # sélection de la frame "accueil" comme frame par défaut
        self.selection_frame("Accueil")

    # Définition des différentes fonctions
    # ------------------------------------
    ## - Fonction pour naviguer entre les pages
    def selection_frame(self, name):
        self.accueil_btn.configure(fg_color=("gray75", "gray25") if name == "Accueil" else "transparent")
        self.page1_btn.configure(fg_color=("gray75", "gray25") if name == "Page_1" else "transparent")
        self.page2_btn.configure(fg_color=("gray75", "gray25") if name == "Page_2" else "transparent")

        # Afficher la frame sélectionnée
        if name == "Accueil":
            self.home_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.home_frame.grid_forget()
        if name == "Page_1":
            self.second_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.second_frame.grid_forget()
        if name == "Page_2":
            self.third_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.third_frame.grid_forget()

    def accueil_btn_event(self):
        self.selection_frame("Accueil")

    def page1_btn_event(self):
        self.selection_frame("Page_1")

    def page2_btn_event(self):
        self.selection_frame("Page_2")

    ### --- Important (remplacer "pass" par le code adéquat) --- ###
    ## - Définition des fonctions à coder
    def valider(self):
        pass

    def mode(self):
        pass

    def ouvrir(self):
        pass



if __name__ == "__main__":
    app = App()
    app.mainloop()