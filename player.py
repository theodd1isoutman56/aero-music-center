import pygame

class MusicPlayer:
    def __init__(self):
        pygame.mixer.init()
        self.playlist = []
        self.current_index = -1
        self.is_paused = False
        self.volume = 0.5
        pygame.mixer.music.set_volume(self.volume)
    @property
    def current_song(self):
        if 0 <= self.current_index < len(self.playlist):
            return self.playlist[self.current_index]
        return None

    def theplaylist(self, songs):
        self.playlist = songs
        self.current_index = -1

    def addsong(self, song_path):
        if song_path not in self.playlist:
            self.playlist.append(song_path)
            print(f"added: {song_path}")
            return True
        else:
            print(f"already in playlist: {song_path}")
            return False

    def play(self, song_path=None):

        if song_path is not None:
            if song_path not in self.playlist:
                self.playlist.append(song_path)
            self.current_index = self.playlist.index(song_path)
        if not self.current_song:
            return False

        
        try:
            pygame.mixer.music.load(self.current_song)
            pygame.mixer.music.play()
            self.is_paused = False
            print(f"playng: {self.current_song}")
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
        self.is_paused = False

    def set_volume(self, volume):
        self.volume = max(0.0, min(1.0, volume))
        pygame.mixer.music.set_volume(self.volume)
    def get_position(self):
        return pygame.mixer.music.get_pos() / 1000


    def next(self):
        if not self.playlist:
            return False
        self.current_index = (self.current_index + 1) % len(self.playlist)
        return self.play()
                                                        #^^ and vv the percentage make it so the playlist loops
    def previous(self):
        if not self.playlist:
            return False
        self.current_index = (self.current_index - 1) % len(self.playlist) 
        return self.play()
