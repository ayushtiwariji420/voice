import speech_recognition as sr
from playsound import playsound
from utils.utils import abriella_speak


# this function works great but we need a stop function to allow pausing and restarting the music or stopping it completely

def play_music(user_name):
    done = False
    abriella_speak(f"ok {user_name}, here is a nice relaxing album for you, it will help you unwind, and, it's especially good for meditating")
    
    while not done:
        try:
            playsound('assets/relaxing-music-vol1.mp3')
            done = True
        # only prints music paused doesn't actually stop music playing needs more work to pause the mp3 file and return to listening for commands
        except KeyboardInterrupt:
            playsound.stop()
            print('music paused')
            done = True
                                
        except sr.UnknownValueError:
            abriella_speak(f"sorry {user_name}, i didn't catch that, please try again")
        
        
        
        
        
        
        