
from mixins.validation_mixin import ValidationMixin
from mixins.historique_mixin import HistoriqueMixin
from mixins.journalisation_mixin import JournalisationMixin
from datetime import datetime

class Tache(ValidationMixin, HistoriqueMixin, JournalisationMixin):
    def __init__(self, titre, description):
        HistoriqueMixin.__init__(self)
        self.titre = self.valider_titre(titre)
        self.description = description
        self.date_creation = datetime.now()
        self.journaliser(f"Tâche créée: {self.titre}")

    def mettre_a_jour(self, nouvelle_description):
        self.enregistrer_historique(self.description)
        self.description = nouvelle_description
        self.journaliser(f"Tâche mise à jour: {self.titre}")
