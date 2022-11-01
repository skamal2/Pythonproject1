from tabulate import tabulate
import random
class car:
    def __init__(self, regnum, maxspd):
        self.regnum = regnum
        self.maxspd = maxspd
        self.curSpeed = 0
        self.travelledDistance = 0
        self.carStatus = {}

    def info(self):
        self.carStatus = {
            "Registration Number": self.regnum,
            "Maximum speed": self.maxspd,
            "Current speed": self.curSpeed,
            "Travelled Distance": self.travelledDistance
        }

    def accelerate(self, speed):
        self.curSpeed += speed
        if self.curSpeed < 0:
            self.curSpeed = 0
        elif self.curSpeed > self.maxspd:
            self.curSpeed = self.maxspd
        return self.curSpeed

    def emergency(self):
        self.curSpeed -= 200
        if self.curSpeed < 0:
            self.curSpeed = 0
        return self.curSpeed

    def drive(self, hours):
        self.travelledDistance += self.curSpeed * hours
        return self.travelledDistance

carList = []
for i in range(1, 11):
    newCar = car("ABC-" + str(i), random.randint(100, 200))
    carList.append(newCar)

maxTravelledDistance = 0
while maxTravelledDistance < 10000:
    for i in range(10):
        carList[i].accelerate(random.randint(-10, 15))
        carList[i].drive(1)
        carList[i].info()
        if maxTravelledDistance < carList[i].travelledDistance:
            maxTravelledDistance = carList[i].travelledDistance

raceResult = []
for i in range(10):
    raceResult.append(carList[i].carStatus)
print(tabulate(raceResult, headers="keys"))


