# Medius Gamp

# ------------------------------------
# ----- Game management functions ----
# ---- Usage: game.action(params) ----
# ------------------------------------


# Import libs
import pyglet
import scene, mode, music, cursor, background, mitosis, dynamics, projectile, cell, data, virus
import math, random

# Default values
GAME_IMAGES = {}
GAME_PAUSE = False
corps = {}
game_state = 'init'

# Initializes the game
def init(game_type):
	assert type(game_type) is str
	
	
	# Store scene (when ready)
	scene.set('game')
	
	# Store mode (when ready)
	mode.set(game_type)

	# Load the data
	data.load()

	# Not yet loaded
	if not GAME_IMAGES:
		# Main layers
		GAME_IMAGES['delay'] = pyglet.image.load('./data/img/backgrounds/game.delay.bg.png')
		GAME_IMAGES['pause'] = pyglet.image.load('./data/img/backgrounds/game.pause.bg.png')
		GAME_IMAGES['win'] = pyglet.image.load('./data/img/backgrounds/game.end.win.bg.png')
		GAME_IMAGES['loose'] = pyglet.image.load('./data/img/backgrounds/game.end.loose.bg.png')
		
		# Sprites
		GAME_IMAGES['projectile'] = pyglet.image.load(data.get_image('projectile'))
		GAME_IMAGES['bacteria'] = pyglet.image.load(data.get_image('bacteria'))
		GAME_IMAGES['virus'] = pyglet.image.load(data.get_image("virus"))
		GAME_IMAGES['cell'] = pyglet.image.load(data.get_image('cellule'))
		GAME_IMAGES['cell1'] = pyglet.image.load(data.get_image('cellule1'))
		GAME_IMAGES['cell2'] = pyglet.image.load(data.get_image('cellule2'))
		GAME_IMAGES['cell3'] = pyglet.image.load(data.get_image('cellule3'))
		GAME_IMAGES['phagocyte'] = pyglet.image.load(data.get_image('Phagocyte'))
	
	# Faster backgrounds
	background.scene_speed('game')
	
	# No game cursor
	cursor.disable()
	
	# Game music
	if game_type is 'bacteria':
		music.play(data.get_musique())
	else:
		music.play('04')
	
	# Launch the game
	launch()
	
	# Process first update
	animer(0)
	
	return True

# Maps game image objects
def images():
	return GAME_IMAGES

# Pauses game
def pause():
	global GAME_PAUSE
	
	# Pause the game
	if GAME_PAUSE is False:
		GAME_PAUSE = True
	else:
		GAME_PAUSE = False
	
	return GAME_PAUSE

# Returns game pause state
def paused():
	return GAME_PAUSE

# Creates a given object (phagocyte, bacteria and so on)
def creerObjet(corps, key, x, y, r, vitesse, angle, pushUp, pushDown, pushLeft, pushRight, limiteVitesse, acceleration, anglePlus, mitoseTime, projectileTime, clock, collisionMemory, inoculate):
	if corps.has_key(key) == False:
		corps[key] = {}
		
		# Bacteria item
		if 'bacteria' in key:
			corps[key]['sprite'] = GAME_IMAGES['bacteria']
			corps[key]['x'] = x
			corps[key]['y'] = y
			corps[key]['r'] = r
			corps[key]['vitesse'] = vitesse
			corps[key]['angle'] = angle
			corps[key]['pushUp'] = pushUp
			corps[key]['pushDown'] = pushDown
			corps[key]['pushLeft'] = pushLeft
			corps[key]['pushRight'] = pushRight
			corps[key]['limiteVitesse'] = limiteVitesse
			corps[key]['acceleration'] = acceleration
			corps[key]['anglePlus'] = anglePlus
			corps[key]['mitoseTime'] = mitoseTime
			corps[key]['projectileTime'] = projectileTime
			corps[key]['clock'] = clock
		
		# Phagocyte item
		elif 'Phagocyte' in key:
			corps[key]['sprite'] = GAME_IMAGES['phagocyte']
			corps[key]['x'] = x
			corps[key]['y'] = y
			corps[key]['r'] = r
			corps[key]['vitesse'] = vitesse
			corps[key]['angle'] = angle
			corps[key]['pushUp'] = pushUp
			corps[key]['pushDown'] = pushDown
			corps[key]['pushLeft'] = pushLeft
			corps[key]['pushRight'] = pushRight
			corps[key]['limiteVitesse'] = limiteVitesse
			corps[key]['acceleration'] = acceleration
			corps[key]['anglePlus'] = anglePlus
			corps[key]['clock'] = clock
		
		# Projectile item
		elif 'projectile' in key:
			corps[key]['sprite'] = GAME_IMAGES['projectile']
			corps[key]['x'] = x
			corps[key]['y'] = y
			corps[key]['r'] = r
			corps[key]['vitesse'] = vitesse
			corps[key]['angle'] = angle
			corps[key]['pushUp'] = pushUp
			corps[key]['pushDown'] = pushDown
			corps[key]['pushLeft'] = pushLeft
			corps[key]['pushRight'] = pushRight
			corps[key]['limiteVitesse'] = limiteVitesse
			corps[key]['acceleration'] = acceleration
			corps[key]['clock'] = clock
		
		# Cell item
		elif 'cellule' in key:
			corps[key]['sprite'] = GAME_IMAGES['cell']
			corps[key]['sprite1'] = GAME_IMAGES['cell1']
			corps[key]['sprite2'] = GAME_IMAGES['cell2']
			corps[key]['sprite3'] = GAME_IMAGES['cell3']
			corps[key]['x'] = x
			corps[key]['y'] = y
			corps[key]['r'] = r
			corps[key]['angle'] = angle
			corps[key]['pushUp'] = pushUp
			corps[key]['pushDown'] = pushDown
			corps[key]['pushLeft'] = pushLeft
			corps[key]['pushRight'] = pushRight
			corps[key]['acceleration'] = acceleration
			corps[key]['anglePlus'] = anglePlus
			corps[key]['mitoseTime'] = mitoseTime 
			corps[key]['clock'] = clock
			corps[key]['collisionMemory'] = collisionMemory
			corps[key]["inoculate"] = inoculate

		# Virus item
		elif "virus" in key:
			corps[key]['sprite'] = GAME_IMAGES['virus']
			corps[key]['x'] = x
			corps[key]['y'] = y
			corps[key]['r'] = r
			corps[key]['vitesse'] = vitesse
			corps[key]['angle'] = angle
			corps[key]['pushUp'] = pushUp
			corps[key]['pushDown'] = pushDown
			corps[key]['pushLeft'] = pushLeft
			corps[key]['pushRight'] = pushRight
			corps[key]['limiteVitesse'] = limiteVitesse
			corps[key]['acceleration'] = acceleration
			corps[key]['anglePlus'] = anglePlus
			corps[key]['mitoseTime'] = mitoseTime 
			corps[key]['clock'] = clock
	
	return True

