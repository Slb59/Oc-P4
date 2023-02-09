from unittest import TestCase
from chessmanager.models import Tournament
from chessmanager.models import Player
from chessmanager.controllers import TournamentController
from chessmanager.models import Round


class TestTournamentController(TestCase):

    def test_sort_players_by_score(self):
        a_tournament = Tournament(
            1,
            'Tournoi des candidats 2020',
            'Double round-robin à 8 joueurs',
            'Dubai',
            '17/03/2020',
            '03/04/2020'
        )
        player1 = Player('AB12345', 'Carlsen', 'Magnus', '30/11/1990', 2852)
        player2 = Player('AB12346', 'Nepomniachtchi', 'Ian', '14/07/1990', 2793)
        player3 = Player('AB12347', 'Liren', 'Ding', '24/10/1992', 2788)
        player4 = Player('AB12348', 'Alireza', 'Firouzja', '18/06/2003', 2785)

        a_tournament.players.append(player1)
        a_tournament.players.append(player2)
        a_tournament.players.append(player3)
        a_tournament.players.append(player4)

        tournament_controller = TournamentController(a_tournament)

        tournament_controller.shuffle_players()

        player1.current_score = 1
        player2.current_score = 5
        player3.current_score = 2
        player4.current_score = 0

        tournament_controller.sort_players_by_score()

        self.assertEqual(a_tournament.players[0] == player2
                         and a_tournament.players[1] == player3
                         and a_tournament.players[2] == player1
                         and a_tournament.players[3] == player4, True)

    def test_pairing_first_round(self):
        a_tournament = Tournament(
            1,
            'Tournoi des candidats 2020',
            'Double round-robin à 8 joueurs',
            'Dubai',
            '17/03/2020',
            '03/04/2020'
        )
        player1 = Player('AB12345', 'Carlsen', 'Magnus', '30/11/1990', 2852)
        player2 = Player('AB12346', 'Nepomniachtchi', 'Ian', '14/07/1990', 2793)
        player3 = Player('AB12347', 'Liren', 'Ding', '24/10/1992', 2788)
        player4 = Player('AB12348', 'Alireza', 'Firouzja', '18/06/2003', 2785)

        a_tournament.players.append(player1)
        a_tournament.players.append(player2)
        a_tournament.players.append(player3)
        a_tournament.players.append(player4)

        tournament_controller = TournamentController(a_tournament)
        result = tournament_controller.pairing_first_round()
        for set_of_player in result:
            print(f'{set_of_player[0]} - {set_of_player[1]}')

        result_must_be = [[player1, player2], [player3, player4]]
        self.assertEqual(result, result_must_be)

    def test_pairing_next_round(self):
        a_tournament = Tournament(
            1,
            'Tournoi des candidats 2020',
            'Double round-robin à 8 joueurs',
            'Dubai',
            '17/03/2020',
            '03/04/2020'
        )
        player1 = Player('AB12345', 'Carlsen', 'Magnus', '30/11/1990', 2852)
        player2 = Player('AB12346', 'Nepomniachtchi', 'Ian', '14/07/1990', 2793)
        player3 = Player('AB12347', 'Liren', 'Ding', '24/10/1992', 2788)
        player4 = Player('AB12348', 'Alireza', 'Firouzja', '18/06/2003', 2785)
        player5 = Player('AB12349', 'Anish', 'Giri', '28/06/1994', 2780)
        player6 = Player('AB12350', 'Hikaru', 'Nakamura', '09/12/2987', 2768)
        player7 = Player('AB12351', 'Fabiano', 'Caruana', '30/06/1992', 2766)
        player8 = Player('AB12352', 'Wesley', 'So', '09/10/1993', 2766)

        a_tournament.players.append(player1)
        a_tournament.players.append(player2)
        a_tournament.players.append(player3)
        a_tournament.players.append(player4)
        a_tournament.players.append(player5)
        a_tournament.players.append(player6)
        a_tournament.players.append(player7)
        a_tournament.players.append(player8)

        tournament_controller = TournamentController(a_tournament)
        round1 = Round(1, 'Round 1', '09/02/2023', '14:00',
                 '09/02/2023', '15:00')

        round1.matches = tournament_controller.pairing_first_round()
        print('FIRST ROUND')
        for match in round1.matches:
            print(f'{match[0]} - {match[1]}')

        result = tournament_controller.pairing_next_round()
        print('NEXT ROUND')
        for match in result:
            print(f'{match[0]} - {match[1]}')
        self.fail()
