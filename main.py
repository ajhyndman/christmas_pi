import sys
import time
import config
import RPi.GPIO as pi

class Player:
    def __init__(self, console=False):
        self.song = []
        self.console = console
        if not console:
            pi.setup(config.PIN1, pi.OUT)

    def set_output(self, vol):
        if console:
            sys.stdout.write('#' * int(3*vol) + '             ')
        else:
            vol = vol > 0.5 and 1 or 0
            pi.output(config.PIN1, vol)
        self.restart_line()

    def restart_line(self):
        sys.stdout.write('\r')
        sys.stdout.flush()

    def load(self, name):
        self.song = [(1,0.1),(3,0.2),(0,0.3)] * 10

    def play(self):
        for vol, dur in self.song:
            self.set_output(vol)
            time.sleep(dur)

if __name__ == "__main__":
    p = Player(console=True)
    p.load('')
    p.play()
    pi.cleanup()
