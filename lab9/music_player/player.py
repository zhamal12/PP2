import pygame
import os

class Player:
    def __init__(self, music_folder):
        self.music_folder = music_folder
        self.playlist = os.listdir(music_folder)
        self.current = 0
        self.playing = False

    def play(self):
        path = os.path.join(self.music_folder, self.playlist[self.current])
        pygame.mixer.music.load(path)
        pygame.mixer.music.play()
        self.playing = True

    def pause(self):
        pygame.mixer.music.pause()
        self.playing = False

    def stop(self):
        pygame.mixer.music.stop()
        self.playing = False

    def next(self):
        self.current = (self.current + 1) % len(self.playlist)
        self.play()

    def prev(self):
        self.current = (self.current - 1) % len(self.playlist)
        self.play()

    def get_track_name(self):
        return self.playlist[self.current]