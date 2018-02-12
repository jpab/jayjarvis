#!/usr/bin/env python3
# Requires PyAudio and PySpeech.
 
import speech_recognition as sr
from time import ctime
import time
import os
from gtts import gTTS
import webbrowser

def speak(audioString):
    print(audioString)
    tts = gTTS(text=audioString, lang='en')
    tts.save("audio.mp3")
    os.system("mpg321 audio.mp3")
 
def recordAudio():
    # Record Audio
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)
 
    # Speech recognition using Google Speech Recognition
    data = ""
    try:
        # Uses the default API key
        # To use another API key: `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        data = r.recognize_google(audio)
        print("You said: " + data)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
 
    return data

 
def jarvis(data):
    if "Quem es tu?" in data:
        speak("I am fine")
    if "Simba" in data:
        speak("Simba!")
        os.system("mpg321 simba.mp3")
        os.system("mpg321 simba.mp3")
        os.system("mpg321 simba.mp3")
        os.system("mpg321 simba.mp3")
    if "simba" in data:
        speak("Simba!")
        os.system("mpg321 simba.mp3")
        os.system("mpg321 simba.mp3")
        os.system("mpg321 simba.mp3")
        os.system("mpg321 simba.mp3")
    if "Madiba" in data:
        speak("Madiba! Madiba! Madiba!")
    if "Que horas sao?" in data:
        speak(ctime())
 
    if "where is" in data:
        data = data.split(" ")
        location = data[2]
        speak("Wait Joao, I gonna show you where " + location + "is")
        os.system("chromium-browser https://www.google.nl/maps/place/" + location + "/&amp;")
    if "open Google" in data:
        webbrowser.open('http://google.com')
        speak("Google is open, do you want to search for something?")
        webbrowser.get('https://www.google.pt/search?q=good+option')
    
# initialization
time.sleep(2)
speak("Hello Joao, what can I do for you?")
while 1:
    data = recordAudio()
    jarvis(data)
    