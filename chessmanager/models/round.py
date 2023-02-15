ROUND_STARTED = 1
ROUND_CLOSED = 2
ROUND_STATES = [ROUND_STARTED, ROUND_CLOSED]


class Round:
    def __init__(self, round_id, name,
                 date_begin, time_begin,
                 date_end='', time_end='', state=ROUND_STARTED):
        self.round_id = round_id
        self.name = name,
        self.date_begin = date_begin
        self.time_begin = time_begin
        self.date_end = date_end
        self.time_end = time_end

        self.matches = []
        self.state = state

    def __str__(self):
        return f'{self.round_id} : {self.name}'

    def to_dict(self) -> dict:
        list_of_matches = []
        for match in self.matches:
            list_of_matches.append(
                ([match[0][0].__dict__, match[0][1]],
                 [match[1][0].__dict__, match[1][1]])
            )

        a_dict = {
            "round_id": self.round_id,
            "name": self.name,
            "date_begin": self.date_begin,
            "time_begin": self.time_begin,
            "date_end": self.date_end,
            "time_end": self.time_end,
            "state": self.state,
            "matches": list_of_matches
        }
        return a_dict
