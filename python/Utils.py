from enum import Enum
class Direction(Enum):
    North = 0
    East = 90
    South = 180
    West = 270

class Ability(Enum):
    Flying = 1
    Archery = 2

class Terrain(Enum):
    Plain = 0
    Lake = 1
    Forest = 2
    Hill = 3

class Species(Enum):
    Flytrap = 0
    Landmine = 1
    Hop = 2

def turnTo(origDir, rotate):
    destDir = origDir.value + rotate
    if destDir < 0:
        destDir += 360
    return Direction(destDir)