import tswift as ly
import eyed3
from eyed3.id3 import Tag
from eyed3.id3 import ID3_V1_0, ID3_V1_1, ID3_V2_3, ID3_V2_4
import sys
import glob


for filename in glob.glob(sys.argv[1]+'\**\*.mp3', recursive=True):
    try:
        aud = eyed3.load(filename)
        print(aud.tag.title, aud.tag.artist)
        song = ly.Song(title=aud.tag.title, artist=aud.tag.artist)
        aud.tag.lyrics.set(str(song.lyrics))
        aud.tag.save(version=ID3_V2_4)
        print("Successfully lyricted", filename)
    except Exception as e:
        print("Couldn't load or fetch lyrics.", e)
    print("--")
