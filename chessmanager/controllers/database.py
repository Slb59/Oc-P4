import json

from datetime import datetime
from tinydb import TinyDB
from tinydb import where
from tinydb import Query
from logs import LOGGER
from chessmanager.models import Player
from chessmanager.models import Tournament
from chessmanager.models import Round
from chessmanager.views import DatabaseView
from chessmanager.views import ChessManagerView
from chessmanager.views import error_player_not_exist


class PlayerDatabase:
    def __init__(self, folder, player):
        self.player = player
        filename = folder + '/db.json'
        db = TinyDB(filename)
        self.players_table = db.table('players')

    def to_dict(self) -> dict:
        a_dict = {
            "chess_id": self.player.chess_id,
            "last_name": self.player.last_name,
            "first_name": self.player.first_name,
            "birthday": datetime.strftime(self.player.birthday, '%d/%m/%Y'),
            "chess_level": self.player.chess_level,
            "current_score": self.player.current_score
        }
        return a_dict

    def from_dict(self, player_dict) -> Player:
        return Player(**player_dict)
    def save(self):
        self.players_table.insert(self.to_dict())

    def get(self, chess_id) -> Player:
        try:
            player_dict = self.players_table.get(where('chess_id') == chess_id)
            player = self.from_dict(player_dict)
            return player
        except IndexError:
            error_player_not_exist(self)
            return Player('', '', '', '', '')



