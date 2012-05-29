# Medius Game

# -------------------------------------
# ----- Levels window functions --------
# ---- Usage: levels.action(params) ----
# -------------------------------------


# Import libs
import pyglet
import scene, music, cursor, background

# Default values
LEVELS_IMAGES = {}

# Initializes the levels
def init():
	# Not yet loaded
	if not LEVELS_IMAGES:
		# Main layers
		LEVELS_IMAGES['select'] = pyglet.image.load('./data/img/backgrounds/levels.select.bg.png')
		LEVELS_IMAGES['bottom'] = pyglet.image.load('./data/img/backgrounds/menu.bottom.bg.png')
		
		# UI images
		LEVELS_IMAGES['fight_button'] = pyglet.image.load('./data/img/buttons/levels.fight.button.png')
		LEVELS_IMAGES['help_button'] = pyglet.image.load('./data/img/buttons/levels.help.button.png')
		LEVELS_IMAGES['logo'] = pyglet.image.load('./data/img/logos/levels.logo.png')
		LEVELS_IMAGES['back_button'] = pyglet.image.load('./data/img/buttons/levels.back.button.png')
		
		# UI labels
		LEVELS_IMAGES['bacteria_label'] = pyglet.image.load('./data/img/labels/levels.bacteria.label.png')
		LEVELS_IMAGES['virus_label'] = pyglet.image.load('./data/img/labels/levels.virus.label.png')
		
		# UI texts
		LEVELS_IMAGES['bacteria_text'] = pyglet.image.load('./data/img/texts/levels.bacteria.text.png')
		LEVELS_IMAGES['virus_text'] = pyglet.image.load('./data/img/texts/levels.bacteria.text.png')
		
		# UI buttons
		LEVELS_IMAGES['difficulty_easy_disabled'] = pyglet.image.load('./data/img/buttons/levels.difficulty.easy.disabled.png')
		LEVELS_IMAGES['difficulty_easy_enabled'] = pyglet.image.load('./data/img/buttons/levels.difficulty.easy.enabled.png')
		
		LEVELS_IMAGES['difficulty_medium_disabled'] = pyglet.image.load('./data/img/buttons/levels.difficulty.medium.disabled.png')
		LEVELS_IMAGES['difficulty_medium_enabled'] = pyglet.image.load('./data/img/buttons/levels.difficulty.medium.enabled.png')
		
		LEVELS_IMAGES['difficulty_hard_disabled'] = pyglet.image.load('./data/img/buttons/levels.difficulty.hard.disabled.png')
		LEVELS_IMAGES['difficulty_hard_enabled'] = pyglet.image.load('./data/img/buttons/levels.difficulty.hard.enabled.png')
	
	# Faster backgrounds
	background.scene_speed('levels')
	
	# Levels cursor
	cursor.set('default')
	
	# Levels music
	music.play('02')
	
	# Store scene (when ready)
	scene.set('levels')
	
	return True

# Maps levels image objects
def images():
	return LEVELS_IMAGES