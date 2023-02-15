import os

from unittest import TestCase

from chessmanager.controllers import Parameters
from chessmanager.controllers import ChessManager
from chessmanager.controllers import TournamentController

from chessmanager.models import Round
from chessmanager.models import ROUND_CLOSED

from tests import TestInit


class TestChessManager(TestCase, TestInit):
    def test_check_directories(self):
        p = Parameters()
        chess_manager = ChessManager(p)
        self.assertEqual(
            os.path.exists(chess_manager.output_directory)
            and os.path.exists(chess_manager.data_directory),
            True
        )

    def test_save_players(self):

        chess_manager = ChessManager(Parameters())

        chess_manager.players = self.create_4_players(self)

        chess_manager.save_players()

        filename = chess_manager.data_directory + '/players.json'

        self.assertEqual(
            os.path.exists(filename) and os.path.getsize(filename) == 829,
            True)

    def test_load_players(self):
        chess_manager = ChessManager(Parameters())
        chess_manager.load_players()
        print(chess_manager.players[0])
        result = str(chess_manager.players[0])
        self.assertEqual(result, 'Carlsen Magnus')

    def test_load_tournaments(self):
        chess_manager = ChessManager(Parameters())
        chess_manager.load_tournaments()
        result_1 = str(chess_manager.tournaments[0].players[0])
        result_2 = str(chess_manager.tournaments[0].rounds[0].matches[0][0][0])
        self.assertEqual(result_1 + ' ' + result_2, 'Carlsen Magnus AB12345')

    def test_save_tournaments(self):

        chess_manager = ChessManager(Parameters())
        a_tournament = self.create_a_tournament(self)
        a_tournament.players = self.create_8_players(self)

        a_round = Round(1, "Round 1", '09/02/2023', '14:00',
                        '09/02/2023', '15:00')

        match = ['AB12345', 0], ['AB12346', 0]
        a_round.matches.append(match)
        match = ['AB12347', 0], ['AB12348', 0]
        a_round.matches.append(match)
        match = ['AB12349', 0], ['AB12310', 0]
        a_round.matches.append(match)
        match = ['AB12311', 0], ['AB12312', 0]
        a_round.matches.append(match)

        a_tournament.rounds.append(a_round)
        chess_manager.tournaments.append(a_tournament)

        chess_manager.save_tournaments()

        filename = chess_manager.data_directory + '/tournaments.json'
        self.assertEqual(
            os.path.exists(filename) and os.path.getsize(filename) == 4095,
            True)

    def test_close_round(self):
        # GIVEN
        parameters = Parameters()
        a_chess_manager = ChessManager(parameters)

        a_tournament = self.create_a_tournament(self)
        a_tournament.players = self.create_8_players(self)
        tournament_controller = TournamentController(a_tournament)
        a_round = Round(1, 'Round 1', '09/02/2023', '14:00',
                        '09/02/2023', '15:00')
        set_of_players = tournament_controller.pairing_next_round()
        # create matches with result
        for elem in set_of_players:
            match = [elem[0], 1], [elem[1], 0]
            a_round.matches.append(match)
        a_tournament.rounds.append(a_round)
        a_chess_manager.tournaments.append(a_tournament)

        # WHEN
        # tournament_controller.close_round() # error when use of questionary in test

        # THEN
        self.assertEqual(a_round.state, ROUND_CLOSED)
