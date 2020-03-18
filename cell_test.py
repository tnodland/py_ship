import unittest
from lib.ship import Ship
from lib.cell import Cell

class CellTest(unittest.TestCase):
    def test_cell_attributes(self):
        cell = Cell("B4")

        self.assertEqual("B4", cell.coordinate)
        self.assertEqual(None, cell.ship)
        self.assertTrue(cell.empty)
        self.assertFalse(cell.fired_upon)

    def test_cell_can_place_a_ship(self):
        cell = Cell("B4")
        cruiser = Ship("cruiser", 1)

        self.assertTrue(cell.empty)
        self.assertEqual(None, cell.ship)

        cell.place_ship(cruiser)

        self.assertFalse(cell.empty)
        self.assertEqual(cruiser, cell.ship)

    def test_cell_cant_place_a_ship_if_not_empty(self):
        cell = Cell("B4")
        cruiser = Ship("cruiser", 1)
        cruiser2 = Ship("cruiser2", 1)

        self.assertTrue(cell.empty)
        self.assertEqual(None, cell.ship)

        cell.place_ship(cruiser)

        self.assertFalse(cell.empty)
        self.assertEqual(cruiser, cell.ship)

        cell.place_ship(cruiser2)

        self.assertFalse(cell.empty)
        self.assertEqual(cruiser, cell.ship)

    def test_cell_can_be_fired_upon(self):
        cell = Cell("B4")
        cruiser = Ship("cruiser", 1)

        cell.place_ship(cruiser)

        self.assertFalse(cell.fired_upon)
        self.assertEqual(1, cruiser.health)

        cell.fire_upon()

        self.assertTrue(cell.fired_upon)
        self.assertEqual(0, cruiser.health)

if __name__ == '__main__':
    unittest.main()
