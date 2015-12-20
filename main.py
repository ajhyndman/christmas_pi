import sys
import time
import config
#import RPi.GPIO as pi
# I can't import/install gpio on windows
pi = None

import pygame

class Player:
    def __init__(self, console=False):
        self.song = []
        self.console = console
        if not self.console:
            pi.setup(config.PIN1, pi.OUT)

    def set_output(self, vol):
        if self.console:
            sys.stdout.write('#' * int(3*vol) + '             ')
        else:
            vol = vol > 0.5 and 1 or 0
            pi.output(config.PIN1, vol)
        self.restart_line()

    def restart_line(self):
        sys.stdout.write('\r')
        sys.stdout.flush()

    def load(self, file):
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load(file)
        #self.song = [(1,0.1),(3,0.2),(0,0.3)] * 10

    def play(self):
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
        #for vol, dur in self.song:
        #    self.set_output(vol)
        #    time.sleep(dur)
        if not self.console:
            pi.cleanup()

if __name__ == "__main__":
    p = Player(console=True)
    p.load('songs/Witch Hunt.mp3')
    p.play()
