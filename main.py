from player import musicplayer
from pathlib import Path
from playlist import playlist1
from library import library

import threading 
import queue
import time

music_library = library()

player = musicplayer()

commands = queue.Queue()
def input1():
    while True:
        commands.put(input("choose: "))

threading.Thread(target=input1, daemon=True).start()

playlist = playlist1()
player.theplaylist(playlist.load())
print("aero prototype")
print("1. play")
print("2. pause")
print("3. resume")
print("4. stop")
print("5. set volume")
print("6. exit")
print("7. add song to playlist")
print("8. show playlist")
print("9. next")
print("10. previous")      
print("11. play playlist")
print("12. remove specific tracks from playlist")
print("13. clear playlist")
print("14. shuffle")



while True:
    player.songend()

    try:

        choice = commands.get_nowait()
    except queue.Empty:
        time.sleep(0.1)
        continue


    if choice == "1":
        path = input("path: ").strip('\'"')
        player.play(path)
    elif choice == "2":
        player.pause()
    elif choice == "3":
        player.resume()
    elif choice == "4":
        player.stop()
    elif choice == "5":
        volume = float(input("volume: "))
        player.set_volume(volume)
    elif choice == "6":
        player.stop()
        break
    elif choice == "7":
        path = input("path: ").strip('\'"')
        player.addsong(path)
        playlist.save(player.playlist)
    elif choice == "8":
        for index, song in enumerate(player.playlist):
            print(f"{index + 1}. {song}")
    elif choice == "9":
        player.next()
    elif choice == "10":
        player.previous()
    elif choice == "11":
        player.play()
    elif choice == "12":
        if player.removesong():
            playlist.save(player.playlist)
            print("song removed")

    elif choice == '13':
        player.clearplaylist()
        playlist.save(player.playlist)

    elif choice == '14':
        player.songshuffle()

    else:
        print("invalid")


