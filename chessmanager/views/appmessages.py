class AppMessages:
    def __init__(self, chessmanager):
        self.chessmanager = chessmanager

    def display_output_directory_created(self):
        print(f"Le répertoire {self.chessmanager.output_directory} est créé")

    def display_data_directory_created(self):
        print(f"Le répertoire {self.chessmanager.data_directory} est créé")