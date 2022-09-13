from SEAS import *
from moveCar import *
from moveCar2 import *

SEAS.loggingLevel = 'Warning'

SEAS.newScene('S1', 60, True)
SEAS.newScene('S2', 60, False)


# Object components
carCords = [[10, 10], [10, 20], [30, 20], [30, 10]]
carComps = [TransformPoly(carCords), RenderPoly(), CharacterPolyController(), CarMovement(), HitboxPoly(points=carCords, moveHitbox=True), CollidePoly()]

testCords = [[200, 200], [300, 200], [300, 300], [200, 300]]
testComps = [TransformPoly(testCords), RenderPoly(), HitboxPoly(points=testCords, moveHitbox=False), CarMovement2(), CharacterPolyController(), CollidePoly()]

# Create objects
SEAS.getScene().addObject(objectName='Car', components=carComps)
SEAS.getScene().addObject(objectName='Test', components=testComps)

# Object hitboxes
SEAS.createHitboxGroup('Finish', True)
SEAS.addNameHitboxGroup('Finish', ['Car', 'Test'])

# Create Materials
SEAS.createMaterial(materialName='Car', materialColor='#d65d0e')
SEAS.createMaterial(materialName='Test', materialColor='#ffffff')

# Adding Materials
SEAS.addMaterial(materialName='Car', objectName='Car')
SEAS.addMaterial(materialName='Test', objectName='Test')


SEAS.coreModules['Screen'].color = "#282828"


run()
