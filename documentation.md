# DOCS
## SEAS (Main Core)
### Variables (that u need to know)


#### SEAS.deltaTime
##### Explenation
The amount of time between frames. Can be used to normalize movement over different amounts of frameLimits.
##### Example use
    self.characterController.moveX(self.vel * SEAS.deltaTime)

#### SEAS.loggingLevel
##### Explenation
The amount of messages SEAS print out. Its defaulted as 'Comment' which is the lowest level. NOTE: This SEAS print feature 
is not yet fully implemented. Only used once in core functions. Works similary with the python package logging.
##### Example use
    SEAS.loggingLevel = 'Warning' # Warning and up
    SEAS.loggingLevel = 'Comment' # Everything
    SEAS.loggingLevel = 'Error' # Only Errors

### Functions (that u need to worry about)
#### createFilePreset
Dont use

#### getCoreModule(coreModName)
Returns the initialized class that is the coreModule of the name u specified.


#### newScene(name, frameLimit, isTargeted, overflowObj)
* Name is self explanitory
* frameLimit also is (check frameLimit above)
* isTargeted is if u want to have that scene as the "main scene" or the scene u want to display from the start. U can later change
this (look downwards) in targetScene(). Also not that after a scene is targeted every new object will be created in that scene.
* Do not use overflowObj. Ur free to but i wont do anything (yet).

#### targetScene(sceneName)
Changes the displayed scene. NOT after change every newly created object will be created in that scene. (Basicly the getScene() 
returns this scene).

#### getScene()
Returns the targeted scene

#### getRawScene(sceneName)
Returns the initialized scene class with specified name.

#### getAllScene()
Returns all the scenes in a dictionary {name: class}

#### transferObject(objectName, toScene, resetObject)
Transfers a object from the tragetedscene to another. You have the option to specify if you want to reset the object initial poses
(defaulted as false)

#### transferRawObject(objectName, fromScene, toScene, resetObject)
Same as transferObject() but u specify from what scene.

#### transferAllObject() and transferRawAllObject()
NOT IMPLEMENTED YET!(yet)

#### createMaterial(materialName, materialColor)
Self explanitory. Get stored in a dictionary. Can get accesed by (look down)

#### addMaterial(materialName, objectName)
Adds a material to a object. Self explanitory

#### getMaterial()
returns the material of the currentObject. Basicly if you call this in a component it returns your objects 
(that the component is attatched to) material. ONLY USE THIS IN A COMPONENT

#### getRawMaterial(materialName)
Returns the color of the material when specified name.

#### getObjectMateirla(objectName)
Returns the material of a object u specifie (in the current scene).

#### input(key)
Ur dum. If u want to look what keys accepted look at pygames system.

#### event
Like pygamames event loop but instead of writing all of that shit u only have to write eventType and equals.

### Concept
SEAS is the core of SEAS. lol. It hosts the core functions. The scene is different that is hosting the objects. U feeeel me.

## Scene
### Variables (that u can care of)
#### framerate
u dum

#### frameLimit
##### Explenation
 The capped frame limit. Defaulted as 60.
##### Example use
    SEAS.getScene().frameLimit = 30

### Functions (that u care of)
#### addObject(objectName, objectModel, hitbox, components, objectLocation)
Returns nothing
objectName is the name of the object
hitbox is a bool and will determine if other object will "ohh collision" while having collidePoly component attatched. In the future 
we will have seperate points for the hitbox
components is a list and is the components that will be attatched to the object
DONT USE OBJECTLOCATIOn. feel free too but it wont do anything

#### getComponent(component)
returns the component that u specify of the object that ur attatcched to. ONLY USE THIS INSIDE A COMPONENT

#### getRawComponent(object, component)
Same as getComponent() but u specify the object

#### getObject()
Returns the object initialized that ur attatched to. ONLY USE THIS IN A COMPONENT

#### getRawObject(objectName)
Returns the object u specify initialized

#### getAllObject()
returns a list of all the initialized objects

#### getAttribute(attribute)
returns a attribute of the object ur attatched to. When u will use this. Maybe in the future I will add getComponentAttribute and than can actually
be useful. ONLY USE THIS WHEN IN A COMPONENT FOR PROPER USE

#### getRawAttribute()
Just like getAttribute but u sepcify object also.

## Components
(NOTE: TransformRect and CollideRect is in the Engine but dont use those)
### TransformPolyComponent
Mandatory for almost all other prebuild components. Have points (more than 3) in a list. Works almost like unities transform. Also have an angle


## MORE COMING SOON


# QUESTIONS
## Just ask me
