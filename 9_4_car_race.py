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

class Car:


    def __init__(self, registration_number, maximum_speed, current_speed = 0, travelled_distance = 0):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = current_speed
        self.travelled_distance = travelled_distance

    def accelerate(self,speed):

        self.current_speed=self.current_speed+speed


        if self.current_speed > self.maximum_speed:
            self.current_speed = self.current_speed-200


        if self.current_speed<0:
            self.current_speed=0

        return

    def drive(self, driving_time):
        self.travelled_distance = self.current_speed*driving_time

"""list_of_cars = {"toyota":"ABC-1",
           "honda":"ABC-2",
           "kia":"ABC-3",
           "mercedes":"ABC-4",
           "ferari":"ABC-5",
           "suzuki":"ABC-6",
           "megane":"ABC-7",
           "lamborgini":"ABC-8",
           "ford":"ABC-9",
           "nissan":"ABC-10"}"""

list_of_cars = ["toyota","honda","kia","ferari","suzuki","megane","lamborgini","ford","nissan"]
toyota = Car("ABC-1", 200)
honda = Car("ABC-2", 250)
kia = Car("ABC-3", 220)
mercedes = Car("ABC-4", 300)
ferari = Car("ABC-5", 275)
suzuki = Car("ABC-6", 300)
megane = Car("ABC-7", 275)
lamborgini = Car("ABC-8", 300)
ford= Car("ABC-9", 250)
nissan= Car("ABC-10",275 )
current_speed=toyota.accelerate(50)
travelled_distance = toyota.drive(4)

print(
    f"The registration number  of toyota is:{toyota.registration_number}."
    f"It's maximum speed is {toyota.maximum_speed}km/h. It's current speed is {toyota.current_speed}km/h & "
    f"It's travelled distance is {toyota.travelled_distance}km.")