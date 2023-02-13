import json
import datetime
from chessmanager.controllers import ChessManager
from chessmanager.models import Player
from chessmanager.models import Tournament
from chessmanager.models import Round


class ChessManagerEncoder(json.JSONEncoder):

    def default(self, o):
        print(o)
        if isinstance(o, ChessManager):
            a_dict = {
                 "players": o.players,
                 "tournaments": o.tournaments
            }
            return a_dict
        elif isinstance(o, Tournament) \
                or isinstance(o, Player) \
                or isinstance(o, Round):
            return o.__dict__
        elif isinstance(o, datetime.datetime):
            return o.isoformat()
        else:
            type_name = o.__class__.__name__
            raise TypeError("Unexpected type {0}".format(type_name))

