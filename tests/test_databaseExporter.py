import datetime
from unittest import TestCase

from chessmanager.models import Player
from chessmanager.models import Tournament
from chessmanager.controllers import DatabaseExporter


class TestDatabaseExporter(TestCase):
    def test_save_database(self):
        player1 = Player('AB12345',
                         'Carlsen', 'Magnus',
                         datetime.datetime.strptime('30/11/1990', '%d/%m/%Y'),
                         2852)
        player2 = Player('AB12346',
                         'Nepomniachtchi', 'Ian',
                         datetime.datetime.strptime('14/07/1990', '%d/%m/%Y'),
                         2793)
        player3 = Player('AB12347', 'Ding', 'Liren',
                         datetime.datetime.strptime('24/10/1992', '%d/%m/%Y'),
                         2788)
        list_of_players = [player1, player2, player3]
        tournament_1 = Tournament(
            1,
            'Tournoi des candidats 2020',
            'Double round-robin à 8 joueurs',
            'Dubai',
            '17/03/2020',
            '03/04/2020'
        )
        tournament_2 = Tournament(
            2,
            'Tournoi de Shamkir',
            'A la mémoire du joueur azerbaïdjanais Vugar Gashimov',
            'Shamkir',
            '31/03/2019',
            '09/04/2019'
        )
        list_of_tournaments = [tournament_1, tournament_2]
        database = DatabaseExporter(list_of_players, list_of_tournaments, 'data/tournaments.json')
        database.save_database()
        self.fail()
