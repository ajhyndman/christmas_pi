import sys
import time
import RPi.GPIO as pi

class Player:
    def __init__(self):
        self.song = []

    def set_output(self, vol):
        sys.stdout.write('#' * int(3*vol) + '             ')
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
    p = Player()
    p.load('')
    p.play()
