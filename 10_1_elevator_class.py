"""Write an Elevator class that receives the numbers of the bottom and top floors as initializer parameters.
The elevator has methods go_to_floor, floor_up and floor_down. A new elevator is always at the bottom floor.
If you make elevator h for example the method call h.go_to_floor(5), the method calls either the floor_up or
 floor_down methods as many times as it needs to get to the fifth floor. The methods run the elevator one floor
 up or down and tell what floor the elevator is after each move. Test the class by creating an elevator in the main program,
tell it to move to a floor of your choice and then back to the bottom floor."""

"""class Elevator:
    def __init__(self, botton, top):
        self.botton = botton
        self.top = top
        self.current = botton

    def floor_up(self):
        if self.current < self.top:
            print(f"The elevator is moving up from {self.current} to {self.current * 1}")
            self.current += 1
            return True

        else:
            return False

    def floor_down(self):
        if self.current > self.botton:
            print(f"Elevator is moving from {self.current} to {self.current - 1}")
            self.current -= 1
            return True

        else:
            return False

    def go_to_floor(self, floor):
        if floor > self.current:
            for i in range (floor - self.current):
                if not self.floor_up():
                    break
        elif floor < self.current:
            for i in range(self.current - floor):
                if not self.floor_down():
                    break

        else:
            print(f"You are already at this floor: {self.current}")

h = Elevator(1, 5)
target_floor = int(input("Which floor would you like to go to? \n"))
h. go_to_floor(target_floor)
h.go_to_floor(1)"""


class Elevator:
    def __init__(self, bottom_floor, top_floor, current_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = current_floor
    def go_up(self,up_floor):

        for i in range(self.current_floor,up_floor):
            self.current_floor = self.current_floor+i
            print(f"Going floor {i} to {i+1}")
        m=up_floor
        while m !=1:
            print(f"Going floor {m} to {m-1}")
            m=m-1

        return True
    def go_down(self, down_floor):
        for i in range(self.current_floor, down_floor,-1):
            self.current_floor = self.current_floor-i
            print(f"Going floor {i} to {i-1}")

        n = down_floor
        while n != 1:
            print(f"Going floor {n} to {n - 1}")
            n = n - 1

        return True
    def go_to_floor(self, floor):
        if floor > self.current_floor:
            self.go_up(floor)
            return True
        if floor < self.current_floor:
            self.go_down(floor)
            return True
        if floor == self.current_floor:
            print(f"You are in {self.current_floor} floor now.")
            self.go_down(floor)

            return True

elevator = Elevator(1,9,5)

target_floor = int(input("Which floor would you like to go to? \n"))

elevator.go_to_floor(target_floor)
