from selenium import webdriver
import datetime
import pyttsx3
import speech_recognition as sr

print('Auto github login system')
Master='Abhishek'
# speak function will pronounce the speech
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

#Function function will wish you on the initializing of jarvis
def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak('Good Morning '+Master) 
    
    elif hour>=12 and hour<18:
        speak('Good Afternoon '+ Master)

    else:
        speak('Good Evening' + Master)

#geckodriver for firefox and chromedriver for chrome
driver = webdriver.Firefox(executable_path=r'geckodriver.exe')
driver.get('https://github.com')
driver.find_element_by_link_text("Sign in").click()
driver.find_element_by_id('login_field').send_keys("email")
driver.find_element_by_id('password').send_keys('password')
driver.find_element_by_name('commit').click()

#Function will take command from microphone
def takeCommand():

    r=sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening..')
        audio=r.listen(source)

    try:
        print('Recognizing..')
        query=r.recognize_google(audio,language='en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        print('Say that again please')
        query=None

    return query 

speak('Web automation')
wishMe()
speak("speak otp {}".format(Master))
otp=takeCommand()
str=""
for elm in otp:
    if elm.isdigit():
        str+=elm
driver.find_element_by_id('otp').send_keys(str)
speak("We have successfully did the automation {}".format(Master))