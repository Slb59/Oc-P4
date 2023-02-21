import questionary
from .check import check_date_format

from .player_view import PlayerView
from .tournament_view import TournamentView


class ChessManagerView:
    """
    Manage menu and chess_manager views
    """
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
                "Liste des joueurs d'un tournoi par ordre alphabétique",
                "Liste de tous les tours du tournoi et de tous les matchs du tour",
                "Revenir au menu principal"
            ]

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
                tournament_view.display_tournament_title()
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
