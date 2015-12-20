import RPi.GPIO as GPIO
import time
import config

for pin in config.PINS:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, config.ON)

time.sleep(5)
GPIO.cleanup()
