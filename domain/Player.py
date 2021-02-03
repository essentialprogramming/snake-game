from domain.Board import Board
from domain.Snake import Snake


class Player:

    def __init__(self):
        self.__gameBoard = Board()
        self.__snake = Snake()

    @property
    def snake(self):
        return self.__snake

    def getGameBoard(self):
        return self.__gameBoard

    def setGameBoard(self, gameBoard=None):
        if gameBoard is None:
            gameBoard = Board()
        self.__gameBoard = gameBoard

    def reset(self):
        self.__gameBoard = Board()
        self.__snake = Snake()

