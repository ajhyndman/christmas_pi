import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

all_pins = (11, 12, 15, 16) 
GPIO.setup(11, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)

p11 = GPIO.PWM(11, 0.25)
p12 = GPIO.PWM(12, 0.25)
p15 = GPIO.PWM(15, 0.25)
p16 = GPIO.PWM(16, 0.25)

p11.start(75)
p12.start(75)
p15.start(75)
p16.start(75)
# input('Press return to stop:')   # use raw_input for Python 2
time.sleep(30)
p11.stop()
p12.stop()
p15.stop()
p16.stop()
GPIO.cleanup()