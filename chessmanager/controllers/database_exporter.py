import json
from .player_encoder import PlayerEncoder


class DatabaseExporter:
    """ Export players and tournaments structure in a json file """

    def __init__(self, players, tournaments, filename):
        self.players = players
        self.tournaments = tournaments
        self.filename = filename

    def save_database(self):
        # TODO : save players and tournaments in a json file

        with open(self.filename, 'w') as json_file:
            json.dump(
                self.players,
                json_file,
                cls=PlayerEncoder,
                indent=4,
                separators=(',', ': ')
            )

