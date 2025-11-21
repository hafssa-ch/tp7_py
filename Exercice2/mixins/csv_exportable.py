
import csv

class CSVExportable:
    @staticmethod
    def exporter_csv(objets, nom_fichier):
        if not objets:
            return
        champs = objets[0].__dict__.keys()
        with open(nom_fichier, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=champs)
            writer.writeheader()
            for o in objets:
                writer.writerow(o.__dict__)
