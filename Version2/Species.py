from WorldEnum import OpCode
from Instruction import Instruction

class Species:

    def __init__(self, name, instructions):
        self.__name = name
        self.__instructions = instructions
        self.__insLength = len(instructions)
    
    @property
    def name(self):
        return self.__name
    
    @property
    def instructions(self):
        return self.__instructions

    @property
    def insLength(self):
        return self.__insLength

    def runToExecutableAddr(self, inputAddr, isEnemy, isEmpty, isSame, isWall):
        '''
        execute the instruction forward
        return the address where the execution stop
        '''
        currentAddr = inputAddr
        if inputAddr >= self.__insLength or inputAddr < 0:
            currentAddr = 0

        currentIns = self.__instructions[currentAddr]
        currentInsOpCode = currentIns.opCode
        if currentInsOpCode == OpCode.HOP or  \
        currentInsOpCode == OpCode.LEFT or  \
        currentInsOpCode == OpCode.RIGHT or  \
        currentInsOpCode == OpCode.INFECT:
            return currentAddr

        elif currentInsOpCode == OpCode.GO or  \
        (currentInsOpCode == OpCode.IFSAME and isSame) or  \
        (currentInsOpCode == OpCode.IFEMPTY and isEmpty) or  \
        (currentInsOpCode == OpCode.IFENEMY and isEnemy) or  \
        (currentInsOpCode == OpCode.IFWALL and isWall):
            return self.runToExecutableAddr(currentIns.targetAddr, isEnemy, isEmpty, isWall, isSame) 

        else:
            return self.runToExecutableAddr(currentAddr + 1, isEnemy, isEmpty, isWall, isSame)

    
    def getOpcode(self, inputAddr):
        currentAddr = inputAddr
        if inputAddr >= self.__insLength or inputAddr < 0:
            currentAddr = 0
        
        return self.__instructions[currentAddr].opCode
        

if __name__ == "__main__":
    ins1 = Instruction(OpCode.HOP, None)
    ins2 = Instruction(OpCode.IFEMPTY, 10)
    inss = [ins1, ins2]
    spec = Species("FLYTRAP", inss)
    print(spec.name)
    print(spec.insLength)
    print(spec.instructions)
