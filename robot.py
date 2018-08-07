from position import Coordinates
from tabletop import TableTop


class Robot:
    FACING_DIRECTION = ["SOUTH", "WEST", "NORTH", "EAST"]
    FACING_COORDINATES = [(0, -1), (-1, 0), (0, 1), (1, 0)]

    def __init__(self, x=0, y=0, facing='NORTH',
                 tabletop=TableTop(Coordinates(0,0),
                                   Coordinates(4,4))):
        self.position = Coordinates(int(x), int(y))

        # setting default direction of 'NORTH'
        if facing and facing in self.FACING_DIRECTION:
            self.facing = facing
        else:
            self.facing = 'NORTH'
        self.tabletop = tabletop

    def turn_robot(self, direction):
        facing_id = self.FACING_DIRECTION.index(self.facing)
        if direction == 'left':
            facing = self.FACING_DIRECTION[(facing_id + 3) % 4]
        elif direction == 'right':
            facing = self.FACING_DIRECTION[(facing_id + 1) % 4]
        else:
            raise Exception('Incorrect direction')

        self.facing = facing
        return self.put_robot(self.position)

    def move_robot(self):
        facing_id = self.FACING_DIRECTION.index(self.facing)
        return self.put_robot(self.position +
                               Coordinates(*self.FACING_COORDINATES[facing_id]))

    def put_robot(self, position):
        if self.tabletop.contains(position):
            self.position = position

    def report(self) -> str:
        return ",".join(map(str, [self.position.x, self.position.y, self.facing]))
