from SEAS import *
from demoFood import *
from demoPlayer import *

import random

scene = SEAS.addScene('MainScene', frameLimit=60, isTargeted=True)

# Objects
playerCoords = [ [100, 100], [120, 100], [120, 150], [100, 170], [50, 64] ]
playerComps = [TransformPoly(playerCoords, -90), RenderPoly(), CharacterPolyController(), HitboxPoly(), PlayerMovement(), CollidePoly()]
scene.addObject('Player', components=playerComps)
scene.addObject('FoodCreater', components=[FoodCreater()])

# Hitbox
SEAS.createHitboxGroup('PlayerColl', True)
SEAS.addRawNameHitboxGroup('PlayerColl', ['Player'])
SEAS.createHitboxGroup('test', True)
SEAS.addRawNameHitboxGroup('test', ['Player'])

# Font
font1 = SEAS.getCoreModule('Font').createFont('SiggboFont')
scene.addText(font=font1, textName='SiggboText', text='Hello, My name is sixten', color="#f0f0f0", position=[200, 200])

# Mat
SEAS.createMaterial('PlayerMat', "#d65d0e")
SEAS.addMaterial('PlayerMat', 'Player')
SEAS.coreModules['Screen'].color = '#282828'

run()
