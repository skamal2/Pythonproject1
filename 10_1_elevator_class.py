class Elevator:
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
h.go_to_floor(1)