import sys
try:
     import pyttsx3
except ImportError:
     sys.exit()
 
tts = pyttsx3.init()  # Initialize the TTS engine.
 
print('Text To Speech Talker, by austinrolert@gmail.com')
print()
print('Enter the text to speak, or QUIT to quit.')
while True:
    text = input('>: ')
 
    if text.upper() == 'QUIT':
         print('Fine, Bye!')
         sys.exit()
 
    tts.say(text)  # Add some text for the TTS engine to say.
    tts.runAndWait()  # Make the TTS engine say it.

