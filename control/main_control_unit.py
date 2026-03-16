class MainControlUnit:
    def __init__(self):
        self.machines = []

    def add_machine(self, machine):
        self.machines.append(machine)
        print(f"{machine.name} added to control unit")

    def start_all(self):
        for m in self.machines:
            m.start()
            m.operate()

    def stop_all(self):
        for m in self.machines:
            m.stop()

    def operate_all(self):
        for m in self.machines:
            m.operate()