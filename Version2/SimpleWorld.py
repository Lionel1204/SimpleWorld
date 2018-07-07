from WorldEnum import Ability, Direction, OpCode, Terrian
from Position import Position
from Species import Species
from Config import Config
from Instruction import Instruction
from Creature import Creature

class SimpleWorld:

    def __init__(self, terrianMap, creatureMap, creatures):
        self.__terrianMap = terrianMap
        self.__creatureMap = creatureMap
        self.__creatures = creatures
        self.__worldWidth = len(terrianMap)
        self.__worldHeight = len(terrianMap[0])
        self.__creatureNumber = len(creatures)
        self.__currentRound = 0


    def run(self):

        print("Game Start!")

        while self.isGameOver == False:


            print("Round {0}".format(self.__currentRound))
            self.drawWorld()

            currentIndex = self.__currentRound % self.__creatureNumber
            currentCreature = self.__creatures[currentIndex]

            # check environment
            currentOp = currentCreature.getNextOpcode(True, True, True, True)

            # execute op



            # next round
            self.__currentRound += 1

            # wait for input
            userinput = raw_input("Next Round?")
            if(userinput == "exit"):
                break

        print("Game Over!")
    
    @property
    def isGameOver(self):
        creature1 = self.__creatures[0]
        for createure in self.__creatures:
            if createure.speciesName != creature1.speciesName:
                return False

        return True

    def drawWorld(self):
        msg = ""
        for widthIndex in range(self.__worldWidth):
            for heightIndex in range(self.__worldHeight):
                terrian = self.__terrianMap[widthIndex][heightIndex]
                creature = self.__creatureMap[widthIndex][heightIndex]
                msg += "["

                if terrian == Terrian.FOREST:
                    msg += "F"
                elif terrian == Terrian.HILL:
                    msg += "H"
                elif terrian == Terrian.LAKE:
                    msg += "L"
                elif terrian == Terrian.PLAIN:
                    msg += "P"
                
                msg += "|"
                if creature != None:
                    # name
                    msg += creature.speciesName[0].upper()

                    # direction
                    msg += "^"

                    if creature.direction == Direction.EAST:
                        msg += "E"
                    elif creature.direction == Direction.WEST:
                        msg += "W"
                    elif creature.direction == Direction.NORTH:
                        msg += "N"
                    elif creature.direction == Direction.SOUTH:
                        msg += "S"

                    # fly
                    msg += "-"
                    if creature.canFly:
                        msg += "F"
                    else:
                        msg += "-"
                    
                    # arch
                    msg += "-"

                    if creature.canArc:
                        msg += "A"
                    else:
                        msg += "-"
                    

                else:
                    msg += "_______"
                
                msg += "] "
            
            msg += "\n"
        
        print(msg)


if __name__ == "__main__":
    ins0 = Instruction(OpCode.IFENEMY, 8)
    ins1 = Instruction(OpCode.IFSAME, 6)
    ins2 = Instruction(OpCode.IFWALL, 6)
    ins3 = Instruction(OpCode.IFEMPTY, 4)
    ins4 = Instruction(OpCode.HOP, None)
    ins5 = Instruction(OpCode.GO, 0)
    ins6 = Instruction(OpCode.RIGHT, None)
    ins7 = Instruction(OpCode.GO, 0)
    ins8 = Instruction(OpCode.INFECT, None)
    ins9 = Instruction(OpCode.GO, 0)
    inss = [ins0, ins1, ins2,ins3, ins4, ins5, ins6, ins7, ins8, ins9]
    spec1 = Species("FLYTRAP", inss)
    creature1 = Creature(spec1, Direction.EAST, [Ability.FLY, Ability.ARCH], Position(1,1))

    spec2 = Species("LAND", inss)
    creature2 = Creature(spec2, Direction.WEST, [Ability.FLY], Position(2,2))

    spec3 = Species("WOLF", inss)
    creature3 = Creature(spec3, Direction.SOUTH, [], Position(1,2))

    creatures = [creature1, creature2, creature3]
    creatureMap = [ 
    [None,  None,       None],
    [None,  creature1,  creature3],
    [None,  None,       creature2]]

    terrianMap = [ 
    [Terrian.FOREST,Terrian.HILL, Terrian.PLAIN],
    [Terrian.PLAIN,Terrian.HILL, Terrian.FOREST],
    [Terrian.LAKE,Terrian.PLAIN, Terrian.PLAIN]]

    sw = SimpleWorld(terrianMap, creatureMap, creatures)
    sw.run()


