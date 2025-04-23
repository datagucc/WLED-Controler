import requests

# Adresse IP de ton WLED
wled_ip = op('../control_WLED_v5').par.Ipwled  # Récupérer l'IP depuis TouchDesigner  # Remplace par l'IP de ton contrôleur

# URL de l'API JSON
URL = f"http://{wled_ip}/json/state"

def toggle_led(on):
    """
    Envoie une requête POST pour allumer ou éteindre les LEDs.
    :param on: True pour allumer, False pour éteindre
    """
    data = {"on": on}
    headers = {"Content-Type": "application/json"}

    try:
        response = requests.post(URL, json=data, headers=headers)
        if response.status_code == 200:
            state = "allumées" if on else "éteintes"
            print(f"SCRIPT ✅ LEDs {state} avec succès !")
        else:
            print(f"⚠️ Erreur {response.status_code} : {response.text}")
    except Exception as e:
        print(f"❌ Erreur lors de l'envoi : {e}")

#print(op('params')[15])
val = op('params')[15]
if val > 0:  # Appui sur le bouton
	toggle_led(False)  # Éteindre les LEDs
else:  # Relâchement du bouton
	toggle_led(True)  # Rallumer les LEDs
#print(op('params')[15])
