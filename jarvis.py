import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os

engine = pyttsx3.init("sapi5")  # initializing text to speech engine
voices = engine.getProperty("voices")  # voices is the list of voices

# set property is to set and change engine's properties
engine.setProperty("voice", voices[0].id)  # set which voice u want
engine.setProperty("rate", 130)  # set what speed u want
engine.setProperty("volume", 1)  # set volume


def speak(audio):
    engine.say(audio)  # speaks whatever text it is inputted
    engine.runAndWait()  # it will process all the audio


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("good morning master")
    elif hour >= 12 and hour < 19:
        speak("good afternoon master")
    else:
        speak("good evening master")
def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 200
        audio = r.listen(source)
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in') #Using google for voice recognition.
        print(f"User said: {query}\n")  #User query will be printed.

    except Exception as e:
        print(e)    
        print("Say that again please...")   #Say that again will be printed in case of improper voice 
        return "None" #None string will be returned
    return query
wishMe()
speak("How may i help you?")
while True:
    query = takeCommand().lower()
    if 'wikipedia' in query :
        speak("According to wikipedia")
        query = query.replace("wikipedia","")
        results = wikipedia.summary(query,sentences=2)
        speak(results) 
        print(results)
    elif 'open youtube' in query :
        speak("opening...")
        webbrowser.open("youtube.com")
    elif 'open google' in query :
        speak("opening...")
        webbrowser.open("google.com")
    elif 'open stack overflow' in query :
        speak("opening...")
        webbrowser.open("stackoverflow.com")
    elif 'play music' in query:
        music_dir ='C:\\Users\\alman\\OneDrive\\Desktop\\PROJECT JARVIS\\Gaana'
        songs = os.listdir(music_dir)
        print(f"playing {songs[0]}")
        speak(f"playing {songs[0]}")
        os.startfile(os.path.join(music_dir,songs[0]))
    elif 'open code' in query:
        codePath = "C:\\Users\\alman\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        os.startfile(codePath)