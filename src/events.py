# Medius Game

# ----------------------------------
# -------- Events functions --------
# -- Usage: events.action(params) --
# ----------------------------------


# Import libs
import pyglet
import math
from pyglet.window import mouse, key
from src import window, scene, mode, settings, background, sound, menu, levels, help, game, cursor, data, dynamics

# Starts the event handlers
def start():
	current_window = window.get()
	
	# Initialize
	@current_window.event
	def on_draw():
		current_window.clear()
		current_scene = scene.get()
		
		# Backgrounds
		main_bg = background.get()
		
		for i in main_bg:
			for sub in main_bg[i]:
				if sub is 'primary' or sub is 'secondary':
					main_bg[i][sub]['bg'].blit(main_bg[i][sub]['x'], main_bg[i][sub]['y'])
		
		# Menu images
		if current_scene is 'menu':
			# Read image objects
			menu_images = menu.images()
			
			# Refresh top & bottom layers
			menu_images['top'].blit(0,461)
			menu_images['bottom'].blit(0,0)
			
			# Refresh UI images
			menu_images['logo'].blit(550,480)
			menu_images['play_button'].blit(40,498)
			menu_images['info_button'].blit(932,13)
			
			# Refresh UI labels
			menu_images['music_label'].blit(105,10)
			menu_images['sound_label'].blit(470,11)
			
			# Refresh checkboxes
			if settings.hasMusic() == True:
				menu_images['music_checkbox_checked'].blit(36,9)
			else:
				menu_images['music_checkbox_unchecked'].blit(36,9)
			
			if settings.hasSound() == True:
				menu_images['sound_checkbox_checked'].blit(400,9)
			else:
				menu_images['sound_checkbox_unchecked'].blit(400,9)
			
			# Refresh about bubble
			if menu.hasAbout() == True:
				menu_images['about_bubble'].blit(650,76)
		
		# Levels & help images
		elif current_scene is 'levels' or current_scene is 'help':
			# Read image objects
			levels_images = levels.images()
			help_images = help.images()
			difficulty_num = settings.hasDifficulty()
			
			# Refresh main layers & UI images
			levels_images['help_button'].blit(129,147)
			levels_images['select'].blit(100,175)
			levels_images['fight_button'].blit(129,199)
			
			levels_images['help_button'].blit(619,147)
			levels_images['select'].blit(590,175)
			levels_images['fight_button'].blit(619,199)
			
			levels_images['bottom'].blit(0,0)
			
			# Refresh UI images
			levels_images['logo'].blit(830,15)
			levels_images['back_button'].blit(20,15)
			
			# Refresh UI labels
			levels_images['bacteria_label'].blit(180,430)
			levels_images['virus_label'].blit(708,429)
			
			# Refresh UI texts
			levels_images['bacteria_text'].blit(143,282)
			levels_images['virus_text'].blit(633,282)
			
			# Refresh UI buttons
			if difficulty_num != 1:
				levels_images['difficulty_easy_disabled'].blit(440,2)
			if difficulty_num != 2:
				levels_images['difficulty_medium_disabled'].blit(485,2)
			if difficulty_num != 3:
				levels_images['difficulty_hard_disabled'].blit(530,2)
			
			if difficulty_num == 1:
				levels_images['difficulty_easy_enabled'].blit(440,1)
			if difficulty_num == 2:
				levels_images['difficulty_medium_enabled'].blit(485,1)
			if difficulty_num == 3:
				levels_images['difficulty_hard_enabled'].blit(530,1)
			
			# Refresh help layer
			if 'bg' in help_images:
				help_images['bg'].blit(-58,help.slider())
		
		# Game images
		elif current_scene is 'game':
			# Read image objects
			game_images = game.images()
			corps = game.GET_CORPS()
			
			# Bacteria mode
			for key in corps.keys():
				if 'Phagocyte' in key:
					# Set an anchor
					corps[key]['sprite'].anchor_x = 40
					corps[key]['sprite'].anchor_y = 40
					
					# Process new position
					phagocyte_sprite = pyglet.sprite.Sprite(corps[key]['sprite'], x = corps[key]['x'], y = corps[key]['y'])
					
					# Process new rotation
					phagocyte_sprite.rotation = math.degrees(-corps[key]['angle'])
					
					# Set it translucent
					if not dynamics.hasPhagocyte():
						phagocyte_sprite.opacity = 80
					
					phagocyte_sprite.draw()
				elif 'cellule' in key:
					if corps[key]['inoculate'][0] is True:
						if corps[key]['inoculate'][1]<=corps[key]['inoculate'][2]/3:
							corps[key]['sprite1'].blit(corps[key]['x'] - corps[key]['r'], corps[key]['y'] - corps[key]['r'])
						elif corps[key]['inoculate'][1]<=2*corps[key]['inoculate'][2]/3:
							corps[key]['sprite2'].blit(corps[key]['x'] - corps[key]['r'], corps[key]['y'] - corps[key]['r'])
						elif corps[key]['inoculate'][1]<=3*corps[key]['inoculate'][2]/3:
							corps[key]['sprite3'].blit(corps[key]['x'] - corps[key]['r'], corps[key]['y'] - corps[key]['r'])
					else:
						corps[key]['sprite'].blit(corps[key]['x'] - corps[key]['r'], corps[key]['y'] - corps[key]['r'])

				else:
					corps[key]['sprite'].blit(corps[key]['x'] - corps[key]['r'], corps[key]['y'] - corps[key]['r'])

			
			# Must wait initialization
			if not dynamics.hasPhagocyte():
				game_images['delay'].blit(170,0)
			
			# Refresh layers
			if game.state() is 'win' or game.state() is 'loose':
				# Display end layer
				if game.state() is 'win':
					game_images['win'].blit(0,0)
				
				elif game.state() is 'loose':
					game_images['loose'].blit(0,0)
			
			elif game.paused():
				game_images['pause'].blit(0,0)
			
			else:
				cursor.disable()
	
	# Events
	@current_window.event
	def on_mouse_press(x, y, button, modifiers):
		current_scene = scene.get()
		
		# Left click
		if button == mouse.LEFT:
			# Menu clicks
			if current_scene is 'menu':
				# Music button
				if (x >= 40 and x <= 86 and y >= 13 and y <= 59) or (x >= 116 and x <= 294 and y >= 21 and y <= 50):
					sound.play('02')
					settings.toggleMusic()
				
				# Sound button
				if (x >= 404 and x <= 450 and y >= 13 and y <= 59) or (x >= 480 and x <= 790 and y >= 21 and y <= 50):
					sound.play('02')
					settings.toggleSound()
				
				# About button
				if x >= 932 and x <= 978 and y >= 13 and y <= 59 or menu.hasAbout() == True:
					sound.play('03')
					menu.toggleAbout()
				
				# Play button
				if x >= 40 and x <= 310 and y >= 497 and y <= 572:
					sound.play('01')
					levels.init()
			
			# Levels clicks
			elif current_scene is 'levels':
				# Back button
				if x >= 20 and x <= 204 and y >= 15 and y <= 57:
					sound.play('01')
					menu.init()
				
				# Fight (bacteria) button
				if x >= 142 and x <= 392 and y >= 199 and y <= 244:
					sound.play('04')
					
					game.init('bacteria')
				
				# Fight (virus) button
				if x >= 632 and x <= 882 and y >= 199 and y <= 244:
					sound.play('04')
					game.init('virus')
				
				# Help (bacteria) button
				if x >= 142 and x <= 392 and y >= 164 and y <= 198:
					sound.play('03')
					help.init('bacteria')
				
				# Help (virus) button
				if x >= 632 and x <= 882 and y >= 164 and y <= 198:
					sound.play('03')
					help.init('virus')
				
				# Difficulty (easy) button
				if x >= 452 and x <= 482 and y >= 15 and y <= 57:
					sound.play('02')
					settings.toggleDifficulty(1)
				
				# Difficulty (medium) button
				if x >= 497 and x <= 528 and y >= 15 and y <= 57:
					sound.play('02')
					settings.toggleDifficulty(2)
				
				# Difficulty (hard) button
				if x >= 542 and x <= 573 and y >= 15 and y <= 57:
					sound.play('02')
					settings.toggleDifficulty(3)
			
			# Help clicks
			elif current_scene is 'help':
				scene.set('levels')
				help.slide(1)
			
			# Game clicks
			elif current_scene is 'game':
				# End of game motion
				if game.state() is 'win' or game.state() is 'loose':
					# Quit button
					if x >= 260 and x <= 304 and y >= 124 and y <= 172:
						pyglet.app.exit()
					
					# Menu button
					elif x >= 324 and x <= 372 and y >= 124 and y <= 166:
						menu.init()
					
					# Retry button
					elif x >= 694 and x <= 742 and y >= 124 and y <= 172:
						game.init(mode.get())
				
				# Paused game clicks
				elif game.paused() is True:
					# Quit button
					if x >= 341 and x <= 386 and y >= 227 and y <= 270:
						pyglet.app.exit()
					
					# Menu button
					elif x >= 405 and x <= 453 and y >= 227 and y <= 270:
						if game.pause() is False:
							menu.init()
					
					# Resume button
					elif x >= 647 and x <= 683 and y >= 227 and y <= 270:
						if game.pause() is False:
							cursor.disable()
							background.scene_speed('game')
		
		return True
	
	@current_window.event
	def on_mouse_motion(x, y, dx, dy):
		current_scene = scene.get()
		
		# Menu motion
		if current_scene is 'menu':
			# Music button
			if (x >= 40 and x <= 86 and y >= 13 and y <= 59) or (x >= 116 and x <= 294 and y >= 21 and y <= 50):
				cursor.set('pointer')
			
			# Sound button
			elif (x >= 404 and x <= 450 and y >= 13 and y <= 59) or (x >= 480 and x <= 790 and y >= 21 and y <= 50):
				cursor.set('pointer')
			
			# About button
			elif x >= 932 and x <= 978 and y >= 13 and y <= 59:
				cursor.set('pointer')
			
			# Play button
			elif x >= 40 and x <= 310 and y >= 497 and y <= 572:
				cursor.set('pointer')
			
			# Default
			else:
				cursor.set('default')
		
		# Levels motion
		elif current_scene is 'levels':
			# Back button
			if x >= 20 and x <= 204 and y >= 15 and y <= 57:
				cursor.set('pointer')
			
			# Fight (bacteria) button
			elif x >= 142 and x <= 392 and y >= 199 and y <= 244:
				cursor.set('pointer')
			
			# Fight (virus) button
			elif x >= 632 and x <= 882 and y >= 199 and y <= 244:
				cursor.set('pointer')
			
			# Help (bacteria) button
			elif x >= 142 and x <= 392 and y >= 164 and y <= 198:
				cursor.set('pointer')
			
			# Help (virus) button
			elif x >= 632 and x <= 882 and y >= 164 and y <= 198:
				cursor.set('pointer')
			
			# Difficulty (easy) button
			elif x >= 452 and x <= 482 and y >= 15 and y <= 57:
				cursor.set('pointer')
			
			# Difficulty (medium) button
			elif x >= 497 and x <= 528 and y >= 15 and y <= 57:
				cursor.set('pointer')
			
			# Difficulty (hard) button
			elif x >= 542 and x <= 573 and y >= 15 and y <= 57:
				cursor.set('pointer')
			
			# Default
			else:
				cursor.set('default')
		
		# Game motion
		elif current_scene is 'game':
			# End of game motion
			if game.state() is 'win' or game.state() is 'loose':
				# Quit button
				if x >= 260 and x <= 304 and y >= 124 and y <= 172:
					cursor.set('pointer')
				
				# Menu button
				elif x >= 324 and x <= 372 and y >= 124 and y <= 166:
					cursor.set('pointer')
				
				# Retry button
				elif x >= 694 and x <= 742 and y >= 124 and y <= 172:
					cursor.set('pointer')
				
				# Default
				else:
					cursor.set('default')
			
			# Paused game motion
			elif game.paused() is True:
				# Quit button
				if x >= 341 and x <= 386 and y >= 227 and y <= 270:
					cursor.set('pointer')
				
				# Menu button
				elif x >= 405 and x <= 453 and y >= 227 and y <= 270:
					cursor.set('pointer')
				
				# Resume button
				elif x >= 647 and x <= 683 and y >= 227 and y <= 270:
					cursor.set('pointer')
				
				# Default
				else:
					cursor.set('default')
		
		return True
	
	# Key down
	@current_window.event
	def on_key_press(symbol, modifiers):
		current_scene = scene.get()
		game_state=game.state()
		corps = game.GET_CORPS()

		# Escape pressed
		if symbol == key.ESCAPE:
			# Game back action
			if current_scene is 'game':
				if game.pause() is True:
					cursor.set('default')
					background.scene_speed('pause')
				
				else:
					cursor.disable()
					background.scene_speed('game')
			
			# Levels back action
			elif current_scene is 'levels':
				menu.init()
			
			# Help back action
			elif current_scene is 'help':
				scene.set('levels')
				help.slide(1)
			
			# Menu back action
			elif current_scene is 'menu':
				pyglet.app.exit()
		
		# Arrow pressed
		elif current_scene is 'game':	
			if 'Phagocyte' in corps.keys():	
				if symbol == key.UP:
					corps['Phagocyte']['pushUp'] = 1
				if symbol == key.DOWN:
					corps['Phagocyte']['pushDown'] = 1
				if symbol == key.RIGHT:
					corps['Phagocyte']['pushRight'] = 1
				if symbol == key.LEFT:
					corps['Phagocyte']['pushLeft'] = 1
		
		return True
	
	@current_window.event
	def on_key_release(symbol, modifiers):
		current_scene = scene.get()
		
		if current_scene is 'game':
			corps = game.GET_CORPS()
			if 'Phagocyte' in corps.keys():	
				if symbol == key.UP:
					corps['Phagocyte']['pushUp'] = 0
				if symbol == key.DOWN:
					corps['Phagocyte']['pushDown'] = 0
				if symbol == key.RIGHT:
					corps['Phagocyte']['pushRight'] = 0
				if symbol == key.LEFT:
					corps['Phagocyte']['pushLeft'] = 0
		
		return True
