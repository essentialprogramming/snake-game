from config.Settings import Settings
from constants import Constants
from domain.Player import Player
from services.GameService import GameService
from ui.UI import UI
from utils.Utils import Utils


def start():
    settings = Settings.getInstance()
    Constants.ROW_COUNT = int(settings.DIM)
    Constants.COLUMN_COUNT = int(settings.DIM)
    Constants.APPLE_COUNT = int(settings.apple_count)

    player = Player()
    gameService = GameService(player)
    ui = UI(gameService)
    ui.run()


start()
