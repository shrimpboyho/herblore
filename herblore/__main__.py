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
    if symbol == key.F1:
        if first_f1_hit == False:
	    window.set_fullscreen(True)
	    first_f1_hit = True
	else:
	    window.set_fullscreen(False)
	    first_f1_hit = False

@window.event
def on_key_release(symbol, modifiers):
    keys_held.pop(keys_held.index(symbol))      

# Mouse input
@window.event
def on_mouse_press(x, y, button, modifiers):
    if button == mouse.LEFT:
        print 'The left mouse button was pressed.'
    if button == mouse.RIGHT:
        print 'The right mouse button was pressed.'

# Set up background map
terrain_image = pyglet.image.load("herblore/assets/sprites/map.png")
terrain_sprite =  pyglet.sprite.Sprite(terrain_image)

# Create a player object
current_player = Player("jewishBoy", "Dire", "Lina")

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
player_sprite = pyglet.sprite.Sprite(player_image)
player_sprite.scale = 0.2

# Set up player spawn point based on team
if(current_player.team == "Dire"):
    player_sprite.x = 330.15
    player_sprite.y = 250.15
    terrain_sprite.x = -830.15
    terrain_sprite.y = -830.15

if(current_player.team == "Radiant"):
    player_sprite.x = 316.65
    player_sprite.y = 237.9
    terrain_sprite.x = 316.65
    terrain_sprite.y = 237.9

# Update function called all the time
def update(interval):
    if key.W in keys_held and player_sprite.y < 250.75:
        player_sprite.y += .05
	terrain_sprite.y -= 4
    if key.S in keys_held and player_sprite.y > 237.25:
        player_sprite.y -= .05
	terrain_sprite.y += 4
    if key.A in keys_held and player_sprite.x > 316.1:
        player_sprite.x -= .05
	terrain_sprite.x += 4
    if key.D in keys_held and player_sprite.x < 330.55:
        player_sprite.x += .05
	terrain_sprite.x -= 4

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

    #print(str(player_sprite.x) + ',' + str(player_sprite.y))

# Begin application
pyglet.app.run()

