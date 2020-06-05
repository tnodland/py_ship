import unittest
from lib.ship import Ship
from lib.cell import Cell
from lib.board import Board

class BoardTest(unittest.TestCase):
    def test_board_attributes(self):
        board = Board()
        example = {
            "A1": board.cells["A1"],
            "A2": board.cells["A2"],
            "A3": board.cells["A3"],
            "A4": board.cells["A4"],
            "B1": board.cells["B1"],
            "B2": board.cells["B2"],
            "B3": board.cells["B3"],
            "B4": board.cells["B4"],
            "C1": board.cells["C1"],
            "C2": board.cells["C2"],
            "C3": board.cells["C3"],
            "C4": board.cells["C4"],
            "D1": board.cells["D1"],
            "D2": board.cells["D2"],
            "D3": board.cells["D3"],
            "D4": board.cells["D4"]
        }

        self.assertDictEqual(example, board.cells)

    def test_valid_coordinates(self):
        board = Board()

        self.assertTrue(board.valid_coordinate("A1"))
        self.assertTrue(board.valid_coordinate("A3"))
        self.assertTrue(board.valid_coordinate("D3"))
        
        self.assertFalse(board.valid_coordinate("Q7"))
        self.assertFalse(board.valid_coordinate("Coordinate"))
        self.assertFalse(board.valid_coordinate("1A"))

if __name__ == '__main__':
    unittest.main()
