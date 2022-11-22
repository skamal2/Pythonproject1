class Car:
    accelerate = 0
    def __init__(self, registration_number, maximum_speed, current_speed=0, travelled_distance=0):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = current_speed
        self.travelled_distance = travelled_distance
        Car.accelerate = Car.accelerate+1


toyota = Car("ABC-123", "142 km/h")


print(
    f"The registration number  of toyota is:{toyota.registration_number}."
    f"It's maximum speed is {toyota.maximum_speed}. It's current speed is {toyota.current_speed} & "
    f"It's travelled distance is {toyota.travelled_distance}.")
"""class Car:
    #not required to define parameters current_speed and travelled_distance here.
    def __init__(self, registration_number, maximum_speed: int, current_speed=0, travelled_distance=0):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0

newcar = Car("ABC-123", 142)
print(f"The registration number of the new car is {newcar.registration_number}.")
print(f"The maximum speed of the new car is {newcar.maximum_speed}.")
print(f"The current speed of the new car is {newcar.current_speed}.")
print(f"The travelled distance of the new car is {newcar.travelled_distance}.")"""




