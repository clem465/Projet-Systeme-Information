import socket
import json

HOST = "127.0.0.1"
PORT = 65432

jeux = []

def traiter_requete(data):
    global jeux
    req = json.loads(data)

    if req["action"] == "ajouter":
        jeux.append(req["data"])
        return "OK"

    elif req["action"] == "liste":
        return json.dumps(jeux)

    return "UNKNOWN"

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()

    print("Serveur lancé...")

    while True:
        conn, addr = s.accept()
        with conn:
            print("Connecté à", addr)
            data = conn.recv(1024).decode()

            if data:
                reponse = traiter_requete(data)
                conn.sendall(reponse.encode())