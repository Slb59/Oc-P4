from unittest import TestCase
from chessmanager.models import Tournament
from chessmanager.models import Player
from chessmanager.controllers import TournamentController
from chessmanager.models import Round


class TestTournamentController(TestCase):

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

    def test_sort_players_by_score(self):
        a_tournament = self.create_a_tournament()

        list_of_4_players = self.create_4_players()

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
        a_tournament = self.create_a_tournament()

        list_of_4_players = self.create_4_players()

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
        a_tournament = self.create_a_tournament()
        list_of_8_players = self.create_8_players()
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

        a_tournament = self.create_a_tournament()

        tournament_controller = TournamentController(a_tournament)
        a_tournament.players = self.create_8_players()

        tournament_controller.create_round()
        print(a_tournament.rounds[0])
        print(a_tournament.rounds[0].matches)

        self.fail()
