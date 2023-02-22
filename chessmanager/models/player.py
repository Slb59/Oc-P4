import datetime

class Player:
    """ Manage the datas of a chess player """
    def __init__(self, chess_id, last_name, first_name, birthday, chess_level, current_score=0):
        self.chess_id = chess_id
        self.last_name = last_name
        self.first_name = first_name
        self.birthday = datetime.datetime.strptime(birthday, '%d/%m/%Y')
        self.chess_level = chess_level
        self.current_score = current_score

    def __str__(self):
        return f'{self.last_name} {self.first_name}'

    def __eq__(self, other):
        """ check if too players are equals : the chess_id is equal """
        if isinstance(other, Player):
            return self.chess_id == other.chess_id
        else:
            return False

    def to_dict(self):
        a_dict = {
            "chess_id": self.chess_id,
            "last_name": self.last_name,
            "first_name": self.first_name,
            "birthday": datetime.datetime.strftime(self.birthday, '%d/%m/%Y'),
            "chess_level": self.chess_level,
            "current_score": self.current_score
        }
        return a_dict






