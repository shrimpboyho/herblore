import pyglet
import os
from pyglet.window import key
from pyglet.window import mouse
from pyglet import clock

# Create window
window = pyglet.window.Window()

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

# Set up play sprites
player_image = pyglet.resource.image("assets/sprites/player.png")
player_sprite = pyglet.sprite.Sprite(player_image)

# Update function called all the time
def update(interval):
    if key.W in keys_held:
        player_sprite.y += 1
    if key.S in keys_held:
        player_sprite.y -= 1
    if key.A in keys_held:
        player_sprite.x -= 1
    if key.D in keys_held:
        player_sprite.x += 1
# Set up interval
clock.schedule_interval(update, .01)

# Draw
@window.event
def on_draw():
    window.clear()
    player_sprite.draw()

# Begin application
pyglet.app.run()
