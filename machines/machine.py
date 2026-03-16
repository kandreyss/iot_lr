from abc import ABC, abstractmethod

class Machine(ABC):
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.status = False
    
    def start(self):
        self.status = True
    
    def stop(self):
        self.status = False

    def get_status(self):
        return self.start
    
    @abstractmethod
    def operate(self):
        pass