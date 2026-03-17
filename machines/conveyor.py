from machines.machine import Machine

class Conveyor(Machine):
    def __init__(self, id, name, speed=1):
        super().__init__(id, name)
        self.speed = speed
        print(f"[{self.name}] Конвейер инициализирован со скоростью {self.speed}.")

    def set_speed(self, speed):
        self.speed = speed
        print(f"[{self.name}] Метод set_speed вызван. Скорость установлена: {self.speed}.")

    def operate(self):
        print(f"[{self.name}] Метод operate вызван.")
        if self.status == "on":
            print(f"[{self.name}] Конвейер движется со скоростью {self.speed}.")
        else:
            print(f"[{self.name}] Конвейер остановлен.")