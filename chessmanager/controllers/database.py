from datetime import datetime
from tinydb import TinyDB
from tinydb import where
from chessmanager.models import Player
from chessmanager.models import Tournament
from chessmanager.models import Round
from chessmanager.views import PlayerStaticView


class ChessManagerDatabase:
    def __init__(self, folder):
        self.data_directory = folder
        self.filename = folder + '/db.json'
        self.db = TinyDB(self.filename)


class RoundDatabase(PlayerStaticView, ChessManagerDatabase):
    def __init__(self, folder):
        super().__init__(folder)
        self.rounds_table = self.db.table('tournaments')

    def round_to_dict(self, a_round) -> dict:
        list_of_matches = []
        for match in a_round.matches:
            list_of_matches.append(
                ([match[0][0].to_dict(), match[0][1]],
                 [match[1][0].to_dict(), match[1][1]])
            )

        a_dict = {
            "round_id": a_round.round_id,
            "name": a_round.name,
            "date_begin": datetime.strftime(a_round.date_begin, '%d/%m/%Y'),
            "time_begin": datetime.strftime(a_round.time_begin, '%H:%M'),
            "date_end": datetime.strftime(
                a_round.date_end, '%d/%m/%Y') if a_round.date_end else '',
            "time_end": datetime.strftime(
                a_round.time_end, '%H:%M') if a_round.time_end else '',
            "state": a_round.state,
            "matches": list_of_matches
        }
        return a_dict

    def round_from_dict(self, a_dict) -> Round:
        new_round = Round(a_dict['round_id'],
                          a_dict['name'],
                          a_dict['date_begin'],
                          a_dict['time_begin'],
                          a_dict['date_end'],
                          a_dict['time_end'],
                          a_dict['state'])
        for a_match in a_dict['matches']:
            player_white = Player(**a_match[0][0])
            player_black = Player(**a_match[1][0])
            new_match = [player_white, a_match[0][1]], \
                        [player_black, a_match[1][1]]
            new_round.matches.append(new_match)
        return new_round

    def get(self, tournament_id, round_id):
        tournament_dict = self.rounds_table.get(
            where('tournament_id') == tournament_id)
        if tournament_dict:
            for round_dict in tournament_dict['rounds']:
                the_round = self.round_from_dict(round_dict)
                if the_round == round_id:
                    return the_round
            return None
        else:
            return None

    def save(self, a_round):
        if self.get(a_round.tournament_id) is None:
            self.rounds_table.insert(self.round_to_dict(a_round))
        else:
            self.rounds_table.update(
                self.round_to_dict(a_round),
                where('round_id') == a_round.round_id
            )

    def get_rounds(self) -> list:
        tournaments_dict = self.rounds_table.all()
        tournaments = []
        for elem in tournaments_dict:
            tournaments.append(self.round_from_dict(elem))
        return tournaments


class TournamentDatabase(PlayerStaticView, ChessManagerDatabase):
    def __init__(self, folder):
        super().__init__(folder)
        self.tournaments_table = self.db.table('tournament')

    def tournament_to_dict(self, tournament) -> dict:
        list_of_players = []
        for a_player in tournament.players:
            list_of_players.append(a_player.chess_id)
        list_of_rounds = []
        for a_round in tournament.rounds:
            list_of_rounds.append(a_round.round_id)
        a_dict = {
            "tournament_id": tournament.tournament_id,
            "title": tournament.title,
            "description": tournament.description,
            "area": tournament.area,
            "date_begin": tournament.date_begin,
            "date_end": tournament.date_end,
            "nb_of_rounds": tournament.nb_of_rounds,
            "state": tournament.state,
            "players": list_of_players,
            "rounds": list_of_rounds
        }
        return a_dict

    def tournament_from_dict(self, a_dict) -> Tournament:
        db_players = PlayerDatabase(self.data_directory)
        tournament = Tournament(a_dict['tournament_id'],
                                a_dict['title'], a_dict['description'],
                                a_dict['area'],
                                a_dict['date_begin'],
                                a_dict['date_end'],
                                a_dict['nb_of_rounds'], a_dict['state'])
        for player_id in a_dict['players']:
            tournament.players.append(db_players.get(player_id))
        for round_id in a_dict['rounds']:
            db = RoundDatabase(self.data_directory)
            db.get(tournament.tournament_id, round_id)
        return tournament

    def get(self, tournament_id):
        tournament_dict = self.tournaments_table.get(
            where('tournament_id') == tournament_id)
        if tournament_dict:
            tournament = self.tournament_from_dict(tournament_dict)
            return tournament
        else:
            return None

    def save(self, tournament):
        if self.get(tournament.tournament_id) is None:
            self.tournaments_table.insert(self.tournament_to_dict(tournament))
        else:
            self.tournaments_table.update(
                self.tournament_to_dict(tournament),
                where('tournament_id') == tournament.tournament_id
            )

    def get_tournaments(self) -> list:
        tournaments_dict = self.tournaments_table.all()
        tournaments = []
        for elem in tournaments_dict:
            tournaments.append(self.tournament_from_dict(elem))
        return tournaments


class PlayerDatabase(PlayerStaticView, ChessManagerDatabase):
    def __init__(self, folder):
        super().__init__(folder)
        self.players_table = self.db.table('players')

    def player_to_dict(self, player) -> dict:
        a_dict = {
            "chess_id": player.chess_id,
            "last_name":player.last_name,
            "first_name": player.first_name,
            "birthday": datetime.strftime(player.birthday, '%d/%m/%Y'),
            "chess_level": player.chess_level,
            "current_score": player.current_score
        }
        return a_dict

    def player_from_dict(self, player_dict) -> Player:
        return Player(**player_dict)

    def save(self, player):
        if self.get(player.chess_id) is None:
            self.players_table.insert(self.player_to_dict(player))
        else:
            self.players_table.update(
                self.player_to_dict(player),
                where('chess_id') == player.chess_id
            )

    def get(self, chess_id):
        player_dict = self.players_table.get(where('chess_id') == chess_id)
        if player_dict:
            player = self.player_from_dict(player_dict)
            return player
        else:
            return None

    def get_players(self) -> list:
        players_dict = self.players_table.all()
        players = []
        for elem in players_dict:
            players.append(self.player_from_dict(elem))
        return players

