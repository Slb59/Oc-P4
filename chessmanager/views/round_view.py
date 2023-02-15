import datetime
import questionary


class RoundView:
    def __init__(self, a_round=None):
        self.round = a_round
        # (new_id, name, date_begin, time_begin, date_end, time_end)

    def check_date_format(self, a_date) -> bool:
        try:
            res = bool(datetime.datetime.strptime(a_date, '%d/%m/%Y'))
        except ValueError:
            res = False
        return res

    def check_time_format(self, a_time) -> bool:
        try:
            res = bool(datetime.datetime.strptime(a_time, '%H:%M'))
        except ValueError:
            res = False
        return res

    def prompt_begin(self) -> tuple:
        a_date = questionary.text('Date de début (DD/MM/YYYY):').ask()
        while not self.check_date_format(a_date):
            print("Format de date incorrect")
            a_date = questionary.text('Date de début (DD/MM/YYYY):').ask()
        a_time = questionary.text('Heure de début (HH:MM):').ask()
        while not self.check_time_format(a_time):
            print("Format de l'heure incorrect")
            a_time = questionary.text('Heure de début (HH:MM):').ask()

    def prompt_end(self):
        a_date = questionary.text('Date de fin (DD/MM/YYYY):').ask()
        while not self.check_date_format(a_date):
            print("Format de date incorrect")
            a_date = questionary.text('Date de fin (DD/MM/YYYY):').ask()
        a_time = questionary.text('Heure de fin (HH:MM):').ask()
        while not self.check_time_format(a_time):
            print("Format de l'heure incorrect")
            a_time = questionary.text('Heure de fin (HH:MM):').ask()

    def display_round_data(self):
        pos_to_align = 50
        len_for_players = 25
        print(f'{self.round.name} du {self.round.date_begin} {self.round.time_begin}'
              f' au {self.round.date_end} {self.round.time_end}')
        for i, match in enumerate(self.round.matches):
            text_match = f'Match {i+1}'
            nb_of_space = len_for_players-len(str(match[0][0]))
            text_white = str(match[0][0]) + nb_of_space*' ' + '|' + f' score:{match[0][1]}'
            text_black = f' | {match[1][0]}, score:{match[1][1]}'
            print(text_match + ' | ' + text_white + (pos_to_align-len(text_white))*' ' + text_black)
