class Vehicle2():
    def __init__(self, wheels, capacity, colour):
        self.wheels = wheels
        self.capacity = capacity
        self.colour = colour

    def accelerate(self):
        return 'vrooom'

    def make_sound(self):
        return '*noises*'

#print(Vehicle2(4,5,'blue'))