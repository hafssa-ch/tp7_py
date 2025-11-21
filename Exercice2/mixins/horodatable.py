
from datetime import datetime

class Horodatable:
    def __init__(self):
        self.created_at = datetime.now()
        self.updated_at = None

    def mettre_a_jour_timestamp(self):
        self.updated_at = datetime.now()
