import json

from chessmanager.models import Player


class PlayerEncoder(json.JSONEncoder):

    def default(self, player):

        if isinstance(player, Player):
            a_dict = {
                "chess_id": player.chess_id,
                "last_name": player.last_name,
                "first_name": player.first_name,
                "birthday": player.birthday.strftime("%D/%M/%Y"),
                "chess_level": player.chess_level
            }
            return a_dict
        else:
            type_name = player.__class__.__name__
            raise TypeError("Unexpected type {0}".format(type_name))
