from machines import Machine

class CNCMachine(Machine):
    def __init__(self, id, name, program="default"):
        super().__init__(id, name)
        self.program = program

    def set_program(self, program):
        self.program = program
        print(f"{self.name} program set to {self.program}")

    def operate(self):
        if self.status == "on":
            print(f"CNC Machine {self.name} is running program {self.program}")
        else:
            print(f"CNC Machine {self.name} is stopped")