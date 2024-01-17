import pyttsx3
import speech_recognition as sr
from datetime import datetime
import shutil


class AI:
    
    __name = ""
    __skill = []

    def __init__(self, name = None):
        self.engine = pyttsx3.init()

        voices = self.engine.getProperty("voices")
        self.engine.setProperty("voice",voices[1].id)
        name = voices[1].name
        print(name)

        self.r = sr.Recognizer()
        self.m = sr.Microphone()

        if name is not None:
            self.__name = name

        print("Listening...")
        with self.m as source:
            self.r.adjust_for_ambient_noise(source)

    def say(self, sentance):
        print(sentance)
        self.engine.say(sentance)
        self.engine.runAndWait()

    def listen(self):
        print("Say Something")
        with self.m as source:
            try:
                audio = self.r.listen(source)
            except:
                pass
        # print("got it")
        phrase = ""
        try:
            phrase = self.r.recognize_google(audio, show_all=False, language="en_US")
            phrase = str(phrase)
           
        except:
            pass
           
        print("You Said", phrase)
        return phrase


    def time(self):
        Time = datetime.now().strftime("%I:%M:%S %p")
        self.say("the current time is")
        self.say(Time)


    def date(self):
        year = int(datetime.now().year)
        month = int(datetime.now().month)
        date = int(datetime.now().day)
        self.say(f"today day is {date} {month} {year}")
       

    def day(self):
        today_day = datetime.today().strftime('%A')
        print(today_day)
        self.say(f"today day is {today_day}")

    
    def username(self):
        self.say("What should i call you sir")
        self.name = self.listen()
        self.say(f"Welcome Mister{self.name}")
        columns = shutil.get_terminal_size().columns
        print("Welcome Mr.", self.name.center(columns))
        self.say("How can i Help you, Sir")

    def greeting(self):
        hour = datetime.now().hour
        if hour >= 6 and hour < 12:
            self.say(f"Good morning {self.name}")
        elif hour >= 12 and hour < 18:
            self.say(f"Good afternoon {self.name}")
        elif hour >= 18 and hour < 24:
            self.say(f"Good evening {self.name}")
        else:
            self.say(f"Good night {self.name}")

    def wishme(self):
        self.date()
        self.time()
        self.day()
        self.greeting()
        self.say("EDITH at your service, please tell me how can i help you")


 