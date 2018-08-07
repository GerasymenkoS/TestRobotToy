from unittest import TestCase

from robot import Robot
from run import parse_commands
from commands import PlaceCommand, COMMANDS_MAP


class TestRobot(TestCase):
    def test_case1(self):
        commands = ["PLACE 1,2,EAST", "MOVE", "MOVE", "LEFT", "MOVE", "REPORT"]
        for command in commands:
            if "PLACE" in command:
                command_name, args = parse_commands(command)
                robot_toy = PlaceCommand(*args)
                robot_toy = robot_toy()
            elif command == "REPORT":
                self.assertEqual(robot_toy.report(), "3,3,NORTH")
            else:
                run_command = COMMANDS_MAP[command]()
                run_command(robot_toy)

    def test_case2(self):
        commands = ["MOVE", "REPORT"]
        robot_toy = Robot()
        for command in commands:
            if command == "REPORT":
                self.assertEqual(robot_toy.report(), "0,1,NORTH")
            else:
                run_command = COMMANDS_MAP[command]()
                run_command(robot_toy)

    def test_case3(self):
        commands = ["PLACE 0,0,NORTH", "LEFT", "MOVE", "MOVE", "MOVE", "RIGHT", "MOVE", "REPORT"]
        for command in commands:
            if "PLACE" in command:
                command_name, args = parse_commands(command)
                robot_toy = PlaceCommand(*args)
                robot_toy = robot_toy()
            elif command == "REPORT":
                self.assertEqual(robot_toy.report(), "0,1,NORTH")
            else:
                run_command = COMMANDS_MAP[command]()
                run_command(robot_toy)