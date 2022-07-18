from Src.Const import *
from Src.pygameSetup import *


class RenderPolyComp:
    
    def start(self, components):
        try: components['TransformPolyComp']

        except KeyError as err: print("Component", err, "not found")


    def update(self, components):
        try: pygame.draw.polygon(wn, playerColor, components['TransformComp'].points, 0)

        except KeyError: pass

        return components
