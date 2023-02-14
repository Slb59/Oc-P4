from unittest import TestCase

from chessmanager.models import Player


class TestPlayer(TestCase):
    def test_init(self):
        player = Player('AB12345', 'Carlsen', 'Magnus', '30/11/1990', 2852)
        self.assertEqual(player.__str__(), 'Carlsen Magnus')

    def test_equal(self):
        player1 = Player('AB12345', 'Carlsen', 'Magnus', '30/11/1990', 2852)
        player2 = Player('AB12345', 'Carlsen', 'Magnus', '30/11/1990', 2852)
        self.assertEqual(player1 == player2, True)

    def test_not_equal(self):
        player1 = Player('AB12345', 'Carlsen', 'Magnus', '30/11/1990', 2852)
        player2 = Player('AB12346', 'Nepomniachtchi', 'Ian', '14/07/1990', 2793)
        self.assertEqual(player1 == player2, False)
