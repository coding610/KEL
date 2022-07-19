from Src.gameCore.event import *
from Src.pygameSetup import *


class GameCore:
    def __init__(self):
        self.coreModules = {'Events': Events()}


    def updateModules(self):
        for module in self.coreModules:
            self.coreModules[module].update()


Engine = GameCore()
