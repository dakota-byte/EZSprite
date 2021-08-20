### EZSprite

Drawing maps onto pygame was too hard. And adding collisions, and making the screen scroll. BLAH! Too hard. So I made this.

And it probably sucks. But it works... for me at least

Interactives makes it easy to tell when a player is standing in a specific tile (for cutscenes, shops, etc)

### First you'd create references to the directory of your CSV files:

interactives = "Assets/interactives.csv"

foundation = "Assets/foundation.csv"

decoration = "Assets/decoration.csv"

### Next, use EZSprite.SimpleSprite to create a SimpleSprite of 16 bit, and scale the size up to 2

visualSpritesheet = SimpleSprite("Assets/dungeonsprites.png", 16, 2)

visualSpritesheet.addCSV(foundation)

visualSpritesheet.addCSV(decoration)

### We'll create another spritesheet for the interactives

interactiveSpriteSheet = SimpleSprite("Assets/interactions.png", 16, 2) # These can be transparent tiles you use for the sake of player interactions

interactiveSpriteSheet.addCSV(interactives)

### Now we use EZSprite.MultiSprite to create a scene

scene1 = MultiSprite()

scene1.addSimpleSprite(spritesheet)

scene1.addInteractive(spritesheet2)

scene1.defineSceneBounds(config.scene1bounds) # These are the tile id's that the player cannot collide with

scene1.defineSceneiBounds(config.scene1interactions) # These are the tile id's that the player can interact with

### Now we can use our scene

scene1.drawEntireScene(WINDOW, self.screen_location_x, self.screen_location_y)

### and bam you got yourself a thing on a screen

### the more i write this the more i realize how bad this actually is so im just gonna stop here cause i doubt anyones ever gonna this

### chao
