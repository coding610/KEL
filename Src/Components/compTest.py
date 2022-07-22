from Src.gameCore.event import *
from Src.gameCore.core import *
from Src.Components.transformRectComp import *


class CompTest:
    def __init__(self) -> None:
        pass

    def start(self, components):
        pass


    def update(self, comps):
        events = Engine.coreModules['Events'].events
        if 'SpaceDown' in events:
            comps['TransformRectComp'].yLT += 1

        return comps
