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
ES = E = EIGHTH_NOTE = score.Note(0.5)
QS = Q = QUARTER_NOTE = score.Note(1)
H = HALF_NOTE = score.Note(2)
W = WHOLE_NOTE = score.Note(4)

R = QUARTER_REST = score.Rest(1)
ER = EIGHTH_REST = score.Rest(0.5)





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
                    ## PAGE 1 ##
                    # 0:00
                    Q, R, R, Q,   R, R, Q, R,   Q, R, R, Q,   R, R, Q, R,
                    Q, R, R, Q,   R, R, Q, R,   Q, R, R, Q,   R, R, Q, R,
                    
                    QS, QS, QS, QS,   W,   W,   W,
                    QS, QS, QS, QS,   W,   W,   W,
                    
                    Q, R, R, Q,   R, R, Q, R,   Q, R, R, Q,   R, R, Q, R,
                    Q, R, R, Q,   R, R, Q, R,   Q, R, R, Q,   R, R, Q, R,
                ] + [
                    ## PAGE 2 ##
                    # 0:42
                    Q, ER, ES, Q, R,   E, ER, ER, E, ER, ER, E, ER,   Q, ER, ES, Q, R,   E, ER, ER, E, ER, ER, E, ER,
                ] + [
                    # 0:50
                    Q, ES, ER, ER, E, R,   E, ER, ER, E, ER, ER, E, ER,   Q, ES, ER, Q, R,   E, ER, ER, E, R, E, ER,
                ] + ([
                    # 0:57
                    Q, R, R, R,   Q, R, R, R,   Q, R, R, R,   Q, R, R, R,
                ] * 4) + ([
                    # 1:26
                    E, E, R, R, R,   E, E, R, R, R,   E, E, R, R, R,   E, E, R, R, R,
                ] * 4) + ([
                    # 1:55
                    E, E, R, E, E, R,   E, E, ER, E, ER, E, R,   E, E, R, E, E, R,  E, E, ER, E, ER, E, R
                ] * 3) + [
                    ## PAGE 3 ##
                    # 2:16
                    E, E, R, E, E, R,   E, E, ER, E, ER, E, R,   E, E, R, E, E, R,   E, E, ER, E, ER, score.Note(1.5)
                ] + [
                    # ~2:25
                    score.Note(3), QS,   Q, R, R, Q,   R, R, R, R,   R, R, Q, R,
                    W,   R, R, R, R,   Q, R, H,   W,
                    score.Note(3), QS,   Q, R, R, Q,   R, R, R, R,   R, R, Q, R,
                    W,   R, R, R, R,   Q, R, H,   W, 
                ] + [
                    ## PAGE 4 ##
                    # 2:53
                    Q, ER, E, Q, R,   E, ER, ER, E, R, E, ER,   Q, ER, E, Q, R,   E, ER, ER, E, R, E, ER,
                ] + [
                    # 3:00
                    Q, E, ER, Q, R,   E, ER, ER, E, R, E, ER,   Q, E, ER, Q, R,   E, ER, ER, E, R, E, ER,
                ] + [
                    # 3:08
                    Q, ER, E, Q, R,   E, ER, ER, E, R, E, ER,   Q, ER, E, Q, R,  E, ER, ER, E, R, E, ER
                ] + [
                    # 3:14
                    Q, E, ER, Q, R,   E, ER, ER, E, R, E, ER
                ] + [
                    # 3:18
                    Q, E, ER, Q, R,   E, ER, ER, E, R,   score.Note(6)
                ] + ([
                    # Ask Violet: 16th notes?
                    score.Note(1/3), score.Note(1/3), score.Note(1/3),
                ] * 16)
            ),
            
            # Bush
            score.Track(1,
                [
                    # 0:00
                    R, Q, R, Q,   R, Q, R, Q,   R, Q, R, Q,   R, Q, R, Q,
                    R, Q, R, Q,   R, Q, R, Q,   R, Q, R, Q,   R, Q, R, Q,
                    
                    W,   QS, QS, QS, QS,   W,   QS, QS, QS, QS,
                    W,   QS, QS, QS, QS,   W,   QS, QS, QS, QS,
                    
                    R, Q, R, Q,   R, Q, R, Q,   R, Q, R, Q,   R, Q, R, Q,
                    R, Q, R, Q,   R, Q, R, Q,   R, Q, R, Q,   R, Q, R, Q,
                ] + [
                    # 0:42
                    
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
