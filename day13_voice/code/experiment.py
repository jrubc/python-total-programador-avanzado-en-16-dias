import pyttsx3


def speak(message):
    engine = pyttsx3.init()
    engine.say(message)
    engine.runAndWait()
    engine.stop()  # 🔥 Asegura que no haya bloqueos


speak("Hello, this is a test")
speak("Hello, now it should be working")
speak("Hello world")  # 🔄 Ahora debería decir esto
speak("Let's see if this works")
