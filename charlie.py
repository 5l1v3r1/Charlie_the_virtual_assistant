'GHOST'

import sys
sys.path.append('G:\\Python\\Charlie\\recognizer')
sys.path.append('G:\\Python\\Charlie\\conversation')
sys.path.append('G:\\Python\\Charlie\\commands')

from detector import *
import speech_recognition as sr
from gtts import gTTS
import urllib3, sys
import pyttsx3
from commands.browser import *
from commands.tell_time import *
from commands.uid import *
from commands.music import  music
from commands.movie import *
from conversation.small_talks import *


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

charlie = pyttsx3.init()
r = sr.Recognizer()
charlie.setProperty('rate', 175)
name=""

def charlee(sentence):
    charlie.say(sentence)
    print(sentence)
    charlie.runAndWait()
    
def greet():
    global name
    name=name+recogniseFace()
    Amit= False
    Sandeep= False
    Ashish= False
    name=name.lower()
    
    if name=='amit' and Amit==False:
        charlie.setProperty('rate',150)
        charlee("Good Morning "+name)
        charlee("what can I do for you?")
        charlie .setProperty('rate',170)
        Amit =True
        
    elif name== 'sandeep' and Sandeep==False:
        charlie.setProperty('rate',150)
        charlee("Good Morning "+name)
        charlee("what can I do for you?")
        charlie .setProperty('rate',170)
        Sandeep=True
    
    elif name=='ashish' and Ashish==False:
        charlie.setProperty('rate',150)
        charlee("Good Morning "+name)
        charlee("what can I do for you?")
        charlie .setProperty('rate',170)
        Ashish=True
    
    


def reply(text):
    global name
    
    if 'time' in text:
        time=time_is()
        charlee(time)
    
    elif 'date' in text:
        date=date_is()
        charlee(date)

    

    elif 'song' in text:
        charlee('Here is a song for you')
        music()

    elif 'movie'  in text:
        charlee('Let\'s watch a movie together')
        movie()
    
    elif 'day' in text:
        day=day_is()
        charlee(day)
        
    elif  'login' in text:
        try:
            login('16BCS1249','Dereshi0511!')

        except:
            charlee("DONE!")
        charlee('I logged in for you')
    
    elif 'who are' in text:
        i=who_are_you()
        charlee(i)
    
    elif 'toss a coin ' in text:
        toss=toss_coin()
        charlee(toss)
    
    elif 'how am i' in text:
        how= how_am_i()
        charlee(how)
    
    elif 'who am i' in text:
        who=who_am_i(name)
        charlee(who)
    
    elif 'where were you born' in text:
        born=where_born()
        charlee(born)
    
    elif 'how are you' in text:
        how=how_are_you()
        charlee(how)
    
    elif 'you up' or 'are you up' in text:
        up=are_you_up()
        charlee(up)

    elif 'bye'  in text:
        b=bye()
        charlee(b)
        sys.exit(0)
        return
    
    elif 'love' or 'love you' in text:
        love=love_you()
        charlee(love)
        
    elif 'youtube' or 'open youtube'  in text:
        youtube()
        
    elif 'google' or 'open google' in text:
        google()
    
    
    else:
        charlee('I couldn\'t understand')
    



def heyCharlie():
    greet()
    
    while True:        
        with sr.Microphone() as source:
            print("--->")
            #r.adjust_for_ambient_noise(source, duration=1)
            
            audio = r.listen(source,phrase_time_limit=3)
                       
            try:
                response=""
                response = r.recognize_google(audio)
                response=response.lower()
                print(response)
            
            except:
                print('something\'s wrong')
                continue
            
       
            reply(response)
        
              
heyCharlie()


    
    




