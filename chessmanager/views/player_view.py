from datetime import datetime


class PlayerView:
    def __init__(self, a_player=None):
        self.player = a_player

    def display_player_data(self):
        print(f'Joueur {self.player.chess_id}: {self.player.last_name} {self.player.first_name}')
        print(f"Date de naissance: {datetime.strftime(self.player.birthday, '%d/%m/%Y')}")
        print(f'Niveau internationnal du joueur: {self.player.chess_level}')
