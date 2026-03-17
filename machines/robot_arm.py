from machines.machine import Machine

class RobotArm(Machine):
    def __init__(self, id, name, operation="idle"):
        super().__init__(id, name)
        self.operation = operation
        print(f"[{self.name}] Робот-манипулятор инициализирован с операцией '{self.operation}'.")

    def set_operation(self, operation):
        self.operation = operation
        print(f"[{self.name}] Метод set_operation вызван. Операция: '{self.operation}'.")

    def operate(self):
        print(f"[{self.name}] Метод operate вызван.")
        if self.status == "on":
            print(f"[{self.name}] Робот-манипулятор выполняет операцию: {self.operation}.")
        else:
            print(f"[{self.name}] Робот-манипулятор бездействует.")