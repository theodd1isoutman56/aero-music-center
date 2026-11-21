import pygame

class MusicPlayer:
    def __init__(self):
        pygame.mixer.init()
        self.current_song = None
        self.is_paused = False
        self.volume = 0.5
        pygame.mixer.music.set_volume(self.volume)

    def play(self, song_path):
        try:
            pygame.mixer.music.load(song_path)
            pygame.mixer.music.play()
            self.current_song = song_path
            self.is_paused = False
            print(f"playng: {song_path}")
            return True
        except pygame.error as e:
            print(f"error: {e}")
            return False
    def pause(self):
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.pause()
            self.is_paused = True

    def resume(self):
        if self.is_paused:
            pygame.mixer.music.unpause()
            self.is_paused = False

    def stop(self):
        pygame.mixer.music.stop()
        self.current_song = None
        self.is_paused = False

    def set_volume(self, volume):
        self.volume = max(0.0, min(1.0, volume))
        pygame.mixer.music.set_volume(self.volume)
    def get_position(self):
        return pygame.mixer.music.get_pos() / 1000
    
