from WorldEnum import Ability, Direction, OpCode, Terrian
from Position import Position
from Species import Species
from Config import Config
from Instruction import Instruction
from Creature import Creature
from SimpleWorld import SimpleWorld

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