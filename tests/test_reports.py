from unittest import TestCase
from tests import TestInit
from chessmanager.controllers import Parameters
from chessmanager.controllers import ChessManager
from chessmanager.controllers import ChessManagerReports


class TestChessManagerReports(TestCase, TestInit):

    def test_all_players_in_alphabetic_order(self):
        # GIVEN
        a_chess_manager = ChessManager(Parameters())
        a_chess_manager.players = self.create_8_players(self)
        chess_manager_reports = ChessManagerReports(
            a_chess_manager.players,
            a_chess_manager.tournaments,
            a_chess_manager.output_directory
        )
        # WHEN
        chess_manager_reports.all_players_in_alphabetic_order()
        # THEN
        self.fail()

    def test_all_tournaments(self):
        self.fail()

    def test_tournament_data(self):
        self.fail()

    def test_tournament_players(self):
        self.fail()

    def test_tournaments_details(self):
        self.fail()
