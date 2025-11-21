
class Historisable:
    def __init__(self, *args, **kwargs):
        self._historique = []
        super().__init__(*args, **kwargs)

    def ajouter_action(self, action):
        self._historique.append(action)

    def afficher_historique(self):
        for a in self._historique:
            print(a)
