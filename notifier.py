import os
import playsound
import json
from gtts import gTTS

config = json.load(open("./config.json"))


def notify(title, message, icon=config["icon"]):
    playsound("./sounds/ding.mp3")
    os.system(
        f"notify-send -u critical -i \"{icon}\" '{title}' '{message}'")


def speak(text):
    tts = gTTS(text, lang="en")
    tts.save("./sounds/speak.mp3")
    playsound.playsound("./sounds/speak.mp3")
