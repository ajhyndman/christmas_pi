import gpio
import score
import tracks.jinglebells as jinglebells




A = One = score.Note(0.25, [gpio.SWITCHES[0], gpio.SWITCHES[1], gpio.SWITCHES[2]])
B = Two = score.Note(0.25, [gpio.SWITCHES[1], gpio.SWITCHES[2]])
D = Three = score.Note(0.25, [gpio.SWITCHES[0], gpio.SWITCHES[1]])
C = Four = score.Note(0.25, [gpio.SWITCHES[0], gpio.SWITCHES[2]])
E = Five = score.Note(0.25, [gpio.SWITCHES[2]])
F = Six = score.Note(0.25, [gpio.SWITCHES[1]])
G = Seven = score.Note(0.25, [gpio.SWITCHES[0]])
REST = score.Rest(0.25)





class Tune:
    name = 'default'
    beat = 1 #length of a bar in seconds
    score = []
    
    def __init__(self, name, beat, score):
        self.name = name
        self.beat = beat
        self.score = score
        
    def set_score(self, score):
        self.score = score
    
    def play(self):
        for note in self.score:
            note.play(self.beat)
            
        for switch in gpio.SWITCHES:
            switch.on()





TUNES = [
    Tune('Mary Had a Little Lamb',
        1,
        [
            score.Note(0.25, [gpio.SWITCHES[0]]),
            score.Note(0.25, [gpio.SWITCHES[1]]),
            score.Note(0.25, [gpio.SWITCHES[2]]),
            score.Note(0.25, [gpio.SWITCHES[1]]),
            score.Note(0.25, [gpio.SWITCHES[0]]),
            score.Note(0.25, [gpio.SWITCHES[0]]),
            score.Note(0.5, [gpio.SWITCHES[0]]),
            score.Note(0.25, [gpio.SWITCHES[1]]),
            score.Note(0.25, [gpio.SWITCHES[1]]),
            score.Note(0.5, [gpio.SWITCHES[1]]),
            score.Note(0.25, [gpio.SWITCHES[0]]),
            score.Note(0.25, [gpio.SWITCHES[0]]),
            score.Note(0.5, [gpio.SWITCHES[0]]),
            score.Note(0.25, [gpio.SWITCHES[0]]),
            score.Note(0.25, [gpio.SWITCHES[1]]),
            score.Note(0.25, [gpio.SWITCHES[2]]),
            score.Note(0.25, [gpio.SWITCHES[1]]),
            score.Note(0.25, [gpio.SWITCHES[0]]),
            score.Note(0.25, [gpio.SWITCHES[0]]),
            score.Note(0.25, [gpio.SWITCHES[0]]),
            score.Note(0.25, [gpio.SWITCHES[0]]),
            score.Note(0.25, [gpio.SWITCHES[1]]),
            score.Note(0.25, [gpio.SWITCHES[1]]),
            score.Note(0.25, [gpio.SWITCHES[0]]),
            score.Note(0.25, [gpio.SWITCHES[1]]),
            score.Note(1, [gpio.SWITCHES[2]]),
        ]),

    # truncates to the first 20 beats (~10s)
    Tune('Jingle Bells',
        1,
        score.build_score_from_beats(jinglebells.harmonic, gpio.SWITCHES[2])[:30]),
        
    Tune('Pachelbel\'s Canon',
        1.75*4,
        [
            D, A, B, F, G, D, G, A,
            D, A, B, F, G, D, G, A,
            D, A, B, F, G, D, G, A,
            D, A, B, F, G, D, G, A,
            
            D, A, B, F, G, D, G, A,
            D, A, B, F, G, D, G, A,
            D, A, B, F, G, D, G, A,
            D, A, B, F, G, D, G, A,
            
            D, A, B, F, G, D, G, A,
            D, A, B, F, G, D, G, A,
            D, A, B, F, G, D, G, A,
            D, A, B, F, G, D, G, A,
            
            D, A, B, F, G, D, G, A,
            D, A, B, F, G, D, G, A,
            D, A, B, F, G, D, G, A,
            D, A, B, F, G, D, G, A
        ])
]
