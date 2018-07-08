from WorldEnum import Ability, Direction, OpCode, Terrian
from Position import Position
from Species import Species
from Config import Config
from Instruction import Instruction
from Creature import Creature
from SimpleWorld import SimpleWorld
import random


def createTerrianMap():
    terrianMap = [[Terrian.HILL for i in range(Config.MAXWIDTH)] for j in range(Config.MAXHEIGHT)]
    for widthIndex in range(Config.MAXWIDTH):
        for heightIndex in range(Config.MAXHEIGHT):
            terrianMap[widthIndex][heightIndex] = random.choice([Terrian.FOREST, Terrian.HILL, Terrian.LAKE, Terrian.PLAIN])

    return terrianMap


def createCreatureMap():
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

    creatureMap = [[None for i in range(Config.MAXWIDTH)] for j in range(Config.MAXHEIGHT)]
    creatures = []
    for widthIndex in range(Config.MAXWIDTH):
        for heightIndex in range(Config.MAXHEIGHT):
            needCreate = random.choice([False,False,False,False, True])
            if needCreate:
                species = random.choice([species1,species1,species1,species2,species2,species2,species3,species3,species4,species4,species5])
                direction = random.choice([Direction.EAST, Direction.WEST, Direction.SOUTH, Direction.NORTH])
                abilities = random.choice([abilites1, abilites2, abilites2, abilites3, abilites3, abilites4, abilites4, abilites4])
                creature = Creature(species, direction, abilities, Position(widthIndex, heightIndex))

                # add into map
                creatureMap[widthIndex][heightIndex] = creature

                # add into list
                creatures.append(creature)

    
    random.shuffle(creatures)
    return (creatureMap, creatures)

if __name__ == '__main__':
    terrianMap = createTerrianMap()
    (creatureMap, creatures) = createCreatureMap()
    sw = SimpleWorld(terrianMap, creatureMap, creatures)
    sw.run()