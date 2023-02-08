import os

from unittest import TestCase

from chessmanager.controllers import Parameters
from chessmanager.controllers import ChessManager


class TestChessManager(TestCase):
    def test_check_directories(self):
        p = Parameters()
        chess_manager = ChessManager(p)
        self.assertEqual(
            os.path.exists(chess_manager.output_directory)
            and os.path.exists(chess_manager.data_directory),
            True
        )

    def test_run(self):
        self.fail()
