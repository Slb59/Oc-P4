import json
import os
from chessmanager.controllers import ChessManager
from chessmanager.views import DatabaseView
from chessmanager.models import Club
from chessmanager.models import Player
from chessmanager.models import Tournament


class DatabaseLoader:
    """ Load a json file to players and tournament structure """
    def __init__(self, parameters):
        self.parameters = parameters
        self.filename = self.parameters.data_directory + '/tournaments.json'
        self.database_view = DatabaseView(self)

    def load_database(self):
        if not os.path.exists(self.filename):
            self.database_view.display_database_not_found()
            club = Club()
            chess_manager = ChessManager(self.parameters, club)
        else:
            f = open(self.filename)
            data = json.load(f)
            players = []
            tournaments = []
            for elem in data['players']:
                player = Player(
                    elem['chess_id'],
                    elem['last_name'],
                    elem['first_name'],
                    elem['birthday'],
                    elem['chess_level']
                )
                players.append(player)

            for elem in data['tournaments']:
                print(elem)
                tournament = Tournament(
                    elem['tournament_id'],
                    elem['title'],
                    elem['description'],
                    elem['area'],
                    elem['date_begin'],
                    elem['date_end'],
                    elem['nb_of_round']
                )
                tournaments.append(tournament)

            club = Club(players, data['tournaments'])
            chess_manager = ChessManager(self.parameters, club)
            self.database_view.display_database_loaded()

        return chess_manager
