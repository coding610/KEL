from Src.pygameSetup import *
from Src.Const import *

class RenderRectComp:
    def start(self, components):
        try: components['TransformRectComp']
        
        except KeyError as err: print("Component", err, "not found")


    def update(self, components):
        lY, lX, w, h = components['TransformRectComp'].xLT, components['TransformRectComp'].yLT, components['TransformRectComp'].width, components['TransformRectComp'].height
        pygame.draw.rect(wn, playerColor, pygame.Rect((lX, lY), (w, h)))



        return components
