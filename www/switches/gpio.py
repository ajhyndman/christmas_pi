try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Error importing RPi.GPIO!  This is probably because you need superuser privileges.  You can achieve this by using 'sudo' to run your script")





GPIO.setmode(GPIO.BOARD)





class Switch:
    id = 0
    
    def __init__(self, id):
        self.id = id
        GPIO.setup(self.id, GPIO.OUT)
        
    def getStatus():
    
    def on():
        GPIO.output(self.id, GPIO.LOW)
        
    def off():
        GPIO.output(self.id, GPIO.HIGH)
        
        
switch_one   = new Switch(11)
switch_two   = new Switch(12)
switch_three = new Switch(15)
switch_four  = new Switch(16)