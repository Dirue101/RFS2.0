import vlc
from time import sleep
import json




def playAudio():
    with open('fight.json') as file:
        fight = json.load(file)
    media_player = vlc.MediaPlayer("story1.mp3")
    media_player.play()
    sleep(1.5)
    duration = media_player.get_length() / 1000
    fight["duration"] = duration
    with open("fight.json", "w") as f:
         json.dump(fight, f, ensure_ascii=False, indent=4)
    sleep(duration)
    media_player.stop()

def getDuration():
    with open('fight.json') as file:
        fight = json.load(file)
    media_player = vlc.MediaPlayer("story1.mp3")
    duration = media_player.get_length() / 1000
    print(duration)
    fight["duration"] = duration
    with open("fight.json", "w") as f:
         json.dump(fight, f, ensure_ascii=False, indent=4)
    