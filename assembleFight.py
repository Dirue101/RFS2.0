from fightClass import *
from scriptGenerator import fightScript
from formatScript import *
import os
from backupcleanup import * 
import webbrowser
from playAudio import *
firefox_path = r"C:/Program Files/Mozilla Firefox/firefox.exe %s"
audioSite = "127.0.0.1:5000/audio"

def generateFight():

    
    initializeFight()
    webbrowser.get(firefox_path).open("127.0.0.1:5000/fightScreen")
    fightScript()
    formatScript()
    produceVoiceActing()
    backup()
    sleep(5)
    webbrowser.get(firefox_path).open("127.0.0.1:5000/teleprompter")

    playAudio()
    cleanup()
    generateFight()
   
    




webbrowser.get(firefox_path).open(audioSite)
while True:
    try: 
        generateFight()

    except Exception as e:
        print(e)
        print("restarting")