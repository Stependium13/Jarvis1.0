from speech_recognition import Recognizer, Microphone
from pyttsx3 import init
from pyjokes import get_joke
from pywhatkit import playonyt
from datetime import datetime

global command

listener = Recognizer()
engine = init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
def take_command():
    try:
        with Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            print(command)

    except UnboundLocalError:
        pass
    return command

def say(sentence):
    engine.say(sentence)
    engine.runAndWait()

def joke():
    return get_joke()

def play(song):
    say('playing' + song)
    playonyt(song)


def run_Jarvis():
    command = take_command()
    if 'play' in command:
        command = command.replace('play', '')
        play(command)
    elif 'joke' in command:
        say(joke())
    elif 'time' in command:
        say(f' Now is {datetime.now().hour} {datetime.now().minute}')
    else:
        say('I dont understand you. Please try again.')




if __name__ == '__main__':
    while True:
        try:
            run_Jarvis()
        except:
            pass

