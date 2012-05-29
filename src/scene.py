# Medius Game

# -----------------------------------
# --- Scene management functions ----
# -- Usage: scene.action(params) ----
# -----------------------------------


# Import libs
from src import menu

# Current scene
CURRENT_SCENE = None

# Creates the scene
def set(scene):
	assert type(scene) is str
	
	global CURRENT_SCENE
	
	CURRENT_SCENE = scene
	
	return True

# Returns the current scene
def get():
	return CURRENT_SCENE