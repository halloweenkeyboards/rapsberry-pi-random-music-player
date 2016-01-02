import os
import vlc
import random
import pyttsx
import time

songs = os.listdir("/home/pi/Music")
random.shuffle(songs)
currentSong = 0

speechEngine = pyttsx.init()
speechEngine.setProperty('rate', 120)

def setup_player(songNumber):
    vlc_instance = vlc.Instance()
    media = vlc_instance.media_new('/home/pi/Music/' + songs[songNumber])
    player = vlc_instance.media_player_new()
    player.set_media(media)
    player.play()
    time.sleep(4)
    while player.is_playing() == True:
        continue
    speechEngine.say(songs[songNumber][:-3])
    speechEngine.runAndWait()


while currentSong <= len(songs):
    setup_player(currentSong)
    currentSong += 1
    
