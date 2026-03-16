class OperatorInterface:
    def __init__(self, control_unit, database):
        self.control_unit = control_unit
        self.database = database

    def start_machine(self, machine):
        machine.start()
        machine.operate()
        self.database.log(machine, "start")

    def stop_machine(self, machine):
        machine.stop()
        self.database.log(machine, "stop")

    def read_sensor(self, sensor):
        value = sensor.read_value()
        self.database.log(sensor, "read", value)
        return value
    