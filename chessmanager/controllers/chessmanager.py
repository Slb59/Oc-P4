import os
import json
import chessmanager

from chessmanager.models import Player
from chessmanager.models import Tournament
from chessmanager.models import Round

from chessmanager.views import ChessManagerView
from chessmanager.views import TournamentView
from chessmanager.views import DatabaseView

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
        database_view = DatabaseView(filename)
        try:
            with open(filename, encoding='utf8') as f:
                data = json.load(f)
            for elem in data:
                player = Player(**elem)
                self.players.append(player)
            database_view.display_database_loaded()
        except FileNotFoundError:
            database_view.display_database_not_found()


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
        database_view = DatabaseView(filename)
        try:
            with open(filename, encoding='utf8') as f:
                data = json.load(f)
            for elem in data:
                tournament = Tournament(elem['tournament_id'], elem['title'], elem['description'],
                                        elem['area'], elem['date_begin'], elem['date_end'],
                                        elem['nb_of_rounds'], elem['state'])
                for player in elem['players']:
                    new_player = Player(**player)
                    tournament.players.append(new_player)
                for a_round in elem['rounds']:
                    new_round = Round(a_round['round_id'], a_round['name'], a_round['date_begin'],
                                      a_round['time_begin'], a_round['date_end'], a_round['time_end'])
                    new_round.matches = a_round['matches']

                    tournament.rounds.append(new_round)

                self.tournaments.append(tournament)
            database_view.display_database_loaded()
        except FileNotFoundError:
            database_view.display_database_not_found()

    def get_tournament(self, tournament_id):
        """ return a tournament if tournament_id is in tournaments list
        else return None """
        for t in self.tournaments:
            if tournament_id == t.tournament_id:
                return t
        return None

    def get_player(self, chess_id):
        """ return a player if chess_id is in players list
        else return None
        """
        for p in self.players:
            if chess_id == p.chess_id:
                return p
        return None

    def close_round(self):
        """ ask the tournament id and the round id
        if all the scores are recorded, close the round
        close the tournament if all the rounds are closed
        """
        a_chessmanager_view = ChessManagerView(self)

        # prompt id tournament
        tournament_id = a_chessmanager_view.prompt_tournament_id()

        tournament = self.get_tournament(tournament_id)

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

        # create view managers
        chess_manager_view = ChessManagerView(self)
        chess_manager_view.display_welcome()

        # load database
        self.load_players()
        self.load_tournaments()
        print('')

        running = True

        while running:
            answer = chess_manager_view.display_main_menu()

            # quit
            if answer == chess_manager_view.main_menu_choices()[7]:
                running = False

            # add a player
            elif answer == chess_manager_view.main_menu_choices()[0]:
                chess_id = chess_manager_view.prompt_player_id()
                player = self.get_player(chess_id)

                if player is None:
                    player_data = chess_manager_view.prompt_player_data()
                    player = Player(chess_id, player_data[0], player_data[1],
                                    player_data[2], player_data[3])
                    self.players.append(player)
                else:
                    chess_manager_view.error_player_already_exists()

                # save players database
                self.save_players()

            # modify a player
            elif answer == chess_manager_view.main_menu_choices()[1]:
                pass

            # create a tournament
            elif answer == chess_manager_view.main_menu_choices()[2]:
                pass

            #  start a tournament
            elif answer == chess_manager_view.main_menu_choices()[3]:
                pass

            # record the results
            elif answer == chess_manager_view.main_menu_choices()[4]:
                pass

            # end a round
            elif answer == chess_manager_view.main_menu_choices()[5]:
                pass

            # generate reports
            elif answer == chess_manager_view.main_menu_choices()[5]:
                pass

