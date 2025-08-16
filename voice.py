import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

recognisor=sr.Recognizer()
sensor=pyttsx3.init()

def speak(text):
    sensor.say(text)
    sensor.runAndWait()

def greet():
    hour=datetime.datetime.now().hour

    if hour<12:
        speak("Good Morning")

    elif hour>=12 and hour<18:
        speak("Good Afternoon")

    elif hour>=18 and hour<24:
        speak("Good Evening")

    speak("Hello! I am your voice assisstant. What can I do for you?")


def listen():
    with sr.Microphone() as mic:
        print("Listening...")
        recognisor.adjust_for_ambient_noise(mic)
        audio=recognisor.listen(mic)
        try:
            print("Understanding")
            command=recognisor.recognize_google(audio)
            print("You spoke",command)
            return command.lower()
        except sr.UnknownValueError:
            speak("I am sorry. I could not understand what you said.")
            return""
        except sr.RequestError:
            speak("Network error!")
            return""
        
def run():
    greet()
    while True:
        command=listen()

        if "hello" in command:
            speak("Hello! Aapka swagat hai")
        if "time" in command:
            time=datetime.datetime.now().strftime("%I %M %p")
            speak(f"The time is{time}")
        if "open google" in command:
            webbrowser.open("https://www.google.com/")
            speak("Opening google")
        if "open youtube" in command:
            webbrowser.open("https://www.youtube.com/")
            speak("Opening Youtube")
        if "paro" in command:
            webbrowser.open("https://www.youtube.com/watch?v=DxsDekHDKXo")
        if "that is all for now" in command or "close" in command:
            speak("It was nice assissting you.")
            break
command=listen()
if "buddy" in command or "badi" in command or "budi" in command:
    run()