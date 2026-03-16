class ManagerInterface:
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

    def set_conveyor_speed(self, conveyor, speed):
        conveyor.set_speed(speed)
        self.database.log(conveyor, "set_speed", speed)

    def set_robot_operation(self, robot, operation):
        robot.set_operation(operation)
        self.database.log(robot, "set_operation", operation)

    def show_database(self):
        self.database.show_history()