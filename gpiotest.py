import RPi.GPIO as GPIO
import time
import config

GPIO.setup(config.PIN1, GPIO.OUT)

for i in range(20):
    time.sleep(0.1)
    GPIO.output(config.PIN1, (i+1)%2)

GPIO.cleanup()
