import sys
from robot import Robot


class BaseCommand:
    def __init__(self, *args):
        self.params = list(args)


class PlaceCommand(BaseCommand):
    def __call__(self, *args):
        return Robot(*self.params)


class MoveCommand(BaseCommand):
    def __call__(self, robot_instance, *args):
        robot_instance.move_robot()


class RightCommand(BaseCommand):
    def __call__(self, robot_instance, *args):
        robot_instance.turn_robot('right')


class LeftCommand(BaseCommand):
    def __call__(self, robot_instance, *args):
        robot_instance.turn_robot('left')


class ReportCommand(BaseCommand):
    def __call__(self, robot_instance, *args):
        sys.exit(robot_instance.report())


COMMANDS_MAP = {
    "PLACE": PlaceCommand,
    "MOVE": MoveCommand,
    "LEFT": LeftCommand,
    "RIGHT": RightCommand,
    "REPORT": ReportCommand
}
