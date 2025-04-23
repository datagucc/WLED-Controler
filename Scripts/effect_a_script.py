import requests

# Paramètres WLED
wled_ip = op('../control_WLED_v5').par.Ipwled  # Récupérer l'IP depuis TouchDesigner

# Récupérer la valeur de l'intensité depuis TouchDesigner
intensity_value = int(op('params')[5] * 255)  # Normaliser entre 0 et 255

# Construire la requête HTTP
url = f"http://{wled_ip}/json/state"
payload = {
    "seg": [{"ix": intensity_value}]  # 'ix' contrôle l'intensité de l'effet
}

# Envoyer la requête HTTP
requests.post(url, json=payload)