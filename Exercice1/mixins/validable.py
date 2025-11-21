
class Validable:
    def valider(self):
        if not getattr(self, "titre", None):
            raise ValueError("Titre manquant")
        print("Validation OK")
