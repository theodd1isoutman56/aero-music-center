from mutagen import File

class library:
    def get_metadata(self, song_path):
        audio = File(song_path)
        print(audio)
        print(audio.tags)
        if audio is None:
            return None

        return {"title": str(audio.get("title", ["Unknown Title"])[0]), "artist": str(audio.get("artist", ["Unknown Artist"])[0]), "album": str(audio.get("album", ["Unknown Album"])[0]), "duration": audio.info.length}


