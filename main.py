import sys
import time
import config
#import RPi.GPIO as pi
# I can't import/install gpio on windows
pi = None

import pygame
#import librosa

class Player:
    def __init__(self, console=False):
        self.song = []
        self.console = console
        if not self.console:
            pi.setup(config.PIN1, pi.OUT)

    def set_output(self, vol):
        if self.console:
            sys.stdout.write('#' * int(3*vol) + '             ')
            sys.stdout.flush()
        else:
            vol = vol > 0.5 and 1 or 0
            pi.output(config.PIN1, vol)
        self.restart_line()

    def restart_line(self):
        sys.stdout.write('\r')
        sys.stdout.flush()

    def load(self, file):
        sys.stdout.write('Loading\n')
        sys.stdout.flush()
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load(file)
        #self.song = [(1,0.1),(3,0.2),(0,0.3)] * 10
        '''
        y, sr = librosa.load(file)
        tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)
        beat_times = librosa.frames_to_time(best_frames, sr=sr)
        sys.stdout.write('Beat times: \n %s \n' % beat_times)
        '''
        sys.stdout.write('Loaded\n')
        sys.stdout.flush()

    def play(self):
        pygame.display.set_mode((100, 100))
        pygame.mixer.music.play()
        count = 0
        while pygame.mixer.music.get_busy() and count <= 40:
            count += 1
            sys.stdout.write('Count is: %s, volume is %s' % (count, pygame.mixer.music.get_volume()))
            sys.stdout.flush()
            self.restart_line()
            pygame.time.Clock().tick(10)
        #for vol, dur in self.song:
        #    self.set_output(vol)
        #    time.sleep(dur)
        if not self.console:
            pi.cleanup()

if __name__ == "__main__":
    p = Player(console=True)
    p.load('songs/Witch Hunt.ogg')
    p.play()
