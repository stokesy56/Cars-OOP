class Bike(Vehicle):
    def __init__(self, wheels, capacity, colour, year, gears, bell, basket_size):
        super().__init__(wheels, capacity, colour, year)
        self.gears = gears
        self.bell = bell
        self.basket_size = basket_size

    def pedal(self):
        return 'pedalpedalpedalpedal'

    def wheelie(self):
        return 'wow look at me!!'

    def chain_it(self):
        return 'My bike is secure'
