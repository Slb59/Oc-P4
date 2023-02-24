from datetime import datetime
from tinydb import TinyDB
from tinydb import where
from chessmanager.models import Player
from chessmanager.models import Tournament
from chessmanager.views import PlayerStaticView


class TournamentDatabase(PlayerStaticView):
    def __init__(self, folder):
        self.data_directory = folder
        self.filename = folder + '/db.json'
        self.db = TinyDB(self.filename)
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
            pass
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


class PlayerDatabase(PlayerStaticView):
    def __init__(self, folder):
        self.filename = folder + '/db.json'
        self.db = TinyDB(self.filename)
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

