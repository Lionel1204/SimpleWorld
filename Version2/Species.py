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

if __name__ == "__main__":
    ins1 = Instruction(OpCode.HOP, None)
    ins2 = Instruction(OpCode.IFEMPTY, 10)
    inss = [ins1, ins2]
    spec = Species("FLYTRAP", inss)
    print(spec.name)
    print(spec.insLength)
    print(spec.instructions)
