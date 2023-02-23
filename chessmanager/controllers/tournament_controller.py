import random

from datetime import datetime

from chessmanager.models.round import ROUND_STARTED
from chessmanager.models.round import ROUND_CLOSED

from chessmanager.views import RoundView
from chessmanager.views import TournamentView

from chessmanager.models import Round
from chessmanager.models import TOURNAMENT_CLOSED
from chessmanager.models import TOURNAMENT_STARTED

from .round_controller import RoundController


class TournamentController:
    """
    Manage a tournament behaviour
    """
    def __init__(self, a_tournament):
        self.tournament = a_tournament

    def set_winner(self):
        """
        The winner is the player which have the best current_score
        :return: None
        """
        winner = self.tournament.players[0]
        for player in self.tournament.players:
            if player.current_score > winner.current_score:
                winner = player
        self.tournament.winner = winner

    def get_round_id(self, round_id):
        """
        if the round_id is found in the list of rounds of the tournament
            return a Round object
        else
            return None
        :param round_id:
        :return: None or a Round
        """
        for r in self.tournament.rounds:
            if round_id == r.round_id:
                return r
        return None

    def start_tournament(self) -> bool:
        tournament_view = TournamentView(self.tournament)
        if self.tournament is None:
            tournament_view.error_tournament_not_found()
            return False
        elif self.tournament.state == TOURNAMENT_CLOSED:
            tournament_view.error_tournament_closed()
            return False
        elif self.tournament.state == TOURNAMENT_STARTED:
            tournament_view.error_tournament_started()
            return False
        else:
            tournament_controller = TournamentController(self.tournament)
            tournament_controller.create_round()
            self.tournament.state = TOURNAMENT_STARTED
            return True

    def record_score(self):
        last_round = self.tournament.rounds[-1]
        round_controller = RoundController(last_round)
        round_controller.record_a_score()

    def check_all_rounds_closed(self) -> bool:
        """
        if all the rounds are created and closed
            return True
        else
            return False
        """
        if len(self.tournament.rounds) < self.tournament.nb_of_rounds:
            return False
        for a_round in self.tournament.rounds:
            if a_round.state == ROUND_STARTED:
                return False
        return True

    def create_round(self):
        """
        - ask the round data
        - pairing the players
        - create matches
        - display tournament data
        :return: None
        """
        a_round_view = RoundView()
        a_round_view.display_create_a_round()

        # input the round data
        new_id = len(self.tournament.rounds) + 1
        name = 'Round ' + str(new_id)
        date_data = a_round_view.prompt_begin()

        # pairing the players
        new_round = Round(new_id, name, date_data[0], date_data[1])
        set_of_players = self.pairing_next_round()

        # create matches
        for elem in set_of_players:
            match = [elem[0], 0], [elem[1], 0]
            new_round.matches.append(match)
        # add the new round to the tournament
        self.tournament.rounds.append(new_round)
        # display tournaments data
        a_tournament_view = TournamentView(self.tournament)
        a_tournament_view.display_tournament_data()

    def update_players_score(self, a_round: Round):
        """
        when the round is finish, update the current score of the players
        :return:
        """
        for a_match in a_round.matches:
            a_match[0][0].current_score += a_match[0][1]
            a_match[1][0].current_score += a_match[1][1]

    def close_round(self):
        """
        ask the tournament id, the last round is attempt to close
        if all the scores are recorded
            close the round
        if all the rounds are closed
            close the tournament
        """

        tournament_view = TournamentView(self.tournament)
        tournament_view.display_tournament_data()

        tournament_controller = TournamentController(self.tournament)
        a_round = self.tournament.rounds[-1]
        round_view = RoundView(a_round)
        round_controller = RoundController(a_round)

        if a_round is None:
            tournament_view.error_round_not_exist()
        elif a_round.state == ROUND_CLOSED:
            round_view.error_round_closed()
        elif round_controller.check_all_score_record():
            round_data = round_view.prompt_end()
            a_round.date_end = datetime.strptime(round_data[0], '%d/%m/%Y')
            a_round.time_end = datetime.strptime(round_data[1], '%H:%M')
            a_round.state = ROUND_CLOSED
            self.update_players_score(a_round)

            if tournament_controller.check_all_rounds_closed():
                tournament_controller.set_winner()
                # display the winner
                tournament_view.display_winner()
                self.tournament.state = TOURNAMENT_CLOSED
            elif len(self.tournament.rounds) < self.tournament.nb_of_rounds:
                # create a new round
                tournament_controller.create_round()
        else:
            tournament_view.error_all_matches_not_closed()

    def shuffle_players(self):
        """ shuffle the players """
        random.shuffle(self.tournament.players)

    def sort_players_by_score(self):
        """ sort the players by current_score """
        self.tournament.players.sort(
            key=lambda x: x.current_score, reverse=True)

    def pairing_first_round(self):
        """
        simple pairing
            player1 whith player2
            player3 whith player4 ...
        """
        list_pairing = []
        self.sort_players_by_score()
        for i in range(0, len(self.tournament.players), 2):
            player_white = self.tournament.players[i]
            player_black = self.tournament.players[i+1]
            set_of_players = [player_white, player_black]
            list_pairing.append(set_of_players)
        return list_pairing

    def check_player_already_played_together(
            self, player_white, player_black) -> bool:
        """
        If the players have already played together
            return True
        else
            return False
        :param player_white:
        :param player_black:
        :return: True or False
        """
        for a_round in self.tournament.rounds:
            for match in a_round.matches:
                if player_white in match and player_black in match:
                    return True
        return False

    def pairing_next_round(self) -> list:
        """
        Pairing the players whith controle
        that they don't already played together
        :return: a list of players
        """
        list_pairing = []
        self.sort_players_by_score()
        players_selected = []
        print('ici')
        for player_white in self.tournament.players:
            if player_white not in players_selected:
                players_selected.append(player_white)
                # looking for player black
                for player_black in self.tournament.players:
                    if player_black not in players_selected and \
                            not self.check_player_already_played_together(
                                player_white, player_black):
                        set_of_players = [player_white, player_black]
                        list_pairing.append(set_of_players)
                        players_selected.append(player_black)
                        break
        return list_pairing
