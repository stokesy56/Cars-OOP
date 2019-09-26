from vehicle_class_2 import *

class Car2(Vehicle2):
    def __init__(self, wheels, capacity, colour, make ,model,plate):
        super().__init__(wheels, capacity, colour)
        self.make = make
        self.model = model
        self.plate = plate
        self._accidents = 0 # visibility is limited (not great literally just because of underscore)
        self.__miles = 0 # visibility and acces is restricted

    def make_sound(self):
        return 'Revving my car! Vroom'

    def accelerate(self):
        self.__increase_miles()
        return ('vrrrrroooooooommmmmm')

    def play_music(self, song):
        return 'Banging song this is' + song

    def show_miles(self): #getter
        return self.__miles

    def set_miles(self,miles): #setter
        #checking some crazy security stuff before setting
        self.__miles = miles
        return 'miles set to ' + miles

    def __increase_miles(self): #encapsulated private method
        self.__miles += 100
