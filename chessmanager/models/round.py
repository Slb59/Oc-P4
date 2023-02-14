ROUND_STARTED = 1
ROUND_CLOSED = 2
ROUND_STATES = [ROUND_STARTED, ROUND_CLOSED]


class Round:
    def __init__(self, round_id, name,
                 date_begin, time_begin,
                 date_end, time_end):
        self.round_id = round_id
        self.name = name,
        self.date_begin = date_begin
        self.time_begin = time_begin
        self.date_end = date_end
        self.time_end = time_end

        self.matches = []
        self.state = ROUND_STARTED

    def __str__(self):
        return f'{self.round_id} : {self.name}'

