from Origine import *
from Metier import *


class Joueur:

    def __init__(self, nom, origine, classe):
        self.nom = nom
        self.origine = origine
        self.classe = classe
        self.EV = self.CalculEV()

    def CalculEV(self):
        if self.classe.classe == "Guerrier":
            if self.origine.race == "Barbare" or self.origine.race == "Humain":
                return 35
            else:
                return self.origine.EV + 5


joueur1 = Joueur("Georges", Barbare, Guerrier)
print joueur1.EV
