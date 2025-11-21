
from copy import deepcopy
from datetime import datetime

class HistoriqueMixin:
    def __init__(self):
        self.historique = []

    def enregistrer_historique(self, description):
        self.historique.append((datetime.now(), deepcopy(description)))

    def afficher_historique(self):
        for dt, desc in self.historique:
            print(f"{dt}: {desc}")
