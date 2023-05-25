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
            xoleza_voice('My name is Xoleza, made by Victor')
            
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


         
 ######################## '''  END ''' #########################
        





