# S5T - Super Simple Song Search (and) Sampling Tool
# By OofySimpsonV3 (github)
# Enjoy :)

# MODULES
from ytmusicapi import YTMusic
from yt_dlp import YoutubeDL
import sys
import os
# from pprint import pprint # For debugging :)

# FETCH SONG FUNCTION
def fetchSong(query):
    search_results = ytmusic.search(query, filter="songs")

    url = search_results[0]["videoId"]

    opts = {
        "outtmpl": musicDir + "/%(title)s-%(id)s.%(ext)s",
        "embed-thumbnail": True,
        "format": "bestaudio/best",
        "writethumbnail": True,
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "320",
            },
            {"key": "FFmpegMetadata"},
            {
                "key": "EmbedThumbnail",
                "already_have_thumbnail": False,
            },
        ],
        "addmetadata": True,
        "add-metadata": True,
    }

    with YoutubeDL(opts) as ydl:
        ydl.download(url)

# FETCH ALBUM FUNCTION
def fetchAlbum(query):
    search_results = ytmusic.search(query, filter="albums")

    # pprint(search_results)

    url = "https://music.youtube.com/playlist?list=" + search_results[0]["playlistId"]

    opts = {
        "outtmpl": musicDir + "/%(playlist_title)s/%(playlist_index)s - %(title)s.%(ext)s",
        "embed-thumbnail": True,
        "format": "bestaudio/best",
        "writethumbnail": True,
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "320",
            },
            {"key": "FFmpegMetadata"},
            {
                "key": "EmbedThumbnail",
                "already_have_thumbnail": False,
            },
        ],
        "parse-metadata": 'playlist_index:%(track_number)s',
        "add-metadata": True,
        "embed-metadata": True,
    }

    with YoutubeDL(opts) as ydl:
        ydl.download(url)

# FETCH YOUTUBE URL
def fetchUrl(url):
    opts = {
        "outtmpl": musicDir + "/%(title)s.%(ext)s",
        "embed-thumbnail": True,
        "format": "bestaudio/best",
        "writethumbnail": True,
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "320",
            },
            {"key": "FFmpegMetadata"},
            {
                "key": "EmbedThumbnail",
                "already_have_thumbnail": False,
            },
        ],
        "addmetadata": True,
        "add-metadata": True,
    }

    with YoutubeDL(opts) as ydl:
        ydl.download(url) 

# STARTUP
if __name__ == "__main__":
    # Find Music Folder and assign VARIABLE accordingly (ensuring Music folder exists)
    global musicDir
    musicDir = os.path.expanduser('~') + '/Music'
    if not os.path.exists(musicDir):
        try:
            os.mkdir(musicDir)
            print("[ WARNING ] S5T was unable to find a Music folder within your home-directory, so we have created one for you. Here are the details: \n" + str(musicDir))
        except Exception as e:
            print("[ ERROR ] S5T unfortunately cannot detect a Music folder within your home-directory, and is unable to create one. More details: " + str(e))
    
    # Declare Command Usage Instructions VARIABLE
    usage = """
Arguments:

--url <URL>
Downloads Youtube media via a URL

--song <QUERY>
Searches and downloads the first song result in Youtube Music.

--album <QUERY>
Searches and downloads the first album result in Youtube Music.

--help
Shows a list of commands.
"""
    
    try:
        arg1 = str(sys.argv[1])
    except:
        print(usage) 
        sys.exit()

    try:
        arg2 = str(sys.argv[2])
    except:
        pass

    try:
        ytmusic = YTMusic()
        
        if arg1 == "--album":
            fetchAlbum(arg2)
        elif arg1 == "--song":
            fetchSong(arg2)
        elif arg1 == "--url":
            fetchUrl(arg2)
        elif arg1 == "--help":
            print(usage)
        else:
            print("invalid command! Append '--help' for a list of commands.") 
            
    except Exception as e:
        print(e)
