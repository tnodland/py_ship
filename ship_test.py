import unittest
from lib.ship import Ship

class ShipTest(unittest.TestCase):
    def test_ship_attributes(self):
        cruiser = Ship("Cruiser", 3)

        self.assertEqual("Cruiser", cruiser.name)
        self.assertEqual(3, cruiser.length)
        self.assertEqual(3, cruiser.health)

    def test_ship_can_be_hit(self):
        cruiser = Ship("Cruiser", 3)

        self.assertEqual(cruiser.health, 3)

        cruiser.hit()

        self.assertEqual(cruiser.health, 2)

    def test_ship_can_be_sunk(self):
        cruiser = Ship("cruiser", 1)

        self.assertFalse(cruiser.sunk())

        cruiser.hit()

        self.assertTrue(cruiser.sunk())

if __name__ == '__main__':
    unittest.main()
