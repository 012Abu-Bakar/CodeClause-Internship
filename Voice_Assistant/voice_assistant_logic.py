import speech_recognition as sr  #  recognize speech
import pyttsx3 #text to speech
import time
from time import ctime
import webbrowser
import playsound
import os
import random
from gtts import gTTS #Google Text To Speech


print('Say something...')
r = sr.Recognizer()
speaker = pyttsx3.init() # inititalize the engine(speaker)



'''Function for Audio Record'''

def record_audio(ask=False):
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

    
''' Function for giving Voice Mudulation '''        

def xoleza_voice(audio_string):
    tts = gTTS(text=audio_string, lang='en')
    r = random.randint(1, 10000000)
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)


''' Function for giving tasks '''

def respond(voice_data):
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


time.sleep(1)
xoleza_voice('How may I help you abu bakar?')
while 1:
    voice_data = record_audio()
    respond(voice_data)


speaker.runAndWait()    


         
