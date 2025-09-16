# config_gpio.py
import MockGPIO as GPIO

def initialiser_broches():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(27, GPIO.OUT)
