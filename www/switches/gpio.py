try:
    import RPi.GPIO as GPIO
except:
    from . import SpoofGPIO as GPIO
    print("Server could not locate RPi.GPIO, using a development placeholder instead")





GPIO.setmode(GPIO.BOARD)





class Switch:
    id = 0
    status = False
    
    def __init__(self, id):
        self.id = id
        GPIO.setup(self.id, GPIO.OUT)
        
    def getStatus(self):
        return self.status
    
    def on(self):
        self.status = GPIO.LOW
        GPIO.output(self.id, self.status)
        
    def off(self):
        self.status = GPIO.HIGH
        GPIO.output(self.id, self.status)





switch_one   = Switch(11)
switch_two   = Switch(12)
switch_three = Switch(15)
switch_four  = Switch(16)