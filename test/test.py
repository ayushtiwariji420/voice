import pyttsx3 as tts
import speech_recognition as sr
import openai

with sr.Microphone() as source:
    while True:
        openai.api_key = "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"    
        # try:
        print("Your turn to speak")

        recognizer = sr.Recognizer()
        recognizer.energy_threshold = 300

        
        print("please speak")
        recognizer.adjust_for_ambient_noise(source, duration=0.2)
        print("listening")
        audio = recognizer.listen(source)
        print("got it")
        try:   
            recognizer_input = recognizer.recognize_google(audio)
            recognizer_input = recognizer_input.lower()
        
            print(recognizer_input)

            completions = openai.Completion.create(
                engine="text-davinci-003",
                prompt=recognizer_input,
                max_tokens=80,
                temperature=0.2,
            )
            print(completions["choices"][0]["text"])
            
            engine = tts.init()
            voices = engine.getProperty('voices')
            #engine.setProperty('voice', 'english+f3') 
            engine.setProperty('rate', 155)
            engine.setProperty('voice', voices[1].id)
            engine.say(completions["choices"][0]["text"])
            engine.runAndWait()
        
        except:
            continue

    