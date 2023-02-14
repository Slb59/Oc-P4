class RoundController:
    def __init__(self, a_round=None):
        self.round = a_round

    def check_all_score_record(self):
        for match in self.round.matches:
            if match[0][1] == 0 and match[1][1] == 0:
                return False
        return True

