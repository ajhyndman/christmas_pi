import gpio
import time
import score
# import tracks.jinglebells as jinglebells





TSO_CANON_BPM = 136





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
    score.Tune(
        'Mary Had a Little Lamb',
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
        
    score.Tune(
        'Pachelbel\'s Canon (Bass Voice)',
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
        TSO_CANON_BPM,
        'audio/christmas_canon_3.5.mp3',
        [
            # Posts Track
            score.Track(0,
                [ R, R, ] +
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
                    R, Q, R, R,   R, Q, R, R,   R, Q, R, R,   R, Q, R, R,
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
                    # ~3:24
                    # Ask Violet: 16th notes?
                    score.Note(1/3), score.Note(1/3), score.Note(1/3),
                ] * 16)
            ),
            
            # Bush Track
            score.Track(1,
                [ R, R ] +
                [
                    ## PAGE 1 ##
                    # 0:00
                    R, Q, R, Q,   R, Q, R, Q,   R, Q, R, Q,   R, Q, R, Q,
                    R, Q, R, Q,   R, Q, R, Q,   R, Q, R, Q,   R, Q, R, Q,
                    
                    W,   QS, QS, QS, QS,   W,   QS, QS, QS, QS,
                    W,   QS, QS, QS, QS,   W,   QS, QS, QS, QS,
                    
                    R, Q, R, Q,   R, Q, R, Q,   R, Q, R, Q,   R, Q, R, Q,
                    R, Q, R, Q,   R, Q, R, Q,   R, Q, R, Q,   R, Q, R, Q,
                ] + [
                    ## PAGE 2 ##
                    # 0:42
                    QS, ES, ER, QS, E, ER,   ER, E, R, ER, E, R,   QS, ES, ER, QS, ES, ER,   ER, E, R, ER, E, R,
                    Q, ER, E, E, E, ER, E,   ER, E, R, ER, E, R,   Q, ER, E, Q, ER, E,   ER, E, R, ER, E, R
                ] + ([
                    # 0:57
                    Q, Q, Q, Q,   Q, Q, Q, Q,   Q, Q, Q, Q,   Q, Q, Q, Q
                ] * 8) + ([
                    # 1:55
                    Q, Q, Q, Q,   Q, Q, Q, Q,   Q, Q, Q, Q,   Q, Q, Q, Q
                ] * 3) + [
                    ## PAGE 3 ##
                    # 2:16
                    Q, Q, Q, Q,   Q, Q, Q, Q,   Q, Q, Q, Q,   Q, Q, Q, Q
                ] + [
                    # ~2:25
                    Q, Q, Q, R,   R, Q, R, R,   score.Note(3), R,   R, Q, R, R,
                    W,   W,   R, R, R, R,   QS, QS, QS, QS
                ] + [
                    # 2:38
                    score.Note(3), R,   R, Q, R, R,   score.Note(3), R,   R, Q, R, R,
                    W,   W,   R, R, R, R,   QS, QS, QS, QS
                ] + [
                    ## PAGE 4 ##
                    # 2:53
                    Q, E, ER, Q, E, ER,   ER, E, R, ER, E, R,   Q, E, ER, Q, E, ER,   ER, E, R, ER, E, R,
                    Q, ER, E, Q, ER, E,   ER, E, R, ER, E, R,   Q, ER, E, Q, ER, E,   ER, E, R, ER, E, R,
                    Q, E, ER, Q, E, ER,   ER, E, R, ER, E, R,   Q, E, ER, Q, E, ER,   ER, E, R, ER, E, R,
                ] + [
                    # 3:14
                    Q, ER, E, Q, ER, E,   ER, E, R, ER, E, R,   Q, ER, E, Q, ER, E,
                    ER, E, R, ER, score.Note(5.5)
                ] + ([
                    # ~3:24
                    # Ask Violet: 16th notes?
                    score.Note(1/4), score.Note(1/4), score.Note(1/4), score.Note(1/4),
                ] * 16)
            ),
            
            # Tree Track
            score.Track(2,
                [ R, R ] +
                [
                    ## PAGE 1 ##
                    # 0:00
                    R, R, Q, R,   Q, R, R, Q,   R, R, Q, R,   Q, R, R, Q,
                    R, R, Q, R,   Q, R, R, Q,   R, R, Q, R,   Q, R, R, Q,
                    
                    W,   W,   QS, QS, QS, QS,   W,
                    W,   W,   QS, QS, QS, QS,   W,
                    
                    R, R, Q, R,   Q, R, R, Q,   R, R, Q, R,   Q, R, R, Q,
                    R, R, Q, R,   Q, R, R, Q,   R, R, Q, R,   Q, R, R, Q,
                ] + [
                    ## PAGE 2 ##
                    # 0:42
                    Q, R, Q, ER, E,   R, E, ER, E, ER, ER, E,   Q, R, Q, ER, E,   R, E, ER, E, ER, ER, E,
                    Q, R, Q, E, ER,   R, E, ER, E, ER, ER, E,   Q, R, Q, ES, ER,   R, E, ER, E, ER, ER, E,
                ] + ([
                    # 0:57
                    R, R, H,   R, R, H,   R, R, H,   R, R, H, 
                ] * 8) + ([
                    # 1:55
                    R, Q, R, Q,  R, E, ER, E, ER, E, ER,   R, Q, R, Q,   R, E, ER, E, ER, E, ER,
                ] * 3) + [
                    ## PAGE 3 ##
                    # 2:16
                    R, Q, R, Q,   R, E, ER, E, ER, E, ER,   R, Q, R, Q,   R, E, ER, E, ER, Q
                ] + [
                    # ~2:25
                    score.Note(3), R,   R, R, Q, R,   score.Note(3), QS,   Q, R, R, Q,
                    R, R, R, R,   W,   R, Q, R, Q,   W,
                ] + [
                    # 2:38
                    score.Note(3), R,   R, R, Q, R,   score.Note(3), QS,   Q, R, R, Q,
                    R, R, R, R,   W,   R, Q, R, Q,   W,
                ] + [
                    ## PAGE 4 ##
                    # 2:53
                    Q, R, Q, ER, E,   R, E, ER, E, ER, ER, E,   Q, R, Q, ER, E,   R, E, ER, E, ER, ER, E,
                    Q, R, Q, E, ER,   R, E, ER, E, ER, ER, E,   Q, R, Q, E, ER,   R, E, ER, E, ER, ER, E,
                    Q, R, Q, ER, E,   R, E, ER, E, ER, ER, E,   Q, R, Q, ER, E,   R, E, ER, E, ER, ER, E,
                ] + [
                    # 3:14
                    Q, R, Q, E, ER,   R, E, ER, E, ER, ER, E,   Q, R, Q, E, ER,  R, E, ER, E, ER, ER, score.Note(4.5),
                ] + ([
                    # ~3:24
                    # Ask Violet: 16th notes?
                    score.Note(1/3), score.Note(1/3), score.Note(1/3),
                ] * 16)
            ),
            
            # Wall Track
            score.Track(3,
                [
                    # 0:00-3:30
                    score.Note(TSO_CANON_BPM*3.5)
                ]
            )
        ],
    ),
    

    score.Track_Compilation(
        '(01.01.16) Pachelbel\'s Canon',
        TSO_CANON_BPM,
        'audio/christmas_canon_3.5.mp3',
        [
            # Posts Track
            score.Track(0,
                [ R, ] +
                [
                    ## PAGE 1 ##
                    # 0:00
                    R, Q, R, R,   Q, R, R, Q,   R, Q, R, R,   Q, R, R, Q,
                    R, Q, R, R,   Q, R, R, Q,   R, Q, R, R,   Q, R, R, Q,
                    
                    QS, QS, QS, score.Note(13),
                    QS, QS, QS, score.Note(13),
                    
                    R, Q, R, R,   Q, R, R, Q,   R, Q, R, R,   Q, R, R, Q,
                    R, Q, R, R,   Q, R, R, Q,   R, Q, R, R,   Q, R, R, Q,
                ] + [
                    ## PAGE 2 ##
                    # 0:42
                    Q, ER, ES, Q, R,   E, ER, ER, E, ER, ER, E, ER,   Q, ER, ES, Q, R,   E, ER, ER, E, ER, ER, E, ER,
                ] + [
                    # 0:50
                    Q, ES, ER, ER, E, R,   E, ER, ER, E, ER, ER, E, ER,   Q, ES, ER, Q, R,   E, ER, ER, E, R, E, ER,
                ] + ([
                    # 0:57
                    R, Q, R, R,   R, Q, R, R,   R, Q, R, R,   R, Q, R, R,
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
                    Q, E, ER, Q, R,   E, ER, ER, E, R,   score.Note(5)
                ] + ([
                    # ~3:24
                    # Ask Violet: 16th notes?
                    score.Note(1.0/3.0), score.Note(1.0/3.0), score.Note(1.0/3.0),
                ] * 12)
            ),
            
            # Bush Track
            score.Track(1,
                [ R, ] +
                [
                    ## PAGE 1 ##
                    # 0:00
                    Q, R, Q, R,   Q, R, Q, R,   Q, R, Q, R,   Q, R, Q, R,
                    Q, R, Q, R,   Q, R, Q, R,   Q, R, Q, R,   Q, R, Q, R,
                    
                    W,   QS, QS, QS, score.Note(5),   QS, QS, QS, QS,
                    W,   QS, QS, QS, score.Note(5),   QS, QS, QS, QS,
                    
                    Q, R, Q, R,   Q, R, Q, R,   Q, R, Q, R,   Q, R, Q, R,
                    Q, R, Q, R,   Q, R, Q, R,   Q, R, Q, R,   Q, R, Q, R,
                ] + [
                    ## PAGE 2 ##
                    # 0:42
                    QS, ES, ER, QS, E, ER,   ER, E, R, ER, E, R,   QS, ES, ER, QS, ES, ER,   ER, E, R, ER, E, R,
                    Q, ER, E, E, E, ER, E,   ER, E, R, ER, E, R,   Q, ER, E, Q, ER, E,   ER, E, R, ER, E, R
                ] + ([
                    # 0:57
                    Q, Q, Q, Q,   Q, Q, Q, Q,   Q, Q, Q, Q,   Q, Q, Q, Q
                ] * 8) + ([
                    # 1:55
                    Q, Q, Q, Q,   Q, Q, Q, Q,   Q, Q, Q, Q,   Q, Q, Q, Q
                ] * 3) + [
                    ## PAGE 3 ##
                    # 2:16
                    Q, Q, Q, Q,   Q, Q, Q, Q,   Q, Q, Q, Q,   Q, Q, Q, Q
                ] + [
                    # ~2:25
                    Q, Q, Q, R,   R, Q, R, R,   score.Note(3), R,   R, Q, R, R,
                    W,   W,   R, R, R, R,   QS, QS, QS, QS
                ] + [
                    # 2:38
                    score.Note(3), R,   R, Q, R, R,   score.Note(3), R,   R, Q, R, R,
                    W,   W,   R, R, R, R,   QS, QS, QS, QS
                ] + [
                    ## PAGE 4 ##
                    # 2:53
                    Q, E, ER, Q, E, ER,   ER, E, R, ER, E, R,   Q, E, ER, Q, E, ER,   ER, E, R, ER, E, R,
                    Q, ER, E, Q, ER, E,   ER, E, R, ER, E, R,   Q, ER, E, Q, ER, E,   ER, E, R, ER, E, R,
                    Q, E, ER, Q, E, ER,   ER, E, R, ER, E, R,   Q, E, ER, Q, E, ER,   ER, E, R, ER, E, R,
                ] + [
                    # 3:14
                    Q, ER, E, Q, ER, E,   ER, E, R, ER, E, R,   Q, ER, E, Q, ER, E,
                    ER, E, R, ER, score.Note(5.5)
                ] + ([
                    # ~3:24
                    # Ask Violet: 16th notes?
                    score.Note(1.0/4.0), score.Note(1.0/4.0), score.Note(1.0/4.0), score.Note(1.0/4.0),
                ] * 12)
            ),
            
            # Tree Track
            score.Track(2,
                [ R, ] +
                [
                    ## PAGE 1 ##
                    # 0:00
                    Q, R, R, Q,   R, Q, R, R,   Q, R, R, Q,   R, Q, R, R,
                    Q, R, R, Q,   R, Q, R, R,   Q, R, R, Q,   R, Q, R, R,
                    
                    score.Note(8),   QS, QS, QS, score.Note(5),
                    score.Note(8),   QS, QS, QS, score.Note(5),
                    
                    Q, R, R, Q,   R, Q, R, R,   Q, R, R, Q,   R, Q, R, R,
                    Q, R, R, Q,   R, Q, R, R,   Q, R, R, Q,   R, Q, R, R,
                ] + [
                    ## PAGE 2 ##
                    # 0:42
                    Q, R, Q, ER, E,   R, E, ER, E, ER, ER, E,   Q, R, Q, ER, E,   R, E, ER, E, ER, ER, E,
                    Q, R, Q, E, ER,   R, E, ER, E, ER, ER, E,   Q, R, Q, ES, ER,   R, E, ER, E, ER, ER, E,
                ] + ([
                    # 0:57
                    R, R, H,   R, R, H,   R, R, H,   R, R, H, 
                ] * 8) + ([
                    # 1:55
                    R, Q, R, Q,  R, E, ER, E, ER, E, ER,   R, Q, R, Q,   R, E, ER, E, ER, E, ER,
                ] * 3) + [
                    ## PAGE 3 ##
                    # 2:16
                    R, Q, R, Q,   R, E, ER, E, ER, E, ER,   R, Q, R, Q,   R, E, ER, E, ER, Q
                ] + [
                    # ~2:25
                    score.Note(3), R,   R, R, Q, R,   score.Note(3), QS,   Q, R, R, Q,
                    R, R, R, R,   W,   R, Q, R, Q,   W,
                ] + [
                    # 2:38
                    score.Note(3), R,   R, R, Q, R,   score.Note(3), QS,   Q, R, R, Q,
                    R, R, R, R,   W,   R, Q, R, Q,   W,
                ] + [
                    ## PAGE 4 ##
                    # 2:53
                    Q, R, Q, ER, E,   R, E, ER, E, ER, ER, E,   Q, R, Q, ER, E,   R, E, ER, E, ER, ER, E,
                    Q, R, Q, E, ER,   R, E, ER, E, ER, ER, E,   Q, R, Q, E, ER,   R, E, ER, E, ER, ER, E,
                    Q, R, Q, ER, E,   R, E, ER, E, ER, ER, E,   Q, R, Q, ER, E,   R, E, ER, E, ER, ER, E,
                ] + [
                    # 3:14
                    Q, R, Q, E, ER,   R, E, ER, E, ER, ER, E,   Q, R, Q, E, ER,  R, E, ER, E, ER, ER, score.Note(4.5),
                ] + ([
                    # ~3:24
                    # Ask Violet: 16th notes?
                    score.Note(1.0/3.0), score.Note(1.0/3.0), score.Note(1.0/3.0),
                ] * 12)
            ),
            
            # Wall Track
            score.Track(3,
                [
                    # 0:00-3:30
                    score.Note(TSO_CANON_BPM*3.5)
                ]
            )
        ],
    )
]
