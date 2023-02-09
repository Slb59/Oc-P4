from unittest import TestCase
from chessmanager.models import Tournament
from chessmanager.models import Player
from chessmanager.controllers import TournamentController


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

    def test_pairing(self):
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
        for set_of_player in tournament_controller.pairing():
            print(f'{set_of_player[0]} - {set_of_player[1]}')

        self.fail()
