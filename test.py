from SEAS import *
from moveCar import *

'''
SEAS.loggingLevel = 'Error'

SEAS.newScene('S1', 60, True)
SEAS.newScene('S2', 60, False)

carCords = [[10, 10], [10, 20], [30, 20], [30, 10]]
carComps = [TransformPoly(carCords), RenderPoly(), CharacterPolyController(), CarMovement()]

testCords = [[200, 200], [300, 200], [300, 300], [200, 300]]
testComps = [TransformPoly(testCords), RenderPoly()]


SEAS.getScene().addObject(objectName='Car', components=carComps)
SEAS.getScene().addObject(objectName='Test', components=testComps)

# Create Materials
SEAS.createMaterial(materialName='Car', materialColor='#d65d0e')
SEAS.createMaterial(materialName='Test', materialColor='#ffffff')

# Adding Materials
SEAS.addMaterial(materialName='Car', objectName='Car')
SEAS.addMaterial(materialName='Test', objectName='Test')


SEAS.coreModules['Screen'].color = "#282828"
'''
run()
