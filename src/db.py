# Medius Game

# ----------------------------------
# --- Database storage functions ---
# ---- Usage: db.action(params) ----
# ----------------------------------


# Import libs
import os
from libs import phpserialize

# Get the db file path
def path(window, type):
	current_entry = window + '_' + type
	current_path = './db/' + current_entry + '.db'
	
	return current_path

# Stores an entry
def store(window, type, data):
	current_path = path(window, type)
	
	store_file = open(current_path, 'w')
	store_file.write(phpserialize.dumps(data))
	store_file.close()
	
	return True

# Reads an entry
def read(window, type):
	current_path = path(window, type)
	
	if os.path.exists(current_path):
		store_file = open(current_path, 'r')
		store_data = store_file.read()
		store_file.close()
		
		if(store_data):
			return phpserialize.loads(store_data)
		
		return None
	
	return None

# Remove an entry
def remove(window, type):
	current_path = path(window, type)
	
	if os.path.exists(current_path):
		os.remove(current_path)
		
		return True
	
	return False