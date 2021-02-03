from configparser import ConfigParser


class Settings:
    __instance = None

    def __init__(self):
        if Settings.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            Settings.__instance = self

        self.config = ConfigParser()
        self.config.read('settings.properties')
        self.DIM = self.config['properties']['DIM']
        self.apple_count = self.config['properties']['apple_count']

    @staticmethod
    def getInstance():
        if Settings.__instance is None:
            Settings()
        return Settings.__instance

