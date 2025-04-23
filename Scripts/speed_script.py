import requests

# Paramètres WLED
wled_ip = op('../control_WLED_v5').par.Ipwled  # Récupérer l'IP depuis TouchDesigner

# Récupérer la valeur de la vitesse depuis TouchDesigner
speed_value = int(op('params')[4])  # Normaliser entre 0 et 255

# Construire la requête HTTP
url = f"http://{wled_ip}/json/state"
payload = {
    "seg": [{"sx": speed_value}]  # 'sx' contrôle la vitesse de l'effet
}

# Envoyer la requête HTTP
requests.post(url, json=payload)