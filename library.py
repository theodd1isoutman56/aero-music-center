from mutagen.mp3 import MP3
from mutagen.flac import FLAC
from mutagen.oggvorbis import OggVorbis
from mutagen import File
from mutagen.easyid3 import EasyID3


class library:
    def get_metadata(self, song_path):
        audio = MP3(song_path, ID3=EasyID3)
        return {"title": audio.get("title", ['Unknown Title'])[0], "artist": audio.get("artist", ['Unknown Artist'])[0], "album": audio.get("album", ["Unknown Album"])[0], "duration": audio.info.length}