# Removes a given object
def supprimerObjet(corps, key):
	if key in corps:
		del(corps[key])
	
	return

# Game management function
def launch():
	global GAME_PAUSE
	global game_state
	global corps
	
	if mode.get() is "bacteria":
		# Reset everything
		GAME_PAUSE = False
		game_state = 'init'
		corps = {}
		mitosis.reset()
		cell.reset()
		dynamics.reset()
	else:
		# Reset everything
		GAME_PAUSE = False
		game_state = 'init'
		corps = {}
		mitosis.reset()
		cell.reset()
		dynamics.reset()
		virus.reset()
	
	return True

# Gets all game bodies
def GET_CORPS():
	return corps

# Animates the game items
def animer(dt):
	# Can animate?
	if scene.get() is not 'game':
		return False
	
	# Game won
	if state() is 'win' or state() is 'loose':
		cursor.set('default')
		background.scene_speed('pause')
		
		return False
	
	# Game not paused
	if not paused() and state() is not 'win' and state() is not 'loose':
		if mode.get() is 'bacteria':
			cell.creerCellule(corps)
			creerPhagocyte(corps)
			mitosis.mitose(corps)	
			projectile.creerProjectile(corps)
			dynamics.deplacerCorps(corps)
			set_state(corps)
		elif mode.get() is "virus":
			cell.creerCellule(corps)
			creerPhagocyte(corps)
			virus.creerVirus(corps)
			dynamics.deplacerCorps(corps)
			set_state(corps)

	
	# Schedule the next update
	pyglet.clock.schedule_once(animer, 0.01)
	
	return True

# Gets an object of the gaming bodies
def GET_OBJET(objet):
	listeKey = []
	
	for key in corps.keys():
		if objet in key:
			listeKey.append(key)
	
	return listeKey

# Creates the phagocyte
def creerPhagocyte(corps):
	if 'Phagocyte' not in corps.keys():
		creerObjet(corps, 'Phagocyte', data.get_objet('Phagocyte', 'x'), data.get_objet('Phagocyte', 'y'), data.get_objet('Phagocyte', 'rayon'), data.get_objet('Phagocyte', 'vitesse'), data.get_objet('Phagocyte', 'angle'), data.get_objet('Phagocyte', 'pushUp'), data.get_objet('Phagocyte', 'pushDown'), data.get_objet('Phagocyte', 'pushLeft'), data.get_objet('Phagocyte', 'pushRight'), data.get_objet('Phagocyte', 'limiteVitesse'), data.get_objet('Phagocyte', 'acceleration'), math.pi / data.get_objet('Phagocyte', 'anglePlus'), None, None, [0, 0, 0], 0, None)
	
	return True

# Sets the game state
def set_state(corps):
	global game_state
	# Get game objects
	listeCellule = GET_OBJET('cellule')
	listeBacteria = GET_OBJET('bacteria')
	listeVirus = GET_OBJET("virus")
	inoculate=False
	
	for celluleKey in listeCellule:
		if corps[celluleKey]["inoculate"][0] is True and inoculate is False:
			inoculate=True
	# Game end?
	if listeCellule == []:
		game_state = 'loose'
	if mode.get() is "bacteria":
		if listeBacteria == []:
			game_state = 'win'
	if mode.get() is "virus":
		if listeVirus == [] and inoculate is False:
			game_state = 'win'
	
	return True

# Returns the game state
def state():
	return game_state
