# me - this DAT
# 
# channel - the Channel object which has changed
# sampleIndex - the index of the changed sample
# val - the numeric value of the changed sample
# prev - the previous sample value
# 
# Make sure the corresponding toggle is enabled in the CHOP Execute DAT.
import requests
import json
import time


# Global variables for timing control
last_send_time = 0  # Store the last time a request was sent
MIN_INTERVAL = 1  # Minimum interval between sends (in seconds)
THRESHOLD = 0.02    # Ignore tiny changes under 2%
def onOffToOn(channel, sampleIndex, val, prev):
	return

def whileOn(channel, sampleIndex, val, prev):
	return

def onOnToOff(channel, sampleIndex, val, prev):
	return

def whileOff(channel, sampleIndex, val, prev):
	return

def onValueChange(channel, sampleIndex, val, prev):
    # IP address of the WLED (retrieved dynamically from the base)
    global last_send_time
    
       # --- Deadzone Check: Ignore tiny changes ---
    if abs(val - prev)< THRESHOLD:
    	return
    	
        # --- Minimum Time Check: Avoid spamming requests ---
    now = time.time()
    if now - last_send_time < MIN_INTERVAL:
    	return
    	
        # Update the last send time
    last_send_time = now
       # --- WLED Parameters ---
    wled_ip = parent().par.Ipwled
   
    

    # Read every params 
    favorite = int(op('effect_params')['Favorite'])    #  effet mode, favorite
    speed = int(op('effect_params')['Speed'])           # speed
    intensity = int(op('effect_params')['Intensity'] )  # intensity
    brightness = int(op('effect_params')['Brigthness']) # brightness
    effect_id = int(op('effect_params')['Effectid']) # effect_id
    

    # Mapping MIDI controller button to favorite WLED effect ID
    mapping_favorite = {1: 88, 2: 28,3: 44,4: 148, 5: 185,6: 144,7: 1,8: 57}
    is_favorite = int(op('effect_params')['Usingfav'])
    
    # Custom effect parameters (for some WLED effects)
    c1 = int(op('effect_params')['Customparama'])
    c2 = int(op('effect_params')['Customparamb'])
    c3 = int(op('effect_params')['Customparamc'])
    
    # Select favorite effect or manual effect ID
    if is_favorite :
    	favorite = mapping_favorite.get(favorite,0) #Default to 0 if not found
    else :
    	favorite = effect_id


    # Construct the data to send, in form of JSON 
    data = {
        "seg": [{
            "id": 0  # my main segment
            ,"fx": favorite   # effect
            ,"sx": speed      # speed
            ,"ix": intensity   # intensity
            ,"c1": c1
            ,"c2": c2
            ,"c3": c3
        }],
        "bri": brightness   # brightness 
    }
    #print(data)

    url = f"http://{wled_ip}/json/state"
    print(favorite)

    headers = { "Content-Type": "application/json" }

    try:
        response = requests.post(url, json=data, headers=headers)
        if response.status_code == 200:
            debug(f"✅ HTTP POST success: {data}")
        else:
            debug(f"⚠️ HTTP error {response.status_code}: {response.text}")
    except Exception as e:
        debug(f"❌ HTTP POST failed: {e}")

    return 
    
   


	