from WorldEnum import OpCode

class Instruction:

    def __init__(self, opCode, targetAddr):
        self.__opCode = opCode
        self.__targetAddr = targetAddr
    
    @property
    def opCode(self):
        return self.__opCode

    @property
    def targetAddr(self):
        return self.__targetAddr

    @staticmethod    
    def createAttackInstructions():
        ins0 = Instruction(OpCode.IFENEMY, 10)
        ins1 = Instruction(OpCode.IFSAME, 6)
        ins2 = Instruction(OpCode.IFWALL, 8)
        ins3 = Instruction(OpCode.IFEMPTY, 4)
        ins4 = Instruction(OpCode.HOP, None)
        ins5 = Instruction(OpCode.GO, 0)
        ins6 = Instruction(OpCode.RIGHT, None)
        ins7 = Instruction(OpCode.GO, 0)
        ins8 = Instruction(OpCode.LEFT, None)
        ins9 = Instruction(OpCode.GO, 0)
        ins10 = Instruction(OpCode.INFECT, None)
        ins11 = Instruction(OpCode.GO, 0)
        inss = [ins0, ins1, ins2,ins3, ins4, ins5, ins6, ins7, ins8, ins9, ins10, ins11]
        return inss
    
    @staticmethod
    def createEscapeInstructions():
        ins0 = Instruction(OpCode.IFENEMY, 6)
        ins1 = Instruction(OpCode.IFSAME, 6)
        ins2 = Instruction(OpCode.IFWALL, 8)
        ins3 = Instruction(OpCode.IFEMPTY, 4)
        ins4 = Instruction(OpCode.HOP, None)
        ins5 = Instruction(OpCode.GO, 0)
        ins6 = Instruction(OpCode.RIGHT, None)
        ins7 = Instruction(OpCode.GO, 0)
        ins8 = Instruction(OpCode.LEFT, None)
        ins9 = Instruction(OpCode.GO, 0)
        ins10 = Instruction(OpCode.INFECT, None)
        ins11 = Instruction(OpCode.GO, 0)
        inss = [ins0, ins1, ins2,ins3, ins4, ins5, ins6, ins7, ins8, ins9, ins10, ins11]
        return inss
    
    @staticmethod
    def createHopAllInstructions():
        ins0 = Instruction(OpCode.IFENEMY, 4)
        ins1 = Instruction(OpCode.IFSAME, 4)
        ins2 = Instruction(OpCode.IFWALL, 4)
        ins3 = Instruction(OpCode.IFEMPTY, 4)
        ins4 = Instruction(OpCode.HOP, None)
        ins5 = Instruction(OpCode.GO, 0)
        ins6 = Instruction(OpCode.RIGHT, None)
        ins7 = Instruction(OpCode.GO, 0)
        ins8 = Instruction(OpCode.LEFT, None)
        ins9 = Instruction(OpCode.GO, 0)
        ins10 = Instruction(OpCode.INFECT, None)
        ins11 = Instruction(OpCode.GO, 0)
        inss = [ins0, ins1, ins2,ins3, ins4, ins5, ins6, ins7, ins8, ins9, ins10, ins11]
        return inss

    @staticmethod
    def createAttackAllInstructions():
        ins0 = Instruction(OpCode.IFENEMY, 10)
        ins1 = Instruction(OpCode.IFSAME, 10)
        ins2 = Instruction(OpCode.IFWALL, 10)
        ins3 = Instruction(OpCode.IFEMPTY, 10)
        ins4 = Instruction(OpCode.HOP, None)
        ins5 = Instruction(OpCode.GO, 0)
        ins6 = Instruction(OpCode.RIGHT, None)
        ins7 = Instruction(OpCode.GO, 0)
        ins8 = Instruction(OpCode.LEFT, None)
        ins9 = Instruction(OpCode.GO, 0)
        ins10 = Instruction(OpCode.INFECT, None)
        ins11 = Instruction(OpCode.GO, 0)
        inss = [ins0, ins1, ins2,ins3, ins4, ins5, ins6, ins7, ins8, ins9, ins10, ins11]
        return inss
    
    @staticmethod
    def createAttackNoEmptyInstructions():
        ins0 = Instruction(OpCode.IFENEMY, 10)
        ins1 = Instruction(OpCode.IFSAME, 10)
        ins2 = Instruction(OpCode.IFWALL, 8)
        ins3 = Instruction(OpCode.IFEMPTY, 4)
        ins4 = Instruction(OpCode.HOP, None)
        ins5 = Instruction(OpCode.GO, 0)
        ins6 = Instruction(OpCode.RIGHT, None)
        ins7 = Instruction(OpCode.GO, 0)
        ins8 = Instruction(OpCode.LEFT, None)
        ins9 = Instruction(OpCode.GO, 0)
        ins10 = Instruction(OpCode.INFECT, None)
        ins11 = Instruction(OpCode.GO, 0)
        inss = [ins0, ins1, ins2,ins3, ins4, ins5, ins6, ins7, ins8, ins9, ins10, ins11]
        return inss

if __name__ == "__main__":
    ins = Instruction(OpCode.HOP, 10)
    print(ins.opCode)
    print(ins.targetAddr)