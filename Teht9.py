import random as r
from classes import Car, Race


cars = []

for i in range(10):
    car = Car("ABC-" + str(i + 1), r.randint(100, 200))
    cars.append(car)

race = Race("10km race", 10000, cars)

while not race.race_finished():
    race.hour_passes([-10, 15])

race.print_status()

