# Medius Game

# ----------------------------------
# ---- Cursor display functions ----
# -- Usage: cursor.action(params) --
# ----------------------------------


# Import libs
import pyglet
from pyglet.window import ImageMouseCursor
import window

# Sets the cursor
def set(name):
	# Pointer coordinates
	x = 0
	y = 32
	
	# Pointer
	if name is 'pointer':
		x = 6
	
	# Down
	elif name is 'down':
		x = 6
		y = 10
	
	# Load the cursor
	image = pyglet.image.load('./data/img/cursors/' + name + '.png')
	cursor = pyglet.window.ImageMouseCursor(image, x, y)
	
	# Apply it!
	current_window = window.get()
	current_window.set_mouse_cursor(cursor)
	
	# Enable the cursor
	enable()
	
	return True

# Enables the cursor
def enable():
	current_window = window.get()
	current_window.set_mouse_visible(True)
	
	return True

# Disables the cursor
def disable():
	current_window = window.get()
	current_window.set_mouse_visible(False)
	
	return True