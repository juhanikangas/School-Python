import random as r


class Car:
    def __init__(self, registration_number, max_speed, current_speed=0, travelled_distance=0):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = current_speed
        self.travelled_distance = travelled_distance

    def accelerate(self, change_of_speed):
        self.current_speed += change_of_speed
        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed
        elif self.current_speed < 0:
            self.current_speed = 0

    def drive(self, hours):
        self.travelled_distance += hours * self.current_speed


cars = []

for i in range(10):
    car = Car("ABC-" + str(i + 1), r.randint(100, 200))
    cars.append(car)

max_distance = 0
max_distance_index = 0

while max_distance < 10000:

    for car in cars:
        car.accelerate(r.randint(-10, 15))
        car.drive(1)

    for i, car in enumerate(cars):
        if car.travelled_distance > max_distance:
            max_distance = car.travelled_distance
            max_distance_index = i

cars = sorted(cars, key=lambda x: x.travelled_distance, reverse=True)
for car in cars:
    print(
        f'{car.registration_number}, max speed: {car.max_speed} distance travelled: {car.travelled_distance} current speed: {car.current_speed}')
