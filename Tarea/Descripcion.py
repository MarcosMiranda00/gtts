from gtts import gTTS
import os 
from NLTKCLASS import *

text = summary
language = 'es'
speech = gTTS(text = text, lang = language, slow = False)
speech.save("Speak.mp3")
os.system("start Speak.mp3")