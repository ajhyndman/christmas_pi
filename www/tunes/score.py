import time
import gpio


BEAT_DURATION = 0.1





class Note:

    # the percentage of one bar that the note should last.
    delay = 0
    # switch = gpio.Switch(0)
    switches = []
    # length of a bar in seconds
    beat = 1
    
    def __init__(self, delay, switches):
        self.delay = delay
        self.switches = switches
    
    def add_switch(self, switch):
        self.switches.append(switch)
    
    # Plays a note.
    #
    # @param beat:
    #   the length of the bar the note is scaled against.
    def play(self, beat):
        if (beat != None):
            self.beat = beat
        
        try:
            for switch in self.switches:
                self.switch.on()
            time.sleep(self.delay*0.75*self.beat)
            for switch in self.switches:
                self.switch.off()
            time.sleep(self.delay*0.25*self.beat)
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
