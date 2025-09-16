# systeme_alerte.py
# Système d'alerte d'urgence avec simulation GPIO
# Utilise une interface console pour simuler les appuis sur le bouton
# et envoie des alertes à un serveur via HTTP POST.
import MockGPIO as GPIO
import time
import requests
import json
from datetime import datetime
import socket
import threading

# Configuration
BUTTON_PIN = 17
LED_PIN = 27
SERVER_URL = "http://localhost:5000/alerte"
DEVICE_ID = f"Simu-{socket.gethostname()}"

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(LED_PIN, GPIO.OUT)

def obtenir_ip_locale():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except:
        return "IP inconnue"

def clignoter_led(nb_fois=3, duree=0.2):
    for _ in range(nb_fois):
        GPIO.output(LED_PIN, GPIO.HIGH)
        time.sleep(duree)
        GPIO.output(LED_PIN, GPIO.LOW)
        time.sleep(duree)

def envoyer_alerte():
    data = {
        "message": "Alerte d'urgence déclenchée !",
        "timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        "source": DEVICE_ID,
        "ip_source": obtenir_ip_locale(),
        "type": "urgence"
    }

    print("[INFO] Envoi de l'alerte en cours...")
    GPIO.output(LED_PIN, GPIO.HIGH)

    try:
        response = requests.post(SERVER_URL, json=data, timeout=3)

        if response.status_code == 200:
            print("Alerte envoyée avec succès !")
            GPIO.output(LED_PIN, GPIO.LOW)
            clignoter_led(2, 0.15)
        else:
            print(f"Erreur : Code serveur {response.status_code}")
            GPIO.output(LED_PIN, GPIO.LOW)
            clignoter_led(4, 0.1)

    except requests.exceptions.ConnectionError:
        print("Serveur injoignable")
        GPIO.output(LED_PIN, GPIO.LOW)
        clignoter_led(6, 0.3)
    except Exception as e:
        print(f"Exception : {e}")
        GPIO.output(LED_PIN, GPIO.LOW)
        clignoter_led(5, 0.2)

def ecoute_bouton():
    derniere_alerte = 0
    while True:
        if GPIO.input(BUTTON_PIN) == GPIO.LOW:
            now = time.time()
            if now - derniere_alerte > 3:
                print("\nBouton d'urgence activé (GPIO)")
                envoyer_alerte()
                derniere_alerte = now
        time.sleep(0.1)

def interface_simulation():
    print("\n--- Interface de simulation ---")
    print("Appuyez sur [Entrée] pour simuler un appui bouton.")
    print("Tapez 'q' puis [Entrée] pour quitter.\n")

    while True:
        user_input = input(">>> ")
        if user_input.lower() == 'q':
            print("Arrêt demandé.")
            break
        else:
            print("[SIMULATION] Appui bouton simulé.")
            GPIO.simulate_button_press(BUTTON_PIN)
            time.sleep(0.5)
            GPIO.simulate_button_release(BUTTON_PIN)

print("=== SYSTÈME D'ALERTE D'URGENCE (SIMULATION) ===")
print(f"Matériel : {DEVICE_ID}")
print(f"Serveur : {SERVER_URL}")
print(f"IP locale : {obtenir_ip_locale()}")
print("--------------------------------------------------")

try:
    # Détection GPIO
    thread_gpio = threading.Thread(target=ecoute_bouton)
    thread_gpio.daemon = True
    thread_gpio.start()

    # Interface utilisateur
    interface_simulation()

except KeyboardInterrupt:
    print("\nInterruption clavier reçue. Fin du programme.")

finally:
    GPIO.cleanup()
    print("GPIO nettoyé. Fin.")
