from Src.pygameSetup import *


class Events:
    def __init__(self):
        self.events = {}

    def update(self):
        self.events = {}

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.events['Quit'] = 1

            if event.type == pygame.KEYDOWN:
                self.events['KeyDown'] = 1

                if event.key == pygame.K_SPACE:
                    self.events['SpaceDown'] = 1

            if event.type == pygame.KEYUP:
                self.events['KeyUp'] = 1

                if event.key == pygame.K_SPACE:
                    self.events['SpaceUp'] = 1
