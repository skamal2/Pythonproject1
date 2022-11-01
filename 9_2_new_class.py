"""Extend the program by adding an accerelate method into the new class.
The method should receive the change of speed (km/h) as a parameter.
If the change is negative, the car reduces speed. The method must change the value of the speed property of the object.
The speed of the car must stay below the set maximum and cannot be less than zero.
Extend the main program so that the speed of the car is first increased by +30 km/h, then +70 km/h and finally +50 km/h.
Then print out the current speed of the car. Finally,
use the emergency brake by forcing a -200 km/h change on the speed and then print out the final speed.
The travelled distance does not have to be updated yet."""



class Car:


    def __init__(self, registration_number, maximum_speed, current_speed = 0, travelled_distance = 0):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = current_speed
        self.travelled_distance = travelled_distance


    def accelerate(self,speed):

        self.current_speed=self.current_speed+speed


        if self.current_speed > self.maximum_speed:
            self.current_speed =self.maximum_speed


        if self.current_speed<0:
            self.current_speed=0

        return
"""Another method:
 def accelerate(self,speed):

        self.current_speed=self.current_speed+speed


        if self.current_speed > self.maximum_speed and self.current_speed <=342:
            self.current_speed = self.current_speed-200
        elif self.current_speed > 342:
            self.current_speed = 142
        if self.current_speed<0:
            self.current_speed=self.current_speed-self.current_speed

"""

toyota = Car("ABC-123", 142)
current_speed=toyota.accelerate(50)
current_speed=toyota.accelerate(30)
current_speed=toyota.accelerate(100)
current_speed = toyota.accelerate(-200)


print(
    f"The registration number  of toyota is:{toyota.registration_number}."
    f"It's maximum speed is {toyota.maximum_speed}. It's current speed is {toyota.current_speed} & "
    f"It's travelled distance is {toyota.travelled_distance}.")
