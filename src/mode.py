# Medius Game

# -----------------------------------
# ---- Mode management functions ----
# --- Usage: mode.action(params) ----
# -----------------------------------


# Import libs
from src import menu

# Current mode
CURRENT_MODE = None

# Creates the mode
def set(mode):
	assert type(mode) is str
	
	global CURRENT_MODE
	
	CURRENT_MODE = mode
	
	return True

# Returns the current mode
def get():
	return CURRENT_MODE