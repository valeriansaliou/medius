# Medius Game

# ---------------------------------
# -------- Main functions ---------
# ---- Master script (no call) ----
# ---------------------------------


# Import libs
import pyglet
from pyglet.window import *
from pyglet.gl import *

# Import sources
from src import window, scene, events, menu, settings

# Main
def main():
	# Build the window
	window.init()
	
	# Get the window
	current_window = window.get()
	
	# Apply the icons
	window.icons(current_window)

# Launch
if __name__ == '__main__':
	# Create the workflow
	main()
	
	# Load settings
	settings.init()
	
	# Build the menu
	menu.init()
	
	# Start events
	events.start()
	
	# Enables PNG alpha support
	glEnable(GL_BLEND)
	glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
	
	# Run app!
	pyglet.app.run()