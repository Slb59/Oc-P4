import os

from unittest import TestCase
from tests import TestInit

from chessmanager.controllers import Parameters
from chessmanager.controllers import ChessManager
from chessmanager.controllers import ChessManagerReports

from chessmanager.models import Player


class TestChessManagerReports(TestCase, TestInit):

    def test_all_players_in_alphabetic_order(self):
        # GIVEN
        a_chess_manager = ChessManager(Parameters())
        a_chess_manager.players = self.create_8_players(self)
        a_player = Player('AB77777', 'Zora', 'Caruana', '01/01/1997', 2700)
        a_chess_manager.players.append(a_player)

        # WHEN
        chess_manager_reports = ChessManagerReports(
            a_chess_manager)
        chess_manager_reports.all_players_in_alphabetic_order()

        # THEN
        filename = 'outputs/chessmanager_report.html'
        print(os.path.getsize(filename))
        self.assertEqual(os.path.exists(filename) and os.path.getsize(filename) == 3163, True)

    def test_all_tournaments(self):
        # GIVEN
        a_chess_manager = ChessManager(Parameters())
        a_chess_manager.tournaments = self.create_6_tournaments()
        # WHEN
        chess_manager_reports = ChessManagerReports(
            a_chess_manager)
        chess_manager_reports.all_tournaments()
        # THEN
        filename = 'outputs/chessmanager_report.html'
        print(os.path.getsize(filename))
        self.assertEqual(os.path.exists(filename) and os.path.getsize(filename) == 4043, True)

    def test_tournament_data(self):
        # WHEN
        a_chess_manager = ChessManager(Parameters())
        a_tournament = self.create_a_tournament(self)
        # GIVEN
        chess_manager_reports = ChessManagerReports(a_chess_manager)
        chess_manager_reports.generate_tournament_data(a_tournament)
        # THEN
        filename = 'outputs/chessmanager_report.html'
        print(os.path.getsize(filename))
        self.assertEqual(os.path.exists(filename) and os.path.getsize(filename) == 1822, True)

    def test_tournament_players(self):
        # WHEN
        a_chess_manager = ChessManager(Parameters())
        a_tournament = self.create_a_tournament(self)
        a_tournament.players = self.create_8_players(self)
        # GIVEN
        chess_manager_reports = ChessManagerReports(a_chess_manager)
        chess_manager_reports.generate_tournament_players(a_tournament)
        # THEN
        filename = 'outputs/chessmanager_report.html'
        print(os.path.getsize(filename))
        self.assertEqual(os.path.exists(filename) and os.path.getsize(filename) == -1, True)


    def test_tournaments_details(self):
        self.fail()
