from unittest import TestCase
from chessmanager.models import Tournament
from chessmanager.models import Player
from chessmanager.controllers import TournamentController
from chessmanager.models import Round
from tests import TestInit


class TestTournamentController(TestCase, TestInit):

    def test_sort_players_by_score(self):
        a_tournament = self.create_a_tournament(self)

        list_of_4_players = self.create_4_players(self)

        a_tournament.players.extend(list_of_4_players)

        tournament_controller = TournamentController(a_tournament)

        a_tournament.players[0].current_score = 1
        a_tournament.players[1].current_score = 5
        a_tournament.players[2].current_score = 2
        a_tournament.players[3].current_score = 0

        tournament_controller.shuffle_players()
        tournament_controller.sort_players_by_score()

        self.assertEqual(a_tournament.players[0] == list_of_4_players[1]
                         and a_tournament.players[1] == list_of_4_players[2]
                         and a_tournament.players[2] == list_of_4_players[0]
                         and a_tournament.players[3] == list_of_4_players[3], True)

    def test_pairing_first_round(self):
        a_tournament = self.create_a_tournament(self)

        list_of_4_players = self.create_4_players(self)

        a_tournament.players.extend(list_of_4_players)

        tournament_controller = TournamentController(a_tournament)
        result = tournament_controller.pairing_first_round()
        for set_of_player in result:
            print(f'{set_of_player[0]} - {set_of_player[1]}')

        result_must_be = [[list_of_4_players[0], list_of_4_players[1]],
                          [list_of_4_players[2], list_of_4_players[3]]
                          ]

        self.assertEqual(result, result_must_be)

    def test_pairing_next_round(self):
        a_tournament = self.create_a_tournament(self)
        list_of_8_players = self.create_8_players(self)
        a_tournament.players.extend(list_of_8_players)

        tournament_controller = TournamentController(a_tournament)
        round1 = Round(1, 'Round 1', '09/02/2023', '14:00',
                       '09/02/2023', '15:00')

        round1.matches = tournament_controller.pairing_first_round()
        a_tournament.rounds.append(round1)

        round2 = Round(2, 'Round 2', '09/02/2023', '17:00',
                       '09/02/2023', '18:00')
        round2.matches = tournament_controller.pairing_next_round()
        a_tournament.rounds.append(round2)

        round3 = Round(3, 'Round 3', '09/02/2023', '18:00',
                       '09/02/2023', '19:00')
        round3.matches = tournament_controller.pairing_next_round()
        a_tournament.rounds.append(round3)

        round4 = Round(4, 'Round 4', '09/02/2023', '19:00',
                       '09/02/2023', '20:00')
        round3.matches = tournament_controller.pairing_next_round()
        a_tournament.rounds.append(round4)

        result_must_be = [[list_of_8_players[0], list_of_8_players[4]],
                          [list_of_8_players[1], list_of_8_players[5]],
                          [list_of_8_players[2], list_of_8_players[6]],
                          [list_of_8_players[3], list_of_8_players[7]]]

        self.assertEqual(result_must_be, round3.matches)

    def test_create_round(self):

        a_tournament = self.create_a_tournament(self)

        tournament_controller = TournamentController(a_tournament)
        a_tournament.players = self.create_8_players(self)

        tournament_controller.create_round()

        result = a_tournament.rounds[0].matches[0][0]

        self.assertEqual(result, ['AB12345', 0])
