import webbrowser
import os
import datetime


class ChessManagerReports:
    """
    Generate html files for the reports of the chess manager
    """
    def __init__(self, players, tournaments, output_directory):
        self.players = players
        self.tournaments = tournaments
        self.filename = output_directory + '/chessmanager_report.html'
        self.css_filename = output_directory + '/style.css'

    def style_css(self):
        # if not os.path.exists(self.css_filename):

        code_css = """      
        body {
        font-family: 'Raleway', sans-serif;
        font-size: 1em;
        background: rgb(242,151,113);
        background: linear-gradient(150deg, rgba(242,151,113,1) 0%, rgba(241,226,94,1) 30%, rgba(232,242,31,1) 100%);
        background-size: cover;
        background-repeat: no-repeat;
        opacity : 0.6
        margin: 0;
        } 
        h1 {color: blue; }
        h2 {text-align: center;}
        h3 {
        font-size: 1.3em;
        color: black;
        }
        footer {
        text-align: center;        
        }
        """
        with open(self.css_filename, 'w', encoding='utf8') as f:
            f.write(code_css)

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

    def report_header(self) -> str:
        return """
        <header>
        <h2>
        <img src="
        """ + os.getcwd() + '/logo.png' + """
        ">
        Gestionnaire de tournois d'échecs</h2>  
        </header>    
        """

    def report_footer(self) -> str:
        now = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")
        return """
        <footer>
            <h3>Extraction des données du """ + now + """
        </h3>
        </footer>
        """

    def open_in_browser(self):
        webbrowser.open(os.getcwd() + '/' + self.filename)

    def all_players_in_alphabetic_order(self):
        """ List the players in alphabetic order
        :return:
        """
        self.style_css()
        with open(self.filename, 'w', encoding='utf8') as f:
            f.write(self.html_header())
            f.write(self.report_header())
            body = """
            <main>
            <h1> Liste des joueurs inscrits dans le club </h1>
            
            </main>
            """
            f.write(body)
            f.write(self.report_footer())
            f.write(self.html_footer())
        self.open_in_browser()

    def all_tournaments(self):
        """ List the tournaments record in the chess manager
        :return:
        """

    def tournament_data(self):
        """
        Give informations about a specifique tournament
        :return:
        """

    def tournament_players(self):
        """
        List the players of a specifique tournament
        :return:
        """

    def tournaments_details(self):
        """
        Give the details of a tournament : all the rounds
        and all the matches of each round
        :return:
        """