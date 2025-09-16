# test_composants.py
import MockGPIO as GPIO
import time

# Configuration GPIO
BUTTON_PIN = 17
LED_PIN = 27

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(LED_PIN, GPIO.OUT)

print("=== Test des Composants ===")
print("Appuyez sur le bouton (simulé)")

try:
    while True:
        if GPIO.input(BUTTON_PIN) == GPIO.LOW:
            print("Bouton détecté !")
            GPIO.output(LED_PIN, GPIO.HIGH)
            time.sleep(0.5)
            GPIO.output(LED_PIN, GPIO.LOW)
            time.sleep(0.3)

        time.sleep(0.1)

except KeyboardInterrupt:
    print("\nArrêt du test")
finally:
    GPIO.cleanup()