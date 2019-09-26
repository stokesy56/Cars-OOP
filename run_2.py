from vehicle_class_2 import *
from car_class_2 import *

vehicle_example = Vehicle2(4,5,'blue')
print(vehicle_example)

print('Proof of Inheritance')
car_example = Car2(2,1,'red', 'volvo','xc90', 'xoxox')
print(car_example) #Inheriting the __init__
print(car_example.accelerate()) #Inheritng the .accelerate

print('Proof of method polymorphism with make_sound()')
print(vehicle_example.make_sound())
print(car_example.make_sound())

print('Playing with encapsulation')
print(car_example.wheels)
print(car_example._accidents)
print(car_example.show_miles())
print(car_example.accelerate())
print(car_example.show_miles())