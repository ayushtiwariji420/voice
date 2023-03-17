
import pyttsx3 as tts
import speech_recognition as sr

def abriella_speak(text):
        engine = tts.init()
        voices = engine.getProperty('voices')
        #engine.setProperty('voice', 'english+f3') 
        engine.setProperty('rate', 155)
        engine.setProperty('voice', voices[1].id)
        engine.say(text)
        engine.runAndWait()

recognizer = sr.Recognizer()
recognizer.energy_threshold = 300
with sr.Microphone() as source:   
    def recognizerOpen(source,callback = None):
            print("please speak")
            recognizer.adjust_for_ambient_noise(source, duration=0.2)
            print("listening")
            audio = recognizer.listen(source,timeout=5)
            print("got it")
                
            recognizer_input = recognizer.recognize_google(audio)
            recognizer_input = recognizer_input.lower()


            return recognizer_input
    

