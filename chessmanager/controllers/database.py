import json
from logs import LOGGER
from chessmanager.models import Player
from chessmanager.models import Tournament
from chessmanager.models import Round
from chessmanager.views import DatabaseView


class ChessManagerDatabase:
    """
    Manage save and load of a chess_manager
    """

    def __init__(self, chess_manager):
        self.chess_manager = chess_manager

    def save_players(self):
        """ save the list of players in players.json file """
        filename = self.chess_manager.data_directory + '/players.json'
        with open(filename, 'w', encoding="utf-8") as json_file:
            json.dump(
                [o.to_dict() for o in self.chess_manager.players],
                json_file,
                indent=4,
                separators=(',', ': ')
        )

    def load_players(self):
        filename = self.chess_manager.data_directory + '/players.json'
        database_view = DatabaseView(filename)
        try:
            with open(filename, encoding="utf-8") as f:
                data = json.load(f)
            for elem in data:
                player = Player(**elem)
                self.chess_manager.players.append(player)
            database_view.display_database_loaded()
        except FileNotFoundError:
            database_view.display_database_not_found()

    def save_tournaments(self):
        filename = self.chess_manager.data_directory + '/tournaments.json'
        LOGGER.debug("Save tournament in " + filename)
        with open(filename, 'w', encoding='utf8') as json_file:
            json.dump(
                [o.to_dict() for o in self.chess_manager.tournaments],
                json_file,
                indent=4,
                separators=(',', ': ')
            )

    def load_tournaments(self):
        filename = self.chess_manager.data_directory + '/tournaments.json'
        database_view = DatabaseView(filename)
        try:
            with open(filename, encoding='utf8') as f:
                data = json.load(f)
            for elem in data:
                tournament = Tournament(elem['tournament_id'], elem['title'], elem['description'],
                                        elem['area'], elem['date_begin'], elem['date_end'],
                                        elem['nb_of_rounds'], elem['state'])
                for player in elem['players']:
                    new_player = Player(**player)
                    tournament.players.append(new_player)
                for a_round in elem['rounds']:
                    new_round = Round(a_round['round_id'], a_round['name'], a_round['date_begin'],
                                      a_round['time_begin'], a_round['date_end'], a_round['time_end'],
                                      a_round['state'])
                    for a_match in a_round['matches']:
                        player_white = Player(**a_match[0][0])
                        player_black = Player(**a_match[1][0])
                        new_match = [player_white, a_match[0][1]], [player_black, a_match[1][1]]
                        new_round.matches.append(new_match)

                    tournament.rounds.append(new_round)

                self.chess_manager.tournaments.append(tournament)
            database_view.display_database_loaded()
        except FileNotFoundError:
            database_view.display_database_not_found()