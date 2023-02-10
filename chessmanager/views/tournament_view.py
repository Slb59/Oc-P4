from .round_view import RoundView
from .player_view import PlayerView


class TournamentView:
    def __init__(self, a_tournament=None):
        self.tournament = a_tournament

    def display_tournament_data(self):
        text = f'****  TOURNOI: {self.tournament.tournament_id} {self.tournament.title} ****'
        print(len(text) * '*')
        print(text)
        print(len(text)*'*')
        print(f'Lieu : {self.tournament.area}  Du : {self.tournament.date_begin} au {self.tournament.date_end}')
        print(f'Jeu en {self.tournament.nb_of_rounds} round'
              + 's' if self.tournament.nb_of_rounds > 1 else '')
        print(len(text) * '*')
        # display the players
        print('Joueurs participants:')
        for a_player in self.tournament.players:
            a_player_view = PlayerView(a_player)
            a_player_view.display_player_data()
            print(len(text)*'-')
        # display the rounds
        for a_round in self.tournament.rounds:
            a_round_view = RoundView(a_round)
            a_round_view.display_round_data()







