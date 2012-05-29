# Medius Game

# ------------------------------------
# ------- Help window functions ------
# ---- Usage: help.action(params) ----
# ------------------------------------


# Import libs
import pyglet
import scene, cursor

# Default values
HELP_IMAGES = {}
HELP_SLIDE = -670

# Initializes the help
def init(bg_type):
	assert type(bg_type) is str
	
	# Not yet loaded
	if not HELP_IMAGES or 'bg_type' in HELP_IMAGES and HELP_IMAGES['bg_type'] is not bg_type:
		# Main layer & its type
		HELP_IMAGES['bg'] = pyglet.image.load('./data/img/backgrounds/help.' + bg_type + '.bg.png')
		HELP_IMAGES['bg_type'] = bg_type
	
	# Help cursor
	cursor.set('down')
	
	# Store scene (when ready)
	scene.set('help')
	
	# Slide help
	slide(1)
	
	return True

# Slides help
def slide(time):
	global HELP_SLIDE
	
	# Help params
	help_height = 670
	help_speed = 40
	
	# Slide ended
	slide_end = False
	
	# Slide up
	if scene.get() is 'help':
		if HELP_SLIDE <= -1 * help_speed:
			HELP_SLIDE = HELP_SLIDE + help_speed
		else:
			slide_end = True
	
	# Slide down
	else:
		if HELP_SLIDE >= -1 * help_height:
			HELP_SLIDE = HELP_SLIDE - help_speed
		else:
			slide_end = True
	
	# Schedule needed?
	if slide_end is False:
		pyglet.clock.schedule_once(slide, 0.01)
	
	return True

# Returns slide position
def slider():
	return HELP_SLIDE

# Maps help image objects
def images():
	return HELP_IMAGES