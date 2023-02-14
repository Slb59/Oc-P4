import os
import json
import chessmanager

from chessmanager.models import Player
from chessmanager.models import Tournament

from chessmanager.views import ChessManagerView
from chessmanager.views import TournamentView

from .tournament_controller import TournamentController
from .round_controller import RoundController
from ..models.round import ROUND_CLOSED


class ChessManager:
    """ Main controller of the application """
    def __init__(self, parameters):
        self.version = chessmanager.controllers.__version__
        self.output_directory = parameters.output_directory
        self.data_directory = parameters.data_directory
        self.app_messages = ChessManagerView(self)
        self.check_directories()
        self.players = []  # list of all the players of the club
        self.tournaments = []  # list of the tournaments organized by the club

    def __str__(self):
        return "Gestionnaire de tournois d'échecs"

    def save_players(self):
        """ save the list of players in players.json file """
        filename = self.data_directory + '/players.json'
        with open(filename, 'w', encoding='utf8') as json_file:
            json.dump(
                [o.__dict__ for o in self.players],
                json_file,
                indent=4,
                separators=(',', ': ')
            )

    def load_players(self):
        filename = self.data_directory + '/players.json'
        f = open(filename)
        data = json.load(f)
        for elem in data:
            player = Player(**elem)
            self.players.append(player)

    def save_tournaments(self):
        filename = self.data_directory + '/tournaments.json'
        with open(filename, 'w', encoding='utf8') as json_file:
            json.dump(
                [o.to_dict() for o in self.tournaments],
                json_file,
                indent=4,
                separators=(',', ': ')
            )

    def load_tournaments(self):
        filename = self.data_directory + '/tournaments.json'
        f = open(filename)
        data = json.load(f)
        for elem in data:
            print(elem)
            tournament = Tournament(**elem)
            self.tournaments.append(tournament)


    # def save_rounds(self):
    #     filename = self.data_directory + '/rounds.json'
    #     with open(filename, 'w', encoding='utf8') as json_file:
    #         json.dump(
    #             [o.to_dict() for o in ???],
    #             json_file,
    #             indent=4,
    #             separators=(',', ': ')
    #         )

    def check_tournament_id_exists(self, tournament_id):

        for t in self.tournaments:
            print(t.tournament_id)
            print(t.title)
            if tournament_id == t.tournament_id:
                return t
        return None

    def close_round(self):
        a_chessmanager_view = ChessManagerView(self)

        # prompt id tournament
        tournament_id = a_chessmanager_view.prompt_tournament_id()

        tournament = self.check_tournament_id_exists(tournament_id)

        print(tournament)
        # TODO : if tournament is None:
        #     print('Ce tournoi n''existe pas !')

        tournament_view = TournamentView(tournament)
        tournament_view.display_tournament_data()

        round_id = tournament_view.prompt_round_id()
        tournament_controller = TournamentController(tournament)
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

    def check_directories(self):
        """ create the directories output and data if not exists """
        if not os.path.exists(self.output_directory):
            os.makedirs(self.output_directory)
            self.app_messages.display_output_directory_created()
        if not os.path.exists(self.data_directory):
            os.makedirs(self.data_directory)
            self.app_messages.display_data_directory_created()

    def run(self):
        """ run the application """
        pass
