class Club:
    def __init__(self, players=None, tournaments=None):
        if players is None:
            players = []
        if tournaments is None:
            tournaments = []
        self.players = players
        self.tournaments = tournaments

    def __str__(self):
        return f'{len(self.players)} joueurs - {len(self.tournaments)} tournois'
