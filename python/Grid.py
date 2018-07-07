import numpy as np
from Square import Square
from Utils import Terrain

class Grid:
    def __init__(self):
        self.__squares = None

    def initializeGrid(self, gridM, gridN, creatureNum):
        self.createSquares(gridM, gridN)
        self.createCreatures(creatureNum)
        #putCreaturesInSquares()

    def createSquares(self, m, n, terrain=None):
        if terrain is None:
            squareTerrain = np.random.randint(len(Terrain), size=(m, n))
        else:
            squareTerrain = np.full((m,n), terrain.value)
        squareGenerator = lambda t: Square(Terrain(t))

        self.__squares = np.vectorize(squareGenerator)(squareTerrain)
        self.connectSquares(m, n)
        print 'Grid with {} X {} squares is generated!'.format(m, n)

    def connectSquares(self, m, n):
        for i in range(m):
            for j in range(n):
                north = self.__squares[i - 1][j] if i - 1 >= 0 else None
                east = self.__squares[i][j + 1] if j + 1 < n else None
                south = self.__squares[i + 1][j] if i + 1 < m else None
                west = self.__squares[i][j - 1] if j - 1 >= 0 else None
                self.__squares[i][j].setConnection(north, east, south, west)

    def createCreatures(self, number):
        pass