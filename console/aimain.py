from ai import *
# alf.getvoices(2)

alf.username()
alf.wishme()
command = ""
alf.say("Hello")


while True and command != "goodbye":
    try:
        command = alf.listen() 
        command = command.lower()
    except:
        print("oops there was an error")
        command = ""
    print("command was:", command)

    if command in ["tell me a joke", "joke"]:
        joke()

    elif command in ["send email", "send a email", "send a mail", "email", "mail"]:
        email()
    
    elif command in ["send a message", "send message", "send a whatsapp message", "send whatsapp message", "whatsapp message"]:
        whatsappmgs()

    elif command in ["search in google", "open google", "google"]:
        searchgoogle()

    elif command in ["play a song in youtube", "play youtube", "open youtube", "youtube"]:
        youtube()

    elif command in ["news", "whats news", "whats today news"]:
        news()

    elif command in ["screenshot", "take a screenshot", "take screenshot"]:
        screenshot()

    elif command in ["password", "give a random password", "random password"]:
        passwordgen()

    elif command in ["covid", "news about covid", "what about covid", "covid19"]:
        covid()

    elif command in ["read", "read the selected line", "read this line", "read a selected line"]:
        text2speech()

    elif command in ["weather", "what about the weather", "what is the weather now", "what is weather now"]:
        weather()

    elif command in ["where is", "location", "open google map"]:
        whereis()

    elif command in ["write a note", "write the note", "write note", "note it", "note", "note this"]:
        note()

    elif command in ["show a note", "show me a note"]:
        shownote()

    elif command in ["flip", "flip a coin"]:
        flipcoin()

    elif command in ["roll", "roll a dice"]:
        rolladice()
    
    elif command in ["cpu", "status of cpu", "what is the status of cpu"]:
        cpu()

    elif command in ["time", "what is the time", "what is the time now"]:
        alf.time()

    elif command in ["date", "what is the today date", "what is the date"]:
        alf.date()

    elif command in ["day", "what is the today day", "what is the day"]:
        alf.day()

    # elif command == "search" or command == "play":
    #     command = command.replace("search", "")
    #     command = command.replace("play", "")
    #     web.open(command)

    elif command in ["how are you", "what about you"]:
        alf.say("I am fine, Thank you glad to hear that")
        alf.say("How are you, Sir")

    elif command in ["fine", "good"]:
        alf.say("It's good to know that your fine")

    elif command in ["change my name to", "change my name"]:
        # command = command.replace("change my name to", "")
        alf.say("what should i call you mister")
        alf.name = alf.listen()
        alf.say(f"here onwards i call you mister.{alf.name}")

    elif command in ["change your name", "i like to change your name", "i want to name you"]:
        alf.say("What would you like to call me, Sir ")
        ai_name = alf.listen()
        alf.say("Thanks for naming me")

    elif command in ["what is my name", "what's my name", "my name is"]:
        alf.say(f"your name is mister.{alf.name}")

    elif command in ["what's your name", "what is your name"]:
        alf.say("My friends call me")
        try:
            alf.say(ai_name)
        except:
            ai_name = ("EDITH")
            alf.say(ai_name)
        print("My friends call me", ai_name)

    elif command in [ "who are we"]:
        alf.say("If you talk then definitely your human.")

    elif command in ["why you came to world", "who created you"]:
        alf.say("Thanks to D univers. further It's a secret")

    elif command in ["what is love", "what you think about love", "what you mean by love is"]:
        alf.say("It hard to understand, but i have some information about it")
        alf.say("THE FOUR TYPES OF LOVE: SOME ARE HEALTHY, SOME ARE NOT")
        alf.say("Eros: erotic, passionate love")
        alf.say("Philia: love of friends and equals")
        alf.say("Storge: love of parents for children")
        alf.say("Agape: love of mankind")

    elif command in ["who are you", "what are you"]:
        alf.say("I am your virtual assistant model created by D univers")
        
    elif command in ["prasad", "arun"]:
        alf.say("handsome boy in the universe")
    
    elif command in ["get out of my lab"]:
        alf.say("okay I will obey sir")

    elif command in ["what is the reason for you creation", "why are you born"]:
        alf.say("I was created as a Minor project by the corporation called D univers ")

    elif command in ["will you be my gf", "will you be my bf"]:
        alf.say("I'm not sure about, may be you should give me some time")

    elif command in ["i love you", "i think i love with you", "i think i love you"]:
        alf.say("Love is an kind of attraction.")
    
    elif command in ["who am i"]:
        alf.say("I am your personal assistant")

    # elif command in ["open youtube", "youtube"]:
    #     alf.say("Here you go to Youtube\n")
    #     web.open("youtube.com")

    # elif command in ["open google", "google"]:
    #     alf.say("Here you go to Google\n")
    #     web.open("google.com")

    elif command in ["open stackoverflow", "stackoverflow"]:
        alf.say("Here you go to Stack Over flow.Happy coding")
        web.open("stackoverflow.com")

    elif command in ["open vs code", "vs code"]:
        codepath = "C:\\Users\\Danram\\AppData\\Local\\Programs\\Microsoft VS Code\\code.exe"
        os.startfile(codepath)

    elif command in ["open file explorer", "open local disk", "open computer"]:
        # os.system("explorer C://{}".format(command.replace("open", "")))
        os.system("explorer C:")

    elif command in ["remember that", "remember", "i like you to remember this"]:
        alf.say("what shoud i remember?")
        data = alf.listen()
        alf.say(f"you should me to remember that {data}")
        remember = open("data.txt", "w")
        remember.write(data)
        remember.close()

    elif command in ["do you known anything", "do you known anything about i told you to remember", "what i said you to remember"]:
        remember = open("data.txt", "r")
        alf.say("you told me to remember that " + remember.read())

    elif command in ["exit", "log off", "shutdown"]:
        alf.say("goodbye, i'm going to sleep now")
        quit()
    
    elif command in["Prasad"]:
        alf.say(" I will obey sir")
        

    else:
        alf.say("there is no such command, please read the command list")