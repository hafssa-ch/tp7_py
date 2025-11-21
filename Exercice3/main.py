
from models.tache import Tache

t1 = Tache("Préparer réunion", "Rédiger l'ordre du jour")
t1.mettre_a_jour("Rédiger et valider l'ordre du jour")
t1.mettre_a_jour("Envoyer l'ordre du jour aux participants")
t1.afficher_historique()
