import datetime
from unittest import TestCase

from chessmanager.models import Player
from chessmanager.models import Tournament
from chessmanager.controllers import DatabaseExporter
from chessmanager.controllers import ChessManager
from chessmanager.controllers import ArgParser


class TestDatabaseExporter(TestCase):
    def test_save_database(self):
        player1 = Player('AB12345',
                         'Carlsen', 'Magnus',
                         datetime.datetime.strptime('30/11/1990', '%d/%m/%Y'),
                         2852)
        player2 = Player('AB12346',
                         'Nepomniachtchi', 'Ian',
                         datetime.datetime.strptime('14/07/1990', '%d/%m/%Y'),
                         2793)
        player3 = Player('AB12347', 'Ding', 'Liren',
                         datetime.datetime.strptime('24/10/1992', '%d/%m/%Y'),
                         2788)
        list_of_players = [player1, player2, player3]
        tournament_1 = Tournament(
            1,
            'Tournoi des candidats 2020',
            'Double round-robin à 8 joueurs',
            'Dubai',
            datetime.datetime.strptime('17/03/2020', '%d/%m/%Y'),
            datetime.datetime.strptime('03/04/2020', '%d/%m/%Y')
        )
        tournament_2 = Tournament(
            2,
            'Tournoi de Shamkir',
            'A la mémoire du joueur azerbaïdjanais Vugar Gashimov',
            'Shamkir',
            datetime.datetime.strptime('31/03/2019', '%d/%m/%Y'),
            datetime.datetime.strptime('09/04/2019', '%d/%m/%Y')
        )
        list_of_tournaments = [tournament_1, tournament_2]

        args = ArgParser()
        the_parameters = args.read_parameters()
        chess_manager = ChessManager(the_parameters)
        chess_manager.players.append(player1)
        chess_manager.players.append(player2)
        chess_manager.players.append(player3)
        chess_manager.tournaments.append(tournament_1)
        chess_manager.tournaments.append(tournament_2)

        database = DatabaseExporter(chess_manager, 'data/tournaments.json')
        database.save_database()
        self.fail()
