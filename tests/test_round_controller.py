from unittest import TestCase
from chessmanager.models import Round
from chessmanager.models import Player
from chessmanager.models import Tournament
from chessmanager.controllers import TournamentController
from chessmanager.controllers import RoundController

class TestRoundController(TestCase):

    def create_a_tournament(self):
        a_tournament = Tournament(
            1,
            'Tournoi des candidats 2020',
            'Double round-robin à 8 joueurs',
            'Dubai',
            '17/03/2020',
            '03/04/2020'
        )
        return a_tournament
    def create_8_players(self):
        list_of_4_players = []
        player1 = Player('AB12345', 'Carlsen', 'Magnus', '30/11/1990', 2852)
        player2 = Player('AB12346', 'Nepomniachtchi', 'Ian', '14/07/1990', 2793)
        player3 = Player('AB12347', 'Liren', 'Ding', '24/10/1992', 2788)
        player4 = Player('AB12348', 'Alireza', 'Firouzja', '18/06/2003', 2785)
        player5 = Player('AB12349', 'Anish', 'Giri', '28/06/1994', 2780)
        player6 = Player('AB12350', 'Hikaru', 'Nakamura', '09/12/2987', 2768)
        player7 = Player('AB12351', 'Fabiano', 'Caruana', '30/06/1992', 2766)
        player8 = Player('AB12352', 'Wesley', 'So', '09/10/1993', 2766)
        list_of_4_players.append(player1)
        list_of_4_players.append(player2)
        list_of_4_players.append(player3)
        list_of_4_players.append(player4)
        list_of_4_players.append(player5)
        list_of_4_players.append(player6)
        list_of_4_players.append(player7)
        list_of_4_players.append(player8)
        return list_of_4_players

    def test_check_all_score_record(self):
        a_round = Round(1, 'Round 1', '09/02/2023', '14:00',
                       '09/02/2023', '15:00')
        a_tournament = self.create_a_tournament()
        a_tournament.players = self.create_8_players()
        tournament_controller = TournamentController(a_tournament)

        set_of_players = tournament_controller.pairing_next_round()
        # create matches
        for elem in set_of_players:
            match = [elem[0], 1], [elem[1], 0]
            a_round.matches.append(match)

        round_controller = RoundController(a_round)
        result = round_controller.check_all_score_record()

        self.assertEqual(result, True)


