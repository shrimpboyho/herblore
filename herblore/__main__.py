import pyglet
import os
from pyglet.window import key
from pyglet.window import mouse
from pyglet import clock
from pyglet.gl import *

# Import the physics engine
import physics

# Import the player class
from player import *

# Create window
window = pyglet.window.Window()

# Fullscreen toggle variable
first_f1_hit = False

# Scale stuff
glScalef(1.0, 1.0, 1.0)

# Set up custom mouse cursor
mouse_image = pyglet.resource.image('assets/sprites/cursor.png')
cursor = pyglet.window.ImageMouseCursor(mouse_image, 20, 28)
window.set_mouse_cursor(cursor)

# Keyboard input
keys_held = []

@window.event
def on_key_press(symbol, modifiers):
    global first_f1_hit
    keys_held.append(symbol)
    
    # Fullscreen toggle f1 key
    if symbol == key.F1:
        if first_f1_hit == False:
	    window.set_fullscreen(True)
	    player_sprite.x = window.width/2
            player_sprite.y = window.height/2
	    current_player.teleport(current_player.coordX,current_player.coordY,terrain_sprite,window)
	    first_f1_hit = True
	else:
	    window.set_fullscreen(False)
	    player_sprite.x = window.width/2
            player_sprite.y = window.height/2
	    current_player.teleport(current_player.coordX,current_player.coordY,terrain_sprite,window)
	    first_f1_hit = False
    
@window.event
def on_key_release(symbol, modifiers):
    keys_held.pop(keys_held.index(symbol))      

# Mouse input
@window.event
def on_mouse_press(x, y, button, modifiers):
    if button == mouse.LEFT:
        print 'The left mouse button was pressed at (' + str(x) + ','+ str(y) + ')'
	print("Player coordinates:" + str(current_player.coordX) + ',' + str(current_player.coordY))
        print("Map coordinates:" + str(terrain_sprite.x) + ',' + str(terrain_sprite.y))
    if button == mouse.RIGHT:
        print 'The right mouse button was pressed at (' + str(x) + ','+ str(y) + ')'

# Set up background map
terrain_image = pyglet.image.load("herblore/assets/sprites/map.png")
terrain_image.anchor_x = terrain_image.width / 2
terrain_image.anchor_y = terrain_image.height / 2
terrain_sprite =  pyglet.sprite.Sprite(terrain_image)

# Create a player object
current_player = Player("jewishBoy", "Radiant", "Lina")

# Create the custom player HUD stuff
player_name_label = pyglet.text.Label(current_player.username,
                          font_name='Garamond',
                          font_size=18,
                          x=3, y=20)
player_level_label = pyglet.text.Label("Level " + str(current_player.level),
                          font_name='Garamond',
                          font_size=15,
                          x=3, y=3)

# Set up player sprites
player_image = pyglet.resource.image("assets/sprites/player.png")
player_image.anchor_x = player_image.width / 2
player_image.anchor_y = player_image.height / 2
player_sprite = pyglet.sprite.Sprite(player_image)
player_sprite.scale = 0.2

# Set up player in center of the screen
player_sprite.x = window.width/2
player_sprite.y = window.height/2

# Draw the map
terrain_sprite.x = window.width/2
terrain_sprite.y = window.height/2

if(current_player.team == "Dire"):
    current_player.teleport(182,164,terrain_sprite,window)
if(current_player.team == "Radiant"):
    current_player.teleport(-182,-164,terrain_sprite,window)

# Update function called all the time to handle input
def update(interval):
    if key.W in keys_held:
	current_player.coordY += 1
	terrain_sprite.y -= 3
    if key.S in keys_held:
	current_player.coordY -= 1
	terrain_sprite.y += 3
    if key.A in keys_held:
	current_player.coordX -= 1    
	terrain_sprite.x += 3
    if key.D in keys_held:
	current_player.coordX += 1
	terrain_sprite.x -= 3

# Set up interval
clock.schedule_interval(update, .01)

# Draw
@window.event
def on_draw():
    # Clear the current stuff
    window.clear()

    # Draw the terrain
    terrain_sprite.draw()

    # Draw the sprite
    player_sprite.draw()
    
    # Draw the HUD
    player_name_label.draw()
    player_level_label.draw()

# Begin application
pyglet.app.run()

