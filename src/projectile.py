# Medius Game

# -------------------------------------
# --- Dynamics management functions ---
# --- Usage: dynamics.action(params) --
# -------------------------------------


# Import libs
import pyglet
import dynamics
import math
import random
import game, data
import string

# Creates a projectile
def creerProjectile(corps):
	for key in corps.keys():
		if 'bacteria' in key:
			if corps[key]['projectileTime'] <= corps[key]['clock'][2]:
				i = 0	
				continuer = 1
				
				while continuer:
					if 'projectile' + str(i)  not in corps.keys():
						game.creerObjet(corps, 'projectile' + str(i), corps[key]['x'], corps[key]['y'], data.get_objet('projectile', 'rayon'), data.get_objet('projectile', 'vitesse'), data.get_objet('projectile', 'angle'), data.get_objet('projectile', 'pushUp'), data.get_objet('projectile', 'pushDown'), data.get_objet('projectile', 'pushLeft'), data.get_objet('projectile', 'pushRight'), data.get_objet('projectile', 'limiteVitesse'), data.get_objet('projectile', 'acceleration'), data.get_objet('projectile', 'anglePlus'), None, None, [0, 0], 0, None)
						
						corps[key]['clock'][2] = 0
						continuer = 0
					
					i += 1
				
				dynamics.projectileAngle(corps, 'projectile' + str(i - 1))
			
			corps[key]['clock'][2] += 1
	
	return True
