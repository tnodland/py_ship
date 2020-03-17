import unittest
from lib.ship import Ship

class ShipTest(unittest.TestCase):
    # def setUp(self):
    #     cruiser = Ship("Cruiser", 3)

    def test_name(self):
        cruiser = Ship("Cruiser", 3)
        self.assertEqual("Cruiser", cruiser.name)

if __name__ == '__main__':
    unittest.main()
