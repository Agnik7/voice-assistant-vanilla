import pyttsx3 as ptx
def speech(text):
    vanilla = ptx.init()
    voices = vanilla.getProperty('voices')
    vanilla.setProperty('voice', voices[1].id)
    vanilla.setProperty('rate', 150) 
    vanilla.say(text)
    vanilla.runAndWait()