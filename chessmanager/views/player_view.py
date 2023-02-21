import questionary
import re

from datetime import datetime
from .check import check_date_format


def prompt_player_id(self) -> str:
    chess_id = questionary.text(
        "Identifiant national d'échecs:",
        validate=lambda text: True if re.match(r"[A-Z][A-Z]\d\d\d\d\d", text)
        else "L'identifiant doit contenir 2 lettres et 5 chiffres"
    ).ask()
    return chess_id


def prompt_player_data(self) -> tuple:
    first_name = questionary.text("Nom:").ask()
    last_name = questionary.text("Prénom:").ask()
    birthday = questionary.text(
        "Date de naissance (dd/mm/yyyy):",
        validate=lambda text: True if check_date_format(text)
        else "Format de date incorrect : dd/mm/yyyy"
    ).ask()
    chess_level = questionary.text(
        "Points ELO:",
        validate=lambda text: True if len(text) > 0 and (1000 <= int(text) <= 3000)
        else "Les points ELO se situe entre 1000 et 3000"
    ).ask()
    return first_name, last_name, birthday, chess_level

class PlayerView:
    """
    Manage display for player
    """
    def __init__(self, a_player=None):
        self.player = a_player

    def display_player_data(self):
        print(f'Joueur {self.player.chess_id}: {self.player.last_name} {self.player.first_name}')
        print(f"Date de naissance: {datetime.strftime(self.player.birthday, '%d/%m/%Y')}")
        print(f'Niveau internationnal du joueur: {self.player.chess_level}')


