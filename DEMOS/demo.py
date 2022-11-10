from SEAS import *
from demoFood import *
from demoPlayer import *

import random

scene = SEAS.newScene('MainScene', True)

# Objects
playerCoords = [ [100, 100], [120, 100], [120, 150], [100, 170], [50, 64] ]
playerComps = [TransformPoly(playerCoords, -90), RenderPoly(), CharacterPolyController(), HitboxPoly(), PlayerMovement(), CollidePoly()]
scene.addObject('Player', components=playerComps)
scene.addObject('FoodCreater', components=[FoodCreater()])

# Hitbox
SEAS.createHitboxGroup('PlayerColl', True)
SEAS.addRawNameHitboxGroup('PlayerColl', ['Player'])

# Mat
SEAS.createMaterial('PlayerMat', "#d65d0e")
SEAS.addMaterial('PlayerMat', 'Player')
SEAS.coreModules['Screen'].color = '#282828'


run()
