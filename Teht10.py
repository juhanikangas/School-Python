from classes import Building
import random as r
from classes import Car, Race


# 1
def test_building_class():
    building = Building(4, 11, 3)
    building.run_elevator(1, 11)
    building.run_elevator(6, 7)
    building.run_elevator(3, 200)
    building.fire_alarm()


# 2 
def execute_race():
    cars = []

    for i in range(10):
        car = Car("ABC-" + str(i + 1), r.randint(100, 200))
        cars.append(car)

    race = Race("Grand Demolition Derby", 8000, cars)
    i = 0
    while not race.race_finished():
        race.hour_passes([-10, 15])
        i += 1
        if i == 10:
            race.print_status()
            i = 0

    race.print_status()
