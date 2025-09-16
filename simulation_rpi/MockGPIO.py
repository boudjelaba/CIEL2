# MockGPIO.py
# Simulation du module RPi.GPIO pour tests sur PC

DEBUG = False

BCM = 'BCM'
IN = 'IN'
OUT = 'OUT'
PUD_UP = 'PUD_UP'
LOW = 0
HIGH = 1

_pins = {}
_mode = None

def setmode(mode):
    global _mode
    _mode = mode
    print(f"[GPIO] Mode défini sur {mode}")

def setup(pin, direction, pull_up_down=None):
    _pins[pin] = {
        'direction': direction,
        'state': HIGH if pull_up_down == PUD_UP else LOW,
        'pull': pull_up_down
    }
    print(f"[GPIO] Réglage pin {pin} en {direction} avec pull={pull_up_down}")

def input(pin):
    #
    if pin not in _pins:
        raise ValueError(f"Pin {pin} non configurée")
    # 
    state = _pins[pin]['state']
    if DEBUG:
        print(f"[GPIO] Lecture pin {pin} : {state}")
    return state

def output(pin, state):
    _pins[pin]['state'] = state
    print(f"[GPIO] Écriture pin {pin} => {'HIGH' if state else 'LOW'}")

def cleanup():
    _pins.clear()
    print("[GPIO] Nettoyage terminé")

# Simulation du bouton
def simulate_button_press(pin):
    print(f"[SIMULATION] Bouton {pin} pressé")
    _pins[pin]['state'] = LOW

def simulate_button_release(pin):
    print(f"[SIMULATION] Bouton {pin} relâché")
    _pins[pin]['state'] = HIGH