"""Now we will program a car race.
The travelled distance of a new car is initialized as zero. At the beginning of the main program,
create a list that consists of 10 car objects created using a loop.
 The maximum speed of each new car is a random value between 100 km/h and 200 km/h.
 The registration numbers are created as follows: "ABC-1", "ABC-2" and so on. Now the race begins.
 One per every hour of the race, the following operations are performed:

The speed of each car is changed so that the change in speed is a random value between -10 km/h and +15 km/h.
This is done using the accerelate method.
Each car is made to drive for one hour. This is done with the drive method.
The race continues until one of the cars has advanced at least 10,000 kilometers.
Finally, the properties of each car are printed out formatted into a clear table."""
import random
from tabulate import tabulate
"""class Car:


    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0
        self.car_status = {}

    def info(self):
        self.car_status = {
            "Registration Number": self.registration_number,
            "Maximum speed": self.maximum_speed,
            "Current speed": self.current_speed,
            "Travelled Distance": self.travelled_distance
        }
    def accelerate(self,speed):

        self.current_speed += speed

        if self.current_speed < 0:
            self.current_speed = 0
        elif self.current_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed

        return self.current_speed

    def emergency_brake(self):
        self.current_speed -= 200
        if self.current_speed < 0:
            self.current_speed = 0

        return self.current_speed

    def drive(self, driving_time):
        self.travelled_distance += self.current_speed*driving_time
        return self.travelled_distance

carlists=[]
for i in range(1,11):
    new_car = Car("ABC-" + str(i), random.randint(100, 200))
    carlists.append(new_car)


total_distance = 0
while total_distance < 10000:
    for i in range(10):
        carlists[i].accelerate(random.randint(-10, 15))
        carlists[i].drive(1)
        carlists[i].info()
        if total_distance< carlists[i].travelled_distance:
            total_distance = carlists[i].travelled_distance

result = []
for i in range(10):
    result.append(carlists[i].car_status)
print(tabulate(result, headers="keys"))"""


class Car:
    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self,speed_change):
        self.current_speed=self.current_speed + speed_change
        if self.current_speed<0:
            self.current_speed = 0
        if self.current_speed>self.maximum_speed:
            self.current_speed = self.maximum_speed
        return True
    def drive_hours(self, hours:float):
        self.travelled_distance=self.current_speed*hours
        return self.travelled_distance
car_list=[]
for i in range(1,11):
    newcar = Car("ABC-" + str(i), random.randint(100, 200))
    car_list.append(newcar)

