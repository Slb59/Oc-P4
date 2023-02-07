class DatabaseLoader:
    """ Load a json file to players and tournament structure """
    def __init__(self, filename):
        self.filename = filename

    def load_players(self):
        # TODO : load players from json file
        list_of_players = []
        return list_of_players

    def load_tournament(self):
        # TODO : load tournament from json file
        list_of_tournaments = []
        return list_of_tournaments

    def load_database(self):
        return self.load_players(), self.load_tournament()
