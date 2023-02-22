import questionary

from datetime import datetime

from .round_view import RoundView
from .player_view import PlayerView
from chessmanager.models.tournament import TOURNAMENT_CLOSED
from chessmanager.models.tournament import TOURNAMENT_STARTED
from .check import check_date_format


def prompt_tournament_id(self) -> int:
    """ ask tournament id """
    tournament_id = questionary.text('Saisissez le numéro du tournoi:').ask()
    return int(tournament_id)


def prompt_tournament_data(self) -> tuple:
    """ ask tournament data """
    title = questionary.text("Titre du tournoi:").ask()
    description = questionary.text("Description du tournoi:").ask()
    area = questionary.text("Lieu:").ask()
    dates_ok = False
    date_begin = ''
    date_end = ''
    while not dates_ok:
        date_begin = questionary.text(
            "Date de début (dd/mm/yyyy):",
            validate=lambda text: True if check_date_format(text)
            else "Format de date incorrect : dd/mm/yyyy"
        ).ask()

        date_end = questionary.text(
            "Date de fin (dd/mm/yyyy):",
            validate=lambda text: True if check_date_format(text)
            else "Format de date incorrect : dd/mm/yyyy"
        ).ask()

        if datetime.strptime(date_begin, '%d/%m/%Y') \
                < datetime.strptime(date_end, '%d/%m/%Y'):
            dates_ok = True
        else:
            print("Erreur dans la saisie des dates")

    return title, description, area, date_begin, date_end


class TournamentView:
    """
    Display data and errors about tournament
    """
    def __init__(self, a_tournament=None):
        self.tournament = a_tournament

    def prompt_round_id(self):
        round_id = input('Saisissez le numéro du round:')
        return int(round_id)

    def display_winner(self):
        print('Le gagnant du tournoi est: ' + str(self.tournament.winner))

    def display_tournament_title(self):
        text = f'TOURNOI: {str(self.tournament)}'
        if self.tournament.state == TOURNAMENT_CLOSED:
            text += ' - Terminé'
            self.display_winner()
        elif self.tournament.state == TOURNAMENT_STARTED:
            text += ' - En cours de jeu'
        else:
            text += ' - Non commencé'
        print(text)

    def display_tournament_resume(self):
        text = f'****  TOURNOI: {str(self.tournament)} ****'
        print(len(text) * '*')
        print(text)
        print(len(text) * '*')
        print(f'Lieu : {self.tournament.area}  '
              f'Du : {self.tournament.date_begin} '
              f'au {self.tournament.date_end}')
        print(f'Jeu en {self.tournament.nb_of_rounds} round'
              + 's' if self.tournament.nb_of_rounds > 1 else '')
        print(len(text) * '*')
        if self.tournament.state == TOURNAMENT_CLOSED:
            print('Le tournoi est terminé')
            self.display_winner()
        elif self.tournament.state == TOURNAMENT_STARTED:
            print("Tournoi en cours de jeu")
        else:
            print("Tournoi non commencé")

    def display_tournament_data(self):
        self.display_tournament_resume()
        if not self.tournament.state == TOURNAMENT_CLOSED:

            # display the players
            print('Joueurs participants:')
            for a_player in self.tournament.players:
                a_player_view = PlayerView(a_player)
                a_player_view.display_player_data()
                print(60*'-')
            # display the rounds
            for a_round in self.tournament.rounds:
                a_round_view = RoundView(a_round)
                a_round_view.display_round_data()

    def error_tournament_not_started(self):
        print("!! Ce tournoi n'a pas démarré")

    def error_tournament_started(self):
        print("!! Ce tournoi est déjà en cours")

    def error_tournament_closed(self):
        print("!! Ce tournoi est terminé")

    def error_round_not_exist(self):
        print("!!! Ce round n'existe pas.")

    def error_all_matches_not_closed(self):
        print("!!! Les scores des matches ne sont pas tous enregistrés.")
