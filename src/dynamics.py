# Medius Game

# -------------------------------------
# --- Dynamics management functions ---
# --- Usage: dynamics.action(params) --
# -------------------------------------


# Import libs
import pyglet, math, random
from pyglet.gl import *
import game, cell, bounce, data, mode, virus, collision

# Default values
autoriserDeplacement = 0
autoriserRebond = [
	[True, 0],
	[True, 0]
]

# Change the angle speed
def modifVitesseAngle(objet):
	if objet['pushUp'] == 1:
		if objet['vitesse'] < objet['limiteVitesse']:
			objet['vitesse'] += objet['acceleration']
	
	if objet['pushDown'] == 1:
		if objet['vitesse'] >- objet['limiteVitesse']:
			objet['vitesse'] -= objet['acceleration']
	
	if objet['pushRight'] == 1:
		objet['angle'] -= objet['anglePlus']
	
	if objet['pushLeft'] == 1:
		objet['angle'] += objet['anglePlus']
	
	if objet['pushUp'] == 0 and objet['pushDown'] == 0:
		if objet['vitesse'] > 0:
			objet['vitesse'] -= objet['acceleration']
		
		if objet['vitesse'] < 0:
			objet['vitesse'] += objet['acceleration']
	
	return True

# Sets a random angle to a given object
def randomAngle(objet):
	i = 0
	i = random.randint(-1 * int(objet['anglePlus'] * 1000), int(objet['anglePlus'] * 1000))
	
	objet['angle'] += i * 0.001

# Moves a body
def deplacer(corps, nombreEnemi):
	global autoriserDeplacement
	global autoriserRebond
	
	vecDeplacement = [0, 0]
	nombreEnemiLimite = data.get_modeItem('nombreEnemiLimite')
	delKey = []
	
	# Gets the object lists
	listeBacteria = game.GET_OBJET('bacteria')
	listeProjectile = game.GET_OBJET('projectile')
	listeCellule = game.GET_OBJET('cellule')
	listeVirus = game.GET_OBJET("virus")
	celluleMap = cell.GET_MAP()
	
	# Move each object
	for key in corps.keys():
		if 'cellule' not in key:
			if corps[key]['angle'] != None:
				vecDeplacement[0] = math.cos(corps[key]['angle']) * corps[key]['vitesse']
				vecDeplacement[1] = math.sin(corps[key]['angle']) * corps[key]['vitesse']
		
		if 'Phagocyte' in key and nombreEnemi>=nombreEnemiLimite or 'Phagocyte' in key and autoriserDeplacement:
			corps[key]['x'] += vecDeplacement[0]
			corps[key]['y'] += vecDeplacement[1]
			autoriserDeplacement = 1
		
		elif 'Phagocyte' not in key and 'cellule' not in key:
			corps[key]['x'] += vecDeplacement[0]
			corps[key]['y'] += vecDeplacement[1]
			
			if 'bacteria' in key:
				for celluleKey in listeCellule:
					corps[celluleKey]['collisionMemory'][1][0] = collision.collisionCellule(corps, key, celluleKey, celluleMap)
					
					if corps[celluleKey]['collisionMemory'][1][0] is False:
						if autoriserRebond[1][0] is True and autoriserRebond[1][1] > 30:
							bounce.change_angle(corps, key, corps[celluleKey]['collisionMemory'][1][1])
							autoriserRebond[1][0] = False
							autoriserRebond[1][1] = 0
					
					else:
						corps[celluleKey]['collisionMemory'][1][1] = corps[celluleKey]['collisionMemory'][1][0]
						autoriserRebond[1][0] = True
			
			autoriserRebond[1][1] += 1
		
		if 'Phagocyte' in key and autoriserDeplacement:
			for bacteriaKey in listeBacteria:
				if collision.collisionCercle(corps['Phagocyte'], corps[bacteriaKey]) is False:
					delKey.append(bacteriaKey)
			for virusKey in listeVirus:
				if collision.collisionCercle(corps['Phagocyte'], corps[virusKey]) is False:
					delKey.append(virusKey)
				
			
			for projectileKey in listeProjectile:
				if collision.collisionCercle(corps['Phagocyte'], corps[projectileKey]) is False:
					if 'Phagocyte' not in delKey:
						delKey.append('Phagocyte')
					if projectileKey not in delKey:
						delKey.append(projectileKey)
			
			for celluleKey in listeCellule:
				corps[celluleKey]['collisionMemory'][0][0] = collision.collisionCellule(corps, key, celluleKey, celluleMap)
				if corps[celluleKey]['collisionMemory'][0][0] is False:
					if autoriserRebond[0][0] is True and autoriserRebond[0][1] > 10:
						bounce.change_angle(corps, key, corps[celluleKey]['collisionMemory'][0][1])
						autoriserRebond[0][0] = False
						autoriserRebond[0][1] = 0
				
				else:
					corps[celluleKey]['collisionMemory'][0][1] = corps[celluleKey]['collisionMemory'][0][0]
					autoriserRebond[0][0] = True
			
			autoriserRebond[0][1] += 1
		
		if 'cellule' in key:
			for projectileKey in listeProjectile:
				if collision.collisionCercle(corps[key], corps[projectileKey]) is False:
					if key not in delKey:
						celluleMap[int(key.strip('cellule'))][2] = 0
						delKey.append(key)
					if projectileKey not in delKey:
						delKey.append(projectileKey)
			if corps[key]["inoculate"][0] is True:
				if corps[key]["inoculate"][1]>=corps[key]["inoculate"][2]:
					virus.lyse(corps, key)
					if key not in delKey:
						celluleMap[int(key.strip('cellule'))][2] = 0
						delKey.append(key)
				else:
					corps[key]["inoculate"][1]+=1

		
		if "virus" in key:
			for celluleKey in listeCellule:
				if collision.collisionCercle(corps[key], corps[celluleKey]) is False:
					delKey.append(key)
					corps[celluleKey]["inoculate"][0]=True
			
		if 'projectile' in key:
			if collision.collisionBord(corps[key]) is False:
				delKey.append(key)
		
		else:
			collision.collisionBord(corps[key])
		
		corps[key]['clock'][0] += 1
	
	# Remove objects
	for key3 in delKey:
		game.supprimerObjet(corps, key3)
	
	return True

