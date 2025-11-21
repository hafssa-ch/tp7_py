
class ValidationMixin:
    def valider_titre(self, titre):
        if not titre or not titre.strip():
            raise ValueError("Le titre doit être renseigné")
        return titre
