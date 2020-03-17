from lib.ship import Ship

class Cell():
    def __init__(self, coordinate):
        self.coordinate = coordinate
        self.ship = None
        self.empty = True

    def place_ship(self, ship):
        self.empty = False
        self.ship = ship
