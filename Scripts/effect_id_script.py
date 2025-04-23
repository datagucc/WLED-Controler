import struct
import requests


# Paramètres WLED
wled_ip_old = "192.168.1.5"  # L'adresse IP de ton WLED
wled_ip = op('../control_WLED_v5').par.Ipwled
port = 21324        # Le port UDP de WLED
udp_out = op('udpout1')  # Ton DAT de sortie UDP
# Fonction pour envoyer une requête HTTP à WLED avec les paramètres spécifiés
def send_wled_command(effect_id):
    """
    Fonction qui envoie une requête HTTP à l'API WLED pour changer l'effet
    et ses paramètres spécifiques comme la vitesse, l'intensité et la couleur.
    """

    # URL de base de l'API WLED pour sélectionner un effet
    url = f"http://{wled_ip}/win&FX={effect_id}"

    # Envoi de la requête HTTP pour appliquer l'effet et ses paramètres
    response = requests.get(url)
    print(url)
    if response.status_code == 200:
        print(f"Effet {effect_id} appliqué avec succès !")
    else:
        print(f"Erreur en appliquant l'effet {effect_id}: {response.text}")

# Récupérer les valeurs du Noise CHOP (supposé op('params') qui contient les params)
effects = op('params') 
op_effect_id = effects[3]

# Récupérer les valeurs des paramètres personnalisés dans TouchDesigner
effect_id = op_effect_id[0]  # Paramètre effect_id

# Appeler la fonction pour envoyer la commande à WLED avec les nouvelles couleurs
send_wled_command(effect_id)