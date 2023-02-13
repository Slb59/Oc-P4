import os
import json
import chessmanager

from chessmanager.views import ChessManagerView


class ChessManager:
    """ Main controller of the application """
    def __init__(self, parameters):
        self.version = chessmanager.controllers.__version__
        self.output_directory = parameters.output_directory
        self.data_directory = parameters.data_directory
        self.app_messages = ChessManagerView(self)
        self.check_directories()
        self.players = []
        self.tournaments = []

    def __str__(self):
        return "Gestionnaire de tournois d'échecs"

    def save_players(self):
        filename = self.data_directory + '/players.json'
        with open(filename, 'w', encoding='utf8') as json_file:
            json.dump(
                [o.__dict__ for o in self.players],
                json_file,
                indent=4,
                separators=(',', ': ')
            )

    def save_tournaments(self):
        filename = self.data_directory + '/tournaments.json'
        with open(filename, 'w', encoding='utf8') as json_file:
            json.dump(
                [o.to_dict() for o in self.tournaments],
                json_file,
                indent=4,
                separators=(',', ': ')
            )

    # def save_rounds(self):
    #     filename = self.data_directory + '/rounds.json'
    #     with open(filename, 'w', encoding='utf8') as json_file:
    #         json.dump(
    #             [o.to_dict() for o in ???],
    #             json_file,
    #             indent=4,
    #             separators=(',', ': ')
    #         )

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
