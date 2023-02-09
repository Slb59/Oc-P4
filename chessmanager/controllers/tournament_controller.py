import random


class TournamentController:
    def __init__(self, a_tournament):
        self.tournament = a_tournament

    def shuffle_players(self):
        random.shuffle(self.tournament.players)

    def sort_players_by_score(self):
        self.tournament.players.sort(key=lambda x: x.current_score, reverse=True)

    def pairing_first_round(self):
        list_pairing = []
        self.sort_players_by_score()
        for i in range(0, len(self.tournament.players), 2):
            player_white = self.tournament.players[i]
            player_black = self.tournament.players[i+1]
            set_of_players = [player_white, player_black]
            list_pairing.append(set_of_players)
        return list_pairing

    def check_player_already_played_together(self, player_white, player_black):
        for a_round in self.tournament.rounds:
            for match in a_round.matches:
                if player_white in match and player_black in match:
                    return True
        return False

    def pairing_next_round(self):
        list_pairing = []
        self.sort_players_by_score()
        players_selected = []
        for player_white in self.tournament.players:
            if player_white not in players_selected:
                players_selected.append(player_white)
                # looking for player black
                for player_black in self.tournament.players:
                    if player_black not in players_selected and \
                            not self.check_player_already_played_together(player_white, player_black):
                        set_of_players = [player_white, player_black]
                        list_pairing.append(set_of_players)
                        players_selected.append(player_black)
                        break
        return list_pairing
