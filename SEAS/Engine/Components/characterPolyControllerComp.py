from SEAS.Engine.Core import *
from SEAS.Engine.Setup import *

import math


class CharacterPolyController:
    def start(self): 
        self.trns = SEAS.getScene().getComponent('TransformPoly')
        self.hitb = SEAS.getScene().getComponent('HitboxPoly')
        
    def update(self): 
        pass

    
    def move(self, angle, vel):
        mX = math.cos(math.radians(angle)) * vel
        mY = math.sin(math.radians(angle)) * vel

        self.moveX(mX)
        self.moveY(mY)


    # make so that points move in the future
    def rotate(self, angle, _axis='centroid'):
        # Cchange the direction that the object is spinning
        self.trns.angle += angle

        if _axis == 'centroid':
            # Find centroid
            xPoints = []
            for p in self.trns.points:
                xPoints.append(p[0])

            yPoints = []
            for p in self.trns.points:
                yPoints.append(p[1])
            
            cX = sum(xPoints)/len(xPoints)
            cY = sum(yPoints)/len(yPoints)
            axis = [cX, cY]

        else:
            axis = _axis


        pygame.draw.circle(SEAS.getCoreModule('Screen').wn, (0, 0, 255), axis, 5)

        # Find all angles
        angles = []
        for p in self.trns.points:
            a = p[0] - axis[0]
            b = p[1] - axis[1]

            if a < 0:
                a = abs(a) + 180
            if b < 0:
                b = abs(b) + 180

            angles.append(
                    math.degrees(math.atan(
                        a / b
                        )))
            
        # Rotate figure
        circles = []
        for p, a in zip(self.trns.points, angles):
            print(p)
            circles.append(
                    [
                    math.sqrt((abs(p[0]-axis[0]))**2 + (abs(p[1]-axis[1]))**2),    # Rad
                    p, # Point on circle
                    a,  # Angle
                    axis # Centr
                    ])
        
        newPs = []
        print(angles)
        for c in circles:
            newP = [
                    math.degrees(math.sin(c[2])) * c[0] + axis[0], # Angle, rad, origon
                    math.degrees(math.cos(c[2])) * c[0] + axis[1]]
            newPs.append(newP)


        for nP, i in zip(newPs, range(len(self.trns.points))):
            self.trns.points[i] = nP



    def drawDir(self):
        len = 50
        lenK1 = math.cos(math.radians(self.trns.angle))*len
        lenK2 = math.sin(math.radians(self.trns.angle))*len

        
        pygame.draw.line(SEAS.coreModules['Screen'].wn,
                (0, 255, 0), 
                (self.trns.points[0][0], self.trns.points[0][1]), 
                (lenK1+self.trns.points[0][0], lenK2+self.trns.points[0][1]) )

    def moveX(self, vel):
        for point in self.trns.points:
            point[0] += vel

    def moveY(self, vel):
        for point in self.trns.points:
            point[1] += vel
