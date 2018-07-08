import Utils

class Operation:
    def __init__(self, creature):
        self.__creature = creature
        self.__readInstructions()
        self.__ip = 0
        self.__hillFlag = False

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
        if self.__ip > len(self.__speciesInstruction):
            print('The creature {} is done!'.format(self.__creature.getSpecies().name))
            return

        if self.needToSkipInst():
            return

        while True:
            inst = self.__speciesInstruction[self.__ip]
            print('The creature {} run inst: {} with ability {}'.format(self.__creature.getSpecies().name, inst, self.__creature.getAbility()))
            try:
                isEnd = self.parseInstruction(inst)
            except EOFError:
                self.__ip += 1
                break

            if isEnd:
                self.__ip += 1
                break

    def parseInstruction(self, inst):
        if ' ' in inst:
            [cmd, step] = inst.split(' ')
            jumpto = int(step)
            # The real instruction index is from 1
            jumpto = jumpto - 1 if jumpto > 0 else jumpto
            self.runInstructions(cmd, jumpto)
            return False
        else:
            self.runInstructions(inst)
            return True

    def runInstructions(self, cmd, jumpto = 0):
        if cmd == 'hop':
            self.runHopIns()
        elif cmd == 'left':
            self.runLeftIns()
        elif cmd == 'right':
            self.runRightIns()
        elif cmd == 'infect':
            self.runInfectIns()
        elif cmd == 'ifempty':
            self.runIfEmptyIns(jumpto)
        elif cmd == 'ifenemy':
            self.runIfEnemyIns(jumpto)
        elif cmd == 'ifsame':
            self.runIfSameIns(jumpto)
        elif cmd == 'ifwall':
            self.runIfWallIns(jumpto)
        elif cmd == 'go':
            self.runGoIns(jumpto)

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
        self.__ip = to if self.__creature.meetEnemy() else (self.__ip + 1)

    def runIfSameIns(self, to):
        self.__ip = to if self.__creature.meetSame() else (self.__ip + 1)

    def runIfWallIns(self, to):
        self.__ip = to if self.__creature.faceWall() else (self.__ip + 1)

    def runGoIns(self, to):
        self.__ip = to

    def needToSkipInst(self):
        # Jump one round
        if not self.__hillFlag and self.__creature.isInHill():
            self.__hillFlag = not self.__hillFlag
            return True

        if self.__hillFlag:
            self.__hillFlag = not self.__hillFlag

        return False