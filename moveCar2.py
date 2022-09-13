from SEAS import *
from moveCar import CarMovement


class CarMovement2(CarMovement):
    def velHandleling(self):
        if SEAS.input('i') and self.vel < self.maxVel: self.vel += self.acc
        if SEAS.input('k') and self.vel > -self.maxVelBack: self.vel -= self.acc

        if not SEAS.input('i') and self.gear == 1:
            self.vel -= self.acc
            if self.vel < 0: self.vel = 0

        if not SEAS.input('k') and self.gear == -1:
            self.vel += self.acc
            if self.vel > 0: self.vel = 0

    def steerHandleling(self):
        if SEAS.input('j') and self.steerVel > -self.maxSteerVel: self.steerVel -= self.steerAcc;
        if SEAS.input('l') and self.steerVel < self.maxSteerVel: self.steerVel += self.steerAcc; 

        if not SEAS.input('j') and self.steerVel < 0: self.steerVel += self.steerAcc; self.steerVel = 0 if self.steerVel > 0 else self.steerVel
        if not SEAS.input('l') and self.steerVel > 0: self.steerVel -= self.steerAcc; self.steerVel = 0 if self.steerVel < 0 else self.steerVel

        if SEAS.input('j') and SEAS.input('l'): self.steerVel = 0
