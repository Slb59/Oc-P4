class ChessManagerView:
    def __init__(self, chess_manager):
        self.chess_manager = chess_manager

    def display_output_directory_created(self):
        print(f"Le répertoire {self.chess_manager.output_directory} est créé")

    def display_data_directory_created(self):
        print(f"Le répertoire {self.chess_manager.data_directory} est créé")

