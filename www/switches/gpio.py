try:
    import RPi.GPIO as GPIO
except:
    from . import SpoofGPIO as GPIO
    print("Server could not locate RPi.GPIO, using a development placeholder instead")





GPIO.setmode(GPIO.BOARD)





class Switch:
    id = 0
    status = GPIO.HIGH
    
    def __init__(self, id):
        self.id = id
        GPIO.setup(self.id, GPIO.OUT)
        GPIO.output(self.id, self.status)
        
    def get_status(self):
        return 'off' if self.status else 'on'
    
    def on(self):
        self.status = GPIO.LOW
        GPIO.output(self.id, self.status)
        
    def off(self):
        self.status = GPIO.HIGH
        GPIO.output(self.id, self.status)
        
    def toggle(self):
        self.status = not self.status
        GPIO.output(self.id, self.status)        





SWITCHES = [Switch(i) for i in [11, 12, 15, 16]]