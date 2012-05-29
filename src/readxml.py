# Medius Game

# -------------------------------------
# --------- XML read functions --------
# --- Usage: readxml.action(params) ---
# -------------------------------------


# Import libs
from xml.dom import minidom
import string

# Default values
medius = {}
scene = {}
mode = {}
celluleMap = {}
objet = {}
listeObjet = ['Phagocyte', 'cellule', 'bacteria', 'projectile', "virus"]
i = 0

# Reads a given XML file
def readFile(fileName):
	fileOpen = open(fileName, 'r')
	xmldoc = minidom.parse(fileOpen)
	fileOpen.close()
	
	racine = xmldoc.childNodes[0]
	parcours(racine)
	
	mode['objet'] = objet
	mode['celluleMap'] = celluleMap
	scene['mode'] = mode
	medius['scene'] = scene
	
	return True

# Browse a given node
def parcours(noeud):
	traiter(noeud)
	
	for noeud2 in noeud.childNodes:
		if noeud2.nodeType is noeud2.ELEMENT_NODE:
			parcours(noeud2)

# Process a given node
def traiter(noeud):
	listeKey = GET_KEY(noeud)
	tag = str(GET_TAG(noeud))
	
	# Window settings
	if 'FENETRE' in tag:
		medius[tag] = {}
		
		for key in listeKey:
			if 'width' in key:
				medius[tag][str(key)] = int(GET_VALUE(noeud, key))
			elif 'height' in key:
				medius[tag][str(key)] = int(GET_VALUE(noeud, key))
		
		tag = ''
	
	# Scene settings
	elif 'scene' in tag:
		medius[tag] = {}
		
		for key in listeKey:
			scene[str(key)] = str(GET_VALUE(noeud, key))
		
		tag = ''
	
	# Scene mode settings
	elif 'mode' in tag:
		scene[tag] = {}
		
		for key in listeKey:
			if 'name' in key:
				mode[str(key)] = str(GET_VALUE(noeud, key))
		
		tag = ''
	
	# Item settings
	elif 'item' in tag:
		global i
		
		if 'item' not in mode.keys():
			mode[tag] = {}
		
		for key in listeKey:
			if 'nombreEnemiLimite' in key:
				mode[tag][str(key)] = int(GET_VALUE(noeud, key))
			elif 'intervalDeplacement' in key:
				mode[tag][str(key)] = int(GET_VALUE(noeud, key))
			elif 'DT_MITOSE_MAX' in key:
				mode[tag][str(key)] = int(GET_VALUE(noeud, key))
			elif 'DT_MITOSE_MIN' in key:
				mode[tag][str(key)] = int(GET_VALUE(noeud, key))
			elif 'enemiPopulationLimite' in key:
				mode[tag][str(key)] = int(GET_VALUE(noeud, key))
			elif 'musique' in key:
				mode[tag][str(key)] = int(GET_VALUE(noeud, key))
		
		if 'item' not in celluleMap.keys():
			celluleMap[tag] = {}
		
		for key in listeKey:
			if 'indice' in key:
				if int(GET_VALUE(noeud, key)) == i:
					celluleMap[tag][int(GET_VALUE(noeud, key))] = {}
					i += 1
					
					for key1 in listeKey:
						if 'x' in key1:
							celluleMap[tag][int(GET_VALUE(noeud, key))][str(key1)] = int(GET_VALUE(noeud, key1))
						if 'y' in key1:
							celluleMap[tag][int(GET_VALUE(noeud, key))][str(key1)] = int(GET_VALUE(noeud, key1))
						if 'presence' in key1:
							celluleMap[tag][int(GET_VALUE(noeud, key))][str(key1)] = int(GET_VALUE(noeud, key1))
						if 'cible1' in key1:
							celluleMap[tag][int(GET_VALUE(noeud, key))][str(key1)] = int(GET_VALUE(noeud, key1))
						if 'cible2' in key1:
							celluleMap[tag][int(GET_VALUE(noeud, key))][str(key1)] = int(GET_VALUE(noeud, key1))
		
		tag = ''
	
	# Map of cells
	elif 'celluleMap' in tag:
		if 'celluleMap' not in mode.keys():
			mode[tag] = {}
		
		tag = ''
	
	# Image
	elif 'image' in tag:
		if 'image' not in mode.keys():
			mode[tag] = {}
		
		for key in listeKey:
			if 'projectile' in key:
				mode[tag][str(key)] = str(GET_VALUE(noeud, key))
			elif 'bacteria' in key:
				mode[tag][str(key)] = str(GET_VALUE(noeud, key))
			elif 'cellule' in key:
				mode[tag][str(key)] = str(GET_VALUE(noeud, key))
			elif 'Phagocyte' in key:
				mode[tag][str(key)] = str(GET_VALUE(noeud, key))
			elif "virus" in key:
				mode[tag][str(key)] = str(GET_VALUE(noeud, key))
		tag = ''
	
	# Object
	elif 'objet' in tag:
		if 'objet' not in mode.keys():
			mode[tag] = {}
	for objet1 in listeObjet:
		if objet1 in tag:
			if objet1 not in objet.keys():
				objet[tag] = {}
			
			for key in listeKey:
				if 'None' not in str(GET_VALUE(noeud, key)):
					if 'x' in key:
						objet[tag][str(key)] = int(GET_VALUE(noeud, key))
					elif 'y' in key:
						objet[tag][str(key)] = int(GET_VALUE(noeud, key))
					elif 'rayon' in key:
						objet[tag][str(key)] = int(GET_VALUE(noeud, key))
					elif 'vitesse' in key:
						objet[tag][str(key)] = int(GET_VALUE(noeud, key))
					elif 'angle' in key:
						objet[tag][str(key)] = int(GET_VALUE(noeud, key))
					elif 'pushUp' in key:
						objet[tag][str(key)] = int(GET_VALUE(noeud, key))
					elif 'pushDown' in key:
						objet[tag][str(key)] = int(GET_VALUE(noeud, key))
					elif 'pushLeft' in key:
						objet[tag][str(key)] = int(GET_VALUE(noeud, key))
					elif 'pushRight' in key:
						objet[tag][str(key)] = int(GET_VALUE(noeud, key))
					elif 'limiteVitesse' in key:
						objet[tag][str(key)] = int(GET_VALUE(noeud, key))
					elif 'acceleration' in key:
						objet[tag][str(key)] = float(GET_VALUE(noeud, key))
					elif 'anglePlus' in key:
						objet[tag][str(key)] = int(GET_VALUE(noeud, key))
					elif 'mitoseTime' in key:
						objet[tag][str(key)] = int(GET_VALUE(noeud, key))
					elif 'projectileTime' in key:
						objet[tag][str(key)] = int(GET_VALUE(noeud, key))
					elif 'lyseTime' in key:
						objet[tag][str(key)] = int(GET_VALUE(noeud, key))
	
	return True

# Gets a node key
def GET_KEY(noeud):
	return noeud.attributes.keys()

# Gets a node value
def GET_VALUE(noeud, key):
	return noeud.attributes[key].value

# Gets a node tag
def GET_TAG(noeud):
	return noeud.tagName

# Gets the global storage object
def GET_MEDIUS():
	return medius
