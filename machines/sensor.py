from machines import Machine
import random

class Sensor(Machine):
    def __init__(self, id, name, sensor_type="temperature"):
        super().__init__(id, name)
        self.sensor_type = sensor_type
        self.value = 0

    def read_value(self):
        self.value = round(random.uniform(20, 100), 2)
        print(f"Sensor {self.name} ({self.sensor_type}) reads {self.value}")
        return self.value

    def operate(self):
        if self.status == "on":
            self.read_value()
        else:
            print(f"Sensor {self.name} is off")