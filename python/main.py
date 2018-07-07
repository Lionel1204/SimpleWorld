import numpy as np
from Creature import Creature
from Utils import Direction, Ability, Species, Terrain
from Square import Square

def main():
    print 'Hello world'
    square = Square(Terrain.Lake)
    creature1 = Creature(Species.Hop, [Ability.Flying, Ability.Archery], Direction.North, square)
    creature2 = Creature(Species.Flytrap, [Ability.Flying], Direction.East, square)




if __name__ == '__main__':
    main()