import webbrowser


class ChessManagerReports:
    """
    Generate html files for the reports of the chess manager
    """
    def __init__(self, players, tournaments, output_directory):
        self.players = players
        self.tournaments = tournaments
        self.filename = output_directory + '/chessmanager_report.html'

    def html_header(self) -> str:
        return """
        <html>
        <head>
        <title>Title</title>
        </head>
        """

    def html_footer(self) -> str:
        return """
        </body>
        </html>
        """

    def all_players_in_alphabetic_order(self):
        """ List the players in alphabetic order
        :return:
        """
        with open(self.filename, 'w') as f:
            f.write(self.html_header())
            body = """<body>
            <h2>Welcome To GFG</h2>  
            <p>Default code has been loaded into the Editor.</p>"""
            f.write(body)
            f.write(self.html_footer())
        webbrowser.open(self.filename)

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