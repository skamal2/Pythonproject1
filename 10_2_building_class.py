class Elevator:
    def __init__(self, bottom, top):
        self.bottom = bottom
        self.top = top
        self.current = bottom

    def floor_up(self):
        if self.current < self.top:
            print(f"The elevator is moving up from {self.current} to {self.current + 1}")
            self.current += 1
            return True

        else:
            return False

    def floor_down(self):
        if self.current > self.bottom:
            print(f"Elevator is moving down from {self.current} to {self.current - 1}")
            self.current -= 1
            return True

        else:
            return False

    def go_to_floor(self, floor):
        if floor > self.current:
            for i in range(floor - self.current):
                if not self.floor_up():
                    break

        elif floor < self.current:
            for i in range(self.current - floor):
                if not self.floor_down():
                    break

        else:
            print(f"you are already at the floor {self.current}")


class Building:
    def __init__(self, bottom, top, elevator_list):
        self.elevator_list = []
        for i in range(elevator_list):
            self.elevator_list.append(Elevator(bottom, top))

    def run_elevator(self, elevator_no, floor):
        print(f"The elevator number {elevator_no} is running")
        self.elevator_list[elevator_no - 1].go_to_floor(floor)


print("Elevator in the building.")
building = Building(1, 7, 3)
building.run_elevator(1, 4)
building.run_elevator(2, 5)
building.run_elevator(3, 2)
