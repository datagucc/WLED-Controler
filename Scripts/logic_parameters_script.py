# me - this DAT
# 
# channel - the Channel object which has changed
# sampleIndex - the index of the changed sample
# val - the numeric value of the changed sample
# prev - the previous sample value
# 
# Make sure the corresponding toggle is enabled in the CHOP Execute DAT.

def onOffToOn(channel, sampleIndex, val, prev):
	return

def whileOn(channel, sampleIndex, val, prev):
	return

def onOnToOff(channel, sampleIndex, val, prev):
	if channel.name == 'effect_bpm' and  op('params')[9]==1:
		print(f"🔄TRIGGER {channel.name} a changé de {prev} à {val}")
		op('script_kick_on').run()
	return

def whileOff(channel, sampleIndex, val, prev):
	return

def onValueChange(channel, sampleIndex, val, prev):
	""" Exécute le script si une des constantes a changé """
	colors1_changed_channels = ['r', 'g', 'b']
	if channel.name in colors1_changed_channels:
		print(f"TRIGGER🔄 {channel.name} a changé de {prev} à {val}")
		# Exécuter un autre script ou une action
		#op('script_effect').run()
		op('script_color1').run()
		
	if channel.name == 'speed':
		print(f"TRIGGER🔄 {channel.name} a changé de {prev} à {val}")
		op('script_speed').run()
		#print('ok')
	if channel.name == 'effect_id':
		print(f"TRIGGER {channel.name} a changé de {prev} à {val}")
		op('script_effect_id').run()
	if channel.name == 'effect_a':
		print(f"🔄TRIGGER {channel.name} a changé de {prev} à {val}")
		op('script_effect_a').run()
	if channel.name == 'brigthness':
		print(f"🔄TRIGGER {channel.name} a changé de {prev} à {val}")
		op('script_brigthness').run()
	if channel.name =='segment':
		print(f"🔄TRIGGER {channel.name} a changé de {prev} à {val}")
		op('script_segment').run()
		
	if channel.name == 'kickT':
		print(f"TRIGGER {channel.name} a changé de {prev} à {val}")
		op('script_brigthnessbpm').run()
	if channel.name == 'kickD' and op('params')[9]==1:
		print(f"🔄TRIGGER {channel.name} a changé de {prev} à {val}")
		op('script_kick_bpm').run()
	if channel.name == 'favorite':
		print(f"TRIGGER {channel.name} a changé de {prev} à {val}")
		op('script_favorite').run()
	return

