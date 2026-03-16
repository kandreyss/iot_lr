from machines import Machine

class RobotArm(Machine):
    def __init__(self, id, name, operation="idle"):
        super().__init__(id, name)
        self.operation = operation

    def set_operation(self, operation):
        self.operation = operation
        print(f"{self.name} operation set to {self.operation}")

    def operate(self):
        if self.status == "on":
            print(f"RobotArm {self.name} performing operation: {self.operation}")
        else:
            print(f"RobotArm {self.name} is idle")