import socket
import json

HOST = "127.0.0.1"
PORT = 65432

def envoyer(req):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(json.dumps(req).encode())
        return s.recv(1024).decode()

while True:
    print("\n1. Ajouter")
    print("2. Liste")

    choix = input("Choix : ")

    if choix == "1":
        titre = input("Titre : ")
        auteur = input("Auteur : ")
        contenu = input("Contenu : ")

        req = {
            "action": "ajouter",
            "data": {
                "titre": titre,
                "auteur": auteur,
                "contenu": contenu
            }
        }

        print(envoyer(req))

    elif choix == "2":
        req = {"action": "liste"}
        print(envoyer(req))