# Medius Game

# ------------------------------------
# --- Bounces management functions ---
# --- Usage: bounce.action(params) ---
# ------------------------------------


# Import libs
import pyglet
import math

# Changes the bounce angle
def change_angle(corps, key, direction):
	# Vertical direction
	if direction is 'verticale':
		corps[key]['angle'] += (math.pi / 2 - corps[key]['angle']) * 2
		corps[key]['angle'] = corps[key]['angle'] % (2 * math.pi)
	
	# Horizontal direction
	if direction is 'horizontale':
		corps[key]['angle'] = -corps[key]['angle']
		corps[key]['angle'] = corps[key]['angle'] % (2 * math.pi)
	
	return True