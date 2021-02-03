import collections

from constants import Constants
from utils.BoardUtils import BoardUtils
from utils.Matrix import Matrix


class Snake(object):
    """description of class"""

    def __init__(self):
        self.snakeCoordinates = collections.deque([])
        self.direction = "UP"

    @staticmethod
    def createMatrix():
        """
        Creates the snake matrix for the up direction
        What the matrix has to look like
          *
          +
          +
        """
        snake_matrix = BoardUtils.createBoard(Constants.EMPTY, 3, 1)
        snake_matrix[0][0] = '*'
        snake_matrix[1][0] = '+'
        snake_matrix[2][0] = '+'
        return snake_matrix

    def getDirection(self):
        return self.direction

    def setDirection(self, direction):
        self.direction = direction

    def addCoordinates(self, snakeCoordinates):
        self.snakeCoordinates.clear()
        self.snakeCoordinates.extend(snakeCoordinates)

    def getCoordinates(self):
        return self.snakeCoordinates

    def getHead(self):
        return self.snakeCoordinates[0]

    def setHead(self, row, column):
        self.snakeCoordinates.appendleft((row, column))

    def growTail(self, row, column):
        self.snakeCoordinates.append((row, column))

    def removeTail(self):
        tailRow, tailColumn = self.snakeCoordinates.pop()
        return tailRow, tailColumn

    def getSnakeTail(self):
        tailRow, tailColumn = self.snakeCoordinates[len(self.snakeCoordinates) - 1]
        return tailRow, tailColumn

    def getTailDirection(self):
        """
         Get relative position between last two elements from the tail
              *
              +       =      down
              +

              *+++    =      right
         """
        row, column = self.snakeCoordinates[len(self.snakeCoordinates) - 2]
        row2, column2 = self.snakeCoordinates[len(self.snakeCoordinates) - 1]
        return Matrix.direction(row, column, row2, column2)
