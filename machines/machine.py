from abc import ABC, abstractmethod

class Machine(ABC):
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.status = "off"
        print(f"[{self.name}] Станок '{self.name}' (ID: {self.id}) создан.")

    def start(self):
        self.status = "on"
        print(f"[{self.name}] Метод start вызван. Статус: {self.status}.")

    def stop(self):
        self.status = "off"
        print(f"[{self.name}] Метод stop вызван. Статус: {self.status}.")

    def get_status(self):
        print(f"[{self.name}] Метод get_status вызван.")
        return self.status

    @abstractmethod
    def operate(self):
        pass