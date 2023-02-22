from datetime import datetime

from logs import LOGGER

ROUND_STARTED = 1
ROUND_CLOSED = 2
ROUND_STATES = [ROUND_STARTED, ROUND_CLOSED]


class Round:
    """
    Manage the data of a round
    """
    def __init__(self, round_id, name,
                 date_begin, time_begin,
                 date_end='', time_end='', state=ROUND_STARTED):
        self.round_id = round_id
        self.name = name
        self.date_begin = datetime.strptime(date_begin, '%d/%m/%Y')
        self.time_begin = datetime.strptime(time_begin, '%H:%M')
        self.date_end = \
            datetime.strptime(date_end, '%d/%m/%Y') if date_end else ''
        self.time_end = datetime.strptime(
            time_end, '%H:%M') if time_end else ''

        self.matches = []
        self.state = state

    def __str__(self):
        return f'{self.round_id} : {self.name}'

    def to_dict(self) -> dict:
        LOGGER.debug(" round to dict : " + self.name)
        list_of_matches = []
        for match in self.matches:
            list_of_matches.append(
                ([match[0][0].to_dict(), match[0][1]],
                 [match[1][0].to_dict(), match[1][1]])
            )

        a_dict = {
            "round_id": self.round_id,
            "name": self.name,
            "date_begin": datetime.strftime(self.date_begin, '%d/%m/%Y'),
            "time_begin": datetime.strftime(self.time_begin, '%H:%M'),
            "date_end": datetime.strftime(
                self.date_end, '%d/%m/%Y') if self.date_end else '',
            "time_end": datetime.strftime(
                self.time_end, '%H:%M') if self.time_end else '',
            "state": self.state,
            "matches": list_of_matches
        }
        return a_dict
