from Src.Models import *
from Src.gameCore import *
from Src.Components import *
from Src.Components.compTest import *

from Assets import *

import sys

def game():
    objects = {}
    objects['Wall'] = emptyModel()
    objects['Wall'].addComponent([ TransformRectComp(100, 100, 10, 100), RenderRectComp(), CompTest() ])

    # Loop thru created objects and start them
    for start in objects:
        objects[start].start()


    while True:
        Engine.updateModules()

        if 'Quit' in Engine.coreModules['Events'].events:
            sys.exit()


        # Wn Fill
        wn.fill(bgColor)

        # Loop thru created objects and update them thru the update function
        for update in objects:
            objects[update].update()


        # Update Display
        pygame.display.update()



# Security
if __name__ == "__main__":
    game()
