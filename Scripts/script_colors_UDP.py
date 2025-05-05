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
	return

def whileOff(channel, sampleIndex, val, prev):
	return

def onValueChange(channel, sampleIndex, val, prev):
	import json
	
	#first color 
	r1 = int(op('colors_params')['red'] * 255)
	g1 = int(op('colors_params')['green'] * 255)
	b1 = int(op('colors_params')['blue'] * 255)
	
	#second color
	r2 = int(op('colors_params')['r2'] * 255)
	g2 = int(op('colors_params')['g2'] * 255)
	b2 = int(op('colors_params')['b2'] * 255)
	
	#thirdcolor
	r3 = int(op('colors_params')['r3'] * 255)
	g3 =  int(op('colors_params')['g3'] * 255)
	b3 = int(op('colors_params')['b3'] * 255)
	
	if op('colors_params')['bo'] ==1:
		r1=0
		g1=0
		b1=0
		r2=0
		g2=0
		b2=0
		r3=0
		g3=0
		b3=0
		#print (r,g,b)
	if op('colors_params')['second_ok'] ==0:
		r2=0
		g2=0
		b2=0
	if op('colors_params')['third_ok'] ==0:
		r3=0
		g3=0
		b3=0
	data = {"seg": [ {  "col": [[r1, g1, b1],[r2,g2,b2],[r3,g3,b3]] } ] }
	# Convert in Bytes
	json_data = json.dumps(data).encode('utf-8')
    #Send to UDP
	udp = op('udpout_colors')
	udp.sendBytes(json_data)

    
    

    #
    #
	

	return
	