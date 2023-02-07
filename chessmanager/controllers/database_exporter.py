import json
from .player_encoder import PlayerEncoder
from .tournament_encoder import TournamentEncoder


class DatabaseExporter:
    """ Export players and tournaments structure in a json file """

    def __init__(self, players, tournaments, filename):
        self.players = players
        self.tournaments = tournaments
        self.filename = filename

    def save_database(self):
        # TODO : save players and tournaments in a json file

        with open(self.filename, 'w', encoding='utf8') as json_file:
            json.dump(
                self.players,
                json_file,
                cls=PlayerEncoder,
                indent=4,
                separators=(',', ': '),

            )
            json.dump(
                self.tournaments,
                json_file,
                cls=TournamentEncoder,
                indent=4,
                separators=(',', ': ')
            )

