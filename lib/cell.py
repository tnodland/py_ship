from lib.ship import Ship

class Cell():
    def __init__(self, coordinate):
        self.coordinate = coordinate
        self.ship = None
        self.empty = True
        self.fired_upon = False

    def place_ship(self, ship):
        if self.empty:
            self.empty = False
            self.ship = ship

    def fire_upon(self):
        self.fired_upon = True
        if not self.empty:
            self.ship.hit()
