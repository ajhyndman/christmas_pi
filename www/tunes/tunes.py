import gpio
import time
import score
# import tracks.jinglebells as jinglebells





# Some light combinations in OLD_Note style.
A = One =   score.OLD_Note(0.5, [gpio.SWITCHES[0], gpio.SWITCHES[1], gpio.SWITCHES[2]])
B = Two =   score.OLD_Note(0.5, [gpio.SWITCHES[1], gpio.SWITCHES[2]])
D = Three = score.OLD_Note(0.5, [gpio.SWITCHES[0], gpio.SWITCHES[1]])
C = Four =  score.OLD_Note(0.5, [gpio.SWITCHES[0], gpio.SWITCHES[2]])
E = Five =  score.OLD_Note(0.5, [gpio.SWITCHES[2]])
F = Six =   score.OLD_Note(0.5, [gpio.SWITCHES[1]])
G = Seven = score.OLD_Note(0.5, [gpio.SWITCHES[0]])
OLD_REST =      score.OLD_Rest(0.5)




# Shorthands for Track Compilation style Notes and Rests
QS = Q = QUARTER_NOTE = score.Note(1)
H = HALF_NOTE = score.Note(2)
W = WHOLE_NOTE = score.Note(4)

R = QUARTER_REST = score.Rest(1)





TUNES = [
    score.Tune('Mary Had a Little Lamb',
        60,
        [
            score.OLD_Note(0.25, [gpio.SWITCHES[0]]),
            score.OLD_Note(0.25, [gpio.SWITCHES[1]]),
            score.OLD_Note(0.25, [gpio.SWITCHES[2]]),
            score.OLD_Note(0.25, [gpio.SWITCHES[1]]),
            score.OLD_Note(0.25, [gpio.SWITCHES[0]]),
            score.OLD_Note(0.25, [gpio.SWITCHES[0]]),
            score.OLD_Note(0.5, [gpio.SWITCHES[0]]),
            score.OLD_Note(0.25, [gpio.SWITCHES[1]]),
            score.OLD_Note(0.25, [gpio.SWITCHES[1]]),
            score.OLD_Note(0.5, [gpio.SWITCHES[1]]),
            score.OLD_Note(0.25, [gpio.SWITCHES[0]]),
            score.OLD_Note(0.25, [gpio.SWITCHES[0]]),
            score.OLD_Note(0.5, [gpio.SWITCHES[0]]),
            score.OLD_Note(0.25, [gpio.SWITCHES[0]]),
            score.OLD_Note(0.25, [gpio.SWITCHES[1]]),
            score.OLD_Note(0.25, [gpio.SWITCHES[2]]),
            score.OLD_Note(0.25, [gpio.SWITCHES[1]]),
            score.OLD_Note(0.25, [gpio.SWITCHES[0]]),
            score.OLD_Note(0.25, [gpio.SWITCHES[0]]),
            score.OLD_Note(0.25, [gpio.SWITCHES[0]]),
            score.OLD_Note(0.25, [gpio.SWITCHES[0]]),
            score.OLD_Note(0.25, [gpio.SWITCHES[1]]),
            score.OLD_Note(0.25, [gpio.SWITCHES[1]]),
            score.OLD_Note(0.25, [gpio.SWITCHES[0]]),
            score.OLD_Note(0.25, [gpio.SWITCHES[1]]),
            score.OLD_Note(1, [gpio.SWITCHES[2]]),
        ]),

    # truncates to the first 20 beats (~10s)
    # Tune('Jingle Bells',
    #     1,
    #     score.build_score_from_beats(jinglebells.harmonic, gpio.SWITCHES[2])[:30]),
        
    score.Tune('Pachelbel\'s Canon (Bass Voice)',
        80,
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
        ]),

    score.Track_Compilation(
        'Pachelbel\'s Canon (Melody)',
        137,
        [
            # score.Track(0, [score.Note(1), score.Note(1), score.Rest(2), score.Note(0.5), score.Note(0.5)]),
            
            # Posts
            score.Track(0,
                [
                    # score.Note(1), score.Rest(1), score.Rest(1), score.Note(1),
                    Q, R, R, Q,   R, R, Q, R,   Q, R, R, Q,   R, R, Q, R,
                    Q, R, R, Q,   R, R, Q, R,   Q, R, R, Q,   R, R, Q, R,
                    
                    QS, QS, QS, QS,   W,   W,   W,
                    QS, QS, QS, QS,   W,   W,   W,
                    
                    Q, R, R, Q,   R, R, Q, R,   Q, R, R, Q,   R, R, Q, R,
                    Q, R, R, Q,   R, R, Q, R,   Q, R, R, Q,   R, R, Q, R,
                ]
            ),
            
            # Bush
            score.Track(1,
                [
                    R, Q, R, Q,   R, Q, R, Q,   R, Q, R, Q,   R, Q, R, Q,
                    R, Q, R, Q,   R, Q, R, Q,   R, Q, R, Q,   R, Q, R, Q,
                    
                    W,   QS, QS, QS, QS,   W,   QS, QS, QS, QS,
                    W,   QS, QS, QS, QS,   W,   QS, QS, QS, QS,
                    
                    R, Q, R, Q,   R, Q, R, Q,   R, Q, R, Q,   R, Q, R, Q,
                    R, Q, R, Q,   R, Q, R, Q,   R, Q, R, Q,   R, Q, R, Q,
                ]
            ),
            
            # Tree
            score.Track(2,
                [
                    R, R, Q, R,   Q, R, R, Q,   R, R, Q, R,   Q, R, R, Q,
                    R, R, Q, R,   Q, R, R, Q,   R, R, Q, R,   Q, R, R, Q,
                    
                    W,   W,   QS, QS, QS, QS,   W,
                    W,   W,   QS, QS, QS, QS,   W,
                    
                    R, R, Q, R,   Q, R, R, Q,   R, R, Q, R,   Q, R, R, Q,
                    R, R, Q, R,   Q, R, R, Q,   R, R, Q, R,   Q, R, R, Q,
                ]
            )
        ]
    )
]
