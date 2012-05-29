import pyglet, random, math
import game, collision, data

i=-1

def creerVirus(corps):
	global i	
	x, y = 0, 0
	FENETRE = data.get_fenetre()

	if i == -1:
		x = random.randint(FENETRE[0][0], FENETRE[0][1] - 2 * data.get_objet("virus", "rayon"))
		y = random.randint(FENETRE[1][0], FENETRE[1][1] - 2 * data.get_objet("virus", "rayon"))

		game.creerObjet(corps, "virus0", x, y, data.get_objet("virus", "rayon"), data.get_objet("virus", "vitesse"), data.get_objet("virus", "angle"), data.get_objet("virus", "pushUp"), data.get_objet("virus", "pushDown"), data.get_objet("virus", "pushLeft"), data.get_objet("virus", "pushRight"), data.get_objet("virus", "limiteVitesse"), data.get_objet("virus", "acceleration"), math.pi/data.get_objet("virus", "anglePlus"), data.get_objet("virus", "mitoseTime"), None, [0, 0, 0], 0, None)
		i=0
	return True

def lyse(corps, celluleKey):
	j=0
	enemiPopulationLimite = data.get_modeItem("enemiPopulationLimite")
	x = corps[celluleKey]["x"]
	y = corps[celluleKey]["y"]
	rayon = corps[celluleKey]["r"]
	listePos=[[x, y+rayon/2], [x+rayon*math.cos(math.pi/6)/2, y+rayon*math.sin(math.pi/6)/2], [x-rayon*math.cos(math.pi/6)/2, y+rayon*math.sin(math.pi/6)/2]]
	listeVirus = game.GET_OBJET("virus")
	nombreVirus = 0
	
	for k in listeVirus:
		nombreVirus+=1
	
	for pos in listePos:
		continuer = 1
		while continuer:
			if nombreVirus<enemiPopulationLimite:
				if "virus"+str(j) not in corps.keys():
					game.creerObjet(corps, "virus"+str(j), pos[0], pos[1], data.get_objet("virus", "rayon"), data.get_objet("virus", "vitesse"), data.get_objet("virus", "angle"), data.get_objet("virus", "pushUp"), data.get_objet("virus", "pushDown"), data.get_objet("virus", "pushLeft"), data.get_objet("virus", "pushRight"), data.get_objet("virus", "limiteVitesse"), data.get_objet("virus", "acceleration"), math.pi/data.get_objet("virus", "anglePlus"), data.get_objet("virus", "mitoseTime"), None, [0, 0, 0], 0, None)
					continuer=0
				else:
					j+=1
			else:
				continuer=0
			
	

	return True

def reset():
	global i
	i=-1
	return True
