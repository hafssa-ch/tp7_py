# TP7 – Mixins en Python
### Objectif général
Apprendre à utiliser les mixins pour enrichir des classes métiers avec des comportements transversaux (validation, horodatage, journalisation, historique, sérialisation),
sans recourir à l’héritage hiérarchique traditionnel. Favoriser la modularité, la réutilisabilité et la séparation des responsabilités.

## Exercice 1 – Document avec Horodatage et Validation
### Objectifs pédagogiques
Découvrir les mixins pour ajouter des fonctionnalités comme l’horodatage et la validation.
Comprendre la composition de comportements sans héritage complexe.

### Concepts clés
Horodatable : journalise la date d’une action.
Validable : vérifie qu’un titre est renseigné.
Document : classe métier utilisant ces mixins.

### Extensions possibles
Ajouter un mixin Serializable pour exporter en JSON.
Ajouter un mixin Historisable pour conserver l’historique des actions.
Utiliser des classes abstraites (abc.ABC) pour définir des méthodes obligatoires.
<img width="1075" height="436" alt="image" src="https://github.com/user-attachments/assets/26813a96-4fe0-4743-978c-0d10f79f10f6" />


## Exercice 2 – Contrat avec Historique et Journalisation
### Objectifs pédagogiques
Approfondir l’usage des mixins pour gérer la traçabilité et la sérialisation.
Séparer les responsabilités : journalisation, historique, sérialisation.

### Concepts clés
Serializable : conversion objet ↔ JSON.
Historisable : enregistre les états précédents de l’objet.
Journalisable : affiche dans la console toute modification.
Contrat : classe métier combinant ces comportements.

### Extensions possibles
Ajouter un mixin Horodatable pour timestamp des opérations.
Ajouter export CSV ou XML via mixins.
Appliquer ce modèle à d’autres classes métiers (Commande, Client).
<img width="1635" height="184" alt="image" src="https://github.com/user-attachments/assets/472fd06d-25c7-4ac8-bcab-0444d982cc12" />


## Exercice 3 – Gestion de tâches professionnelles
### Objectifs pédagogiques
Modéliser un système de tâches avec validation, historique et journalisation.
Illustrer la composition via mixins pour structurer des comportements transversaux.

### Concepts clés
ValidationMixin : vérifie que le titre est renseigné et non vide.
HistoriqueMixin : enregistre chaque version précédente de la description.
JournalisationMixin : affiche dans la console les actions (création, modification).
Tâche : classe principale utilisant ces trois mixins.

### Fonctionnalités
mettre_a_jour(description) : met à jour la description, journalise et conserve l’historique.
afficher_historique() : affiche les anciennes versions de la description.

### Contraintes techniques
Pas d’héritage hiérarchique classique.
Utiliser datetime.now() pour les timestamps.
Utiliser copy si nécessaire pour cloner l’état des objets.
<img width="1645" height="210" alt="image" src="https://github.com/user-attachments/assets/76725826-69f9-4641-8e6d-55cd9e34f556" />
