import shutil
import json
import os
def backup():
    with open('fight.json') as file:
        fight = json.load(file)
    title = fight["fighter1"]["power"] + "Vs." + fight["fighter2"]["power"]
    shutil.copy("fight.json", f"D:\RFS SCRIPTS\{title}.json")
    shutil.copy("story1.mp3", f"D:\RFS SCRIPTS\{title}.mp3")

def cleanup():
    os.remove("story1.mp3")