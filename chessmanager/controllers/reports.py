import webbrowser
import os
import shutil
import datetime

from chessmanager.models import STATES


class ChessManagerReports:
    """
    Generate html files for the reports of the chess manager
    """
    def __init__(self, chess_manager):
        self.chess_manager = chess_manager
        self.filename = self.chess_manager.output_directory + '/chessmanager_report.html'

    def style_css(self):
        # if not os.path.exists(self.css_filename):
        shutil.copyfile('assets/style.css', self.chess_manager.output_directory + '/style.css')

    def html_header(self) -> str:
        return """
        <!DOCTYPE html>
        <html lang="fr">
        <head>
            <meta charset="utf-8">
            <title>Gestion de tournois d'échecs</title>  
            <link href="style.css" rel="stylesheet">     
            <link rel="preconnect" href="https://fonts.googleapis.com">
            <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
            <link href="https://fonts.googleapis.com/css2?family=Raleway:wght@100&display=swap" rel="stylesheet"> 
                          
        </head>
        <body>
        """

    def html_footer(self) -> str:
        return """
        </body>
        </html>
        """

    def report_header(self, title) -> str:
        return """
        <header>
        <h1>""" + title + """</h1>  
        <hr width="70%" size="8" align="center">
        </header>    
        """

    def report_footer(self) -> str:
        now = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")
        img = """<img src="
        """ + os.getcwd() + '/assets/logo.png' + """        
        " /> """

        return """
        <footer>
            <h3> """ + img + """
        Gestionnaire de tournois d'échecs - Extraction des données du """ + now + img + """
        </h3>        
        </footer>
        """

    def open_in_browser(self):
        webbrowser.open(os.getcwd() + '/' + self.filename)

    def sort_alpha_order(self, player):
        return player.first_name.lower(), player.last_name.lower()

    def html_body_for_list_of_players(self, players) -> str:
        body = """
                    <main>
                    <h3>
                    <div class="conteneur-players">
                    <div class="box">Identifiant</div>
                    <div class="box">Nom</div>
                    <div class="box">Prénom</div>
                    <div class="box">Date de naissance</div>
                    <div class="box">Niveau ELO</div>
                    """
        for player in sorted(players, key=self.sort_alpha_order):
            body += """ <div class="box"> """ + player.chess_id + """ </div> """
            body += """ <div class="box"> """ + player.first_name + """ </div> """
            body += """ <div class="box"> """ + player.last_name + """ </div> """
            body += """ <div class="box"> """
            body += datetime.datetime.strftime(player.birthday,'%d/%m/%Y') + """ </div> """
            body += """ <div class="box"> """ + str(player.chess_level) + """ </div> """

        body += """</div></h3>>            
                    </main>
                    """
        return body

    def all_players_in_alphabetic_order(self):
        """ List the players in alphabetic order
        :return:
        """
        self.style_css()
        with open(self.filename, 'w', encoding='utf8') as f:
            f.write(self.html_header())
            f.write(self.report_header('Liste des joueurs inscrits dans le club'))
            f.write(self.html_body_for_list_of_players(self.chess_manager.players))
            f.write(self.report_footer())
            f.write(self.html_footer())
        self.open_in_browser()

    def box_from_state(self, state) -> str:
        if state == STATES[0]:
            return """ <div class="box"> Non commencé </div> """
        elif state == STATES[1]:
            return """ <div class="box"> En cours </div> """
        else:
            return """ <div class="box"> Terminé </div> """

    def all_tournaments(self):
        """ List the tournaments record in the chess manager
        :return:
        """
        self.style_css()
        with open(self.filename, 'w', encoding='utf8') as f:
            f.write(self.html_header())
            f.write(self.report_header('Liste des tournois enregistrés dans le club'))
            body = """<main>
            <h3>
            <div class="conteneur-tournaments">
            <div class="box">Numéro</div>
            <div class="box">Titre</div>
            <div class="box">Description</div>
            <div class="box">Lieu</div>
            <div class="box">Date début</div>
            <div class="box">Date fin</div>
            <div class="box">Nombre de rounds</div>
            <div class="box">Etat</div>
            """
            for tournament in self.chess_manager.tournaments:
                body += """ <div class="box"> """ + str(tournament.tournament_id) + """ </div> """
                body += """ <div class="box"> """ + tournament.title + """ </div> """
                body += """ <div class="box"> """ + tournament.description + """ </div> """
                body += """ <div class="box"> """ + tournament.area + """ </div> """
                body += """ <div class="box"> """ + tournament.date_begin + """ </div> """
                body += """ <div class="box"> """ + tournament.date_end + """ </div> """
                body += """ <div class="box"> """ + str(tournament.nb_of_rounds) + """ </div> """
                body += self.box_from_state(tournament.state)
            body += """</div></h3>></main>"""
            f.write(body)
            f.write(self.report_footer())
            f.write(self.html_footer())
        self.open_in_browser()

    def generate_tournament_data(self, tournament):
        self.style_css()
        with open(self.filename, 'w', encoding='utf8') as f:
            f.write(self.html_header())
            f.write(self.report_header(
                'Description du tournoi numéro ' + str(tournament.tournament_id)))
            body = """<main><h3>
            <div class="conteneur-tournament-data">"""
            body += """<div class="box">Titre:</div>"""
            body += """<div class="box">""" + tournament.title + """</div>"""
            body += """<div class="box">Description:</div>"""
            body += """<div class="box">""" + tournament.description + """</div>"""
            body += """<div class="box">Lieu:</div>"""
            body += """<div class="box">""" + tournament.area + """</div>"""
            body += """<div class="box">Date début:</div>"""
            body += """<div class="box">""" + tournament.date_begin + """</div>"""
            body += """<div class="box">Date fin:</div>"""
            body += """<div class="box">""" + tournament.date_end + """</div>"""
            body += """<div class="box">Nombre de rounds:</div>"""
            body += """<div class="box">""" + str(tournament.nb_of_rounds) + """</div>"""
            body += """<div class="box">Etat:</div>"""
            body += self.box_from_state(tournament.state)
            body += """</div></h3>></main>"""
            f.write(body)
            f.write(self.report_footer())
            f.write(self.html_footer())
        self.open_in_browser()

    def generate_tournament_players(self, tournament):
        """
        List the players of a specifique tournament
        :return:
        """
        self.style_css()
        with open(self.filename, 'w', encoding='utf8') as f:
            f.write(self.html_header())
            f.write(self.report_header(
                'Liste des joueurs du tournoi numéro ' + str(tournament.tournament_id)))
            f.write(self.html_body_for_list_of_players(tournament.players))
            f.write(self.report_footer())
            f.write(self.html_footer())
        self.open_in_browser()


    def tournaments_details(self, tournament):
        """
        Give the details of a tournament : all the rounds
        and all the matches of each round
        :return:
        """

        self.style_css()
        with open(self.filename, 'w', encoding='utf8') as f:
            f.write(self.html_header())
            f.write(self.report_header(
                'Liste des tours du tournoi numéro ' + str(tournament.tournament_id)))
            body = """<main>"""
            for a_round in tournament.rounds:
                body += """<h2>"""
                body += a_round.name
                body += '   Du ' + a_round.date_begin + ' au ' + a_round.date_end + """</h2>"""
                body += """</div><h3>"""
                body += """<div class="conteneur-match">"""
                body += """<div class="box">Numéro</div>"""
                body += """<div class="box">Joueur 1</div>"""
                body += """<div class="box">Score joueur 1</div>"""
                body += """<div class="box">Joueur 2</div>"""
                body += """<div class="box">Score joueur 2</div>"""
                for index, match in enumerate(a_round.matches):
                    body += """ <div class="box"> """ + str(index + 1) + """ </div> """
                    body += """ <div class="box"> """ + str(match[0][0]) + """ </div> """
                    body += """ <div class="box"> """ + str(match[0][1]) + """ </div> """
                    body += """ <div class="box"> """ + str(match[1][0]) + """ </div> """
                    body += """ <div class="box"> """ + str(match[1][1]) + """ </div> """
                body += """</div></h3>"""
            body += """</main>"""
            f.write(body)
            f.write(self.report_footer())
            f.write(self.html_footer())
        self.open_in_browser()
