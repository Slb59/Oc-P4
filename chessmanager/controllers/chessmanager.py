import os
from datetime import datetime
from logs import LOGGER

from chessmanager.models import Player
from chessmanager.models import Tournament
from chessmanager.models import TOURNAMENT_CLOSED
from chessmanager.models import TOURNAMENT_NOT_STARTED
from chessmanager.models import MAX_NUMBER_OF_PLAYERS

from chessmanager.views import ChessManagerView
from chessmanager.views import TournamentView
from chessmanager.views import prompt_tournament_id
from chessmanager.views import prompt_tournament_data
from chessmanager.views import prompt_player_id
from chessmanager.views import prompt_player_data

from .tournament_controller import TournamentController
from .reports import ChessManagerReports
from .database import ChessManagerDatabase


class ChessManager:
    """ Main controller of the application """
    def __init__(self, parameters):
        self.output_directory = parameters.output_directory
        self.data_directory = parameters.data_directory
        self.app_messages = ChessManagerView(self)
        self.check_directories()
        self.players = []  # list of all the players of the club
        self.tournaments = []  # list of the tournaments organized by the club

    def __str__(self):
        return "Gestionnaire de tournois d'échecs"

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
        """
        - ask a tournament id
        - close a round
        - save the database
        :return:
        """
        chess_manager_view = ChessManagerView(self)
        chess_manager_view.display_all_tournaments()

        # prompt id tournament
        tournament_id = prompt_tournament_id(self)
        tournament = self.get_tournament(tournament_id)
        tournament_view = TournamentView(tournament)
        if tournament is None:
            chess_manager_view.error_tournament_not_found()
        elif tournament.state == TOURNAMENT_CLOSED:
            tournament_view.error_tournament_closed()
        elif tournament.state == TOURNAMENT_NOT_STARTED:
            tournament_view.error_tournament_not_started()
        else:
            tournament_controller = TournamentController(tournament)
            tournament_controller.close_round()
        database = ChessManagerDatabase(self)
        database.save_tournaments()

    def check_directories(self):
        """ create the directories output and data if not exists """
        if not os.path.exists(self.output_directory):
            os.makedirs(self.output_directory)
            self.app_messages.display_output_directory_created()
        if not os.path.exists(self.data_directory):
            os.makedirs(self.data_directory)
            self.app_messages.display_data_directory_created()

    def add_player(self):
        """
        - ask a chess_id
        if chess_id not in database :
            ask the data of the player
            save database
        else
            prompt an error
        """
        chess_manager_view = ChessManagerView(self)
        chess_id = prompt_player_id(self)
        player = self.get_player(chess_id)

        if player is None:
            player_data = prompt_player_data(self)
            player = Player(chess_id, player_data[1], player_data[0],
                            player_data[2], player_data[3])
            self.players.append(player)

            # save players database
            database = ChessManagerDatabase(self)
            database.save_players()
        else:
            chess_manager_view.error_player_already_exists()

    def modify_player(self):
        """
        - display all players
        - ask the chess_id to modify
        - ask the new data of the player
        - save database
        """
        chess_manager_view = ChessManagerView(self)
        # display the list of players
        chess_manager_view.display_all_players()
        # prompt the chess id
        chess_id = prompt_player_id(self)
        player = self.get_player(chess_id)
        if player is None:
            chess_manager_view.error_player_not_exist()
        else:
            player_data = prompt_player_data(self)
            player.last_name = player_data[1]
            player.first_name = player_data[0]
            player.birthday = datetime.strptime(player_data[2], '%d/%m/%Y')
            player.chess_level = player_data[3]

            # save players database
            database = ChessManagerDatabase(self)
            database.save_players()

    def create_tournament(self):
        """
        - ask the tournament data
        - display the players that can be selected
        - ask the selection of the 8 (MAX_NUMBER_OF_PLAYER) players
        - create the tournament object
        - save database
        :return: None
        """
        chess_manager_view = ChessManagerView(self)

        # ask the data of the tournament
        tournament_data = prompt_tournament_data(self)

        # display the list of players
        chess_manager_view.display_all_players()

        # ask players selection
        chess_manager_view.display_players_selection()
        players = []
        players_id = []
        while len(players) < MAX_NUMBER_OF_PLAYERS:
            chess_id = prompt_player_id(self)
            player = self.get_player(chess_id)
            if player is None:
                chess_manager_view.error_player_not_exist()
            elif player in players:
                chess_manager_view.error_player_already_selected()
            else:
                players.append(player)
                players_id.append(chess_id)
            print(f'selection : {players_id}')

        # save the tournament
        tournament_id = len(self.tournaments) + 1
        a_tournament = Tournament(tournament_id, tournament_data[0],
                                  tournament_data[1], tournament_data[2],
                                  tournament_data[3], tournament_data[4])
        a_tournament.players = players
        self.tournaments.append(a_tournament)
        database = ChessManagerDatabase(self)
        database.save_tournaments()

    def call_start_tournament(self):
        """
        - display the tournaments
        - ask the id of the tournament to start
        - create the first round of the tournament
        """
        chess_manager_view = ChessManagerView(self)
        # display the tournaments
        chess_manager_view.display_all_tournaments()
        tournament_id = prompt_tournament_id(self)
        a_tournament = self.get_tournament(tournament_id)
        tournament_controller = TournamentController(a_tournament)
        if tournament_controller.start_tournament():
            database = ChessManagerDatabase(self)
            database.save_tournaments()

    def record_a_match(self):
        """
        - display the tournaments
        - ask the id of the tournament to record
        - record the scores
        - save database
        :return:
        """
        chess_manager_view = ChessManagerView(self)
        # display the tournaments
        chess_manager_view.display_all_tournaments()
        tournament_id = prompt_tournament_id(self)
        a_tournament = self.get_tournament(tournament_id)
        tournament_view = TournamentView(a_tournament)
        if a_tournament is None:
            chess_manager_view.error_tournament_not_found()
        elif a_tournament.state == TOURNAMENT_CLOSED:
            tournament_view.error_tournament_closed()
        elif a_tournament.state == TOURNAMENT_NOT_STARTED:
            tournament_view.error_tournament_not_started()
        else:
            tournament_view.display_tournament_data()
            tournament_controller = TournamentController(a_tournament)
            tournament_controller.record_score()
            tournament_view.display_tournament_data()
            database = ChessManagerDatabase(self)
            database.save_tournaments()

    def ask_tournament_id(self):
        """
        ask a tournament id
        :return:  a_tournament, None if not found
        """

        chess_manager_view = ChessManagerView(self)
        chess_manager_view.display_all_tournaments()
        # prompt id tournament
        tournament_id = prompt_tournament_id(self)
        tournament = self.get_tournament(tournament_id)
        if tournament is None:
            chess_manager_view.error_tournament_not_found()
        else:
            return tournament

    def generate_reports(self):
        """
        Display the reports menu
        then launch the html page corresponding
        :return:
        """
        chess_manager_view = ChessManagerView(self)
        chess_manager_reports = ChessManagerReports(self)
        running = True

        while running:
            answer = chess_manager_view.display_reports_menu()
            if answer == chess_manager_view.report_menu_choices()[5]:
                running = False
            # List of players in alphabetic order
            elif answer == chess_manager_view.report_menu_choices()[0]:
                chess_manager_reports.all_players_in_alphabetic_order()
            # List of all the tournaments
            elif answer == chess_manager_view.report_menu_choices()[1]:
                chess_manager_reports.all_tournaments()
            # Name and date of a tournament
            elif answer == chess_manager_view.report_menu_choices()[2]:
                tournament = self.ask_tournament_id()
                chess_manager_reports.generate_tournament_data(tournament)
            # List of players of a tournament in alphabetic order
            elif answer == chess_manager_view.report_menu_choices()[3]:
                tournament = self.ask_tournament_id()
                chess_manager_reports.generate_tournament_players(tournament)
            # List all the rounds of a tournament and all the matches
            elif answer == chess_manager_view.report_menu_choices()[4]:
                tournament = self.ask_tournament_id()
                chess_manager_reports.tournaments_details(tournament)

    def run(self):
        """ run the application """

        # create view managers
        chess_manager_view = ChessManagerView(self)
        chess_manager_view.display_welcome()

        # load database
        database = ChessManagerDatabase(self)
        database.load_players()
        database.load_tournaments()
        chess_manager_view.display_chess_data()

        running = True

        while running:
            answer = chess_manager_view.display_main_menu()
            LOGGER.debug("main menu choice " + answer)
            confirm = chess_manager_view.prompt_are_you_sure()
            if confirm == 'Y':

                # quit
                if answer == chess_manager_view.main_menu_choices()[7]:
                    running = False

                # add a player
                elif answer == chess_manager_view.main_menu_choices()[0]:
                    self.add_player()

                # modify a player
                elif answer == chess_manager_view.main_menu_choices()[1]:
                    self.modify_player()

                # create a tournament
                elif answer == chess_manager_view.main_menu_choices()[2]:
                    # check the number of players in the database
                    if len(self.players) < MAX_NUMBER_OF_PLAYERS:
                        chess_manager_view.error_not_enough_players()
                        continue
                    else:
                        self.create_tournament()

                #  start a tournament
                elif answer == chess_manager_view.main_menu_choices()[3]:
                    self.call_start_tournament()

                # record the results
                elif answer == chess_manager_view.main_menu_choices()[4]:
                    self.record_a_match()

                # end a round
                elif answer == chess_manager_view.main_menu_choices()[5]:
                    self.close_round()

                # generate reports
                elif answer == chess_manager_view.main_menu_choices()[6]:
                    self.generate_reports()
        LOGGER.debug("Quit program")
