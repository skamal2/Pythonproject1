import random


class Car:
    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, acceleration):
        self.current_speed = min(max(self.current_speed + acceleration, 0), self.maximum_speed)

    def drive(self, time):
        self.travelled_distance += self.current_speed * time


class Race:
    def __init__(self, name, distance, cars_list):
        self.name = name
        self.distance = distance
        self.cars_list = cars_list

    def hour_passes(self):
        for car in self.cars_list:
            car.accelerate(random.randint(-10, 15))
            car.drive(1.)

    def print_status(self):
        print(self.name + ":")
        print("Plate  Speed Travelled Distance")
        print("------------------------------")
        for car in self.cars_list:
            print(f"{car.registration_number:6s}: {car.current_speed:3d}, {car.travelled_distance} km")

    def race_finished(self):
        for car in self.cars_list:
            if car.travelled_distance >= self.distance:
                return True
        return False


car_list = []
for i in range(10):
    car_list.append(Car("ABC-" + str(i + 1), random.randint(100, 200)))

race = Race("  Grand Demolition Derby", 8000, car_list)
n = 0
while not race.race_finished():
    race.hour_passes()
    n += 1
    if n % 10 == 0:
        print(f"After {n} hours")
        race.print_status()
print(f"The final result after {n} hours is: ")
race.print_status()
