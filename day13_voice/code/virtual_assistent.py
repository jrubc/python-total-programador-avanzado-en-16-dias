import datetime
import webbrowser

import pyjokes
import pyttsx3
import speech_recognition as sr
import wikipedia
import yfinance as yf
from pywhatkit.misc import playonyt, search

# voice options / languagues
ID1 = "English_(America)"


# listen microphone and return audio as string format
def convert_audio_to_string():
    # save recognizer in variable
    r = sr.Recognizer()

    # configure microphone
    with sr.Microphone() as origen:
        # wait
        r.pause_threshold = 0.8

        # log recording start
        print("Now you can talk")

        # save audio
        audio = r.listen(origen)

        try:
            # search in google
            request = r.recognize_google(audio)

            # test
            print("You said: " + request)

            # return request
            return request

        # if it was not capable of recognize audio
        except sr.UnknownValueError:

            # proof that it don't understands the audio
            print("ups, I don't understood")

            # return error
            return "I am waiting"

        # not capable to return request
        except sr.RequestError:
            # proof that it don't understands the audio
            print("ups, there are not service")

            # return error
            return "I am waiting"
        except:
            # proof that it don't understands the audio
            print("something is wrong")

            # return error
            return "I am waiting"


# function to hear assistent
engine = pyttsx3.init()


def speak(message):
    engine.setProperty("voice", ID1)
    engine.say(message)
    engine.runAndWait()


# report week day
def ask_day():
    # create a variable using today date
    day = datetime.date.today()
    print(day)

    # create a variable for the day of the week
    week_day = day.weekday()
    print(week_day)

    # dictionarie with day names
    calendar = {
        0: "Monday",
        1: "Tuesday",
        2: "Wednesday",
        3: "Thursday",
        4: "Friday",
        5: "Saturday",
        6: "Sunday",
    }
    # Tell week day
    speak(f"Today is {calendar[int(week_day)]}")


# report hour
def ask_hour():
    # create a variable using hour dates
    hour = datetime.datetime.now()
    hour = f"At moment is {hour.hour} hours with {hour.minute} minutes and {hour.second} seconds"
    print(hour)

    # tell hour
    speak(hour)


def initial_greeting():
    # create variable with hour dates
    hour = datetime.datetime.now()
    if hour.hour < 6 or hour.hour > 20:
        moment = "Good night"
    elif 6 <= hour.hour and hour.hour < 13:
        moment = "Good day"
    else:
        moment = "Good morning"

    # say greeting
    speak(
        f"{moment}, I am Helena, your assistant personal. Could you tell me what can I do for you"
    )


# main function
def ask_things():
    # active initial greeting
    initial_greeting()

    # cut variable
    start = True
    while start:
        # Active micro and save request
        request = convert_audio_to_string().lower()

        if "open youtube" in request:
            speak("Okay, I am opening youtube")
            webbrowser.open("https://www.youtube.com")
            continue

        elif "open browser" in request:
            speak("Of course, I am doing that")
            webbrowser.open("https://search.brave.com")
            continue

        elif "what day is" in request:
            ask_day()
            continue

        elif "what time is" in request:
            ask_hour()
            continue

        elif "search wikipedia" in request or "search in wikipedia" in request:
            speak("Searching on Wikipedia...")

            # Limpiar la consulta
            request = request.replace("search in wikipedia", "").strip()
            request = request.replace("search wikipedia", "").strip()

            try:
                wikipedia.set_lang("en")
                result = wikipedia.summary(request, sentences=1, auto_suggest=True)
                speak(f"Wikipedia says: {result}")

            except wikipedia.exceptions.DisambiguationError as e:
                speak(
                    f"There are multiple results for {request}. Please be more specific."
                )
                print(
                    f"DisambiguationError: {e.options}"
                )  # Muestra las opciones en consola

            except wikipedia.exceptions.PageError:
                speak("I couldn't find anything on Wikipedia. Try another search.")

            except Exception as e:
                speak("An unexpected error occurred.")
                print(f"Error: {e}")  # Muestra otros errores en consola
            continue
        elif "search in internet" in request:
            speak("I am doing that")
            request = request.replace("search in internet", "")
            search(request)
            speak("This is what I found")
            continue
        elif "play" in request:
            speak("okay, I'm gonna play that")
            playonyt(request)
            continue
        elif "joke" in request:
            speak(pyjokes.get_joke())
            continue
        elif "price of the actions" in request:
            action = request.split("of")[-1].strip()
            wallet = {"apple": "APPL", "amazon": "AMZN", "google": "GOOGL"}
            try:
                searched_action = wallet[action]
                searched_action = yf.Ticker(searched_action)
                actually_price = searched_action.info["regularMarketPrice"]
                speak(f"I found it, the price of {action} is {actually_price}")
            except:
                speak("I'm sorry, i couldn't do it")
                continue

        elif "goodbye" or "good bye" in request:
            speak("Goodbye bitch")
            break


ask_things()
