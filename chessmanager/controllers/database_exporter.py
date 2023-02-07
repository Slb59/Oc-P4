import json

from .chessmanager_encoder import ChessManagerEncoder


class DatabaseExporter:
    """ Export players and tournaments structure in a json file """

    def __init__(self, chess_manager, filename):
        self.chess_manager = chess_manager
        self.filename = filename

    def save_database(self):
        with open(self.filename, 'w', encoding='utf8') as json_file:
            json.dump(
                self.chess_manager,
                json_file,
                cls=ChessManagerEncoder,
                indent=4,
                separators=(',', ': ')
            )


