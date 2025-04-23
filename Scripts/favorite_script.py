import struct
import requests
import json


# Paramètres WLED
wled_ip_old = "192.168.1.5"  # L'adresse IP de ton WLED
wled_ip = op('../control_WLED_v5').par.Ipwled
port = 21324        # Le port UDP de WLED
udp_out = op('udpout1')  # Ton DAT de sortie UDP

# Récupérer les valeurs du Noise CHOP (supposé op('params') qui contient les params)
effects = op('params') 
fav_id = effects[12]


	
def send_wled_preset(preset_id):

    # URL de l'API JSON de WLED
    url = f"http://{wled_ip}/json"

    # Données JSON à envoyer
    data = { "ps": int(preset_id) }

    # Headers pour indiquer que c'est du JSON
    headers = { "Content-Type": "application/json" }
    #preset_id = list[preset_id]
	
    try:
        # Envoi de la requête POST
        response = requests.post(url, json=data, headers=headers)
        
        # Vérification de la réponse
        if response.status_code == 200:
            print(f"SCRIPT✅ Preset {preset_id} activé avec succès !")
        else:
            print(f"⚠️ Erreur {response.status_code} : {response.text}")

    except Exception as e:
        print(f"❌ Erreur lors de l'envoi : {e}")

# Exemple d'appel avec un preset ID dynamique
send_wled_preset(fav_id)  # Change 5 par le preset voulu



# Récupérer les valeurs des paramètres personnalisés dans TouchDesigner
#effect_id = op_effect_id[0]  # Paramètre effect_id

