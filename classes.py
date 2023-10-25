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


class Race:

    def __init__(self, name, distance, cars):
        self.name = name
        self.distance = distance
        self.cars = cars

    def hour_passes(self, range_of_speed_change):
        for car in self.cars:
            car.accelerate(r.randint(range_of_speed_change[0], range_of_speed_change[1]))
            car.drive(1)

    def race_finished(self):
        max_distance = 0

        for i, car in enumerate(self.cars):
            if car.travelled_distance > max_distance:
                max_distance = car.travelled_distance

        if max_distance >= self.distance:
            return True
        else:
            return False

    def print_status(self):
        self.cars = sorted(self.cars, key=lambda x: x.travelled_distance, reverse=True)
        for car in self.cars:
            print(
                f'{car.registration_number}, max speed: {car.max_speed} distance travelled: {car.travelled_distance} current speed: {car.current_speed}')


class Elevator:
    def __init__(self, bot_floor, top_floor):
        self.bot_floor = bot_floor
        self.top_floor = top_floor
        self.current_floor = bot_floor

    def go_to_floor(self, destination):
        if destination < self.bot_floor:
            destination = self.bot_floor
        if destination > self.top_floor:
            destination = self.top_floor
        print(f'Elevator is at floor {self.current_floor}')
        while self.current_floor != destination:
            if destination > self.current_floor:
                self.floor_up()
            elif destination < self.current_floor:
                self.floor_down()
            print(f'Elevator is at floor {self.current_floor}')

    def floor_up(self):
        self.current_floor += 1

    def floor_down(self):
        self.current_floor -= 1


class Building:
    def __init__(self, bot_floor, top_floor, elevator_amount):
        self.bot_floor = bot_floor
        self.top_floor = top_floor
        self.elevators = []

        for i in range(elevator_amount):
            self.elevators.append(Elevator(bot_floor, top_floor))

    def run_elevator(self, elevator_number, floor_destination):
        try:
            self.elevators[elevator_number - 1].go_to_floor(floor_destination)
        except IndexError:
            print("Invalid elevator number!")

    def fire_alarm(self):
        for i in range(len(self.elevators)):
            self.run_elevator(i + 1, self.bot_floor)
