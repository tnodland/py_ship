import unittest
from lib.ship import Ship

class ShipTest(unittest.TestCase):
    def test_ship_attributes(self):
        cruiser = Ship("Cruiser", 3)

        self.assertEqual("Cruiser", cruiser.name)
        self.assertEqual(3, cruiser.length)
        self.assertEqual(3, cruiser.health)


if __name__ == '__main__':
    unittest.main()
