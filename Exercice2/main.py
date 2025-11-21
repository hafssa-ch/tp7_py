
from models.contrat import Contrat
from models.commande import Commande
from mixins.csv_exportable import CSVExportable

c1 = Contrat(1, "Initial")
c1.modifier("Révisé")
c2 = Contrat(2, "Confidentiel")
c2.modifier("Mis à jour")

Commandes = [c1, c2]
CSVExportable.exporter_csv(Commandes, "contrats.csv")
print(c1.to_json())
