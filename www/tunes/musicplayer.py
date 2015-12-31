import pygame

class MusicPlayer:
    selected = 0

    def __init__(self):
        self.songs = [
            ("/home/pi/Music/ChristmasCanon.mp3", "Christmas Canon"),
            ("/home/pi/Music/JingleBells.mp3", "Jingle Bells"),
            ("/home/pi/Music/Witch Hunt.mp3", "Witch HUnt"),
        ]
        try:
            pygame.mixer.init()
        except:
            print('No sound is enabled on this device.  Continuing.')
            return
        self.load(self.songs[self.selected][0])

    def song_list(self):
        return ((index, song[1]) for index, song in enumerate(self.songs))

    def load(self, filename):
        self.song = filename
        pygame.mixer.music.load(filename)

    def play(self, index):
        if self.is_playing():
            self.stop()
        if index != self.selected:
            self.selected = index
            self.load(self.songs[index][0])
        pygame.mixer.music.play()

    def is_playing(self):
        return pygame.mixer.music.get_busy()

    def stop(self):
        pygame.mixer.music.stop()

PLAYER = MusicPlayer()
