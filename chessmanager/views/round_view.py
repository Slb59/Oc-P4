import questionary

from datetime import datetime
from chessmanager.models import ROUND_CLOSED
from .check import check_date_format, check_time_format


class RoundView:
    """
    Manage promt, display and errors for a round
    """
    def __init__(self, a_round=None):
        self.round = a_round

    def prompt_begin(self) -> tuple:
        a_date = questionary.text(
            'Date de début (DD/MM/YYYY):',
            validate=lambda text: True if check_date_format(text)
            else "Format de date incorrect : dd/mm/yyyy"
        ).ask()

        a_time = questionary.text(
            'Heure de début (HH:MM):',
            validate=lambda text: True if check_time_format(text)
            else "Format de l'heure incorrect : HH:MM"
        ).ask()

        return a_date, a_time

    def prompt_end(self) -> tuple:
        a_date = questionary.text(
            'Date de fin (DD/MM/YYYY):',
            validate=lambda text: True if check_date_format(text)
            else "Format de date incorrect : dd/mm/yyyy"
        ).ask()

        a_time = questionary.text(
            'Heure de fin (HH:MM):',
            validate=lambda text: True if check_time_format(text)
            else "Format de l'heure incorrect : HH:MM"
        ).ask()

        return a_date, a_time

    def prompt_match_result(self, index) -> int:
        print('Saisir 1 si le joueur de gauche gagne, '
              'saisir 2 si le joueur de droite gagne, 0 sinon')
        result = questionary.text(
            f'Résultat du match {index+1}:',
            validate=lambda text:
            True if len(text) > 0 and int(text) in [0, 1, 2]
            else 'Veuillez saisir 0, 1 ou 2 selon le résultat du match'
        ).ask()

        return int(result)

    def prompt_a_match_result(self) -> tuple:

        index = questionary.text(
            "Numéro du match (1 à 4)",
            validate=lambda text:
            True if len(text) > 0 and int(text) in [1, 2, 3, 4]
            else 'Saisir une valeur entre 1 et 4'
        ).ask()

        print('Résultats:  0 - Egalité, '
              '1: Le premier joueur gagne, '
              '2: Le deuxième joueur gagne')
        result = questionary.text(
            f'Résultat du match {index}:',
            validate=lambda text:
            True if len(text) > 0 and int(text) in [0, 1, 2]
            else 'Veuillez saisir 0, 1 ou 2 selon le résultat du match'
        ).ask()

        return int(index)-1, int(result)

    def display_create_a_round(self):
        print("un nouveau round commence !!")

    def display_round_data(self):
        pos_to_align = 50
        len_for_players = 25
        text = f'{self.round.name} du '
        text += f"{datetime.strftime(self.round.date_begin, '%d/%m/%Y')}"
        text += f" {datetime.strftime(self.round.time_begin, '%H:%M')}"
        text += ' au '
        if self.round.date_end:
            text += f"{datetime.strftime(self.round.date_end, '%d/%m/%Y')}"
            text += f" {datetime.strftime(self.round.time_end, '%H:%M')}"
        print(text)
        if self.round.state == ROUND_CLOSED:
            print('ROUND TERMINE')
        for i, match in enumerate(self.round.matches):
            text_match = f'Match {i+1}'
            nb_of_space = len_for_players - len(str(match[0][0]))
            text_white = \
                str(match[0][0]) \
                + nb_of_space*' ' \
                + '|' + f' score:{match[0][1]}'
            nb_of_space = len_for_players - len(str(match[1][0]))
            text_black = f' | {match[1][0]}' + \
                         nb_of_space*' ' + '|' + \
                         f' score:{match[1][1]}'
            print(text_match + ' | ' + text_white
                  + (pos_to_align-len(text_white))*' ' + text_black)

    def error_round_closed(self):
        print('!!! Ce round est terminé')
