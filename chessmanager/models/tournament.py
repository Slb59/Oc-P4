TOURNAMENT_NOT_STARTED = 0
TOURNAMENT_STARTED = 1
TOURNAMENT_CLOSED = 2
STATES = [TOURNAMENT_NOT_STARTED, TOURNAMENT_STARTED, TOURNAMENT_CLOSED]
MAX_NUMBER_OF_PLAYERS = 8


class Tournament:
    def __init__(self, tournament_id,
                 title,
                 description,
                 area,
                 date_begin,
                 date_end, nb_of_rounds=4, state=TOURNAMENT_NOT_STARTED):

        self.tournament_id = tournament_id
        self.title = title
        self.description = description
        self.area = area
        self.date_begin = date_begin
        self.date_end = date_end
        self.nb_of_rounds = nb_of_rounds
        self.state = state
        self.winner = ''

        self.rounds = []  # list of the round (max length : nb_of_rounds)
        self.players = []  # list of the players selected for the tournament

    def __str__(self):
        return f'{self.tournament_id} : {self.title}'

    def __eq__(self, other):
        """ check if 2 tournament are equal : the tournament_id are equal """
        if isinstance(other, Tournament):
            return self.tournament_id == other.tournament_id
        else:
            return False

    def to_dict(self):
        """ give the class tournament in a dictoniary format for json save """
        list_of_players = []
        for a_player in self.players:
            a_player_dict = a_player.__dict__
            list_of_players.append(a_player_dict)
        list_of_rounds = []
        for a_round in self.rounds:
            a_round_dict = a_round.to_dict()
            list_of_rounds.append(a_round_dict)
        a_dict = {
            "tournament_id": self.tournament_id,
            "title": self.title,
            "description": self.description,
            "area": self.area,
            "date_begin": self.date_begin,
            "date_end": self.date_end,
            "nb_of_rounds": self.nb_of_rounds,
            "state": self.state,
            "players": list_of_players,
            "rounds": list_of_rounds
        }
        return a_dict



