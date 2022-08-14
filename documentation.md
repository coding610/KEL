# Core (KEL)
The core in this framework is called KEL (also the libarys name). It has many functions and it will be displayed here:

## Variables
### KEL.framerate
This holds the framerate to the game. NOTE: this is not the frameLimit.

### KEL.frameLimit
Defaulted as 60.
This is the speed the game is running. It controls how many frames the game loads per second.

### KEL.deltaTime
This is the time between the frames. It can be used to create an frame independent game. (look at demo)


## Methods ur sposed to use
### KEL.addObject()
#### Parameters: 
* STR: objectName: This is self explanatory. Defaulted as "emptyModel"

* CLASS: objectModel: This is the model u can use. By the moment there is only EmptyModel(). Defaulted as EmptyModel() In the future it might be like: triangle or rect.

* BOOL: hitbox: This is if u want ur object to have a hitbox or nah. The hitbox is the transformComponents
values.

* LIST: components: This is the additional components u would like to add. There are prebuild components but u can make ur own by copying the component layout on the readme or just write it.

* STR: objectLocation: Experimental. DO NOT USE.

#### Deskription:
ur dum


### KEL.getComponent()
#### Parameters
* STR: Component: What component u would like.

#### Deksription
When u call this ur ovbiusly in a component. That component is attatched to a object. That object probably has other compnents.
This function takes a componentName as a parameter and returns a component of your object.

### KEL.getRawComponent()
#### Parameters
* STR: object
* STR: component

#### Deskription
Its like getComponent() but we sepcify an object

### KEL.getObject()
#### Parameters: None

#### Description
Returns the object that the component thats calling is attatched to

### KEL.getRawObject()
#### Prameters
* STR: object

#### Description
We specify a objectName (look at the parameter objectName at KEL.addObject())

### KEL.getAllObject()
#### Parameters: None

#### Description
It returns all the objects in a list format

### KEL.getAttribute()
#### Parameters
* STR: attribute

#### Description
This is the attribute of the currentObject (such as idk material or hitbox)

### KEL.getRawAttribute()
#### Parameters
* STR: object
* STR: attribute

#### Description
The attribute of an object u specify

### KEL.Input()
#### Parameters
* STR: inputKey ex: 'K_a'
* STR: state ex: 'Down' Defaulted as 'Down'

#### Description
inputKey is the key that u want to check and state is where ever u should check if its being put up or down.
Whats a legal inputKey. Checks pygames keys and just remove 'pygame.' and ur good.

### KEL.rawInput()
#### Parameters
* STR: leftSide
* STR: rightSide

#### Description
its basicly a pygame event loop. U just do a mental conversion between 'if pygame.type == pygame.KEYDOWN' 
and 'KEL.rawInput('type', 'KEYDOWN')'. u get me.

### KEL.createMaterial()
#### Parameters
* STR: materialName
* STR: materialColor

#### Description
Creates and saves a material for further use

### KEL.addMaterial()
#### Parameters
* STR: materialName
* STR: objectName

#### Description
Takes a already created material with the createMaterial method and adds it to an object sepcified by a objectName

### KEL.getMaterial()
#### Parameters: None

#### Description
Gets the material of the component that is callings object.

### KEL.getRawMaterial()
#### Parameters
* materialName
#### Description
Returns the color of the materialName u just passed

### KEL.getObjectMaterial()
#### Parameters: 
* objectName
#### Description
gets the material of the object u just passed

### KEL.createFilePreset() (DO NOT USE EXPERIMENTAL ONLY)


# Components and what are they?
Components are a class that can be added to an object.

## Prebuild components:
### TransformPolyComp()
The transformPolyComponent (positions) of a object. it takes one init parameter: LIST of points
It has two methods that u can call.
moveX() : Parameters : changeX
moveY() : Parameters : changeY


### TransformRectComp():
The transformRectComponent (positions) of a object.
#### Parameters:
* xLT (x left top)
* yLT (y left top)
* widht
* height

### CollidePolyComp()
It collides with every object that has the bool hitbox to True (see add object)
#### Parameters:
* None

### CollideRectComp does not exist yet. Just use collidePoly and transformPoly

### GravityComp: 
#### Parameters: None
#### Description
Adds gravity to a object.
EXPERIMENTAL: just use ur own


### RenderRectComp
#### Parameters: None
#### Description
render a rect

### RenderPolyComp
#### Parameters: None
#### Description
render a poly




## CompnentPreset
    class yourComponent:
        # Called before the first frame
        def start():
            # Here u can get components and stuff and decleare vars

        # Called every frame
        def update():
            # Here u do u




# DOCS END
To learn further look at example or ask in the issues tab.
MORE FEATURES WILL COME
