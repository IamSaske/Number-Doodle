'''Requirements
1.You will need continuos internet
'''

import speech_recognition as sr
import pyttsx3
import random


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold=1
        audio=r.listen(source)
        try:
            print('Recognizing....')
            query=r.recognize_google(audio,language='en-in')
            print(f"User said {query}\n")
        except Exception as e:
            speak('Say that again please..')
            return "None"
        return query
if __name__ == '__main__':
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    newvoiceRate = 145
    engine.setProperty('rate', newvoiceRate)
    # speak('Hi')
# while True:
#     query=takecommand().lower()

#game:
    num=random.randint(0,100)
    print(num)
    speak('Guess the number between 0 to 100')
    attempts=0
    while True:
        query=takecommand().lower()
        attempts+=1
        if query==str(num):
            speak(f'Congrats,You win in {attempts} attempts')
            break
        elif query>str(num):
            speak('Enter Lower number please')
            continue
        elif query<str(num):
            speak('Enter higher number please')
            continue

