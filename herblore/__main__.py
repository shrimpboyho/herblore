import pyglet
import os
from pyglet.window import key
from pyglet.window import mouse
from pyglet import clock
from pyglet.gl import *
import physics

# Create window
window = pyglet.window.Window()

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
    keys_held.append(symbol)
    if symbol == key.SPACE:
        pass

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

# Set up player sprites
player_image = pyglet.resource.image("assets/sprites/player.png")
player_sprite = pyglet.sprite.Sprite(player_image)
player_sprite.scale = 0.2
player_sprite.x = window.width/2
player_sprite.y = window.height/2

# Update function called all the time
def update(interval):
    if key.W in keys_held and physics.notOutofBounds(player_sprite):
        player_sprite.y += .05
	terrain_sprite.y -= 4
    if key.S in keys_held and physics.notOutofBounds(player_sprite):
        player_sprite.y -= .05
	terrain_sprite.y += 4
    if key.A in keys_held and physics.notOutofBounds(player_sprite):
        player_sprite.x -= .05
	terrain_sprite.x += 4
    if key.D in keys_held and physics.notOutofBounds(player_sprite):
        player_sprite.x += .05
	terrain_sprite.x -= 4

# Set up interval
clock.schedule_interval(update, .01)

# Draw
@window.event
def on_draw():
    window.clear()
    terrain_sprite.draw()
    player_sprite.draw()
    print(str(player_sprite.x) + ',' + str(player_sprite.y))

# Begin application
pyglet.app.run()

