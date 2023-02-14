import questionary
import re
import datetime

class ChessManagerView:
    def __init__(self, chess_manager):
        self.chess_manager = chess_manager

    def display_output_directory_created(self):
        print(f"Le répertoire {self.chess_manager.output_directory} est créé")

    def display_data_directory_created(self):
        print(f"Le répertoire {self.chess_manager.data_directory} est créé")

    def prompt_tournament_id(self):
        tournament_id = input('Saisissez le numéro du tournoi:')
        return int(tournament_id)

    def display_welcome(self):
        text = "  Bienvenue dans le manager de tournois d'échecs"
        print(len(text) * '-')
        print(text)
        print(len(text) * '-')
        print('')

    def main_menu_choices(self) -> list:
        return [
                "Ajouter un joueur",
                "Modifier les informations d'un joueur",
                "Créer un tournoi",
                "Démarrer un tournoi",
                "Enregistrer les résultats d'un match",
                "Terminer un round",
                "Générer les rapports",
                "Quitter le programme"
            ]

    def display_main_menu(self):
        print('')
        print(50 * '-')
        answer = questionary.select(
            "Que souhaitez-vous faire ?",
            choices=self.main_menu_choices()
        ).ask()
        return answer

    def prompt_player_id(self) -> str:
        print(" - Ajout d'un nouveau joueur -")
        chess_id = questionary.text("Identifiant national d'échecs:").ask()
        while not re.match(r"[A-Z][A-Z]\d\d\d\d\d", chess_id ):
            print("L'identifiant doit contenir 2 lettres et 5 chiffres")
            chess_id = questionary.text("Identifiant national d'échecs:").ask()
        return chess_id

    def check_date_format(self, a_date) -> bool:
        try:
            res = bool(datetime.datetime.strptime(a_date, '%d/%m/%Y'))
        except ValueError:
            res = False
        return res
    def prompt_player_data(self) -> tuple:
        first_name = questionary.text("Nom:").ask()
        last_name = questionary.text("Prénom:").ask()
        birthday = questionary.text("Date de naissance (dd/mm/yyyy):").ask()
        while not self.check_date_format(birthday):
            print("Format de date incorrect")
            birthday = questionary.text("Date de naissance (dd/mm/yyyy):").ask()
        chess_level = questionary.text("Points ELO:").ask()
        return first_name, last_name, birthday, chess_level

    def error_player_already_exists(self):
        print('!! Ce joueur est déjà présent dans la base de données')

