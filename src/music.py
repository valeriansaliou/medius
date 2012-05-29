# Medius Game

# ------------------------------------
# ---- Music management functions ----
# --- Usage: music.action(params) ----
# ------------------------------------

# Legal notice: the music files we are using are licensed under the terms of the Creative Commons license.
# The album can be downloaded here: http://www.jamendo.com/fr/album/830


# Import libs
import pyglet, os, settings

# Current music
CURRENT_MUSIC = None

# Plays a music (given ID)
def play(id = '01', loop = True):
	assert type(id) is str or int and type(loop) is bool
	
	# If AVBin exists
	try:
		global CURRENT_MUSIC
		
		# Not allowed to play music?
		if settings.hasMusic() != True:
			return False
		
		# Stops other music
		if CURRENT_MUSIC != None:
			stop()
		
		music_file = os.path.join('data', './mus/' + id + '.ogg')
		
		CURRENT_MUSIC = pyglet.media.Player()
		CURRENT_MUSIC.queue(pyglet.media.load(music_file))
		
		# Must loop?
		if loop == True:
			CURRENT_MUSIC.eos_action = 'loop'
		
		CURRENT_MUSIC.play()
		
		return True
	
	except:
		return False

# Stops the music (current music)
def stop():
	global CURRENT_MUSIC
	
	if CURRENT_MUSIC != None:
		CURRENT_MUSIC.pause()
		CURRENT_MUSIC = None
	
	return True