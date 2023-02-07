from unittest import TestCase

from chessmanager.models import Tournament


class TestTournament(TestCase):
    def test_init(self):
        tournament_1 = Tournament(
            1,
            'Tournoi des candidats 2020',
            'Double round-robin à 8 joueurs',
            'Dubai',
            '17/03/2020',
            '03/04/2020'
        )
        self.assertEqual(tournament_1.__str__(), '1 : Tournoi des candidats 2020')

    def test_equal(self):
        tournament_1 = Tournament(
            1,
            'Tournoi des candidats 2020',
            'Double round-robin à 8 joueurs',
            'Dubai',
            '17/03/2020',
            '03/04/2020'
        )
        tournament_2 = Tournament(
            1,
            'Tournoi des candidats 2020',
            'Double round-robin à 8 joueurs',
            'Dubai',
            '17/03/2020',
            '03/04/2020'
        )
        self.assertEqual(tournament_1 == tournament_2, True)
