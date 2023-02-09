import random


class TournamentController:
    def __init__(self, a_tournament):
        self.tournament = a_tournament

    def shuffle_players(self):
        random.shuffle(self.tournament.players)

    def sort_players_by_score(self):
        self.tournament.players.sort(key=lambda x: x.current_score, reverse=True)

    def pairing(self):
        list_pairing = []
        for i in range(0, len(self.tournament.players), 2):
            player_white = self.tournament.players[i]
            player_black = self.tournament.players[i+1]
            set_of_players = [player_white, player_black]
            list_pairing.append(set_of_players)
        return list_pairing
