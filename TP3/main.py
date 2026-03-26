import json
import os

FICHIER = "jeux.json"

# Charger les jeux
def charger_jeux():
    if os.path.exists(FICHIER):
        with open(FICHIER, "r") as f:
            return json.load(f)
    return []

# Sauvegarder
def sauvegarder_jeux(jeux):
    with open(FICHIER, "w") as f:
        json.dump(jeux, f, indent=4)

# Ajouter un jeu
def ajouter_jeu(jeux):
    titre = input("Titre : ")
    auteur = input("Auteur : ")
    contenu = input("Contenu : ")

    jeux.append({
        "titre": titre,
        "auteur": auteur,
        "contenu": contenu
    })

    print("Jeu ajouté")

# Afficher les jeux
def afficher_jeux(jeux):
    for i, jeu in enumerate(jeux):
        print(f"{i} - {jeu['titre']}")

# Détail
def detail_jeu(jeux):
    index = int(input("Index du jeu : "))
    if 0 <= index < len(jeux):
        print(jeux[index])
    else:
        print("Index invalide")

# Supprimer
def supprimer_jeu(jeux):
    index = int(input("Index à supprimer : "))
    if 0 <= index < len(jeux):
        jeux.pop(index)
        print("Supprimé")
    else:
        print("Index invalide")

# Menu
def menu():
    jeux = charger_jeux()

    while True:
        print("\n1. Ajouter")
        print("2. Liste")
        print("3. Detail")
        print("4. Supprimer")
        print("5. Quitter")

        choix = input("Choix : ")

        if choix == "1":
            ajouter_jeu(jeux)
        elif choix == "2":
            afficher_jeux(jeux)
        elif choix == "3":
            detail_jeu(jeux)
        elif choix == "4":
            supprimer_jeu(jeux)
        elif choix == "5":
            sauvegarder_jeux(jeux)
            break

menu()