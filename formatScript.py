import os, json
from pydub import AudioSegment
import vlc
def formatScript():
    with open('fight.json') as file:
        fight = json.load(file)
    uneditedScript = fight["script"]
    PassOne = uneditedScript.replace(":\n",":")
    PassTwo = PassOne.replace(")\n", ")")
    Script_Array = PassTwo.split("\n")
    Script_Array = [i for i in Script_Array if i]
    fight["Formatted_Script"] = Script_Array
    fight["SSML"] = Script_Array
    with open("fight.json", "w") as f:
         json.dump(fight, f, ensure_ascii=False, indent=4)


def SSMLArray():
    with open('fight.json') as file:
        fight = json.load(file)
    FormattedScript = fight["SSML"]
    name1 = fight["fighter1"]["name"] + ":"
    name2 = fight["fighter2"]["name"] + ":"

    for i in range(len(FormattedScript)):
        if(FormattedScript[i].startswith(name1) or FormattedScript[i].startswith(name1.upper())):
                FormattedScript[i] = f'<voice name="{fight["fighter1"]["voice"]}">' + FormattedScript[i].replace(".",'. <break time = ".5s"/>')  + '<break time = "1s"/>'+'</voice>'

        elif(FormattedScript[i].startswith(name2) or FormattedScript[i].startswith(name2.upper())):
            FormattedScript[i] = f'<voice name="{fight["fighter2"]["voice"]}">' + FormattedScript[i].replace(".",'. <break time = ".5s"/>')  + '<break time = "1s"/>'+'</voice>'     
        else:
            FormattedScript[i] = f'<voice name="en-AU-Standard-B">' + FormattedScript[i].replace(".",'. <break time = ".5s"/>') + '<break time = "1s"/>'+ '</voice>'
    
    for i in range(len(FormattedScript)):
        if((i+1) % 25 == 0):
            FormattedScript.insert(i, "</speak>\n^<speak>")
    with open("fight.json", "w") as f:
         json.dump(fight, f, ensure_ascii=False, indent=4)
    
def ToText():
    with open('fight.json') as file:
        fight = json.load(file)
    SSMLArray = fight["SSML"]
    SSML = "<speak> \n"
    for x in SSMLArray:
        SSML += x + "\n"
    SSML += "</speak>"
    splitSSML = SSML.split("^")
    for i in range(len(splitSSML)):
        with open(f"Temp/SSML{i}.txt", 'w') as Script:
            Script.write(splitSSML[i])
    del fight["SSML"]
    fight["SSML"] = SSML
    
    
def synthesize_ssml_file(): 
    from google.cloud import texttospeech
    client = texttospeech.TextToSpeechClient()
    voice = texttospeech.VoiceSelectionParams(
        language_code="en-US", ssml_gender=texttospeech.SsmlVoiceGender.FEMALE
    )

    audio_config = texttospeech.AudioConfig(
         audio_encoding=texttospeech.AudioEncoding.MP3
    )

       
    for filename in os.listdir(r"C:\Users\DigBixby\Desktop\RFS 2.0\Temp"):
        
    
        with open(f"Temp/{filename}", "rb") as f:
            ssml = f.read()
            input_text = texttospeech.SynthesisInput(ssml=ssml)
            
        response = client.synthesize_speech(
            input=input_text, voice=voice, audio_config=audio_config
        )
        mp3filename = filename.replace(".txt","") + ".mp3"
        
        
        with open(f"Temp/{mp3filename}", "wb") as out:
            out.write(response.audio_content)
            print('Audio content written to file "output.mp3"')



def removeTemp(type):
    for file in os.listdir(r"C:\Users\DigBixby\Desktop\RFS 2.0\Temp"):
        if(file.find(type) != -1):
            os.remove(f"Temp/{file}")    
        
        
        
        
        
    
    
def merge_songs():
   if(len(os.listdir(r"C:\Users\DigBixby\Desktop\RFS 2.0\Temp")) > 1):
        story = AudioSegment.empty()
        for filename in os.listdir(r"C:\Users\DigBixby\Desktop\RFS 2.0\Temp"):
            story += AudioSegment.from_file(f"Temp/{filename}")

        story.export("story1.mp3",format="mp3")
   else:
       os.rename(r"C:\Users\DigBixby\Desktop\RFS 2.0\Temp\SSML0.mp3",r"C:\Users\DigBixby\Desktop\RFS 2.0\story1.mp3")
        

    



def produceVoiceActing():
    removeTemp(".txt")
    removeTemp(".mp3")
    SSMLArray()
    ToText()
    synthesize_ssml_file()
    removeTemp(".txt")
    merge_songs()
    removeTemp(".mp3")
    


