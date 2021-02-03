from utils.BoardUtils import BoardUtils
from utils.Utils import Utils


class UI:

    def __init__(self, gameController):
        self.controller = gameController

        self.MENU = {
            1: "1. Move <n>",
            2: "2. Up",
            3: "3. Down",
            4: "4. Left",
            5: "5. Right",
            6: "6. Exit"
        }

        """
        A dictionary containing references to
        certain functions based on user input
        """
        self.commandsDictionary = {
            'move': self.move,
            'up': self.up,
            'down': self.down,
            'left': self.left,
            'right': self.right
        }

        self.INVALID_COMMAND = 'Invalid command, please try again.'
        self.GOODBYE_MESSAGE = 'We are sorry to see you go..'

    def drawSnakeAndApples(self):
        playerBoard = self.controller.getPlayer().getGameBoard()
        self.controller.placeSnake()
        self.controller.placeApples()

        playerBoard = self.controller.getPlayer().getGameBoard()
        BoardUtils.printBoardV4(playerBoard.getBoard())

    def move(self, n=1):
        n = int(n)

        self.controller.moveSnake(n)

        playerBoard = self.controller.getPlayer().getGameBoard()
        BoardUtils.printBoardV4(playerBoard.getBoard())

    def down(self):
        self.controller.moveDown()

        playerBoard = self.controller.getPlayer().getGameBoard()
        BoardUtils.printBoardV4(playerBoard.getBoard())

    def left(self):
        self.controller.moveLeft()

        playerBoard = self.controller.getPlayer().getGameBoard()
        BoardUtils.printBoardV4(playerBoard.getBoard())

    def right(self):
        self.controller.moveRight()

        playerBoard = self.controller.getPlayer().getGameBoard()
        BoardUtils.printBoardV4(playerBoard.getBoard())

    def up(self):
        self.controller.moveUp()

        playerBoard = self.controller.getPlayer().getGameBoard()
        BoardUtils.printBoardV4(playerBoard.getBoard())

    def showMenu(self):
        """
        Prints the menu options
        """
        for value in self.MENU.values():
            print(value)

    def run(self):
        self.showMenu()
        self.drawSnakeAndApples()
        while True:

            try:
                currentCommand, currentArguments = Utils.parseCommand(input("Command: "))

                if currentCommand == "exit":
                    print(self.GOODBYE_MESSAGE)
                    break

                try:
                    currentCommand = currentCommand.lower()
                    self.commandsDictionary[currentCommand](*currentArguments)
                except KeyError:
                    print(self.INVALID_COMMAND)

            except Exception as valueError:
                Utils.handleException(valueError)
                break
