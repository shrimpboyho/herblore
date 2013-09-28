import pyglet
import os
from pyglet.window import key
from pyglet.window import mouse

# Create window
window = pyglet.window.Window()

# Keyboard input
@window.event
def on_key_press(symbol, modifiers):
    if symbol == key.W:
        print 'The "W" key was pressed.'
    elif symbol == key.A:
        print 'The "A" key was pressed.'
    elif symbol == key.S:
        print 'The "S" key was pressed.'
    elif symbol == key.D:
        print 'The "D" key was pressed.'

# Mouse input
@window.event
def on_mouse_press(x, y, button, modifiers):
    if button == mouse.LEFT:
        print 'The left mouse button was pressed.'
    if button == mouse.RIGHT:
        print 'The right mouse button was pressed.'

explosion = pyglet.media.load('/assets/music/background.wav', streaming=False)
explosion.play()


@window.event
def on_draw():
    window.clear()

# Begin application
pyglet.app.run()

