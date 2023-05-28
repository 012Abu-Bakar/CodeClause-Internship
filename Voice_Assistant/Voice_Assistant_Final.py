import speech_recognition as sr  #  recognize speech
import pyttsx3 #text to speech
import time
from time import ctime
import webbrowser
import playsound
import os
import random
from gtts import gTTS #Google Text To Speech

from tkinter import *
from PIL import ImageTk,Image

print('Say something...')
r = sr.Recognizer()
speaker = pyttsx3.init() # inititalize the engine(speaker)

def record_audio(ask=False):
    #Function for Audio Record
    with sr.Microphone() as source:     #use the default microphone as the audio source
        if ask:
            xoleza_voice(ask)
        audio = r.listen(source)       #listen for the first phrase and extract it into audio data
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)      # recognize speech using Google Speech Recognition
            print('Recognizer voice: ' + voice_data)

        except Exception:
            print('OOPS! something went wrong')
            xoleza_voice('OOPS! something went wrong')   # speech is unintelligible 
        return voice_data

def xoleza_voice(audio_string):
    # Function for giving Voice Mudulation      
    tts = gTTS(text=audio_string, lang='en')
    r = random.randint(1, 10000000)
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)

class Widget:
    #GUI of Virtual Assistant and commands given 
    def __init__(self):

        root = Tk()

        root.title('Xoleza')
        root.geometry('500x320')

        img = ImageTk.PhotoImage(Image.open('assistantt.png'))
        panel = Label(root, image=img)
        panel.pack(side='right', fill='both', expand='no')

        compText = StringVar()
        userText = StringVar()
        # StringVar: Helps to manage the value of a widget such as Labels or Entry more effeciently

        userText.set("Your Voice Assistant")
        userFrame = LabelFrame(root, text="Xoleza", font=('Railways',24,'bold'))
        userFrame.pack(fill='both', expand='yes')

        top = Message(userFrame, textvariable=userText, bg='black', fg='white')
        top.config(font=("Century Gothic",15,'bold'))
        top.pack(side='top', fill='both', expand='yes')

        button_run = Button(root, text='Run', font=('railway',10,'bold'), bg='red', fg='white', command=self.clicked).pack(fill='x', expand='no')
        button_close = Button(root, text='Close', font=('railway',10,'bold'), bg='yellow', fg='black', command=root.destroy).pack(fill='x', expand='no')
        xoleza_voice('How may I help you Victor?')
        root.mainloop()

    def clicked(self):
        # Calling Fucntion
        print("Working...")

        voice_data = record_audio()
        voice_data = voice_data.lower()

        if 'who are you' in voice_data:
            xoleza_voice('My name is Xoleza, made by Abu Bakar')
            
        if 'search' in voice_data:
            search = record_audio('What do you want to search for?')
            url = 'https://google.com/search?q=' + search
            webbrowser.get().open(url)
            xoleza_voice('Here is what I found' + search)

        if 'find location' in voice_data:
             location = record_audio('What is the location?')
             url = 'https://google.nl/maps/place/' + location + '/&amp;'

        if 'What is the time' in voice_data:
             xoleza_voice('The time is: ' + ctime())

        if 'exit' in voice_data:
             xoleza_voice('Thanks, have a good day')
             exit()


if __name__ == '__main__':
    widget = Widget()
    
time.sleep(1)
#xoleza_voice('How may I help you?')
while 1:
    voice_data = record_audio()
    respond(voice_data)


speaker.runAndWait()    


                    #########  EDITED CODE  ########

'''

import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import webbrowser


listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                #print(command)
    except:
        pass
    return command


def run_alexa():
    command = take_command()
    print(command)

    if 'who are you' in command:
        talk('My name is Alexa, made by Abu Bakar')

    elif 'how are you' in command:
        talk('I am fine, what about you')

    elif 'search' in command:
        search = take_command('What do you want to search for?')
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        talk('Here is what I found' + search)

    elif 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)

    elif 'who the heck is' in command:
        person = command.replace('who the heck is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)

    elif 'how to' in command:
        person = command.replace('How to', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)

    elif 'find location' in command:
        location = take_command('What is the location?')
        url = 'https://google.nl/maps/place/' + location + '/&amp;'
        webbrowser.get().open(url)

    elif 'are you single' in command:
        talk('Since I am not a human, so I have no relationship status, and I am created by Abu Bakar')

    elif 'joke' in command:
        talk(pyjokes.get_joke())

    elif 'exit' in command:
        talk('Thanks, have a good day')
        exit()

    else:
        talk('Please say the command again.')


talk('How may I help you Abu Bakar,my name is Alexa')
while True:
    run_alexa()


'''









         
 ######################## '''  END ''' #########################
        





