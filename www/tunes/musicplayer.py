from subprocess import Popen


class MusicPlayer:
    playing = False
    process = None
    song = None

    def __init__(self):
        self.load("/home/pi/christmas_pi/songs/Witch Hunt.mp3")

    def load(self, filename):
        self.song = filename

    def play(self):
        if self.is_playing():
            self.stop()
        self.playing = True
        command = ["omxplayer", self.song]
        self.process = Popen(command)

    def is_playing(self):
        self.playing = self.playing and self.process.poll()
        return self.playing

    def stop(self):
        if self.is_playing():
            self.process.terminate()

PLAYER = MusicPlayer()
