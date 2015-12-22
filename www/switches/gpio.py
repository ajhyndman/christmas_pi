try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Error importing RPi.GPIO!  This is probably because you need superuser privileges.  You can achieve this by using 'sudo' to run your script")





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
        
        
switch_one   = new Switch(11)
switch_two   = new Switch(12)
switch_three = new Switch(15)
switch_four  = new Switch(16)