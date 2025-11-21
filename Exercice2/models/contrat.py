
from mixins.serializable import Serializable
from mixins.historisable import Historisable
from mixins.journalisable import Journalisable
from mixins.horodatable import Horodatable

class Contrat(Serializable, Historisable, Journalisable, Horodatable):
    def __init__(self, id, description):
        Historisable.__init__(self)
        Horodatable.__init__(self)
        self.id = id
        self.description = description

    def modifier(self, nouvelle_desc):
        self.journaliser(f"Modification du contrat {self.id}")
        self.enregistrer_etat()
        self.description = nouvelle_desc
        self.mettre_a_jour_timestamp()
