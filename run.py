import sys
from robot import Robot
from commands import COMMANDS_MAP


def parse_commands(command_line):
    command_line = command_line.split()

    if not len(command_line):
        raise ValueError

    command_name = command_line[0].upper()
    args = command_line[1:][0].upper().split(",") if len(command_line) > 1 else []
    return command_name, args


def run_commands():
    toy_robot = Robot()

    for line in sys.stdin:
        command_name, args = parse_commands(line)
        if command_name in COMMANDS_MAP:
            run_command = COMMANDS_MAP[command_name](*args)
            if command_name == "PLACE":
                toy_robot = run_command()
            else:
                run_command(toy_robot)
        else:
            raise ValueError('Unknown command')


if __name__ == '__main__':
    print("Running toy robot simulator...")
    run_commands()
