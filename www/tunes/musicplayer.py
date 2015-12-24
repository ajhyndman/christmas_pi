import pygame

class MusicPlayer:
    def __init__(self):
        pygame.mixer.init()
        self.load("/home/pi/christmas_pi/songs/Witch Hunt.mp3")

    def load(self, filename):
        self.song = filename
        pygame.mixer.music.load(filename)

    def play(self):
        if self.is_playing():
            self.stop()
        pygame.mixer.music.play()

    def is_playing(self):
        return pygame.mixer.music.get_busy()

    def stop(self):
        pygame.mixer.music.stop()

PLAYER = MusicPlayer()
