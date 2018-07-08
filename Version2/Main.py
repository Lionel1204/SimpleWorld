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
    inss1 = Instruction.createAttachInstructions()
    inss2 = Instruction.createEscapeInstructions()
    inss3 = Instruction.createAttachAllInstructions()
    inss4 = Instruction.createAttachNoEmptyInstructions()
    inss5 = Instruction.createHopAllInstructions()

    speciesName1 = "Apower"
    speciesName2 = "Kpower"
    speciesName3 = "Qpower"
    speciesName4 = "Jpower"
    speciesName5 = "Tpower"

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
                speciesName = random.choice([speciesName1,speciesName2,speciesName3,speciesName4,speciesName5])
                inss = random.choice([inss1,inss2,inss3,inss4,inss5])
                species = Species(speciesName, inss)

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