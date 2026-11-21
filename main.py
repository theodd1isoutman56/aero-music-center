from player import MusicPlayer
player = MusicPlayer()
print("prototype")


while True:
    choice = int(input("choose: "))
    if choice == 1:
        path = input("path: ")
        player.play(path)
    elif choice == 2:
        player.pause()
    elif choice == 3:
        player.resume()
    elif choice == 4:
        player.stop()
    elif choice == 5:
        volume = float(input("volume: "))
        player.set_volume(volume)
    elif choice == 6:
        player.stop()
        break

    else:
        print("invalid")



