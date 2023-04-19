from flask import Flask, render_template, request
import json

app = Flask(__name__)

def fightInfo():
    with open('fight.json') as file:
        fight = json.load(file)
    return fight

@app.route('/fightScreen')
def FightScreen():
    fight = fightInfo()
    return render_template('FightScreen.html', nameOne = fight["fighter1"]["name"], nameTwo = fight["fighter2"]["name"], genderOne = fight["fighter1"]["pronouns"],genderTwo = fight["fighter2"]["pronouns"],powerOne = fight["fighter1"]["power"], powerTwo = fight["fighter2"]["power"], taglineOne = fight["fighter1"]["interests"], taglineTwo = fight["fighter2"]["interests"], ageOne = fight["fighter1"]["age"], ageTwo = fight["fighter2"]["age"],Location = fight["location"], Circumstance = fight["circumstance"])

@app.route("/audio")
def serve_audio():
    
    return render_template('MusicScreen.html')

@app.route("/teleprompter")
def createTeleprompter():
    fight = fightInfo()
    return render_template("teleprompter.html", script1 = fight["script"])

@app.route("/winner:<winner>")
def winnerScreen(winner):
    return render_template("winner.html", winner = winner)


def run():
    if __name__ == '__main__':
        app.run()


run()
