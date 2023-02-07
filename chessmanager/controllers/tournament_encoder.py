import json

from chessmanager.models import Tournament


class TournamentEncoder(json.JSONEncoder):

    def default(self, tournament):

        if isinstance(tournament, Tournament):
            a_dict = {
                "tournament_id": tournament.tournament_id,
                "title": tournament.title,
                "description": tournament.description,
                "area": tournament.area,
                "date_begin": tournament.date_begin.strftime("%D/%M/%Y"),
                "date_end": tournament.date_end.strftime("%D/%M/%Y"),
                "nb_of_round": tournament.nb_of_rounds,
                "state": tournament.state
                # self.rounds = []
                # self.players = []
            }
            return a_dict
        else:
            type_name = tournament.__class__.__name__
            raise TypeError("Unexpected type {0}".format(type_name))