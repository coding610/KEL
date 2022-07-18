from Src.gameCore.event import *
from Src.gameCore.core import *
from Src.Components.renderRectComp import *


class compTest:
    def __init__(self) -> None:
        pass

    def start(self):
        pass


    def update(self, comps):
        print(Engine.coreModules['Events'].events)
        #if Engine.coreModules['Events'].events.key('SpaceDown') != None:
         #   comps['Transform'].yPos += 10
        
        return comps
