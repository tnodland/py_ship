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

    def test_cell_rendering(self):
        cell1 = Cell("B4")
        cell2 = Cell("C5")
        cell3 = Cell("D6")
        cruiser1 = Ship("cruiser", 1)
        cruiser2 = Ship("cruiser", 2)

        cell1.place_ship(cruiser1)
        cell2.place_ship(cruiser2)

        self.assertEqual(".", cell1.render())
        self.assertEqual(".", cell2.render())
        self.assertEqual(".", cell3.render())

        cell1.fire_upon()
        cell2.fire_upon()
        cell3.fire_upon()

        self.assertEqual("X", cell1.render())
        self.assertEqual("H", cell2.render())
        self.assertEqual("M", cell3.render())


if __name__ == '__main__':
    unittest.main()
