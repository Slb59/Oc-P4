class PlayerView:
    def __init__(self, a_player=None):
        self.player = a_player

    def display_player_data(self):
        print(f'Joueur {self.player.chess_id}: {self.player.last_name} {self.player.first_name}')
        print(f'Date de naissance: {self.player.birthday}')
        print(f'Niveau internationnal du joueur: {self.player.chess_level}')
