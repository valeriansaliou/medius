# Medius Game

# ------------------------------------------
# ----- Background management functions ----
# ---- Usage: background.action(params) ----
# ------------------------------------------


# Import libs
import pyglet

# Globals
ACTIVE_BACKGROUNDS = {}

# Slides a background
def slide(time, id):
	assert type(id) is int
	
	global ACTIVE_BACKGROUNDS
	
	# Read background data
	increment = ACTIVE_BACKGROUNDS[id]['speed']['current']
	old_primary_y = ACTIVE_BACKGROUNDS[id]['primary']['y']
	old_secondary_y = ACTIVE_BACKGROUNDS[id]['secondary']['y']
	
	# Process new position
	new_primary_y = old_primary_y + increment
	new_secondary_y = old_secondary_y + increment
	
	# Out of scope?
	if increment < 0 and new_primary_y <= -598:
		new_primary_y = 0
		new_secondary_y = 598
	
	elif increment >= 0 and new_primary_y >= 598:
		new_primary_y = 0
		new_secondary_y = -598
	
	# Store new positions
	ACTIVE_BACKGROUNDS[id]['primary']['y'] = new_primary_y
	ACTIVE_BACKGROUNDS[id]['secondary']['y'] = new_secondary_y
	
	return True

# Adds a background
def add(index, speed):
	assert type(index) is int and type(speed) is float or int
	
	global ACTIVE_BACKGROUNDS
	
	# Already added?
	if index in ACTIVE_BACKGROUNDS:
		return ACTIVE_BACKGROUNDS[index]
	
	# Load background
	bg_primary = bg_secondary = pyglet.image.load('./data/img/backgrounds/main.bg.' + str(index) + '.png')
	
	# Process initial positions
	initial_y_primary = 0
	initial_y_secondary = -598
	
	if speed < 0:
		initial_y_secondary = 598
	
	# Store background
	ACTIVE_BACKGROUNDS[index] = {}
	
	ACTIVE_BACKGROUNDS[index]['primary'] = {}
	ACTIVE_BACKGROUNDS[index]['secondary'] = {}
	
	ACTIVE_BACKGROUNDS[index]['primary']['bg'] = bg_primary;
	ACTIVE_BACKGROUNDS[index]['primary']['x'] = 0;
	ACTIVE_BACKGROUNDS[index]['primary']['y'] = initial_y_primary;
	
	ACTIVE_BACKGROUNDS[index]['secondary']['bg'] = bg_secondary;
	ACTIVE_BACKGROUNDS[index]['secondary']['x'] = 0;
	ACTIVE_BACKGROUNDS[index]['secondary']['y'] = initial_y_secondary;
	
	ACTIVE_BACKGROUNDS[index]['speed'] = {}
	ACTIVE_BACKGROUNDS[index]['speed']['current'] = speed
	ACTIVE_BACKGROUNDS[index]['speed']['target'] = speed
	ACTIVE_BACKGROUNDS[index]['speed']['previous'] = speed
	
	# Slide background
	pyglet.clock.schedule_interval(slide, 0.01, id = index)
	
	return ACTIVE_BACKGROUNDS[index]

# Changes the speed of a given background
def speed(index, value):
	assert type(index) is int and type(speed) is float or int
	
	if index in ACTIVE_BACKGROUNDS:
		# Setup speed builder
		ACTIVE_BACKGROUNDS[index]['speed']['previous'] = ACTIVE_BACKGROUNDS[index]['speed']['current']
		ACTIVE_BACKGROUNDS[index]['speed']['target'] = value
		
		# Launch the progressive loop!
		progressive_speed(0, index)
		
		return True
	
	return False

# Increase the background speed progressively
def progressive_speed(time, index):
	assert type(index) is int
	
	global ACTIVE_BACKGROUNDS
	
	if not index in ACTIVE_BACKGROUNDS:
		return False
	
	# Get speeds
	previous_speed = ACTIVE_BACKGROUNDS[index]['speed']['previous']
	target_speed = ACTIVE_BACKGROUNDS[index]['speed']['target']
	old_value = ACTIVE_BACKGROUNDS[index]['speed']['current']
	
	# Reset target
	if target_speed == 0:
		ACTIVE_BACKGROUNDS[index]['speed']['current'] = 0
	
	# No need to continue?
	if (abs(target_speed) < abs(previous_speed) and abs(old_value) <= abs(target_speed)) or (abs(target_speed) > abs(previous_speed) and abs(old_value) >= abs(target_speed)):
		return True
	
	# Process the speed increment coefficient
	speed_coefficient = abs(old_value) * 0.04
	
	# Process speed modifier
	if (target_speed < 0 and abs(old_value) < abs(target_speed)) or (target_speed > 0 and abs(old_value) > abs(target_speed)):
		speed_modifier = -1.0 * speed_coefficient
	else:
		speed_modifier = speed_coefficient
	
	# Change speed value
	new_value = old_value + speed_modifier
	ACTIVE_BACKGROUNDS[index]['speed']['current'] = new_value
	
	# Schedule next iteration
	pyglet.clock.schedule_once(progressive_speed, 0.01, index = index)
	
	return True

# Changes the speed according to the current scene
def scene_speed(scene):
	assert type(scene) is str
	
	# Switch the scene
	if scene is 'levels':
		speed_list = [ 0.4, 2, -0.4 ]
	elif scene is 'game':
		speed_list = [ 0.8, 3, -0.8 ]
	elif scene is 'pause':
		speed_list = [ 0.1, 0.5, -0.1 ]
	else:
		speed_list = [ 0.2, 1, -0.2 ]
	
	# Apply the scene speed
	speed(1, speed_list[0])
	speed(2, speed_list[1])
	speed(3, speed_list[2])

# Gets backgrounds
def get():
	return ACTIVE_BACKGROUNDS