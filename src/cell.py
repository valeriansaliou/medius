# Medius Game

# -------------------------------------
# ---- Cells management functions -----
# ---- Usage: cell.action(params) -----
# -------------------------------------


# Import libs
import game, data

# Default values
i = -1

# Creates a given cell
def creerCellule(corps):
	global i
	
	celluleMap = data.get_celluleMap()
	
	if i == -1:
		for cel in celluleMap:
			i += 1
			
			game.creerObjet(corps, 'cellule' + str(cel[3]), cel[0], cel[1], data.get_objet('cellule', 'rayon'), data.get_objet('cellule', 'vitesse'), data.get_objet('cellule', 'angle'), data.get_objet('cellule', 'pushUp'), data.get_objet('cellule', 'pushDown'), data.get_objet('cellule', 'pushLeft'), data.get_objet('cellule', 'pushRight'), data.get_objet('cellule', 'limiteVitesse'), data.get_objet('cellule', 'acceleration'), data.get_objet('cellule', 'anglePlus'), data.get_objet('cellule', 'mitoseTime'), data.get_objet('cellule', 'projectileTime'), [0, 0, 0], [[0, 0], [0, 0]], [False, 0, data.get_objet("cellule", "lyseTime")])
		
		i=0
	
	else:
		listeCellule = game.GET_OBJET('cellule')
		mitose(corps, celluleMap, listeCellule)
	
	return True

# Process a mitosis for a cell
def mitose(corps, celluleMap, listeCellule):
	doubleMitose = 0
	celluleManquante = 0
	celluleMap=data.get_celluleMap()
	
	# Generate a random mitosis for each cell
	for key in listeCellule:
		celMap = 0
		celMapCible1 = 0
		celMapCible2 = 0
		celMap = celluleMap[int(key.strip('cellule'))]
		
		if celMap[4][0] != -1:
			celMapCible1 = celluleMap[celMap[4][0]]
		
		if celMap[4][1] != -1:
			celMapCible2 = celluleMap[celMap[4][1]]
		
		if celMapCible1 != 0:
			if celMapCible1[2] == 0:
				if corps[key]['clock'][1] >= corps[key]['mitoseTime']:
					game.creerObjet(corps, 'cellule' + str(celMapCible1[3]), celMapCible1[0], celMapCible1[1], data.get_objet('cellule', 'rayon'), data.get_objet('cellule', 'vitesse'), data.get_objet('cellule', 'angle'), data.get_objet('cellule', 'pushUp'), data.get_objet('cellule', 'pushDown'), data.get_objet('cellule', 'pushLeft'), data.get_objet('cellule', 'pushRight'), data.get_objet('cellule', 'limiteVitesse'), data.get_objet('cellule', 'acceleration'), data.get_objet('cellule', 'anglePlus'), data.get_objet('cellule', 'mitoseTime'), data.get_objet('cellule', 'projectileTime'), [0, 0, 0], [[0, 0], [0, 0]], [False, 0, data.get_objet("cellule", "lyseTime")])
					corps[key]['clock'][1] = 0
					doubleMitose = 1
				
				else:
					 
					corps[key]['clock'][1] += 1
		
		if celMapCible2 != 0 and not doubleMitose:
			if celMapCible2[2] == 0:
				if corps[key]['clock'][1] >= corps[key]['mitoseTime']:
					game.creerObjet(corps, 'cellule' + str(celMapCible2[3]), celMapCible2[0], celMapCible2[1], data.get_objet('cellule', 'rayon'), data.get_objet('cellule', 'vitesse'), data.get_objet('cellule', 'angle'), data.get_objet('cellule', 'pushUp'), data.get_objet('cellule', 'pushDown'), data.get_objet('cellule', 'pushLeft'), data.get_objet('cellule', 'pushRight'), data.get_objet('cellule', 'limiteVitesse'), data.get_objet('cellule', 'acceleration'), data.get_objet('cellule', 'anglePlus'), data.get_objet('cellule', 'mitoseTime'), data.get_objet('cellule', 'projectileTime'), [0, 0, 0], [[0, 0], [0, 0]], [False, 0, data.get_objet("cellule", "lyseTime")])
					corps[key]['clock'][1] = 0
				
				else:
					corps[key]['clock'][1] += 1
	return True

# Returns a map of available cells
def GET_MAP():
	celluleMap = data.get_celluleMap()
	
	return celluleMap

# Resets the cell markers
def reset():
	global i
	
	i = -1
	
	return True
