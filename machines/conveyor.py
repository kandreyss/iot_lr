from machines import Machine

class Conveyor(Machine):
    def __init__(self, id, name, speed=1):
        super().__init__(id, name)
        self.speed = speed

    def set_speed(self, speed):
        self.speed = speed

    def operate(self):
        if self.status == "on":
            print(f"Conveyor {self.name} is moving at speed {self.speed}")
