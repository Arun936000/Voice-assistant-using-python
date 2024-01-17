import pyjokes
import smtplib
from email.message import EmailMessage
from secrets import senderemail, epwd
import webbrowser as web
from time import sleep
import pyautogui
import pywhatkit
from newsapi import NewsApiClient
import clipboard
import requests
import time as t
import string
import random
import wikipedia
import datetime
import psutil
import os


from newai import AI

alf = AI()

#*******Get Joke********
def joke():
    funny = pyjokes.get_joke()
    print(funny)
    alf.say(funny)
#*******Get Joke********


#*******send email********
def sendemail(receiver, subject, content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(senderemail, epwd)
    email = EmailMessage()
    email["From"] = senderemail
    email["To"] = receiver
    email["Subject"] = subject
    email.set_content(content)
    server.send_message(email)
    # server.sendmail(senderemail, to, content)
    server.close()

def email():
    email_list = {}
    try:
        alf.say("To whom you want to send the mail?")
        name = alf.listen()
        receiver = email_list[name]
        alf.say("what is the subject of the mail?")
        subject = alf.listen()
        alf.say("what should i say?")
        content = alf.listen()
        sendemail(receiver, subject, content)
        alf.say("email has been send")
    except Exception as e:
        print(e)
        alf.say(f"sorry {alf.name} unable to send the email, because of less secure app access option, please check it or check the recevier name.")
#*******send email********

#*******whatsapp message********
def sendwhatsappmsg(phone_no, message):
    Message = message
    web.open("https://web.whatsapp.com/send?phone=" + phone_no + "&text=" + Message)
    sleep(5)
    pyautogui.press("enter")

def whatsappmgs():
    user_name = {}
    try:
        alf.say("To whom you want to send the whatsapp message?")
        name = alf.listen()
        phone_no = user_name[name]
        alf.say("what is the message?")
        message = alf.listen()
        sendwhatsappmsg(phone_no, message)
        alf.say("the message has been send")
    except Exception as e:
        print(e)
        alf.say(f"sorry {alf.name} unable to send the message.")
#*******whatsapp message********

#*******google********
def searchgoogle():
    alf.say("What should i search for?")
    search = alf.listen()
    web.open("https://www.google.com/search?q=" + search)
#*******google********

#*******youtube********
def youtube():
    alf.say("what should i play on youtube?")
    topic = alf.listen()
    pywhatkit.playonyt(topic)
#*******youtube********

#*******news********
def news():
    alf.say("what the topic you need the news about?")
    topic = alf.listen()
    newsapi = NewsApiClient(api_key="1d25ffe41b79414aa7dec4a5171a6eda")
    data = newsapi.get_top_headlines(q=topic, language="en", page_size=5)
    newsdata = data["articles"]
    for x, y in enumerate(newsdata):
        print(f"{x} {y['description']}")
        alf.say(f"{x} {y['description']}")

    alf.say("that's it for now i'll update you in some time")
#*******news********

#*******texttospeech*******
def text2speech():
    text = clipboard.paste()
    print(text)
    alf.say(text)
#*******texttospeech*******

#*******covid*******
def covid():
    r = requests.get("https://coronavirus-19-api.herokuapp.com/all")
    data = r.json()
    covid_data = f"Confiremed Cases: {data['cases']}\nDeaths: {data['deaths']}\nRecovered:{data['recovered']}"
    print(covid_data)
    alf.say(covid_data)
#*******covid*******

#*******screenshot*******
def screenshot():
    name_img = t.time()
    name_img = f"C:\\Users\\Arun\\Desktop\\screenshots\\{name_img}.png"
    img = pyautogui.screenshot(name_img)
    img.show()
#*******screenshot*******

#*******randompassword*******
def passwordgen():
    s1 = string.ascii_uppercase
    s2 = string.ascii_lowercase
    s3 = string.digits
    s4 = string.punctuation

    passlen = 8
    s = []
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))

    random.shuffle(s)
    newpass = ("".join(s[0:passlen]))
    print(newpass)
    alf.say(newpass)
#*******randompassword*******

#*******wikipedia*******
def wikipediawe():
    alf.say("searching on wikipedia...")
    query = query.replace("wikipedia", "")
    result = wikipedia.summary(query, sentences=2)
    print(result)
    alf.say(result)
#*******wikipedia*******

#*******weather*******
def weather():
    alf.say("which city?")
    cities = alf.listen()
    print(cities)
    url = f"https://api.openweathermap.org/data/2.5/weather?q={cities}&units=imperial&appid=497dc1cb7f3e9bea2a0b53c2d759016d"
    resquest_1 = requests.get(url)
    data = resquest_1.json()
    weather = data["weather"][0]["main"]
    temp = data["main"]["temp"]
    desp = data["weather"][0]["description"]
    temp = round((temp - 32) * 5 / 9)
    print(f"{weather} {temp} {desp}")
    alf.say(f"The weather in {cities} city is like")
    alf.say("Temperature : {} degree celcius".format(temp))
    alf.say("Weather is {}".format(desp))
#*******weather*******

#*******randompassword*******
def whereis():
    alf.say("which place you want to locate")
    location = alf.listen()
    web.open(f"https://www.google.com/maps/place/{location}")
#*******randompassword*******

#*******write a note*******
def note():
    alf.say("What should i write, sir")
    note = alf.listen()
    file = open('jarvis.txt', 'w')
    alf.say("Sir, Should i include date and time")
    snfm = alf.listen()
    if 'yes' in snfm or 'sure' in snfm:
        strTime = datetime.datetime.now().strftime("%H: %M: %S")
        file.write(strTime)
        file.write(" :- ")
        file.write(note)
    else:
        file.write(note)
#*******write a note*******

#*******show a note*******
def shownote():
    alf.say("Showing Notes")
    file = open("jarvis.txt", "r")
    a = file.read()
    print(a)
    alf.say(a)
#*******show a note*******

#*******flip a coin*******
def flipcoin():
    alf.say(f"okay {alf.name}, flipping a coin")
    coin = ["heads", "tails"]
    toss = []
    toss.extend(coin)
    random.shuffle(toss)
    toss = ("".join(toss[0]))
    # print(f"I filpped the coin you got "+toss)
    alf.say("I filpped the coin you got "+toss)
#*******flip a coin*******

#*******roll a dice*******
def rolladice():
    alf.say(f"okay {alf.name}, rolling a dice for you")
    dice = ["1","2","3","4","5","6"]
    roll = []
    roll.extend(dice)
    random.shuffle(roll)
    roll = ("".join(roll[0]))
    print("i rolled a dice and you got "+roll)
    alf.say("i rolled a dice and you got "+roll)
#*******roll a dice*******

#*******cpu usage*******
def cpu():
    usage = str(psutil.cpu_percent())
    alf.say("CPU is at "+usage)
    battery = psutil.sensors_battery()
    alf.say("battery is at"+battery.percent)
#*******cpu usage*******
