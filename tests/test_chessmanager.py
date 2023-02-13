import os

from unittest import TestCase

from chessmanager.controllers import Parameters
from chessmanager.controllers import ChessManager
from chessmanager.controllers import ArgParser
from chessmanager.models import Player
from chessmanager.models import Tournament


class TestChessManager(TestCase):
    def test_check_directories(self):
        p = Parameters()
        chess_manager = ChessManager(p)
        self.assertEqual(
            os.path.exists(chess_manager.output_directory)
            and os.path.exists(chess_manager.data_directory),
            True
        )

    def test_run(self):
        self.fail()

    def create_4_players(self):
        list_of_4_players = []
        player1 = Player('AB12345', 'Carlsen', 'Magnus', '30/11/1990', 2852)
        player2 = Player('AB12346', 'Nepomniachtchi', 'Ian', '14/07/1990', 2793)
        player3 = Player('AB12347', 'Liren', 'Ding', '24/10/1992', 2788)
        player4 = Player('AB12348', 'Alireza', 'Firouzja', '18/06/2003', 2785)
        list_of_4_players.append(player1)
        list_of_4_players.append(player2)
        list_of_4_players.append(player3)
        list_of_4_players.append(player4)
        return list_of_4_players

    def test_save_players(self):
        args = ArgParser()
        the_parameters = args.read_parameters()
        chess_manager = ChessManager(the_parameters)

        chess_manager.players = self.create_4_players()

        # chess_manager.save_players()

        filename = chess_manager.data_directory + '/players.json'

        self.assertEqual(
            os.path.exists(filename) and os.path.getsize(filename) == 829,
            True)

    def test_save_tournaments(self):
        args = ArgParser()
        the_parameters = args.read_parameters()
        chess_manager = ChessManager(the_parameters)

        a_tournament = Tournament(
            1,
            'Tournoi des candidats 2020',
            'Double round-robin à 8 joueurs',
            'Dubai',
            '17/03/2020',
            '03/04/2020'
        )

        chess_manager.tournaments.append(a_tournament)

        # chess_manager.save_tournaments()

        self.fail()
