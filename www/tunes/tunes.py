import gpio
import score
import tracks.jinglebells as jinglebells





class Tune:
    name = 'default'
    score = []
    
    def __init__(self, name, score):
        self.name = name
        self.score = score
        
    def set_score(self, score):
        self.score = score
    
    def play(self):
        for note in self.score:
            note.play()





TUNES = [
    Tune('Mary Had a Little Lamb',
        [
            score.Note(0.25, gpio.SWITCHES[0]),
            score.Note(0.25, gpio.SWITCHES[1]),
            score.Note(0.25, gpio.SWITCHES[2]),
            score.Note(0.25, gpio.SWITCHES[1]),
            score.Note(0.25, gpio.SWITCHES[0]),
            score.Note(0.25, gpio.SWITCHES[0]),
            score.Note(0.5, gpio.SWITCHES[0]),
            score.Note(0.25, gpio.SWITCHES[1]),
            score.Note(0.25, gpio.SWITCHES[1]),
            score.Note(0.5, gpio.SWITCHES[1]),
            score.Note(0.25, gpio.SWITCHES[0]),
            score.Note(0.25, gpio.SWITCHES[0]),
            score.Note(0.5, gpio.SWITCHES[0]),
            score.Note(0.25, gpio.SWITCHES[0]),
            score.Note(0.25, gpio.SWITCHES[1]),
            score.Note(0.25, gpio.SWITCHES[2]),
            score.Note(0.25, gpio.SWITCHES[1]),
            score.Note(0.25, gpio.SWITCHES[0]),
            score.Note(0.25, gpio.SWITCHES[0]),
            score.Note(0.25, gpio.SWITCHES[0]),
            score.Note(0.25, gpio.SWITCHES[0]),
            score.Note(0.25, gpio.SWITCHES[1]),
            score.Note(0.25, gpio.SWITCHES[1]),
            score.Note(0.25, gpio.SWITCHES[0]),
            score.Note(0.25, gpio.SWITCHES[1]),
            score.Note(1, gpio.SWITCHES[2]),
        ]),

    # truncates to the first 20 beats (~10s)
    Tune('Jingle Bells',
        score.build_score_from_beats(jinglebells.harmonic, gpio.SWITCHES[2])[:30])
]
