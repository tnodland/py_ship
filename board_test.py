import unittest
from lib.ship import Ship
from lib.cell import Cell
from lib.board import Board

class BoardTest(unittest.TestCase):
    def test_board_attributes(self):
        board = Board()

        self.assertEqual(True, board.exists)
