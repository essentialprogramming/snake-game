from constants import Constants
from services.ServiceException import ServiceException
from domain.Snake import Snake
from utils.BoardUtils import BoardUtils
from utils.Matrix import Matrix


class GameService:

    def __init__(self, player):
        self.__player = player
        self.__turn = Constants.PLAYER

    @property
    def currentPlayer(self):
        return self.__player

    def moveLeft(self):
        self.currentPlayer.snake.setDirection("LEFT")
        self.moveSnake(1)

    def moveUp(self):
        self.currentPlayer.snake.setDirection("UP")
        self.moveSnake(1)

    def moveRight(self):
        self.currentPlayer.snake.setDirection("RIGHT")
        self.moveSnake(1)

    def moveDown(self):
        self.currentPlayer.snake.setDirection("DOWN")
        self.moveSnake(1)

    def moveSnake(self, n):
        gameBoard = self.currentPlayer.getGameBoard()
        direction = self.currentPlayer.snake.getDirection().lower()
        directionRowIndex, directionColumnIndex = BoardUtils.DIRECTIONS.get(direction)
        for i in range(n):
            board = BoardUtils.clone(gameBoard.getBoard())
            row, column = self.currentPlayer.snake.getHead()
            GameService.validateMove(board, row + directionRowIndex, column + directionColumnIndex)
            eatApple = False
            if board[row + directionRowIndex][column + directionColumnIndex] == Constants.APPLE:
                eatApple = True
            self.moveHead(board, row + directionRowIndex, column + directionColumnIndex, eatApple)
            gameBoard.setBoard(board)

    def moveHead(self, board, row, column, eatApple):
        headRow, headColumn = self.currentPlayer.snake.getHead()
        board[headRow][headColumn] = "+"
        board[row][column] = "*"

        tailRow, tailColumn = self.currentPlayer.snake.removeTail()
        board[tailRow][tailColumn] = Constants.EMPTY
        if eatApple:
            tailRow, tailColumn = self.currentPlayer.snake.getSnakeTail()
            directionRow, directionColumn = self.currentPlayer.snake.getTailDirection()
            self.currentPlayer.snake.growTail(tailRow + directionRow, tailColumn + directionColumn)
            board[tailRow + directionRow][tailColumn + directionColumn] = "+"
        self.currentPlayer.snake.setHead(row, column)

    def placeSnake(self):
        playerBoard = self.currentPlayer.getGameBoard()
        board = BoardUtils.clone(playerBoard.getBoard())

        row, column = BoardUtils.rowCount(board) // 2 - 1, BoardUtils.columnCount(board) // 2
        board, snake_coordinates = GameService.insertSnake(board, row, column)

        playerBoard.setBoard(board)
        self.currentPlayer.snake.addCoordinates(snake_coordinates)

    def placeApples(self):
        applesInserted = False
        while not applesInserted:
            board = self.currentPlayer.getGameBoard().getBoard()
            try:
                for appleCount in range(Constants.APPLE_COUNT):
                    rowIndex, columnIndex = \
                        BoardUtils.randomCustomPosition(board, lambda
                            row, column: not BoardUtils.neighboursContains(board, row, column, "."))
                    board[rowIndex][columnIndex] = Constants.APPLE
                applesInserted = True
            except (ServiceException, ValueError):
                continue

    @staticmethod
    def insertApple(board):
        appleInserted = False
        while not appleInserted:
            try:
                rowIndex, columnIndex = BoardUtils.randomPosition(board)
                if BoardUtils.surroundingContains(board, rowIndex, columnIndex, "."):
                    print("Hmm")
                    raise ServiceException()
                board[rowIndex][columnIndex] = Constants.APPLE
                appleInserted = True
            except ServiceException:
                continue

    @staticmethod
    def insertSnake(board, row, column):
        snake = Snake.createMatrix()

        GameService.validatePosition(board, snake, row, column, 0, 0)
        Matrix.insertMatrixAtPosition(board, snake, row, column, 0, 0)

        return board, Matrix.getCoordinates(board, snake, row, column, 0, 0)

    @staticmethod
    def validatePosition(board, plane, row, column, rowInSubMatrix, columnInSubMatrix):
        position_error = ServiceException("There's not enough space to draw a snake given this start position and "
                                          "direction.")
        overlap_error = ServiceException("The items cannot overlap ")
        if not Matrix.fitsInGrid(board, plane, row, column, rowInSubMatrix, columnInSubMatrix):
            raise position_error
        if Matrix.isOverlapping(board, plane, row, column, rowInSubMatrix, columnInSubMatrix):
            raise overlap_error

    @staticmethod
    def validateMove(board, row, column):
        position_error = ServiceException("Game Over - snake hits the wall!")
        overlap_error = ServiceException("Game Over - snake hits the snake!")
        try:
            Matrix.checkIsInRange(board, row, column)
        except Exception:
            raise position_error
        if board[row][column] == "+":
            raise overlap_error

    def getPlayer(self):
        return self.currentPlayer

    def resetPlayerBoard(self):
        self.currentPlayer.reset()
