import Utils
from Utils import Terrain, Ability, Direction
from Operation import Operation

class Creature:

    def __init__(self, species, ability, direction=Direction.East, square=None):
        self.__species = species
        self.__ability = ability
        self.__direction = direction
        self.__location = square
        self.__instructions = Operation(self)

    def standOn(self, square):
        self.__location = square

    def located(self):
        return self.__location

    def hop(self):
        lastSquare = self.__location
        nextSquare = lastSquare.getNext(self.__direction, self.__ability)
        if nextSquare.getLivingCreature() is None:
            self.__location = nextSquare
            lastSquare.setLivingCreature(None)
            self.__location.setLivingCreature(self)

    def left(self):
        #Set direction
        self.__direction = Utils.turnTo(self.__direction, -90)

    def right(self):
        #Set direction
        self.__direction = Utils.turnTo(self.__direction, 90)

    def getDirection(self):
        return self.__direction

    def setDirection(self, direction):
        self.__direction = direction

    def getSpecies(self):
        return self.__species

    def getAbility(self):
        return self.__ability

    def getInstructions(self):
        return self.__instructions

    def infect(self):
        frontSquare = self.__location.getNext(self.__direction, self.__ability)
        targetCreature = frontSquare.getLivingCreature()

        if targetCreature is None:
            return

        if targetCreature.canBeSeen() or (Ability.Archery in self.__ability):
            targetCreature.isInfected(self.__species)

    def isInfected(self, species):
        self.__species = species
        self.__instruction.changeSpecies(species)

    def canBeSeen(self):
        return self.__location.getTerrian() is not Terrain.Forest

    def isSlowdown(self):
        return (Ability.Flying not in self.__ability) and (self.__location.getTerrian() is Terrain.Hill)

    def meetEnemy(self):
        try:
            nextSquare = self.__location.getNext(self.__direction, self.__ability)
            nextCreature = nextSquare.getLivingCreature()
            if nextCreature is None:
                return False

            return nextCreature.getSpecies() is not self.__species
        except EOFError:
            return False

    def meetSame(self):
        try:
          nextSquare = self.__location.getNext(self.__direction, self.__ability)
          nextCreature = nextSquare.getLivingCreature()
          if nextCreature is None:
              return False

          return nextCreature.getSpecies() is self.__species

        except EOFError:
            return False

    def faceWall(self):
        try:
          return not self.isNextSquareAvailable()
        except EOFError:
            return True

    def isNextSquareAvailable(self):
        return self.__location.isNextAvailable(self.__direction, self.__ability)

    def isInHill(self):
        return self.__location.getTerrain() is Terrain.Hill