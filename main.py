import pyttsx3
# pip install pyttsx3 it is a a text-to-speech conversion lib/package
import speech_recognition as sr
# pip install speechRecognition this will help ai to understand the thing which we say
import datetime
# datetime help baymax to tell time and also in greetings
import wikipedia
# pip install wikipedia , this library contains all the information(knowledge of maximum thing which will help baymax to answer.
import webbrowser
# we want our baymax to open different different sites so webbrowser will help us open sites as per command
import os
# helps us to interact with the native OS Python is currently running on
import smtplib

# it's a python lib help us to send mails

engine = pyttsx3.init('sapi5')
# sapi is nothing but it's a speech api that is we will take voice through it
voices = engine.getProperty('voices')
# print(voices[1].id)
# here we set up the voice property, generally there are two voice bydefault that is male and female  0=male/1=female
engine.setProperty('voice', voices[0].id)


#

# here we are writing speak function so that our AI can speak
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


# here wishme def will help baymax in saying appropriate greetings such as good morning ,goodnight
def wishMe():
    hour = int(datetime.datetime.now().hour)  # datetime module will help us here
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")
    # after greeting we wanted bae-max to ask us that we need so the below line will command him to say the written thing
    speak("I am Baymax. Please tell me how may I help you")


def takeCommand():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 300  ######################################################################
        # pause threshold is number of seconds our ai will pause or stop before terminating the code.
        audio = r.listen(source)
    # but what if we got any error or baymax is not able to understand what we said
    # so at this point try will help us here we are using recognize along with google and chosing language english(en) we can also choose hindi(hn)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        speak("say that again please")
        return "None"
    return query


# for sending mail here smtlib is a package in python this will help us to send directly mails from google gmail.
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    # this part is little bit risky because for this we have to enable less secure apps and it may breach the data of the user.
    server.ehlo()
    server.starttls()
    server.login('baymax@gmail.com', '*****baymaxpassword')
    server.sendmail('yash.dev.6116@gmail.com', to, content)
    server.close()


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()  # using .lower so that every word it takes will be in lower case, which will help us in not havinng uppar/lower case errors.

        # Logic for executing tasks based on query that if we want to know about something then we can directly say wikipedia ... and further whatever we need to search
        if 'wikipedia' in query:
            speak('Searching ...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query,
                                        sentences=1)  # here we are giving sentence 1 because we dont want to make it big here 1 will only let or baymax real 1 sentence.
            speak("According to me")
            print(results)
            speak(results)

        # now from here we are opening sites so webbrowser module will help baymax to open diffrent sites for us.
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open baymax gpt' in query:
            webbrowser.open("https://chat.openai.com/")




        elif 'hello baymax' in query:
            speak("hello sir")

        elif 'how are you' in query:
            speak("i am fine,thank you")
            speak("how can i help you")




        # baymax music play (os module/lib will help us here.)
        elif 'play music' in query:
            music_dir = "D:\\baymaxmusictrial"
            songs = os.listdir(music_dir)
            print(songs)
            speak("playing songs for you")
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")


        elif 'open zen z code' in query:
            webbrowser.open("https://youtu.be/ga8ZSDrYekY")

        elif "baymax turn off" in query:
            speak("Have a good day, see you soon")
            exit()

        elif 'email to ' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "baymax@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                # print(e)
                speak(
                    "Sorry currenty i am in beta version, this feature will be unlocking soon. I am not able to send this email")
