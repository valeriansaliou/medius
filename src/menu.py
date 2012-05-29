# Medius Game

# ----------------------------------
# ----- Menu window functions ------
# --- Usage: menu.action(params) ---
# ----------------------------------


# Import libs
import pyglet
import scene, background, music, cursor

# Default values
ABOUT_VISIBLE = False
MENU_IMAGES = {}

# Initializes the menu
def init():
	global MENU_IMAGES
	
	# Not yet loaded
	if not MENU_IMAGES:
		# Top & bottom layers
		MENU_IMAGES['top'] = pyglet.image.load('./data/img/backgrounds/menu.top.bg.png')
		MENU_IMAGES['bottom'] = pyglet.image.load('./data/img/backgrounds/menu.bottom.bg.png')
		
		# UI images
		MENU_IMAGES['logo'] = pyglet.image.load('./data/img/logos/menu.logo.png')
		MENU_IMAGES['play_button'] = pyglet.image.load('./data/img/buttons/menu.play.button.png')
		MENU_IMAGES['info_button'] = pyglet.image.load('./data/img/buttons/menu.info.button.png')
		MENU_IMAGES['music_checkbox_checked'] = MENU_IMAGES['sound_checkbox_checked'] = pyglet.image.load('./data/img/checkboxes/menu.checkbox.checked.png')
		MENU_IMAGES['music_checkbox_unchecked'] = MENU_IMAGES['sound_checkbox_unchecked'] = pyglet.image.load('./data/img/checkboxes/menu.checkbox.unchecked.png')
		
		# UI labels
		MENU_IMAGES['music_label'] = pyglet.image.load('./data/img/labels/menu.music.label.png')
		MENU_IMAGES['sound_label'] = pyglet.image.load('./data/img/labels/menu.sound.label.png')
		
		# About bubble
		MENU_IMAGES['about_bubble'] = pyglet.image.load('./data/img/others/menu.about.png')
	
	# Add backgrounds
	background.add(1, 0.2)
	background.add(2, 1)
	background.add(3, -1)
	
	# Slower backgrounds
	background.scene_speed('menu')
	
	# Menu cursor
	cursor.set('default')
	
	# Menu music
	music.play('01')
	
	# Store scene (when ready)
	scene.set('menu')
	
	return True

# Toggles about visibility
def toggleAbout():
	global ABOUT_VISIBLE
	
	# Change visibility
	if ABOUT_VISIBLE == True:
		ABOUT_VISIBLE = False
	else:
		ABOUT_VISIBLE = True
	
	return ABOUT_VISIBLE

# Returns about visibility
def hasAbout():
	return ABOUT_VISIBLE

# Maps menu image objects
def images():
	return MENU_IMAGES