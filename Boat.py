from vehicle_class import *
class Boat(Vehicle):
    def __init__(self, wheels, capacity, colour, year, hull_size, propeller_size):
        super().__init__(wheels, capacity, colour, year)
        self.hull_size = hull_size
        self.propeller_size = propeller_size

