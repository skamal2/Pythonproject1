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

class ElectricCar(Car):
    def __init__(self, registration_number, maximum_speed,battery_capacity):
        super().__init__(registration_number, maximum_speed)
        self.battery_capacity = battery_capacity
class GasolineCar(Car):
    def __init__(self, registration_number, maximum_speed, volume_tank):
        super().__init__(registration_number, maximum_speed)
        self.volume_tank = volume_tank


newEcar = ElectricCar("ABC-15", 180, 52.5)
newEcar.accelerate(80)
newEcar.drive_hours(3)
print(f"Electric car travelled: {newEcar.travelled_distance} km")
newGcar = GasolineCar("DEF-123", 165, 32.3)
newGcar.accelerate(120)
newGcar.drive_hours(3)
print(f"Gasoline car travelled: {newGcar.travelled_distance} km")

