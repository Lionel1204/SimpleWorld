import Utils
from Utils import Terrain, Ability

class Creature:

    def __init__(self, species, ability, direction, square = None):
        self.__species = species
        self.__ability = ability
        self.__direction = direction
        self.__location = square

    def standOn(self, square):
        self.__location = square

    def hop(self):
        lastSquare = self.__location
        nextSquare = self.__square.getNext(self.__direction, self.__ability)
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
        return self.__direction.name

    def getSpecies(self):
        return self.__species

    def infect(self):
        frontSquare = self.__direction.getNext()
        targetCreature = frontSquare.getLivingCreature()

        if targetCreature is None:
            return

        if targetCreature.canBeSeen() or (Ability.Archery in self.__ability):
            targetCreature.isInfected(self.__species)

    def isInfected(self, species):
        self.__species = species

    def canBeSeen(self):
        return self.__location.getTerrian() is not Terrain.Forest

    def isSlowdown(self):
        return (Ability.Flying not in self.__ability) and (self.__location.getTerrian() is Terrain.Hill)

    def meetSame(self):
        try:
          nextSquare = self.__location.getNext()
          nextCreature = nextSquare.getLivingCreature()
          if nextCreature is None:
              return False

          return nextCreature.getSpecies() is self.__species

        except EOFError:
            return False

    def faceWall(self):
        try:
          self.__location.getNext()
          return False
        except EOFError:
            return True