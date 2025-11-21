
from datetime import datetime

class Historisable:
    def __init__(self):
        self.historique = []

    def enregistrer_etat(self):
        self.historique.append(self.__dict__.copy())
