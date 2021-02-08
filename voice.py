#installed speechrecognition
#pip install speechrecognition

#installed pyaudio
#pip install pyaudio

#installed gTTS
#pip install gTTS

#installed playsound
#pip install playsound

import speech_recognition as sr # recognise speech
import playsound # to play an audio file
from gtts import gTTS # google text to speech
import random
from time import ctime # get time details
import webbrowser # open browser
#import yfinance as yf # to fetch financial data
#import ssl
#import certifi
import time
import os # to remove created audio files


r = sr.Recognizer()

def record_audio(ask = False):
    with sr.Microphone() as source:
        if ask:
            cruise_speak(ask)
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
            print("You :",voice_data)
        except sr.UnknownValueError:
            cruise_speak("Sorry, I don't understand")
        except sr.RequestError:
            cruise_speak("Sorry, Can You Please say again?")
        return voice_data
    
def cruise_speak(audio_string):
    tts = gTTS(text=audio_string, lang='en')
    r = random.randint(1,1000000)
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print("Bot :",audio_string)
    os.remove(audio_file)  
    
def respond(voice_data):
    voice_data = voice_data.lower()
    if "what is your name" in voice_data:
        cruise_speak("My name is Cruise") 
    if "what is the time now" in voice_data:
        cruise_speak(ctime())
    if "search" in voice_data:
        search = record_audio("What do you want to search for?")
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        cruise_speak('Here is what I found for '+ search)
    if "find location" in voice_data:
        location = record_audio("What is the location?")
        url = 'https://google.nl/maps/place/' + location + '/&amp;'
        webbrowser.get().open(url)
        cruise_speak('Here is the location of '+ location)
    if "youtube" in voice_data:
        youtube_search = record_audio("What do you want to search for?")
        search_term = youtube_search.split("for")[-1]
        url = f"https://www.youtube.com/results?search_query={search_term}"
        webbrowser.get().open(url)
        cruise_speak(f'Here is what I found for {search_term} on youtube')
    if "exit" in voice_data:
        cruise_speak("Thank You")
        exit()
        
    
    
cruise_speak("Hi, How may I help you?")
while 1:
    voice_data = record_audio()
    respond(voice_data)
    
        





 