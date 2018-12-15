# -*- coding: utf-8 -*-
"""
Created on Sat Dec 15 10:07:19 2018

@author: Radhika
"""

import speech_recognition as sr
print("Test")

r = sr.Recognizer() 
with sr.Microphone() as source:
    print("speak:")
    audio = r.listen(source)
    
try:
    print("you said:"+r.recognize_google(audio))
except sr.UnknownValueError:
    print("could not understand audio")
except sr.RequestError as e:
    print("Could not request results; {0}".format(e))
    
