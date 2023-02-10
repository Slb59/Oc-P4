class RoundView:
    def __init__(self, a_round=None):
        self.round = a_round
        # (new_id, name, date_begin, time_begin, date_end, time_end)

    def prompt_date_begin(self):
        pass

    def prompt_time_begin(self):
        pass

    def prompt_date_end(self):
        pass

    def prompt_time_end(self):
        pass

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
