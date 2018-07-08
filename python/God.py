import numpy as np
from Utils import SpeciesType, Ability, Direction, Terrain
from Creature import Creature
from Grid import Grid
from printf import printf

class God:
    def __init__(self):
        self.__land = None
        self.__creatures = None

    def createWorld(self, creaturesNumber, gridX, gridY):
        self.createCreatures(creaturesNumber, SpeciesType.PathFinder)
        self.createLand(gridX, gridY)
        self.putCreaturesToLand()
        self.outputWorld()

    def createLand(self, gridX, gridY):
        grid = Grid()
        grid.createSquares(gridX, gridY)
        self.__land = grid.getLand()

    # Random generate abilities
    def abilityGenerator(self, number):
        abilityGroup = [[Ability.Nothing, Ability.Nothing], [Ability.Flying, Ability.Nothing], [Ability.Archery, Ability.Nothing], [Ability.Flying, Ability.Archery]]
        seeds = np.random.randint(len(abilityGroup), size=number)

        abilityGen = lambda a: abilityGroup[a]
        abilities = np.vectorize(abilityGen)(seeds)

        return abilities

    def directionGenerator(self, number, direction=None):
        if direction is None:
            directionArr = np.random.randint(len(Direction), size=(1, number))
        else:
            directionArr = np.full((1, number), direction.value)
        return np.multiply(directionArr, 90)

    def speciesGenerator(self, number, speciesType=None):
        if speciesType is None:
            speciesArr = np.random.randint(len(SpeciesType), size=(1, number))
        else:
            speciesArr = np.full((1, number), speciesType.value)
        return speciesArr

    def createCreatures(self, number=1, speciesType=None, direction=None):
        self.__creatures = []
        species = self.speciesGenerator(number, speciesType)
        abilities = self.abilityGenerator(number)
        directions = self.directionGenerator(number, direction)
        params = zip(species, abilities, directions)

        self.__creatures = map(lambda s: Creature(SpeciesType(s[0]), s[1], Direction(s[2])), params)

    def putCreaturesToLand(self):
        creatureNum = len(self.__creatures)
        landSize = self.__land.size
        if creatureNum > landSize:
            raise StandardError("The world is too crowded");
        index = np.random.choice(range(landSize), creatureNum, replace=False)
        flattenLand = self.__land.flatten()
        for i in range(len(index)):
            square = flattenLand[index[i]]
            creature = self.__creatures[i]
            square.setLivingCreature(creature)
            creature.standOn(square)

    def outputWorld(self):
        [x, y] = self.__land.shape
        for i in range(x):
            for j in range(y):
                terrian = self.__land[i][j].getTerrain()
                creature = self.__land[i][j].getLivingCreature()
                direction = '-' + creature.getDirection().name[:1] if creature is not None else ''
                creatureName = creature.getSpecies().name if creature is not None else ''
                printf("[%s, %s%s]\t\t\t", terrian.name, creatureName, direction)
            printf("\r\n")
        printf("\r\n")

    def runARound(self, creatures):
        creatures.getInstructions().runInstructionsOneRound()
        self.outputWorld()

    def runWorld(self):
        while True:
            map(self.runARound, self.__creatures)
            print 'Run one round complete'