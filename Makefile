# *//Etape 1 Etape 1 Etape 1 Etape 1
# mot1:
# 	echo Carnus

# mot2:
# 	@echo BTS CIEL


# //TODO Ecrire les lignes précédentes
# //TODO dans le terminal taper 
# *? make + Touche Entrée
# *? make mot2 + Touche Entrée
# *? make mot1 + Touche Entrée
# //TODO et vérifier le résultat de chaque commande

# *//Etape 2 Etape 2 Etape 2 Etape 2
# *! Effacer toutes les lignes écrites (ou les commenter #)

# //TODO Ecrire les lignes suivantes

# all:
# 	g++ prog1.cpp -o prog1

# //TODO dans le terminal taper make pour compiler
# //TODO le programme prog1.cpp 
# *? make + Touche Entrée
# *? Exécuter le programme : ./prog1

# *//Etape 3 Etape 3 Etape 3 Etape 3
# *! Effacer toutes les lignes écrites (ou les commenter #)

# //TODO Ecrire les lignes suivantes

# CC = g++

# executable:
# 	$(CC) prog1.cpp -o executable

# //TODO dans le terminal taper make pour compiler
# //TODO le programme prog1.cpp 
# *? make + Touche Entrée
# *? Exécuter le programme : ./executable

# *//Etape 4 Etape 4 Etape 4 Etape 4
# *! Effacer toutes les lignes écrites (ou les commenter #)

# //TODO Ecrire les lignes suivantes

# CC = g++

# final: prog1.o
# 	$(CC) prog1.o -o final

# prog1.o: prog1.cpp
# 	$(CC) -c prog1.cpp

# clean:
# 	rm *.o final

# //TODO dans le terminal taper make pour compiler
# //TODO le programme prog1.cpp 
# *? make + Touche Entrée
# *? Exécuter le programme : ./final
# *? make clean + Touche Entrée : pour effacer les fichiers binaires générés

# *//Etape 5 Etape 5 Etape 5 Etape 5
# *! Effacer toutes les lignes écrites (ou les commenter #)

# //TODO Ecrire les lignes suivantes

# CC = g++

# all:final

# final: prog1.o
# 	@echo "Génération des liens et production de l'exécutable"
# 	$(CC) prog1.o -o final

# prog1.o: prog1.cpp
# 	@echo "Compilation du fichier prog1.cpp"
# 	$(CC) -c prog1.cpp

# clean:
# 	@echo "Supprimer tout sauf les fichiers sources"
# 	rm *.o final

# //TODO dans le terminal taper make pour compiler
# //TODO le programme prog1.cpp 
# *? make + Touche Entrée
# *? Exécuter le programme : ./final
# *? make clean + Touche Entrée : pour effacer les fichiers binaires générés
