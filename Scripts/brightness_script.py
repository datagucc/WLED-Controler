import requests

# Paramètres WLED
wled_ip = op('../control_WLED_v5').par.Ipwled  # Récupérer l'IP depuis TouchDesigner

# Récupérer la valeur de brightness depuis TouchDesigner
brightness_value = int(op('params')[10] )  # Normaliser entre 0 et 255

# Construire la requête HTTP
url = f"http://{wled_ip}/json/state"
payload = {
    "bri": brightness_value  # 'bri' contrôle la luminosité globale
}

# Envoyer la requête HTTP
requests.post(url, json=payload)