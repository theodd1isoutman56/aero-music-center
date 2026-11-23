import pygame
import random
import threading 
import queue
import time


class musicplayer:
    def __init__(self):
        pygame.mixer.init()
        self.playlist = []
        self.current_index = -1
        self.is_paused = False
        self.standalone_song = None
        self.volume = 0.5
        self.shuffle = False
        self.shuffle_order = []
        self.shuffle_position = -1
        self.is_playing = False
        self.autoplay = True
        self.loop1 = False
        self.looplaylist = False
        
        pygame.mixer.music.set_volume(self.volume)
        pygame.mixer.music.set_endevent(pygame.USEREVENT)
        

    
    def current_song(self):
        if self.standalone_song:
            return self.standalone_song
        
        if 0 <= self.current_index < len(self.playlist):
            return self.playlist[self.current_index]
        return None

    def theplaylist(self, songs):
        self.playlist = songs
        self.current_index = -1

    def songend(self):
            if not self.autoplay or not self.is_playing or self.is_paused:
                return
            if pygame.mixer.music.get_busy():
                return
            if self.loop1:
                pygame.mixer.music.play()
                return
            if not self.looplaylist:
                if self.shuffle:
                    if self.shuffle_position == len(self.shuffle_order) -1:
                        self.is_playing = False
                        return
                elif self.current_index == len(self.playlist) -1:
                    self.is_playing=False
                    return
            self.is_playing=False
            self.next()

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
            if song_path in self.playlist:
                self.current_index=self.playlist.index(song_path)
                self.standalone_song=None

                if self.shuffle:
                    if not self.shuffle_order:
                        self.shuffle_order =list(range(len(self.playlist)))
                        random.shuffle(self.shuffle_order)
                    self.shuffle_position=self.shuffle_order.index(self.current_index)

        elif self.current_index==-1 and self.playlist:
            self.standalone_song = None

            if self.shuffle:
                self.shuffle_order=list(range(len(self.playlist)))
                random.shuffle(self.shuffle_order)
                self.shuffle_position=0
                self.current_index=self.shuffle_order[self.shuffle_position]
            else:
                self.current_index=0
           
        song = self.current_song()

        if song is None:
            print("no song selected")
            return False

        try:
            pygame.mixer.music.load(song)
            pygame.mixer.music.play()
            self.is_playing = True
            self.is_paused=False
            print(f"playing: {song}")
            return True
        except (pygame.error, TypeError) as e:
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
        self.current_index = -1
        self.shuffle_position = -1
        self.is_playing = False

    def set_volume(self, volume):
        self.volume = max(0.0, min(1.0, volume))
        pygame.mixer.music.set_volume(self.volume)
    def get_position(self):
        return pygame.mixer.music.get_pos() / 1000


    def next(self):
        if not self.playlist:
            return False

        if self.shuffle:
            if not self.shuffle_order:
                self.shuffle_order = list(range(len(self.playlist)))
                random.shuffle(self.shuffle_order)
                self.shuffle_position = -1
                
            self.shuffle_position = (self.shuffle_position+1) % len(self.shuffle_order)
            self.current_index = self.shuffle_order[self.shuffle_position]
        else:
            self.current_index =(self.current_index+1) % len(self.playlist)
            
        self.standalone_song = None
        return self.play()
        
                                               #^^ and vv the percentage make it so the playlist loops
    def previous(self):
        if not self.playlist:
            return False

        if self.shuffle:
            if not self.shuffle_order:
                self.shuffle_order  = list(range(len(self.playlist)))
                random.shuffle(self.shuffle_order)
                self.shuffle_position=0
                self.current_index = self.shuffle_order[self.shuffle_position]
            else:
                self.shuffle_position= (self.shuffle_position-1)% len(self.shuffle_order)
                self.current_index = self.shuffle_order[self.shuffle_position]


        else:
            self.current_index=(self.current_index-1)% len(self.playlist)

        self.standalone_song =None
        return self.play()

    def removesong(self):

        if not self.playlist:
            print("empty playlist")
            return False

        for number, song in enumerate(self.playlist, start=1):

            print(f"{number}. {song}")
        try:
            choice = int(input('track numebr to remove'))
            if not 1 <= choice <= len(self.playlist):
                print("invalid")
                return False
            removedsong = self.playlist.pop(choice-1)
            if removedsong == self.current_song():
                self.stop()
                self.current_index = -1

            elif choice - 1 < self.current_index:
                self.current_index -= 1
            return True
        except ValueError:
            print("error error error error reeororoeoroe")
            return False


    def clearplaylist(self):
            self.stop()
            self.playlist.clear()
            self.current_index = -1
            self.standalone_song = None
            self.shuffle_order=[]
            self.shuffle_position = -1
            print("playlist cleared")



    def songshuffle(self):
        self.shuffle=not self.shuffle
        if self.shuffle:
            self.shuffle_order = list(range(len(self.playlist)))
            random.shuffle(self.shuffle_order)
            if self.current_index != -1:
                self.shuffle_order.remove(self.current_index)
                self.shuffle_order.insert(0, self.current_index)
                self.shuffle_position =0

            else: 
                self.shuffle_position = -1
            

            print("shuffle on")

        else:
            self.shuffle_order = []
            self.shuffle_position = -1
            print("shuffle off")


    def autoplaytoggle(self):
        self.autoplay = not self.autoplay
        print(f"autoplay{'on' if self.autoplay else 'off'}")


    def looptoggle(self):
        self.loop1 = not self.loop1
        print("loop song on" if self.loop1 else "loop song off")

    def playlistloop(self):
        self.looplaylist = not self.looplaylist
        print("loop playlist on" if self.looplaylist else "loop playlist off")

