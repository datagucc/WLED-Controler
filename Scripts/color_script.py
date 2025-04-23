import struct
import requests


# Paramètres WLED
wled_ip_old = "192.168.1.5"  # L'adresse IP de ton WLED
wled_ip = op('../control_WLED_v5').par.Ipwled
port = 21324        # Le port UDP de WLED
udp_out = op('udpout1')  # Ton DAT de sortie UDP


# Fonction pour envoyer une requête de changement de couleur
def update_wled_color(r, g, b):
    """
    Met à jour uniquement la couleur des LEDs sans toucher aux autres paramètres (effet, vitesse, etc.).
    """

    # Construction de l'URL en envoyant uniquement les valeurs RGB
    url = f"http://{wled_ip}/win&R={r}&G={g}&B={b}"
    
    # Envoi de la requête HTTP
    response = requests.get(url)
    
    # Vérification du statut de la requête
    if response.status_code == 200:
        print(f"Couleur mise à jour : R={r}, G={g}, B={b}")
    else:
        print(f"Erreur lors de la mise à jour de la couleur : {response.text}")


# Récupérer les valeurs du Noise CHOP (supposé op('colors') contient les valeurs RGB)
color_rgb = op('params') 
op_r = color_rgb[0]
op_b = color_rgb[2]
op_g = color_rgb[1]
r_value = int(op_r[0] * 255)
g_value = int(op_g[0] * 255)
b_value = int(op_b[0] * 255)

# Envoi de la mise à jour de la couleur
update_wled_color(r_value, g_value, b_value)