from WorldEnum import Ability, Direction, OpCode, Terrian
from Position import Position
from Species import Species
from Config import Config
from Instruction import Instruction
from Creature import Creature
from SimpleWorld import SimpleWorld
import random

terrianDistr = []
speciesDistr = []
abilityDistr = []
creaturDistr = []

def generateDistr():

    inss1 = Instruction.createAttackInstructions()
    inss2 = Instruction.createEscapeInstructions()
    inss3 = Instruction.createAttackAllInstructions()
    inss4 = Instruction.createAttackNoEmptyInstructions()
    inss5 = Instruction.createHopAllInstructions()

    species1 = Species("SmartPower", inss1)
    species2 = Species("EscapePower", inss2)
    species3 = Species("KillAllPower", inss3)
    species4 = Species("NoEmptyAttackPower", inss4)
    species5 = Species("HopAllpower", inss5)

    abilites1 = [Ability.FLY, Ability.ARCH]
    abilites2 = [Ability.ARCH]
    abilites3 = [Ability.FLY]
    abilites4 = []

    for number in range(Config.TERRIAN_F):
        terrianDistr.append(Terrian.FOREST)
    for number in range(Config.TERRIAN_H):
        terrianDistr.append(Terrian.HILL)
    for number in range(Config.TERRIAN_L):
        terrianDistr.append(Terrian.LAKE)
    for number in range(Config.TERRIAN_P):
        terrianDistr.append(Terrian.PLAIN)
    
    for number in range(Config.SPECIES_S):
        speciesDistr.append(species1)
    for number in range(Config.SPECIES_E):
        speciesDistr.append(species2)
    for number in range(Config.SPECIES_K):
        speciesDistr.append(species3)
    for number in range(Config.SPECIES_N):
        speciesDistr.append(species4)
    for number in range(Config.SPECIES_H):
        speciesDistr.append(species5)

    for number in range(Config.ABILITY_FA):
        abilityDistr.append(abilites1)
    for number in range(Config.ABILITY_A):
        abilityDistr.append(abilites2)
    for number in range(Config.ABILITY_F):
        abilityDistr.append(abilites3)
    for number in range(Config.ABILITY_):
        abilityDistr.append(abilites4)

    for number in range(Config.CREATURE_Y):
        creaturDistr.append(True)
    for number in range(Config.CREATURE_N):
        creaturDistr.append(False)

def createTerrianMap():
    terrianMap = [[Terrian.HILL for i in range(Config.MAXWIDTH)] for j in range(Config.MAXHEIGHT)]

    for widthIndex in range(Config.MAXWIDTH):
        for heightIndex in range(Config.MAXHEIGHT):
            terrianMap[widthIndex][heightIndex] = random.choice(terrianDistr)

    return terrianMap


def createCreatureMap():
    creatureMap = [[None for i in range(Config.MAXWIDTH)] for j in range(Config.MAXHEIGHT)]
    creatures = []
    for widthIndex in range(Config.MAXWIDTH):
        for heightIndex in range(Config.MAXHEIGHT):
            needCreate = random.choice(creaturDistr)
            
            if needCreate:
                species = random.choice(speciesDistr)
                direction = random.choice([Direction.EAST, Direction.WEST, Direction.SOUTH, Direction.NORTH])
                abilities = random.choice(abilityDistr)
                creature = Creature(species, direction, abilities, Position(widthIndex, heightIndex))

                # add into map
                creatureMap[widthIndex][heightIndex] = creature

                # add into list
                creatures.append(creature)

    
    random.shuffle(creatures)
    return (creatureMap, creatures)


class WorldFactory:

    @staticmethod
    def generateWorld():
        generateDistr()
        terrianMap = createTerrianMap()
        (creatureMap, creatures) = createCreatureMap()
        simpleWorld = SimpleWorld(terrianMap, creatureMap, creatures)
        return simpleWorld