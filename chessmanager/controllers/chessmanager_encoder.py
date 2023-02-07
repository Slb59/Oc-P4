import json
from chessmanager.controllers import ChessManager
from chessmanager.models import Player
from chessmanager.models import Tournament
from chessmanager.models import Round
from chessmanager.models import Match


class ChessManagerEncoder(json.JSONEncoder):

    def default(self, o):

        if isinstance(o, ChessManager):
            a_dict = {
                "players": o.players,
                "tournaments": o.tournaments
            }
            return a_dict
        elif isinstance(o, Player):
            a_dict = {
                "chess_id": o.chess_id,
                "last_name": o.last_name,
                "first_name": o.first_name,
                "birthday": o.birthday.strftime("%D/%m/%Y"),
                "chess_level": o.chess_level
            }
            return a_dict
        elif isinstance(o, Tournament):
            a_dict = {
                "tournament_id": o.tournament_id,
                "title": o.title,
                "description": o.description,
                "area": o.area,
                "date_begin": o.date_begin.strftime("%D/%m/%Y"),
                "date_end": o.date_end.strftime("%D/%m/%Y"),
                "nb_of_round": o.nb_of_rounds,
                "state": o.state,
                "rounds": o.rounds,
                "players": o.players
            }
            return a_dict
        elif isinstance(o, Round):
            a_dict = {
                "round_id": o.round_id,
                "name": o.name,
                "date_begin": o.date_begin.strftime("%D/%m/%Y"),
                "time_begin": o.time_begin.strftime("%H:%M:%S"),
                "date_end": o.date_end.strftime("%D/%m/%Y"),
                "time_end": o.time_end.strftime("%H:%M:%S"),
                "matches": o.matches,
                "state": o.state
            }
            return a_dict
        elif isinstance(o, Match):
            a_dict = {
                "no_match": o.no_match,
                "white": o.player_white,
                "black": o.player_black
            }
            return a_dict
        else:
            type_name = o.__class__.__name__
            raise TypeError("Unexpected type {0}".format(type_name))

