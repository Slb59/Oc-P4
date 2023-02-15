import random

from chessmanager.models.round import ROUND_STARTED
from chessmanager.models.round import ROUND_CLOSED

from chessmanager.views import RoundView
from chessmanager.views import TournamentView

from chessmanager.models import Round

from .round_controller import RoundController


class TournamentController:
    def __init__(self, a_tournament):
        self.tournament = a_tournament

    def set_winner(self):
        winner = self.tournament.players[0]
        for player in self.tournament.players:
            if player.current_score > winner.current_score:
                winner = player
        self.tournament.winner = winner

    def get_round_id(self, round_id):
        for r in self.tournament.rounds:
            if round_id == r.round_id:
                return r
        return None

    def check_all_rounds_closed(self):
        for a_round in self.tournament.rounds:
            if a_round.state == ROUND_STARTED:
                return False
        return True

    def create_round(self):
        a_round_view = RoundView()

        # input the round data
        new_id = len(self.tournament.rounds) + 1
        name = 'Round ' + str(new_id)
        date_begin = a_round_view.prompt_date_begin()
        time_begin = a_round_view.prompt_time_begin()
        date_end = a_round_view.prompt_date_end()
        time_end = a_round_view.prompt_time_end()

        # pairing the players
        new_round = Round(new_id, name, date_begin, time_begin, date_end, time_end)
        set_of_players = self.pairing_next_round()

        # create matches
        for elem in set_of_players:
            match = [elem[0].chess_id, 0], [elem[1].chess_id, 0]
            new_round.matches.append(match)
        # add the new round to the tournament
        self.tournament.rounds.append(new_round)
        # display tournaments data
        a_tournament_view = TournamentView(self.tournament)
        a_tournament_view.display_tournament_data()

    def close_round(self):
        """ ask the tournament id and the round id
        if all the scores are recorded, close the round
        close the tournament if all the rounds are closed
        """

        # TODO : if tournament is None:
        #     print('Ce tournoi n''existe pas !')

        tournament_view = TournamentView(self.tournament)
        tournament_view.display_tournament_data()

        round_id = tournament_view.prompt_round_id()
        tournament_controller = TournamentController(self.tournament)
        a_round = tournament_controller.get_round_id(round_id)
        # TODO : if a_round is None:
        #     print('Ce round n''existe pas !')

        # test all matches closed
        round_controller = RoundController(a_round)
        # if check_all_matches_closed
        if round_controller.check_all_score_record():
            # TODO : input date_end and time_end
            a_round.state = ROUND_CLOSED
        else:
            # TODO : error, all matches are not recorded
            pass

        if tournament_controller.check_all_rounds_closed():
            tournament_controller.set_winner()
            # display the winner
            tournament_view.display_winner()
        else:
            # create a new round
            tournament_controller.create_round()

    def shuffle_players(self):
        random.shuffle(self.tournament.players)

    def sort_players_by_score(self):
        self.tournament.players.sort(key=lambda x: x.current_score, reverse=True)

    def pairing_first_round(self):
        list_pairing = []
        self.sort_players_by_score()
        for i in range(0, len(self.tournament.players), 2):
            player_white = self.tournament.players[i]
            player_black = self.tournament.players[i+1]
            set_of_players = [player_white, player_black]
            list_pairing.append(set_of_players)
        return list_pairing

    def check_player_already_played_together(self, player_white, player_black):
        for a_round in self.tournament.rounds:
            for match in a_round.matches:
                if player_white in match and player_black in match:
                    return True
        return False

    def pairing_next_round(self):
        list_pairing = []
        self.sort_players_by_score()
        players_selected = []
        for player_white in self.tournament.players:
            if player_white not in players_selected:
                players_selected.append(player_white)
                # looking for player black
                for player_black in self.tournament.players:
                    if player_black not in players_selected and \
                            not self.check_player_already_played_together(player_white, player_black):
                        set_of_players = [player_white, player_black]
                        list_pairing.append(set_of_players)
                        players_selected.append(player_black)
                        break
        return list_pairing
