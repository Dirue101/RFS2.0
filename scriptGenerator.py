import json
import os, openai
from dotenv import load_dotenv
load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')


    


def fightScript():
    with open('fight.json') as file:
        fight = json.load(file)
    prompt = fight["prompt"]
    
    print("Creating A fight!")
    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": prompt}]
)
    fight["script"] = response.choices[0].message.content
    with open("fight.json", "w") as f:
         json.dump(fight, f, ensure_ascii=False, indent=4)
    print("Done!")
    
