# Medius Game

# --------------------------------------
# ----- Object collision functions -----
# -- Usage: collision.action(params) ---
# --------------------------------------


# Import libs
import pyglet, math, random
import data
from pyglet.gl import *

# Handles the collisions on the sides
def collisionBord(objet1):
	FENETRE = data.get_fenetre()
	collision = 0
	
	if objet1['x'] + objet1['r'] < FENETRE[0][0]:
		objet1['x'] += FENETRE[0][1] + objet1['r'] * 2
		collision=1
	
	if objet1['x'] - objet1['r'] > FENETRE[0][1]:
		objet1['x'] -= FENETRE[0][1] + objet1['r'] * 2
		collision=1
	
	if objet1['y'] - objet1['r'] < FENETRE[1][0]:
		objet1['y'] += FENETRE[1][1] + objet1['r'] * 2
		collision=1
	
	if objet1['y'] - objet1['r'] > FENETRE[1][1]:
		objet1['y'] -= FENETRE[1][1] + objet1['r'] * 2
		collision=1
	
	if collision:
		return False
	
	return True

# Collision with two circles
def collisionCercle(objet1, objet2):
	if abs(math.pow(objet1['y'] - objet2['y'], 2) + math.pow(objet1['x'] - objet2['x'], 2)) <= (math.pow(objet1['r'] + objet2['r'], 2)):
		return False
	
	return True

# Collision with phagocytes and bacterias
def collisionPhagocyteBacteria(corps, key):
	for key1 in corps.keys():
		if key1 is not key and 'bacteria' in key1:
			if collisionCercle(corps[key], corps[key1]) is False:
				return key1
	
	return True

# Collision with a cell
def collisionCellule(corps, key, celluleKey, celluleMap):
	indiceCelluleMap = int(celluleKey.strip('cellule'))
	
	if corps[key]['x'] - corps[key]['r'] >= corps[celluleKey]['x'] + corps[celluleKey]['r']:
		return 'verticale'
	
	if corps[key]['x'] + corps[key]['r'] <= corps[celluleKey]['x'] - corps[celluleKey]['r']:
		return 'verticale'
	
	if corps[key]['y'] - corps[key]['r'] >= corps[celluleKey]['y'] + corps[celluleKey]['r']:
		return 'horizontale'
	
	if corps[key]['y'] + corps[key]['r'] <= corps[celluleKey]['y'] - corps[celluleKey]['r']:
		return 'horizontale'
	
	return False
