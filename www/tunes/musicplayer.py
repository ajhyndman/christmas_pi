import pygame

class MusicPlayer:
    selected = 0

    def __init__(self):
        self.songs = [
            "/home/pi/Music/ChristmasCanon.mp3",
            "/home/pi/Music/JingleBells.mp3",
            "/home/pi/Music/Witch Hunt.mp3",
        ]
        pygame.mixer.init()
        self.load(self.songs[0])

    def load(self, filename):
        self.song = filename
        pygame.mixer.music.load(filename)

    def play(self, index):
        if self.is_playing():
            self.stop()
        if index != self.selected:
            self.selected = index
            self.load(self.songs[index])
        pygame.mixer.music.play()

    def is_playing(self):
        return pygame.mixer.music.get_busy()

    def stop(self):
        pygame.mixer.music.stop()

PLAYER = MusicPlayer()
