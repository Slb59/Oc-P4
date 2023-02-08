class DatabaseView:

    def __init__(self, database_loader):
        self.database_loader = database_loader

    def display_database_not_found(self):
        print(f"La base de données {self.database_loader.filename} n''a pas été trouvée")

    def display_database_loaded(self):
        print(f"La base de données {self.database_loader.filename} est chargée")