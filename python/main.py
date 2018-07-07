import numpy as np
from Creature import Creature
from Utils import Direction, Ability, SpeciesType, Terrain
from Square import Square
from Grid import Grid
from Operation import Operation

def main():
    print 'Hello world'
    grid = Grid()
    grid.createSquares(2, 3, Terrain.Lake)
    creature1 = Creature(SpeciesType.Hop, [Ability.Flying, Ability.Archery], Direction.North)
    creature2 = Creature(SpeciesType.Flytrap, [Ability.Flying], Direction.East)

    operation = Operation(creature1)
    print 'test'



if __name__ == '__main__':
    main()