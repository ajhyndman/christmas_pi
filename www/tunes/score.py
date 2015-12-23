import time
from . import gpio





class Note:
    delay = 0
    # switch = gpio.Switch(0)
    switch = None
    
    def __init__(self, delay, switch):
        self.delay = delay
        self.switch = switch
    
    def play(self):
        try:
            self.switch.on()
            time.sleep(self.delay*0.75)
            self.switch.off()
            time.sleep(self.delay*0.25)
        except:
            print('Notes must be played with an object of type "Switch".')





class Rest:
    delay = 0
    
    def __init__(self, delay):
        self.delay = delay
    
    def play(self):
        time.sleep(self.delay)