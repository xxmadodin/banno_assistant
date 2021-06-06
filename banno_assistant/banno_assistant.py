import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib


engine= pyttsx3.init("sapi5")
voices=engine.getProperty("voices")
#print(voices)
engine.setProperty("voice",voices[1].id)




def speak(audio): 
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning saurabh ")
    elif hour>=12 and hour<18:
        speak("good after noon saurabh ")
    else:
        speak("good evening saurabh ")

    speak("hello my name is banno how can i help you")

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("i am listening.........")
        r.pause_threshold = 1
        audio=r.listen(source)

    try:
        print("recognizing....")
        query= r.recognize_google(audio,language="en-in")
        print("user said: ",query) 

    except Exception as e:
       # print(e)
        print("say that again please......")
        return "None"

    return query

def sendemail(to, content):
    server= smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls() 
    server.login("saurabhk.ic.19@nitj.ac.in","#yourpassword")
    server.sendmail("saurabhk.ic.19@nitj.ac.in",to,content)
    server.close()


if __name__ == "__main__":
   wishme()
   while True:
       query = takeCommand().lower()
       
       if "wikipedia" in query:
           speak ("searching wikipeadia....")
           query= query.replace("wikipedia","")
           results= wikipedia.summary(query, sentences=2)
           speak("according to wikipedia")
           print(results)
           speak(results)


       elif "open google" in query:
           webbrowser.open("google.com")

       elif "open youtube" in query:
           webbrowser.open("youtube.com")

       elif "open codechef" in query:
           webbrowser.open("codechef.com")

       elif "open stackoverflow" in query:
           webbrowser.open("stackoverflow.com")

       elif "play music" in query:
           music_dir = "D:\\Music"
           songs=os.listdir(music_dir)
           print(songs)
           os.startfile(os.path.join(music_dir,songs[0]))
       
       elif "the time" in query:
           strTime = datetime.datetime.now().strftime("%H:%M:%S")
           speak("the time is: " + strTime)

       elif "open visual studio"  in query:
           codepath="C:\\Program Files (x86)\\Microsoft Visual Studio\\2019\\Community\\Common7\\IDE\\devenv.exe"
           os.startfile(codepath)

       elif "email to saurabh" in query:
           try:
               speak ("what should i say")
               content=takeCommand()
               to="sknk08837@gmail.com"
               sendemail(to,content)
               speak("Email has been sent")
           except Exception as e:
               print(e)
               speak("sorry i could not send email ")



       elif "email to rahul" in query:
           try:
               speak ("what should i say")
               content=takeCommand()
               to="rahulk.ic.19@nitj.ac.in"
               sendemail(to,content)
               speak("Email has been sent")
           except Exception as e:
               print(e)
               speak("sorry i could not send email ")

       elif "email to devansh" in query:
           try:
               speak ("what should i say")
               content=takeCommand()
               to="devanshp.ic.19@nitj.ac.in"
               sendemail(to,content)
               speak("Email has been sent")
           except Exception as e:
               print(e)
               speak("sorry i could not send email ")

       elif "email to likitha" in query:
           try:
               speak ("what should i say")
               content=takeCommand()
               to="likithae.ic.19@nitj.ac.in"
               sendemail(to,content)
               speak("Email has been sent")
           except Exception as e:
               print(e)
               speak("sorry i could not send email ")

       elif "ok take care bye" in query:
           speak ("ok i am going thankyou take care bye bye")
           print ("ok i am going thankyou take care bye bye")
           break




