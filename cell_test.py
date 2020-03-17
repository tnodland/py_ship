import unittest
from lib.ship import Ship
from lib.cell import Cell

class CellTest(unittest.TestCase):
    def test_cell_attributes(self):
        cell = Cell("B4")

        self.assertEqual("B4", cell.coordinate)
        self.assertEqual(None, cell.ship)
        self.assertTrue(cell.empty)

    def test_cell_can_place_a_ship(self):
        cell = Cell("B4")
        cruiser = Ship("cruiser", 1)

        self.assertTrue(cell.empty)
        self.assertEqual(None, cell.ship)

        cell.place_ship(cruiser)

        self.assertFalse(cell.empty)
        self.assertEqual(cruiser, cell.ship)


if __name__ == '__main__':
    unittest.main()
