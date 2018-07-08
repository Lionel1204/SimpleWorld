from Utils import Direction, Ability, Terrain

class Square:

    def __init__(self, terrain, creature=None, north=None, east=None, south=None, west=None):

        self.__livingCreature = creature
        self.__terrain = terrain
        #(0,0) is left upper
        self.__x = 0
        self.__y = 0
        self.setConnection(north, east, south, west)

    def setConnection(self, north=None, east=None, south=None, west=None):
        self.__north = north
        self.__east = east
        self.__south = south
        self.__west = west

    def getLivingCreature(self):
        return self.__livingCreature

    def setLivingCreature(self, creature):
        self.__livingCreature = creature

    def setAxis(self, x, y):
        self.__x = x
        self.__y = y

    def isBoundaryNext(self, direction):
        if direction is Direction.North:
            result = self.__north is None
        elif direction is Direction.East:
            result = self.__east is None
        elif direction is Direction.South:
            result = self.__south is None
        elif direction is Direction.North:
            result = self.__north is None
        else:
            raise TypeError('Unknown direction')

        return result

    def isAbilityBoundaryNext(self, direction, ability):
        return (Ability.Flying not in ability) and (self.getTerrain(direction) is Terrain.Lake)

    def getTerrianNext(self, direction):
        ter = None
        if not self.isBoundary(direction):
            if direction is Direction.North:
                ter = self._north.getTerrain()
            elif direction is Direction.East:
                ter = self._east.getTerrain()
            elif direction is Direction.South:
                ter = self._south.getTerrain()
            elif direction is Direction.North:
                ter = self.__north.getTerrain()
            else:
                raise TypeError('Unknown direction')
        return ter

    def getTerrain(self):
        return self.__terrain

    def setTerrain(self, terrain):
        self.__terrain = terrain

    def getNext(self, direction, ability):
        if self.isBoundaryNext(direction) or self.isAbilityBoundaryNext(direction, ability):
            raise EOFError('It is boundary!')

        if direction is Direction.North:
            nextSquare = self.__north
        elif direction is Direction.East:
            nextSquare = self.__east
        elif direction is Direction.South:
            nextSquare = self.__south
        elif direction is Direction.North:
            nextSquare = self.__north
        else:
            raise TypeError('Unknown direction')

        return nextSquare