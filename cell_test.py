import unittest
from lib.ship import Ship
from lib.cell import Cell

class CellTest(unittest.TestCase):
    def test_cell_attributes(self):
        cell = Cell("B4")

        assertEqual("B4", cell.coordinate)
        assertEqual(null, cell.ship)
        assertEqual(True, cell.empty)

if __name__ == '__main__':
    unittest.main()
