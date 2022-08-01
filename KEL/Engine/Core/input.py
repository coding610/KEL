from KEL.Engine.Game.pygameSetup import *
from KEL.Engine.Core.core import *


def Input(eventEquals):
    for event in KELCORE.coreModules['Events'].events:    

        if hasattr(event, 'key'):
            pygameAttr = getattr(pygame, eventEquals)
            if event.key == pygameAttr:
                return True
