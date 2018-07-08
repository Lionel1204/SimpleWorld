import json
from enum import Enum

class Direction(Enum):
    North = 0
    East = 90
    South = 180
    West = 270

class Ability(Enum):
    Nothing = 0
    Flying = 1
    Archery = 2

class Terrain(Enum):
    Plain = 0
    Lake = 1
    Forest = 2
    Hill = 3

class SpeciesType(Enum):
    Flytrap = 0
    LandMine = 1
    Hop = 2
    Food = 3
    PathFinder = 4
    Lrover = 5
    Rrover = 6
    AltRover = 7

def turnTo(origDir, rotate):
    destDir = origDir.value + rotate
    if destDir < 0:
        destDir += 360
    if destDir >= 360:
        destDir %= 360
    return Direction(destDir)

def loadJson(filename):
    with open(filename) as f:
        data = json.load(f)
    return data
