from mixins.horodatable import Horodatable
from mixins.validable import Validable
from mixins.serializable import Serializable
from mixins.historisable import Historisable
from mixins.exportable import Exportable

class Document(Horodatable, Validable, Serializable, Historisable, Exportable):
    def __init__(self, titre, contenu):
        super().__init__()
        self.titre = titre
        self.contenu = contenu

    def sauvegarder(self):
        self.horodatage()
        self.valider()
        self.ajouter_action("Sauvegarde")
        print(f"Document '{self.titre}' sauvegardé.")

    def exporter(self):
        print("Export PDF effectué")
