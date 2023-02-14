class DatabaseView:

    def __init__(self, filename):
        self.filename = filename

    def display_database_not_found(self):
        print(f"La base de données {self.filename} n''a pas été trouvée")

    def display_database_loaded(self):
        print(f"La base de données {self.filename} est chargée")

    def display_database_save(self):
        print(f"Les données de {self.filename} ont été sauvegardées")
