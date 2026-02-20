class Vaisseau:
    def __init__(self, nom, couleur, vitesse_nominale, duree_acceleration):
        self.nom = nom
        self.couleur = couleur
        self.vitesse_nominale = vitesse_nominale
        self.duree_acceleration = duree_acceleration
        self.position = 0
        self.vitesse_actuelle = 0
        self.temps = 0

    def tick(self):
        self.temps += 1

        if self.temps <= self.duree_acceleration:
            self.vitesse_actuelle = (self.vitesse_nominale / self.duree_acceleration) * self.temps
        else:
            self.vitesse_actuelle = self.vitesse_nominale

        self.position += self.vitesse_actuelle

    def __repr__(self):
        return f"{self.nom} -> position: {self.position:.2f}"


class Circuit:
    def __init__(self, distance_tour, nombre_tours):
        self.distance_totale = distance_tour * nombre_tours


# Simulation
v1 = Vaisseau("Falcon", "Rouge", 10, 5)
v2 = Vaisseau("Comet", "Bleu", 8, 3)

for i in range(10):
    print(f"Tick {i+1}")
    v1.tick()
    v2.tick()
    print(v1)
    print(v2)
    print()
