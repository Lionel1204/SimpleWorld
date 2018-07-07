class Operation:
    def __init__(self, creature):
        self.__creature = creature
        self.__readInstructions()
        self.__ip = 0

    def __readInstructions(self):
        'open file and read'
        self.__instructions = ''

    def getInstructionsArray(self):
        return self.__instructions

    def runInstructionsOneRound(self):
        while True:
            inst = self.__instructions(self.__ip)
            isEnd = self.parseInstruction(inst)
            if isEnd:
                self.__ip += 1
                break


    def parseInstruction(self, inst):
        realInst = inst.trim()
        if ' ' in realInst:
            [cmd, jumpto] = realInst.split(' ')
            self.runInstructions(cmd, jumpto)
            return False
        else:
            self.runInstructions(inst)
            return True

    def runInstructions(self, cmd, jumpto = 0):
        if cmd is 'hop':
            self.__creature.hop()
        elif cmd is 'left':
            self.__creature.left()
        elif cmd is 'right':
            self.__creature.right()
        elif cmd is 'infect':
            self.__creature.infect()
        elif cmd is 'ifempty':
            pass
        elif cmd is 'ifenemy':
            if not self.__creature.meetSame():
                self.__ip = jumpto
        elif cmd is 'ifsame':
            if self.__creature.meetSame():
                self.__ip = jumpto
        elif cmd is 'ifwall':
            if self.__creature.faceWall():
                self.__ip = jumpto
