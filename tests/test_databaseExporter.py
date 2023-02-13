import datetime
import os
from unittest import TestCase

from chessmanager.models import Player
from chessmanager.models import Tournament
from chessmanager.controllers import DatabaseExporter
from chessmanager.controllers import ChessManager
from chessmanager.controllers import ArgParser
from chessmanager.controllers import TournamentController
from chessmanager.models import Round


class TestDatabaseExporter(TestCase):

    def create_8_players(self):
        list_of_4_players = []
        player1 = Player('AB12345', 'Carlsen', 'Magnus', '30/11/1990', 2852)
        player2 = Player('AB12346', 'Nepomniachtchi', 'Ian', '14/07/1990', 2793)
        player3 = Player('AB12347', 'Liren', 'Ding', '24/10/1992', 2788)
        player4 = Player('AB12348', 'Alireza', 'Firouzja', '18/06/2003', 2785)
        player5 = Player('AB12349', 'Anish', 'Giri', '28/06/1994', 2780)
        player6 = Player('AB12350', 'Hikaru', 'Nakamura', '09/12/2987', 2768)
        player7 = Player('AB12351', 'Fabiano', 'Caruana', '30/06/1992', 2766)
        player8 = Player('AB12352', 'Wesley', 'So', '09/10/1993', 2766)
        list_of_4_players.append(player1)
        list_of_4_players.append(player2)
        list_of_4_players.append(player3)
        list_of_4_players.append(player4)
        list_of_4_players.append(player5)
        list_of_4_players.append(player6)
        list_of_4_players.append(player7)
        list_of_4_players.append(player8)
        return list_of_4_players


    def test_save_database(self):

        tournament_1 = Tournament(
            1,
            'Tournoi des candidats 2020',
            'Double round-robin à 8 joueurs',
            'Dubai',
            datetime.datetime.strptime('17/03/2020', '%d/%m/%Y'),
            datetime.datetime.strptime('03/04/2020', '%d/%m/%Y')
        )
        tournament_2 = Tournament(
            2,
            'Tournoi de Shamkir',
            'A la mémoire du joueur azerbaïdjanais Vugar Gashimov',
            'Shamkir',
            datetime.datetime.strptime('31/03/2019', '%d/%m/%Y'),
            datetime.datetime.strptime('09/04/2019', '%d/%m/%Y')
        )

        args = ArgParser()
        the_parameters = args.read_parameters()
        chess_manager = ChessManager(the_parameters)

        chess_manager.players = self.create_8_players()

        # add players on tournament_2
        tournament_2.players = self.create_8_players()
        # add a round on tournament_2
        new_round = Round(1, 'Round1', '13/02/2023', '15:00', '13/02/2023', '16:00')
        tournament_controller = TournamentController(tournament_2)
        set_of_players = tournament_controller.pairing_next_round()
        # create matches
        for elem in set_of_players:
            match = [elem[0], 0], [elem[1], 0]
            new_round.matches.append(match)
        tournament_2.rounds.append(new_round)

        # add the tournament on chess_manager
        chess_manager.tournaments.append(tournament_1)
        chess_manager.tournaments.append(tournament_2)

        tournaments_file = chess_manager.data_directory + '/tournaments.json'

        database = DatabaseExporter(chess_manager, tournaments_file)
        database.save_database()

        self.assertEqual(
            os.path.exists(tournaments_file) and os.path.getsize(tournaments_file) == 1525,
            True)

