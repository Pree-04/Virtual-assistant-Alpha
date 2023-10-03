# importing necessary packages
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import sys
import webbrowser

listener = sr.Recognizer()  # Recognising your voice
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # changing the voice


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            # talk('Hi! I am your personal virtual assistant alpha.')
            # talk('how can i help you?')
            talk('Please give your command')
            print('listening.....')
            voice = listener.listen(source)  # listening to the source
            command = listener.recognize_google(voice, language="en-IN")
            command = command.lower()
            print(command)
            if 'alpha' in command:
                command = command.replace('alpha', '')


    except:
        pass
    return command


def run_alpha():
    command = take_command()
    # print(command)

    if 'stop' in command:
        talk("Alpha terminated")
        sys.exit()

    elif 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)

    elif "open netflix" in command:
        show = command.replace('open netflix', '')
        talk('Opening Netflix ' + show)
        netflix_url = "https://www.netflix.com/in/"
        #Opening the URL in the default web browser
        webbrowser.open(netflix_url)

    elif "open whatsapp" in command:
        show = command.replace('open whatsapp', '')
        talk('Opening whatsapp ' + show)
        whatsapp_url = "https://web.whatsapp.com/"
        #Opening the URL in the default web browser
        webbrowser.open(whatsapp_url)

    elif "open twitter" in command:
        show = command.replace('open twitter', '')
        talk('Opening X ' + show)
        twt_url = "https://x.com/"
        webbrowser.open(twt_url)

    elif "open instagram" in command:
        show = command.replace('open instagram', '')
        talk('Opening instagram ' + show)
        ig_url = "https://www.instagram.com/"
        webbrowser.open(ig_url)


    elif 'time' in command:
        time = datetime.datetime.now().strftime('%H:%M %p')
        print(time)
        talk('The Current time is ' + time)

    elif 'who' in command:
        person = command.replace('who', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)

    elif 'what is' in command:
        person = command.replace('what is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)

    elif 'info on' in command:
        person = command.replace('info on', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)

    elif 'joke' in command:
        joke = (pyjokes.get_joke())
        print(joke)
        talk(joke)

    else:
        talk('Please say that command again.')


talk('Hi! I am your personal virtual assistant alpha.')
while True:
    run_alpha()
