class Position:
    
    def __init__(self, row, column):
        self.__row = row
        self.__column = column

    @property
    def row(self):
        return self.__row

    @row.setter
    def row(self, value):
        self.__row = value
    
    @property
    def column(self):
        return self.__column

    @column.setter
    def column(self, value):
        self.__column = value

if __name__ == "__main__":
    pos = Position(1,2)
    print(pos.row)
    print(pos.column)
    pos.row = 3
    pos.column = 4
    print(pos.row)
    print(pos.column)