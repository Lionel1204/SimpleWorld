from enum import Enum

class Direction(Enum):
    EAST = 0
    WEST = 1
    SOUTH = 2
    NORTH = 3

class Terrian(Enum):
    PLAIN = 0
    HILL = 1
    FOREST = 2
    LAKE = 3

class Ability(Enum):
    FLY = 0
    ARCH = 1


class OpCode(Enum):
    HOP = 0
    LEFT = 1
    RIGHT = 2
    INFECT = 3
    IFEMPTY = 4
    IFENEMY = 5
    IFSAME = 6
    IFWALL = 7
    GO = 8

if __name__ == "__main__":
    print(OpCode.HOP)
    print(Ability.FLY)
    print(Terrian.PLAIN)
    print(Direction.EAST)
    
