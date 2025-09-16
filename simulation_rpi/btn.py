import MockGPIO as GPIO
from config_gpio import initialiser_broches
import time

initialiser_broches()
GPIO.simulate_button_press(17)
time.sleep(1)
GPIO.simulate_button_release(17)