# Updates the body position
def deplacerCorps(corps):
	intervalDeplacement = data.get_modeItem('intervalDeplacement')	
	nombreEnemi = 0
	
	for key in corps.keys():
		if mode.get() is "bacteria":
			if 'bacteria' in key:
				randomAngle(corps[key])
				nombreEnemi += 1
		elif mode.get() is "virus":
			if "virus" in key:
				randomAngle(corps[key])
				nombreEnemi += 1

		if 'cellule' not in key:	
			if corps[key]['clock'][0] >= intervalDeplacement:
				modifVitesseAngle(corps[key])
				corps[key]['clock'][0] = 0
	
	deplacer(corps, nombreEnemi)
	
	return True

# Sets an angle to a projectile
def projectileAngle(corps, key):
	a, b, px, py, Phagocytex, Phagocytey = 0, 0, 0, 0, 0, 0
	
	# We got a phagocyte
	if 'Phagocyte' in corps.keys():
		px = corps[key]['x'] - corps[key]['r']
		py = corps[key]['y'] - corps[key]['r']
		Phagocytex = corps['Phagocyte']['x']
		Phagocytey = corps['Phagocyte']['y']
		
		a = px-Phagocytex
		b = py-Phagocytey
		
		alpha = math.atan(float(b)/float(a))
		
		if a > 0 :
			corps[key]['angle'] = alpha+math.pi
		
		elif a < 0 :
			if b != 0:
				corps[key]['angle'] = alpha
		
		else:
			if b > 0:
				corps[key]['angle'] = 0
			if b < 0:
				corps[key]['angle'] = math.pi
			else:
				corps[key]['angle'] = None
	
	return True

# Returns the phagocyte display state
def hasPhagocyte():
	if autoriserDeplacement == 0:
		return False
	
	return True

# Resets the dynamics markers
def reset():
	global autoriserDeplacement
	global autoriserRebond
	
	autoriserDeplacement = 0
	autoriserRebond = [
		[True, 0],
		[True, 0]
	]
	
	return True
