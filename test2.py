from SEAS import *
import time
import random

class PlayerMovement:
    def start(self):
        self.cntrl = SEAS.getScene().getComponent('CharacterPolyController')
        self.trns = SEAS.getScene().getComponent('TransformPoly')
        self.coll = SEAS.getScene().getComponent('CollidePoly')
        
        self.steerVel = 0.0 
        self.maxSteerVel = 4
        self.steerAcc = 1
        self.steerB = None

        self.gear = 1
        self.vel = 0.0
        self.drift = None
        self.acc = 10
        self.maxVel = 999 
        self.maxVelBack = 300

    def update(self):
        # VEL HANDLELING
        self.gearHandleling()
        self.steerHandleling()
        self.velHandleling()
        self.driftHandleling()
        self.moveCar()
        self.cntrl.drawDir()

    def velHandleling(self): 
        if SEAS.input('w') and self.vel < self.maxVel: self.vel += self.acc
        if SEAS.input('s') and self.vel > -self.maxVelBack: self.vel -= self.acc

        if not SEAS.input('w') and self.gear == 1:
            self.vel -= self.acc
            if self.vel < 0: self.vel = 0

        if not SEAS.input('s') and self.gear == -1:
            self.vel += self.acc
            if self.vel > 0: self.vel = 0
    
    def steerHandleling(self):
        if SEAS.input('a') and self.steerVel > -self.maxSteerVel: self.steerVel -= self.steerAcc;
        if SEAS.input('d') and self.steerVel < self.maxSteerVel: self.steerVel += self.steerAcc; 

        if not SEAS.input('a') and self.steerVel < 0: self.steerVel += self.steerAcc; self.steerVel = 0 if self.steerVel > 0 else self.steerVel
        if not SEAS.input('d') and self.steerVel > 0: self.steerVel -= self.steerAcc; self.steerVel = 0 if self.steerVel < 0 else self.steerVel

        if SEAS.input('a') and SEAS.input('d'): self.steerVel = 0

    def driftHandleling(self):
        pass

    def gearHandleling(self):
        if self.vel > 0:  self.gear = 1
        if self.vel == 0: self.gear = 0
        if self.vel < 0: self.gear = -1

    def moveCar(self):
        self.cntrl.move(self.trns.angle, self.vel * SEAS.deltaTime)
        self.cntrl.rotate(self.steerVel)

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

SEAS.newScene('MainScene', True)

# Objects
playerCoords = [ [100, 100], [120, 100], [120, 120], [100, 120] ]
trailComps = [ [200, 200], [220, 200], [220, 220], [200, 220] ]

playerComps = [TransformPoly(playerCoords), RenderPoly(), CharacterPolyController(), HitboxPoly(), PlayerMovement(), CollidePoly()]
trailComps = [TransformPoly(playerCoords), RenderPoly(), CharacterPolyController(), HitboxPoly(), PlayerMovement(), CollidePoly()]

SEAS.getScene().addObject('Trail', components=trailComps)
SEAS.getScene().addObject('Player', components=playerComps)
SEAS.getScene().addObject('FoodCreater', components=[FoodCreater()])

# Hitbox
SEAS.createHitboxGroup('PlayerColl', True)
SEAS.addRawNameHitboxGroup('PlayerColl', ['Player'])

# Mat
SEAS.createMaterial('PlayerMat', "#d65d0e")
SEAS.addMaterial('PlayerMat', 'Player')
SEAS.coreModules['Screen'].color = '#282828'


run()
