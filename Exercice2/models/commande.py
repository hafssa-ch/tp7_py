
from mixins.serializable import Serializable
from mixins.historisable import Historisable
from mixins.journalisable import Journalisable
from mixins.horodatable import Horodatable

class Commande(Serializable, Historisable, Journalisable, Horodatable):
    def __init__(self, id, montant):
        Historisable.__init__(self)
        Horodatable.__init__(self)
        self.id = id
        self.montant = montant

    def modifier(self, nouveau_montant):
        self.journaliser(f"Modification de la commande {self.id}")
        self.enregistrer_etat()
        self.montant = nouveau_montant
        self.mettre_a_jour_timestamp()
