import numpy as np
from Square import Square
from Utils import Terrain

class Grid:
    def __init__(self):
        self.__squares = None

    def initializeGrid(self, m, n):
        self.createSquares(m, n)
        #createCreatures()
        #connectSquares()
        #putCreaturesInSquares()


    def createSquares(self, m, n):
        squareTerrain = np.random.randint(4, size=(m, n))
        squareGenerator = lambda t: Square(Terrain(t))

        self.__squares = np.vectorize(squareGenerator)(squareTerrain)
        print 'Grid with {} X {} squares is generated!'.format(m, n)