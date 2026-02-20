class Moldu:
    def __init__(self, nom):
        self.nom = nom


class Sorcier(Moldu):
    def __init__(self, nom, maison):
        super().__init__(nom)
        self.maison = maison

    def lancer_un_sort(self):
        print(f"Lancer un sort par {self.nom}")
        

# Instances
harry = Sorcier("Harry", "Gryffondor")
jean = Moldu("Jean")

# Tests
harry.lancer_un_sort()   # OK
# jean.lancer_un_sort()  # ❌ Erreur normale (un moldu ne lance pas de sort)
