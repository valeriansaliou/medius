# Medius Game

# ------------------------------------
# -- Settings management functions ---
# -- Usage: settings.action(params) --
# ------------------------------------


# Required tools
import db, music

# Default values
SETTINGS_MUSIC = True
SETTINGS_SOUND = True
SETTINGS_DIFFICULTY = 2

# Initializes settings
def init():
	global SETTINGS_MUSIC
	global SETTINGS_SOUND
	global SETTINGS_DIFFICULTY
	
	# Loads settings
	setting_music = db.read('setting', 'music')
	setting_sound = db.read('setting', 'sound')
	setting_difficulty = db.read('setting', 'difficulty')
	
	# Apply settings
	if(setting_music == False):
		SETTINGS_MUSIC = False
	if(setting_sound == False):
		SETTINGS_SOUND = False
	
	if(type(setting_difficulty) is int):
		SETTINGS_DIFFICULTY = setting_difficulty
	
	return

# Toggles music settings
def toggleMusic():
	global SETTINGS_MUSIC
	
	# Change setting
	if SETTINGS_MUSIC == True:
		SETTINGS_MUSIC = False
		music.stop()
	else:
		SETTINGS_MUSIC = True
		music.play('01')
	
	# Store setting
	db.store('setting', 'music', SETTINGS_MUSIC)
	
	return SETTINGS_MUSIC

# Toggles sound settings
def toggleSound():
	global SETTINGS_SOUND
	
	# Change setting
	if SETTINGS_SOUND == True:
		SETTINGS_SOUND = False
	else:
		SETTINGS_SOUND = True
	
	# Store setting
	db.store('setting', 'sound', SETTINGS_SOUND)
	
	return SETTINGS_SOUND

# Toggles difficulty settings
def toggleDifficulty(num):
	assert type(num) is int
	
	global SETTINGS_DIFFICULTY
	
	# Change setting
	SETTINGS_DIFFICULTY = num
	
	# Store setting
	db.store('setting', 'difficulty', SETTINGS_DIFFICULTY)
	
	return SETTINGS_DIFFICULTY

# Returns the music setting
def hasMusic():
	return SETTINGS_MUSIC

# Returns the sound setting
def hasSound():
	return SETTINGS_SOUND

# Returns the difficulty setting
def hasDifficulty():
	return SETTINGS_DIFFICULTY