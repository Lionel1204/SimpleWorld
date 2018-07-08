import Utils

class Operation:
    def __init__(self, creature):
        self.__creature = creature
        self.__readInstructions()
        self.__ip = 0

    def __readInstructions(self):
        self.__instructions = Utils.loadJson('./Instruction.json')
        self.changeSpecies()

    def changeSpecies(self, species=None):
        if species is None:
            species = self.__creature.getSpecies()
        self.__speciesInstruction = self.__instructions[species.name]
        # If species has been change, the instructions should restart
        self.__ip = 0
        print self.__speciesInstruction

    def getInstructionsArray(self, species=None):
        return self.__instructions if species is None else self.__speciesInstruction

    def runInstructionsOneRound(self):
        while True:
            inst = self.__speciesInstruction[self.__ip]
            print('The creature {} run inst: {}'.format(self.__creature.getSpecies().name, inst))
            isEnd = self.parseInstruction(inst)
            if isEnd:
                self.__ip += 1
                break


    def parseInstruction(self, inst):
        if ' ' in inst:
            [cmd, jumpto] = inst.split(' ')
            # The real instruction index is from 1
            jumpto = jumpto - 1 if jumpto > 0 else jumpto
            self.runInstructions(cmd, jumpto)
            return False
        else:
            self.runInstructions(inst)
            return True

    def runInstructions(self, cmd, jumpto = 0):
        if cmd is 'hop':
            self.runHopIns()
        elif cmd is 'left':
            self.runLeftIns()
        elif cmd is 'right':
            self.runRightIns()
        elif cmd is 'infect':
            self.runInfectIns()
        elif cmd is 'ifempty':
            self.runIfEmptyIns(jumpto)
        elif cmd is 'ifenemy':
            self.runIfEnemyIns(jumpto)
        elif cmd is 'ifsame':
            self.runIfSameIns(jumpto)
        elif cmd is 'ifwall':
            self.runIfWallIns(jumpto)

    def runHopIns(self):
        self.__creature.hop()

    def runLeftIns(self):
        self.__creature.left()

    def runRightIns(self):
        self.__creature.right()

    def runInfectIns(self):
        self.__creature.infect()

    def runIfEmptyIns(self, to):
        self.__ip = to if self.__creature.isNextSquareAvailable() else (self.__ip + 1)

    def runIfEnemyIns(self, to):
        self.__ip = to if not self.__creature.meetSame() else (self.__ip + 1)

    def runIfSameIns(self, to):
        self.__ip = to if self.__creature.meetSame() else (self.__ip + 1)

    def runIfWallIns(self, to):
        self.__ip = to if self.__creature.faceWall() else (self.__ip + 1)
