class Player:
    def __init__(self, chess_id, last_name, first_name, birthday, chess_level):
        self.chess_id = chess_id
        self.last_name = last_name
        self.first_name = first_name
        self.birthday = birthday
        self.chess_level = chess_level
        self.current_score = 0

    def __str__(self):
        return f'{self.last_name} {self.first_name}'

    def __eq__(self, other):
        if isinstance(other, Player):
            return self.chess_id == other.chess_id
        else:
            return False

