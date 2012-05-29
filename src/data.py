# Medius Game

# ----------------------------------
# ------ Data load functions -------
# --- Usage: data.action(params) ---
# ----------------------------------


# Import libs
import readxml, settings, mode

# Default values
medius = {}
celluleMap = []
i=0
listeFileBacteria = ['./data/scn/gameBacteria1.xml', './data/scn/gameBacteria2.xml', './data/scn/gameBacteria3.xml']
listeFileVirus = ['./data/scn/gameVirus1.xml', './data/scn/gameVirus2.xml', './data/scn/gameVirus3.xml']

# Loads an XML data file
def load():
	global i
	i=settings.hasDifficulty()-1
	if mode.get() is "bacteria":
		readxml.readFile(listeFileBacteria[i])
	elif mode.get() is "virus":
		readxml.readFile(listeFileVirus[i])

	medius[i]=readxml.GET_MEDIUS()
	celluleMap=set_celluleMap()

# Returns the storage object
def GET_MEDIUS():
	return medius

# Sets an item
def set(j):
	global i
	
	i = j
	
	return True

# Gets an image
def get_image(objet):
	return medius[i]['scene']['mode']['image'][objet]

# Gets a music
def get_musique():
	return medius[i]['scene']['mode']['item']['musique']

# Gets an object
def get_objet(objet, item):
	if 'Phagocyte' in objet:
		return medius[i]['scene']['mode']['objet'][objet][item]
	if 'cellule' in objet:
		return medius[i]['scene']['mode']['objet'][objet][item]
	if 'bacteria' in objet:
		return medius[i]['scene']['mode']['objet'][objet][item]
	if 'projectile' in objet:
		return medius[i]['scene']['mode']['objet'][objet][item]
	if "virus" in objet:
		return medius[i]['scene']['mode']['objet'][objet][item]


# Sets a list
def set_liste(indice):
	liste = [0, 0, 0, 0, [0, 0]]
	
	# Store the items
	liste[0] = medius[i]['scene']['mode']['celluleMap']['item'][indice]['x']
	liste[1] = medius[i]['scene']['mode']['celluleMap']['item'][indice]['y']
	liste[2] = medius[i]['scene']['mode']['celluleMap']['item'][indice]['presence']
	liste[3] = indice
	liste[4][0], liste[4][1] = [medius[i]['scene']['mode']['celluleMap']['item'][indice]['cible1'], medius[i]['scene']['mode']['celluleMap']['item'][indice]['cible2']]
	
	return liste

# Sets a map of cells
def set_celluleMap():
	k = 0
	
	for k in range (100):
		if k in medius[i]['scene']['mode']['celluleMap']['item'].keys():
			celluleMap.append(set_liste(k))
	
	return celluleMap

# Gets a map of cells
def get_celluleMap():
	return celluleMap

# Gets the window
def get_fenetre():
	return [[0, medius[i]['FENETRE']['width']], [0, medius[i]['FENETRE']['height']]]

# Gets the mode for an item
def get_modeItem(item):
	if item is 'nombreEnemiLimite':
		return medius[i]['scene']['mode']['item']['nombreEnemiLimite']
	elif item is 'intervalDeplacement':
		return medius[i]['scene']['mode']['item']['intervalDeplacement'] 	
	elif item is 'DT_MITOSE_MAX':
		return medius[i]['scene']['mode']['item']['DT_MITOSE_MAX']
	elif item is 'DT_MITOSE_MIN':
		return medius[i]['scene']['mode']['item']['DT_MITOSE_MIN']
	elif item is 'enemiPopulationLimite':
		return medius[i]['scene']['mode']['item']['enemiPopulationLimite'] 
