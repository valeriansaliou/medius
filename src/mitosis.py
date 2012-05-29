# Medius Game

# --------------------------------------
# ---- Mitosis management functions ----
# ---- Usage: mitosis.action(params) ---
# --------------------------------------


# Import libs
import pyglet
import math
import random
from pyglet.gl import *
import collision
import game
import dynamics, data, mode
import cell
import math

# Default values
i = -1

# Rules the mitosis process
def loiMitose(objet1, objet2):
	DTMAX, DTMIN = data.get_modeItem('DT_MITOSE_MAX'), data.get_modeItem('DT_MITOSE_MIN')
	dt = 0
	
	# Randomize the first object mitosis time
	dt = random.randint(-DTMIN, DTMAX)
	objet1['mitoseTime'] += dt
	
	# Randomize the second object mitosis time
	dt = random.randint(-DTMIN, DTMAX)
	objet2['mitoseTime'] += dt
	
	return True

# Processes a mitosis on a given body
def mitose(corps):
	global i
	
	listeCellule = game.GET_OBJET('cellule')
	listeVirus = game.GET_OBJET("virus")
	celluleMap = cell.GET_MAP()
	FENETRE = data.get_fenetre()
	
	# Limit of allowed active bacterias
	enemiPopulationLimite = data.get_modeItem('enemiPopulationLimite')
	x, y, continuer = 0, 0, 0
	
	# Initializes the initial mitosis
	if mode.get() is "bacteria":
		item="bacteria"
		if i == -1:
			for celluleKey in listeCellule:
				continuer = 0
				
				while continuer == 0:
					x = random.randint(FENETRE[0][0], FENETRE[0][1] - 2 * data.get_objet('bacteria', 'rayon'))
					y = random.randint(FENETRE[1][0], FENETRE[1][1] - 2 * data.get_objet('bacteria', 'rayon'))
					game.creerObjet(corps, 'bacteria0', x, y, data.get_objet('bacteria', 'rayon'), data.get_objet('bacteria', 'vitesse'), data.get_objet('bacteria', 'angle'), data.get_objet('bacteria', 'pushUp'), data.get_objet('bacteria', 'pushDown'), data.get_objet('bacteria', 'pushLeft'), data.get_objet('bacteria', 'pushRight'), data.get_objet('bacteria', 'limiteVitesse'), data.get_objet('bacteria', 'acceleration'), math.pi/data.get_objet('bacteria', 'anglePlus'), data.get_objet('bacteria', 'mitoseTime'), data.get_objet('bacteria', 'projectileTime'), [0, 0, 0], 0, None)
				
					if collision.collisionPhagocyteBacteria(corps, 'bacteria0') == True and collision.collisionCellule(corps, 'bacteria0', celluleKey, celluleMap) is not False:
						continuer = 1
					else:
						game.supprimerObjet(corps, 'bacteria0')
			
			i = 0
		
		# Process mitosis
		for key in corps.keys():
			if i > enemiPopulationLimite:
				i = 0
			
			if 'bacteria' in key:
				if corps[key]['clock'][1] == corps[key]['mitoseTime']:
					game.creerObjet(corps, 'bacteria' + str(i), corps[key]['x'] + corps[key]['r'] * 2, corps[key]['y'], data.get_objet('bacteria', 'rayon'), data.get_objet('bacteria', 'vitesse'), data.get_objet('bacteria', 'angle'), data.get_objet('bacteria', 'pushUp'), data.get_objet('bacteria', 'pushDown'), data.get_objet('bacteria', 'pushLeft'), data.get_objet('bacteria', 'pushRight'), data.get_objet('bacteria', 'limiteVitesse'), data.get_objet('bacteria', 'acceleration'), math.pi/data.get_objet('bacteria', 'anglePlus'), data.get_objet('bacteria', 'mitoseTime'), data.get_objet('bacteria', 'projectileTime'), [0, 0, 0], 0, None)
					loiMitose(corps[key], corps['bacteria' + str(i)])
					
					i += 1
					corps[key]['clock'][1] = 0
				
				corps[key]['clock'][1] += 1
		
	return True

# Resets the mitosis markers
def reset():
	global i
	
	i = -1
	
	return True
