TOURNAMENT_NOT_STARTED = 0
TOURNAMENT_STARTED = 1
TOURNAMENT_CLOSED = 2
STATES = [TOURNAMENT_NOT_STARTED, TOURNAMENT_STARTED, TOURNAMENT_CLOSED]


class Tournament:
    def __init__(self, new_id, title, description, area, date_begin, date_end, nb_of_rounds=4):

        self._tournament_id = new_id
        self.title = title
        self.description = description
        self.area = area
        self.date_begin = date_begin
        self.date_end = date_end
        self.nb_of_rounds = nb_of_rounds

        self.rounds = []
        self.players = []
        self.state = TOURNAMENT_NOT_STARTED

    def __str__(self):
        return f'{self._tournament_id} : {self.title}'

    def __eq__(self, other):
        if isinstance(other, Tournament):
            return self._tournament_id == other._tournament_id
        else:
            return False
    @property
    def tournament_id(self):
        return self._tournament_id

