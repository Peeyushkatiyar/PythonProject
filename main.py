import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes
import os
import time

def sptext():
    recognizer=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print("recognising...")
            data = recognizer.recognize_google(audio)
            print(data)
            return data
        except sr.UnknownValueError:
            print("Not Understand")
#sptext()

def speechtx(x):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate',125)
    engine.say(x)
    engine.runAndWait()
#speechtx("Hey ! How are you ")

if __name__ == '__main__':

    if "start" in sptext():
            while True:
                    data1 = sptext()
                    if "your name" in data1:
                        name = " my name is Sonal"
                        speechtx(name)

                    elif "created" in data1:
                        creater_name = " I am created by Peeyush katiyar"
                        speechtx(creater_name)

                    elif " age" in data1:
                        age = "I am twenty years old"
                        speechtx(age)

                    elif " how are you" in data1:
                        thik = " I am always fine"
                        speechtx(thik)

                    elif "time" in data1:
                        time = datetime.datetime.now().strftime("%I%M%p")
                        speechtx(time)

                    elif "amazon" in data1:
                        webbrowser.open("https://www.amazon.in/")

                    elif "joke" in data1:
                        joke_1 = pyjokes.get_joke(language="en", category="neutral")
                        print(joke_1)
                        speechtx(joke_1)

                    elif "trip" in data1:
                        add = "D:\guhati"
                        listfile = os.listdir(add)
                        print(listfile)
                        os.startfile(os.path.join(add, listfile[108]))

                    elif "exit" in data1:
                        speechtx('thank you')
                        break
                    time.sleep(3)
    else:
        print("thanks")







