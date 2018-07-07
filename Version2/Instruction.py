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

if __name__ == "__main__":
    ins = Instruction(OpCode.HOP, 10)
    print(ins.opCode)
    print(ins.targetAddr)