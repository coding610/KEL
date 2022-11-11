from SEAS import *


class FoodCreater:
    def start(self):
        self.counter = 0.0
        self.nameAddon = 0

    def update(self):
        self.counter += SEAS.deltaTime*100

        if self.counter > 200:
            self.nameAddon += 1
            self.counter = 0.0
            self.createFood()


    def createFood(self):
        wW, wH = SEAS.coreModules['Screen'].wW, SEAS.coreModules['Screen'].wH
        cords = self.rndPos()
        SEAS.getScene().addObject('Food' , components=[TransformPoly(cords), RenderPoly(), Food(), CollidePoly(), HitboxPoly()])

    def rndPos(self):
        wW = SEAS.coreModules['Screen'].wW
        wH = SEAS.coreModules['Screen'].wH


        change = 10

        posX1 = random.randint(1, wW)
        posX2 = posX1 + change

        posY1 = random.randint(1, wH)
        posY2 = posY1 + change

        return [ [posX1, posY1], [posX2, posY1], [posX2, posY2], [posX1, posY2] ]

    
class Food:
    def start(self):
        SEAS.addRawInitHitboxGroup('PlayerColl', [SEAS.getScene().getObject()])
        self.counter = 0.0
        self.coll = SEAS.getScene().getComponent('CollidePoly')

    def update(self):
        self.counter += SEAS.deltaTime*100

        if self.counter > 200:
            self.counter = 0.0
        self.eaten()

    def eaten(self):
        if self.coll.collide:
            SEAS.getScene().removeObject()
