from WorldEnum import Direction

class Position:
    
    def __init__(self, row, column):
        self.__row = row
        self.__column = column

    @property
    def row(self):
        return self.__row
    
    @property
    def column(self):
        return self.__column
    
    def getNextPosition(self, direction):
        nextPos = Position(self.row, self.column)
        if(direction == Direction.EAST):
            nextPos.__column += 1
        elif(direction == Direction.WEST):
            nextPos.__column -= 1
        elif(direction == Direction.NORTH):
            nextPos.__row -= 1
        elif(direction == Direction.SOUTH):
            nextPos.__row += 1
        
        return nextPos

if __name__ == "__main__":
    pos = Position(1,2)
    print(pos.row)
    print(pos.column)
    pos.row = 3
    pos.column = 4
    print(pos.row)
    print(pos.column)