"""Again, extend the program by adding a new drive method that receives the number of hours as a parameter.
The method increases the travelled distance by how much the car has travelled in constant speed in the given time. Example:
The travelled distance of car object is 2000 km. The current speed is 60 km/h.
Method call car.drive(1.5) increases the travelled distance to 2090 km."""

"""class Car:


    def __init__(self, registration_number, maximum_speed, current_speed = 0, travelled_distance = 0):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = current_speed
        self.travelled_distance = travelled_distance

    def accelerate(self,speed):

        self.current_speed=self.current_speed+speed


        if self.current_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed

        if self.current_speed<0:
            self.current_speed=0

        return

    def drive(self, driving_time):
        self.travelled_distance = self.current_speed*driving_time


toyota = Car("ABC-123", 142)
current_speed=toyota.accelerate(200)
travelled_distance = toyota.drive(4)

print(
    f"The registration number  of toyota is:{toyota.registration_number}."
    f"It's maximum speed is {toyota.maximum_speed}km/h. It's current speed is {toyota.current_speed}km/h & "
    f"It's travelled distance is {toyota.travelled_distance}km.")"""

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
        return
    def drive_hours(self, hours:float):
        self.travelled_distance=self.current_speed*hours
newcar = Car("ABC-123", 142)

current_speed=newcar.accelerate(30)
travelled_distance = newcar.drive_hours(2.5)
print(f"The current speed of the car is {newcar.current_speed}km/hr.")
print(f"The travelled distance of the car is {newcar.travelled_distance}km.")
current_speed=newcar.accelerate(50)
travelled_distance = newcar.drive_hours(1.5)
print(f"The current speed of the car is {newcar.current_speed}km/hr.")
print(f"The travelled distance of the car is {newcar.travelled_distance}km.")

current_speed=newcar.accelerate(70)
travelled_distance = newcar.drive_hours(1)
print(f"The current speed of the car is {newcar.current_speed}km/hr.")
print(f"The travelled distance of the car is {newcar.travelled_distance} km.")
current_speed=newcar.accelerate(-200)
travelled_distance = newcar.drive_hours(1)
print(f"The current speed of the car is {newcar.current_speed}")
print(f"The travelled distance of the car is {newcar.travelled_distance} km.")