import requests
import json

# Adresse IP du WLED (modifie avec la tienne)
WLED_IP = op('../control_WLED_v5').par.Ipwled
URL = f"http://{WLED_IP}/json/state"

# Récupération des valeurs depuis TouchDesigner
params = op('params')  
start_led = 0  # Début du segment
stop_led = int(params[11])   # Fin du segment

# Construire la charge utile JSON
data = {
    "seg": [{
        "id": 0,  # ID du segment (0 par défaut)
        "start": start_led,
        "stop": stop_led
    }]
}

# Envoyer la requête HTTP
response = requests.post(URL, json=data)

# Vérifier la réponse
if response.status_code == 200:
    print(f"✅ Longueur du segment modifiée : LEDs {start_led} à {stop_led}")
else:
    print(f"❌ Erreur ({response.status_code}) : {response.text}")