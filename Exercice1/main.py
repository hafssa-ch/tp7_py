
from models.document import Document

doc = Document("Rapport", "Contenu important")
doc.sauvegarder()
print(doc.to_json())
doc.afficher_historique()
doc.exporter()
