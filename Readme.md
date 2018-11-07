# mp3 id3 Lyric Tagger

This script adds lyrics to id3 tag of mp3 files. Lyrics are provided by metrolyrics thanks to https://github.com/brenns10/tswift.

## Prerequisites
To use the script you have to install eyeD3 and tswift. It is written in python3.

```
pip3 install tswift
pip3 install eyed3
```

## Usage

Script recursively iterates through every `.mp3` file in a folder.

```
python3 ./lyrictor.py "D:\Music"
```

It doesn't write lyrics when:
 - there is no lyrics found on metrolyrics
 - there is no tagged artist and song name
 - there are connection problems

## Issues
It might not work on id3v2.2 tags since eyeD3 is not supporting that version, but it tries to convert to id3v2.4 and add the lyrics. Sometimes the lyrics do not show up when this happens. You can fix this by using free program mp3tag (https://www.mp3tag.de/en/). Simply select the mp3 file, open its extended tags, and click OK. This will propably fix the problem.
