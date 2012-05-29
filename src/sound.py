# Medius Game

# ------------------------------------
# ---- Sound management functions ----
# --- Usage: sound.action(params) ----
# ------------------------------------


# Import libs
import pyglet, settings

# Plays a music (given ID)
def play(id = '01'):
	assert type(id) is str or int
	
	# If AVBin exists
	try:
		# Not allowed to play music?
		if settings.hasSound() != True:
			return False
		
		# Play it!
		play_sound = pyglet.media.load('./data/snd/' + id + '.ogg')
		play_sound.play()
		
		return True
	
	except:
		return False