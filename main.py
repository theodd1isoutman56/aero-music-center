from player import MusicPlayer
player = MusicPlayer()
print("aero prototype")
print("1. play")
print("2. pause")
print("3. resume")
print("4. stop")
print("5. set volume")
print("6. exit")


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



