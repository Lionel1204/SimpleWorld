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
        self.__worldHeight = len(terrianMap)
        self.__worldWidth = len(terrianMap[0])
        self.__creatureNumber = len(creatures)
        self.__currentRound = 0
        self.__activeCreature = None

    def run(self):

        print("Game Start!")

        while self.isGameOver == False:

            currentIndex = self.__currentRound % self.__creatureNumber
            currentCreature = self.__creatures[currentIndex]
            self.__activeCreature = currentCreature

            print("===Round {0}===".format(self.__currentRound))
            self.drawWorld()

            # check environment
            nextPos = currentCreature.getNextPosition()
            isEmpty = self.isEmpty(nextPos)
            isWall = self.isWall(nextPos, currentCreature)
            isEnemy = self.isEnemy(nextPos, currentCreature)
            isSame = self.isSame(nextPos, currentCreature)
            isHill = self.isTerrian(nextPos, Terrian.HILL)


            # get execute code
            executableOpcode = currentCreature.getExecutableOpcode(isEnemy, isEmpty, isSame, isWall)

            # execute op
            if executableOpcode == OpCode.LEFT:
                currentCreature.turnLeft()

            elif executableOpcode == OpCode.RIGHT:
                currentCreature.turnRight()

            elif executableOpcode == OpCode.HOP:
                print("Try to hop to {0}|{1}".format(nextPos.row, nextPos.column))
                self.hopCurrentCreature(currentCreature, isWall, isEmpty, isHill)
                    
            elif executableOpcode == OpCode.INFECT:
                self.infectTargetEnemy(nextPos, currentCreature)                

            # draw world after behavior
            self.drawWorld()
            # wait for input
            userinput = raw_input("Press any key for Next Round or input 'exit' for stop.\n>")
            print("")
            if(userinput == "exit"):
                break
            

            # next round
            self.__currentRound += 1

        print("Game Over!")
    
    @property
    def isGameOver(self):
        creature1 = self.__creatures[0]
        for createure in self.__creatures:
            if createure.speciesName != creature1.speciesName:
                return False

        return True

    def isEmpty(self, pos):
        if self.isOutBoundary(pos):
            return False

        return self.__creatureMap[pos.row][pos.column] == None
    
    def isWall(self, pos, creature):
        if self.isOutBoundary(pos):
            return True
        
        if creature == None:
            return False # Tricky thing here

        if creature.canFly == False and self.isTerrian(pos, Terrian.LAKE):
            return True
        
        return False

    def isEnemy(self, pos, creature):
        if self.isOutBoundary(pos):
            return False

        if self.isTerrian(pos, Terrian.FOREST):
            return False
        
        if creature == None:
            return False

        hostCreature = self.getCreature(pos)
        if hostCreature == None:
            return False
        
        if hostCreature.speciesName == creature.speciesName:
            return False

        return True

    def isSame(self, pos, creature):
        if self.isOutBoundary(pos):
            return False

        if self.isTerrian(pos, Terrian.FOREST):
            return False
        
        if creature == None:
            return False

        hostCreature = self.getCreature(pos)
        if hostCreature == None:
            return False
        
        if hostCreature.speciesName != creature.speciesName:
            return False

        return True  
    
    def isTerrian(self, pos, terrian):
        if self.isOutBoundary(pos):
            return False

        return self.getTerrian(pos) == terrian       

    def isOutBoundary(self, pos):
        if pos.row < 0 or pos.row >= self.__worldHeight or  \
        pos.column < 0 or pos.column >= self.__worldWidth:
            return True
        
        return False
    
    def getTerrian(self, pos):
        if self.isOutBoundary(pos):
            return None
        
        return self.__terrianMap[pos.row][pos.column]

    def getCreature(self, pos):
        if self.isOutBoundary(pos):
            return None
        
        return self.__creatureMap[pos.row][pos.column]

    def hopCurrentCreature(self, creature, isWall, isEmpty, isHill):
        if isWall:
            print("Ocha...hit a wall")
            return
        
        if isEmpty == False:
            print("Hmm...some creature in the target")
            return

        self.__creatureMap[creature.position.row][creature.position.column] = None
        creature.hop(isHill)
        self.__creatureMap[creature.position.row][creature.position.column] = creature 
    
    def infectTargetEnemy(self, pos, creature):
        print("Try to infect to {0}|{1}".format(pos.row, pos.column))
        if self.isOutBoundary(pos):
            print("Hmm...nothing infected")
            return

        if self.isEnemy(pos, creature):
            targetCreature = self.getCreature(pos)
            targetCreature.infected(creature)
            return
        
        if creature.canArc == False:
            return
        else:
            nextPos = pos.getNextPosition(creature.direction)
            self.infectTargetEnemy(nextPos, creature) # recursive here
        

    def drawWorld(self):
        msg = ""

        for widthIndex in range(self.__worldWidth):
            for heightIndex in range(self.__worldHeight):
                terrian = self.__terrianMap[widthIndex][heightIndex]
                creature = self.__creatureMap[widthIndex][heightIndex]
                isActiveCreature = creature == self.__activeCreature 

                if(isActiveCreature):
                    msg += "<|"
                else:
                    msg += " |"

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
                    if creature.direction == Direction.EAST:
                        msg += ">"
                    elif creature.direction == Direction.WEST:
                        msg += "<"
                    elif creature.direction == Direction.NORTH:
                        msg += "^"
                    elif creature.direction == Direction.SOUTH:
                        msg += "V"

                    # fly
                    msg += "-"
                    if creature.canFly:
                        msg += "F"
                    else:
                        msg += "-"

                    if creature.canArc:
                        msg += "A"
                    else:
                        msg += "-"
                    

                else:
                    msg += "_____"
                
                if(isActiveCreature):
                    msg += "|>"
                else:
                    msg += "| "
            
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
    [Terrian.PLAIN,Terrian.HILL, Terrian.PLAIN],
    [Terrian.LAKE,Terrian.HILL, Terrian.HILL]]

    sw = SimpleWorld(terrianMap, creatureMap, creatures)
    sw.run()


