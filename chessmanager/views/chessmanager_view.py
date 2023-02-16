import questionary
import re
import datetime

from .player_view import PlayerView
from .tournament_view import TournamentView


class ChessManagerView:
    def __init__(self, chess_manager):
        self.chess_manager = chess_manager

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

    def report_menu_choices(self) -> list:
        return [
                "Liste des joueurs par ordre alphabétique",
                "Liste de tous les tournois",
                "Nom et dates d'un tournoi donné",
                "Liste des joeurs d'un tournoi par ordre alphabétique",
                "liste de tous les tours du tournoi et de tous les matchs du tour",
                "revenir au menu principal"
            ]

    def check_date_format(self, a_date) -> bool:
        try:
            res = bool(datetime.datetime.strptime(a_date, '%d/%m/%Y'))
        except ValueError:
            res = False
        return res

    def prompt_tournament_id(self) -> int:
        tournament_id = questionary.text('Saisissez le numéro du tournoi:').ask()
        return int(tournament_id)

    def prompt_player_id(self) -> str:
        chess_id = questionary.text("Identifiant national d'échecs:").ask()
        while not re.match(r"[A-Z][A-Z]\d\d\d\d\d", chess_id):
            print("L'identifiant doit contenir 2 lettres et 5 chiffres")
            chess_id = questionary.text("Identifiant national d'échecs:").ask()
        return chess_id

    def prompt_player_data(self) -> tuple:
        first_name = questionary.text("Nom:").ask()
        last_name = questionary.text("Prénom:").ask()
        birthday = questionary.text("Date de naissance (dd/mm/yyyy):").ask()
        while not self.check_date_format(birthday):
            print("Format de date incorrect")
            birthday = questionary.text("Date de naissance (dd/mm/yyyy):").ask()
        chess_level = questionary.text("Points ELO:").ask()
        return first_name, last_name, birthday, chess_level

    def prompt_tournament_data(self) -> tuple:
        title = questionary.text("Titre du tournoi:").ask()
        description = questionary.text("Description du tournoi:").ask()
        area = questionary.text("Lieu:").ask()
        date_begin = questionary.text("Date de début (dd/mm/yyyy):").ask()
        while not self.check_date_format(date_begin):
            print("Format de date incorrect")
            date_begin = questionary.text("Date de début (dd/mm/yyyy):").ask()
        date_end = questionary.text("Date de fin (dd/mm/yyyy):").ask()
        while not self.check_date_format(date_end):
            print("Format de date incorrect")
            date_end = questionary.text("Date de fin (dd/mm/yyyy):").ask()
        return title, description, area, date_begin, date_end

    def display_output_directory_created(self):
        print(f"Le répertoire {self.chess_manager.output_directory} est créé")

    def display_data_directory_created(self):
        print(f"Le répertoire {self.chess_manager.data_directory} est créé")

    def display_welcome(self):
        text = "  Bienvenue dans le manager de tournois d'échecs"
        print(len(text) * '-')
        print(text)
        print(len(text) * '-')
        print('')

    def display_main_menu(self) -> str:
        print('')
        print(50 * '-')
        answer = questionary.select(
            "Que souhaitez-vous faire ?",
            choices=self.main_menu_choices()
        ).ask()
        return answer

    def display_reports_menu(self) -> str:
        print('')
        print(50 * '-')
        answer = questionary.select(
            "Que souhaitez-vous faire ?",
            choices=self.report_menu_choices()
        ).ask()
        return answer

    def display_all_players(self):
        if len(self.chess_manager.players):
            print('!! Aucun joueur actuellemnt dans la base')
        for player in self.chess_manager.players:
            player_view = PlayerView(player)
            player_view.display_player_data()
            print('')

    def display_chess_data(self):
        print(f" Nombre de joueur : {len(self.chess_manager.players)}")
        print(f" Nombre de tournoi : {len(self.chess_manager.tournaments)}")

    def display_all_tournaments(self):
        if len(self.chess_manager.tournaments) == 0:
            print('!! Aucun tournoi créer dans la base')
        else:
            for tournament in self.chess_manager.tournaments:
                tournament_view = TournamentView(tournament)
                tournament_view.display_tournament_resume()
                print('')
    def display_players_selection(self):
        print('Sélectionnez 8 joueurs parmis les joueurs ci-dessus')

    def error_player_already_exists(self):
        print('!! Ce joueur est déjà présent dans la base de données')

    def error_player_already_selected(self):
        print('!! Ce joueur est déjà présent dans la sélection')

    def error_player_not_exist(self):
        print("!! Ce joueur n'existe pas")

    def error_tournament_not_found(self):
        print("!! Ce tournoi n'existe pas dans la base")

    def error_not_enough_players(self):
        print('!! Nombre de joueurs insuffisant dans la base')
