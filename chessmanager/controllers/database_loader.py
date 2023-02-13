import json
import os
from chessmanager.controllers import ChessManager
from chessmanager.views import DatabaseView
from chessmanager.models import Player
from chessmanager.models import Tournament
from chessmanager.models import Round


class DatabaseLoader:
    """ Load a json file to players and tournament structure """
    def __init__(self, parameters):
        self.parameters = parameters
        self.filename = self.parameters.data_directory + '/tournaments.json'
        self.database_view = DatabaseView(self)

    def load_database(self):
        if not os.path.exists(self.filename):
            self.database_view.display_database_not_found()
            chess_manager = ChessManager(self.parameters)
        else:
            f = open(self.filename)
            data = json.load(f)

            players = []
            tournaments = []

            for elem in data['players']:
                player = Player(**elem)
                players.append(player)

            for elem in data['tournaments']:
                tournament = Tournament(
                    elem['_tournament_id'],
                    elem['title'],
                    elem['description'],
                    elem['area'],
                    elem['date_begin'],
                    elem['date_end'],
                    elem['nb_of_rounds']
                )

                # read the players of the tournaments
                for player in elem['players']:
                    player = Player(**player)
                    tournament.players.append(player)

                # read the rounds of the tournaments
                for a_round in elem['rounds']:
                    new_round = Round(a_round['_round_id'],
                                      a_round['name'],
                                      a_round['date_begin'],
                                      a_round['time_begin'],
                                      a_round['date_end'],
                                      a_round['time_end'])

                    new_round.matches = a_round['matches']
                    tournament.rounds.append(new_round)

                tournaments.append(tournament)

            chess_manager = ChessManager(self.parameters)
            chess_manager.players = players
            chess_manager.tournaments = tournaments

            self.database_view.display_database_loaded()

        return chess_manager
