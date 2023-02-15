from chessmanager.views import RoundView

class RoundController:
    def __init__(self, a_round=None):
        self.round = a_round

    def check_all_score_record(self):
        """
        if there is a match with the score 0 for the two players
            return False
        else
            return True
        :return:
        """
        for match in self.round.matches:
            if match[0][1] == 0 and match[1][1] == 0:
                return False
        return True

    def record_score(self):
        """
        for each match of the round, ask the result
        then change the score
        :return:
        """
        round_view = RoundView(self.round)
        for index, match in enumerate(self.round.matches):
            result = round_view.prompt_match_result()
            if result == 1:
                match[0][1] = 1
                match[1][1] = 0
            elif result == 2:
                match[0][1] = 0
                match[1][1] = 1
            else:
                match[0][1] = 0.5
                match[1][1] = 0.5

    def record_a_score(self):
        """
        ask the index of the match
        ask the result
        then change the score
        :return:
        """
        round_view = RoundView(self.round)
        result = round_view.prompt_a_match_result()
        if result[1] == 1:
            self.round.matches[result[0]][0][1] = 1
            self.round.matches[result[0]][1][1] = 0
        elif result[1] == 2:
            self.round.matches[result[0]][0][1] = 0
            self.round.matches[result[0]][1][1] = 1
        else:
            self.round.matches[result[0]][0][1] = 0.5
            self.round.matches[result[0]][1][1] = 0.5


