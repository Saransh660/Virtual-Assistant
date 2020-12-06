import pyttsx3
import datetime
import speech_recognition as sr
import pyaudio
import wikipedia
import webbrowser
import os
import winshell
import smtplib

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
# there are 2 voices generally voices[0] is of david and voices[1] is of zara.
def speak(audio):     #speak function
    engine.say(audio)
    engine.runAndWait()

def wishme():
    t=int(datetime.datetime.now().hour)
    if t>=0 and t<12:
        speak("Good morning sir")
    elif t>=12 and t<18:
        speak("Good afternoon sir")
    else:
        speak("Good evening sir")
    speak("Welcome,sir i am your assistant   ,what can i do for you")

def command():      #taking command from user
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold= 1
        # r.energy_threshold=1000
        audio=r.listen(source)
    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language='en-in')
        print("want to confirm your order")
        print("User said: ", query)
        speak(query)
    except Exception as e:
        print(e)
        print("Please , repeat again.....")
        return "None"
    return  query

# def sendemail(to,body):
#     serv=smtplib.SMTP('smtp.gmail.com',587)
#     serv.ehlo()
#     serv.starttls()
#     serv.login('sender email','sender password')
#     serv.sendmail('sender email',to,body)
#     serv.close()

if __name__ == '__main__':
    wishme()
query=command().lower()

#logic for execution of tasks
if 'wikipedia' in query:
    speak("Searching, wikipedia")
    query=query.replace("wikipedia","")
    results=wikipedia.summary(query,sentences=1)
    speak("according to wikipedia,")
    print(results)
    speak(results)
elif 'open youtube' in query:
    webbrowser.open("www.youtube.com")
elif 'open google' in query:
    webbrowser.open("www.google.com")
elif 'open codechef' in query:
    webbrowser.open("www.codechef.com")
elif 'the time' in query:
    time=datetime.datetime.now().strftime("%H:%M:%S")
    print(time)
    speak(f"Sir, the time is {time}")
elif 'open cmd' in query:
    os.startfile("C:\\WINDOWS\\system32\\cmd")
# elif "send email to" in query:
#     try:
#         speak("what should i say?")
#         body=command()
#         to="destination email"
#         sendEmail(to,body)
#         speak("email sent")
#     except Exception as e:
#         print(e)
#         speak("Try again unable to send")
elif "empty recycle bin" in query:
    winshell.recycle_bin().empty(confirm=False, show_progress=True, sound=True)
    speak("recycle bin cleaned")








