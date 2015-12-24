import time
import gpio


BEAT_DURATION = 0.1





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





# class Score:
#     notelist = []
    
#     def __init__(self, notelist):
#         self.notelist = notelist


# Build a Score from a list of beat timings
def build_score_from_beats(beatlist, switch):
    score = []
    t, tprev, tdelta = 0, 0, 0
    
    for beat in beatlist:
        tprev = t
        t = beat
        tdelta = t - tprev
        score.append(Note(tdelta, switch))

    return score
