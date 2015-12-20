import RPi.GPIO as GPIO
import time
import config

for pin in config.PINS[:1]:
    GPIO.setup(pin, GPIO.OUT)
    time.sleep(0.5)
    GPIO.output(pin, config.ON)

time.sleep(5)
GPIO.cleanup()
