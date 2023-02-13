from unittest import TestCase
from chessmanager.controllers import DatabaseLoader
from chessmanager.controllers import Parameters


class TestDatabaseLoader(TestCase):
    def test_load_database(self):
        parameters = Parameters()
        database = DatabaseLoader(parameters)
        chess_manager = database.load_database()
        print(chess_manager.players[0])
        print(chess_manager.tournaments[0])
        print(chess_manager.tournaments[1].rounds[0].matches[0])
        self.fail()
