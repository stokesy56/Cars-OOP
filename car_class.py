from vehicle_class import *
class Car(Vehicle):

    def __init__(self,wheels, capacity, colour, year, brand, model, license_plate, airbag):
        super().__init__(wheels, capacity, colour, year)
        self.brand = brand
        self.model = model
        self.license_plate = license_plate
        self.airbag = airbag

    def play_music(self,song_name):
        return f"Now playing {song_name}"

    def horn(self):
        return 'beeeeeep'

    def lock(self):
        return 'click'

    def cruise_control(self):
        return 'Your car is now in cruise control'

    def air_conditioning(self,temperature):
        if temperature == 'cold':
            return 'brrr chilliy now!'
        elif temperature == 'warm':
            return 'mhhhhmmm nice and warm'

    def convertible(self):
        return 'Your car now has no roof'

