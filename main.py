import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclibrary
import requests
import datetime
import pywhatkit


recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi ="d4aee33b28534e549049e938d26c1c95"
def speak(text):
    engine.say(text)
    engine.runAndWait()



def tell_time_and_date():
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    current_date = datetime.datetime.now().strftime("%d-%m-%Y")
    speak("वर्तमान समय " + current_time + " और तारीख " + current_date + " है")


def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif   "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif "open instagram" in c.lower():
        webbrowser.open("https://instagram.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musiclibrary.music[song]
        webbrowser.open(link)

    elif "news" in c.lower():
        r = requests.get("https://newsapi.org/v2/top-headlines?country=us&apiKey=d4aee33b28534e549049e938d26c1c95")
        if r.status_code == 200:
            data = r.json()
            articles = data.get('articles',[])
            for article in articles:
                print(article["title"])

    elif  "samay" in c.lower():
        tell_time_and_date()

    

    elif "send message" in c.lower():
       speak("mummy")
    # yahan number aur message input lo
       pywhatkit.sendwhatmsg("+917897119936", "Hello from Jarvis!", 11, 7)  # 15:30 time pe bhejega



    
if __name__ == "__main__":
    speak("Initializing Jarvis...")
    while True:
        r = sr.Recognizer()
        

        print("recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=2, phrase_time_limit=2)
            word = r.recognize_google(audio)
            if(word.lower() == "jarvis"):
                speak("ya")

                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)

        except Exception as e:
            print("Error; {0}".format(e))
        
