from machines.conveyor import Conveyor
from machines.robot_arm import RobotArm
from machines.sensor import Sensor
from machines.cnc_machine import CNCMachine

from control.main_control_unit import MainControlUnit
from database.database import Database

from interfaces.operator_interface import OperatorInterface
from interfaces.manager_interface import ManagerInterface


db = Database()
control = MainControlUnit()


conv = Conveyor(1, "Conveyor A", speed=5)
robot = RobotArm(2, "Robot Arm 1", operation="welding")
sensor = Sensor(3, "Temp Sensor 1", sensor_type="temperature")
cnc = CNCMachine(4, "CNC Machine 1", program="cutting")


control.add_machine(conv)
control.add_machine(robot)
control.add_machine(sensor)
control.add_machine(cnc)


# создаём интерфейсы
operator = OperatorInterface(control, db)
manager = ManagerInterface(control, db)


print("\n--- Operator actions ---")
operator.start_machine(conv)
operator.read_sensor(sensor)


print("\n--- Manager actions ---")
manager.set_conveyor_speed(conv, 10)
manager.set_robot_operation(robot, "assembly")

cnc.set_program("drilling")

manager.start_machine(robot)
manager.start_machine(cnc)


print("\n--- System operation ---")
control.operate_all()

print()
manager.show_database()