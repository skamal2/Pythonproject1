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
