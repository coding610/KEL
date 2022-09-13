from SEAS import *


class CarMovement:
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
        self.maxVelBack = 5

    def update(self):
        # VEL HANDLELING
        self.gearHandleling()
        self.steerHandleling()
        self.velHandleling()
        self.driftHandleling()
        self.moveCar()
        self.newMap()
        self.toggleHitbox()
    
    def toggleHitbox(self):
        if SEAS.input('SPACE') and SEAS.getHitboxGroupState('Finish'):
            SEAS.toggleHitboxGroup('Finish')


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
        self.cntrl.drawDir()

    def newMap(self):
        if self.coll.collide:
            SEAS.transferObject('Car', 'S2', resetObject=False)
            SEAS.targetScene('S2')
