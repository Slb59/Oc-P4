from unittest import TestCase
from tests import TestInit

from chessmanager.controllers import PlayerDatabase
from chessmanager.controllers import Parameters


class TestPlayerDatabase(TestCase, TestInit):

    def test_save(self):
        #GIVEN
        players = self.create_8_players(self)
        parameters = Parameters()
        #WHEN
        for player in players:
            db = PlayerDatabase(parameters.data_directory, player)
            db.save()
        #THEN
        self.fail()

    def test_get(self):
        self.fail()
