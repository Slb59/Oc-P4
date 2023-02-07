import os
import chessmanager

from chessmanager.views import AppMessages


class ChessManager:
    """ Main controller of the application """
    def __init__(self, parameters):
        self.version = chessmanager.controllers.__version__
        self.output_directory = parameters.output_directory
        self.data_directory = parameters.data_directory
        self.app_messages = AppMessages(self)
        self.check_directories()
        self.players = []
        self.tournaments = []

    def __str__(self):
        return "Gestionnaire de tournois d'échecs"

    def check_directories(self):
        """ create the directories output and data if not exists """
        if not os.path.exists(self.output_directory):
            os.makedirs(self.output_directory)
            self.app_messages.display_output_directory_created()
        if not os.path.exists(self.data_directory):
            os.makedirs(self.data_directory)
            self.app_messages.display_data_directory_created()

    def load_database(self):
        """ load the database json file """
        pass

    def run(self):
        """ run the application """
        pass
