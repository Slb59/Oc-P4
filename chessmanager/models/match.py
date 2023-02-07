class Match:
    def __init__(self, no_match, player_white, player_black):
        self.no_match = no_match
        self.player_white = player_white
        self.player_black = player_black

    def __str__(self):
        return f'match {self.no_match}: {self.player_white} - {self.player_black}'
