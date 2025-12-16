cmake_minimum_required(VERSION 3.10)

# Nom du projet (CMake moderne)
project(TP_Rectangle_Carre LANGUAGES CXX)

# Version du standard C++
set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

# Création de l'exécutable
add_executable(prog1
    src/main.cpp
    src/Rectangle.cpp
    src/Carre.cpp
)

# Utiliser des propriétés ciblées plutôt que des commandes globales
target_include_directories(prog1 PRIVATE include)
target_compile_features(prog1 PUBLIC cxx_std_11)
target_compile_options(prog1 PRIVATE -Wall -Wextra)
