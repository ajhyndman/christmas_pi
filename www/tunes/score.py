import time
import gpio





ON = True
OFF = False





class OLD_Note:

    # the percentage of one bar that the note should last.
    delay = 0
    # switch = gpio.Switch(0)
    switches = []
    # length of a bar in seconds
    beat_duration = 1
    
    def __init__(self, delay, switches):
        self.delay = delay
        self.switches = switches
    
    def add_switch(self, switch):
        self.switches.append(switch)
    
    # Plays a note.
    #
    # @param beat:
    #   the length of the bar the note is scaled against.
    def play(self, beat_duration):
        if (beat_duration != None):
            self.beat_duration = beat_duration
        
        try:
            for switch in self.switches:
                switch.on()
            time.sleep(self.delay*0.8*self.beat_duration)
            for switch in self.switches:
                switch.off()
            time.sleep(self.delay*0.2*self.beat_duration)
        except Exception:
            print('Notes must be played with an object of type "Switch".')


class OLD_Rest:
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
def OLD_build_score_from_beats(beatlist, switch):
    score = []
    t, tprev, tdelta = 0, 0, 0
    
    for beat in beatlist:
        tprev = t
        t = beat
        tdelta = t - tprev
        score.append(Note(tdelta, switch))

    return score





class Tune(object):
    name = 'default'
    bpm = 75 # beats per minute
    score = []
    
    def __init__(self, name, bpm, score):
        self.name = name
        self.bpm = bpm
        self.score = score
        
    def set_score(self, score):
        self.score = score
    
    def play(self):
        for note in self.score:
            note.play(60/self.bpm)
            
        for switch in gpio.SWITCHES:
            switch.on()
            
            
            
            
            
            
class Note(object):
    duration = 0
    silent = False

    def __init__(self, duration, silent=False):
        self.duration = duration
        self.silent = silent





class Rest(Note):
    def __init__(self, duration):
        super(Rest, self).__init__(duration, silent=True) 





class Track:
    notes = []
    switch = None
    
    def __init__(self, switch, notes):
        self.switch = switch
        self.notes = notes
    
    # Returns a list of 3-tuples: timestamp, bool on/off, switch number.
    def get_timestamps(self, bpm):
        cur_timestamp = 0
        timestamps = []
        beat_duration = 60.0/bpm

        for note in self.notes:
            if not note.silent:
                timestamps.append((cur_timestamp, ON, self.switch))
            cur_timestamp += note.duration * beat_duration
            if not note.silent:
                timestamps.append((cur_timestamp - 0.2 * beat_duration, OFF, self.switch))

        return timestamps
        


class Track_Compilation(Tune):
    # Sorted list of 3-tuples: timestamp, bool on/off, switch number.
    switch_timings = []
    
    def __init__(self, title, bpm, tracks = []):
        super(Track_Compilation, self).__init__(title, bpm, [])
        for track in tracks:
            self.add_track(track)
    
    def add_track(self, track):
        self.switch_timings.extend(track.get_timestamps(self.bpm))
        self.switch_timings = sorted(self.switch_timings)

    def play(self):
        # Turn off all lights.
        for switch in gpio.SWITCHES:
            switch.off()
    
        prev_time = 0
        for timestamp, state, switch_index in self.switch_timings:
            time.sleep(timestamp - prev_time)
            prev_time = timestamp
            if state is ON:
                gpio.SWITCHES[switch_index].on()
            if state is OFF:
                gpio.SWITCHES[switch_index].off()
                
        # Turn on all lights
        for switch in gpio.SWITCHES:
            switch.on()