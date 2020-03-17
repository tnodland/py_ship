from lib.ship import Ship

class Cell():
    def __init__(self, coordinate):
        self.coordinate = coordinate
        self.ship = None
        self.empty = True
