from machines.machine import Machine

class CNCMachine(Machine):
    def __init__(self, id, name, program="default"):
        super().__init__(id, name)
        self.program = program
        print(f"[{self.name}] Станок ЧПУ инициализирован с программой '{self.program}'.")

    def set_program(self, program):
        self.program = program
        print(f"[{self.name}] Метод set_program вызван. Программа: '{self.program}'.")

    def operate(self):
        print(f"[{self.name}] Метод operate вызван.")
        if self.status == "on":
            print(f"[{self.name}] Станок ЧПУ выполняет программу '{self.program}'.")
        else:
            print(f"[{self.name}] Станок ЧПУ остановлен.")