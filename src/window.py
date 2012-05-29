# Medius Game

# -----------------------------------
# --- Window management functions ---
# -- Usage: window.action(params) ---
# -----------------------------------


# Import libs
import pyglet
from pyglet.window import Window

# Current window
CURRENT_WINDOW = None

# Creates the window
def init():
	global CURRENT_WINDOW
	
	# Create the window
	window = pyglet.window.Window(1024, 600, caption='Medius')
	
	# Store the window
	CURRENT_WINDOW = window
	
	return True

# Applies the window icons
def icons(window):
	icon16 = pyglet.image.load('./data/img/icons/app.16.png')
	icon32 = pyglet.image.load('./data/img/icons/app.32.png')
	icon128 = pyglet.image.load('./data/img/icons/app.128.png')
	
	window.set_icon(icon16, icon32, icon128)
	
	return True

# Returns the current window
def get():
	return CURRENT_WINDOW