from data_funcs import get_data, save_json
import speech_recognition as sr
import time
import pprint
import os
import json
from notifier import notify, speak


config = json.load(open("./config.json"))

uName = "User" if config["username"] == "" else config['username']
delay = 3600 if config["time"] < 10 else config['time']
icon_path = config["icon"]


myUrl = "https://en.wikipedia.org/wiki/Special:Random"
r = sr.Recognizer()

while True:
    def main():
        data = get_data(myUrl)
        pprint.pprint(data)
        title = data['title']
        try:
            notify(title, data["desc"][:100] + ".............", icon=icon_path)
        except:
            pass
        speak(f"Dear,{uName}, do you want to hear about {title}?")

        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source, duration=0.2)
            try:
                audio = r.listen(source)
                text = r.recognize_google(audio)

                if "yes" in text:
                    speak(data["desc"])

                elif "no" in text:
                    speak("Ok")
                    time.sleep(2)
                    speak("Do you want to hear another article?")

                    try:
                        audio2 = r.listen(source)
                        text2 = r.recognize_google(audio2)

                        if "yes" in text2:
                            data2 = get_data(myUrl)
                            title2 = data2['title']
                            speak(f"Ok then, telling you about {title2}")

                        elif "no" in text2:
                            speak("Ok then, I will talk to you later")
                            return 0
                        else:
                            speak("Invalid")
                            return 0
                    except:
                        print("Error")
                        main()
                else:
                    speak("Invalid")
                    main()

                save_json(data)

            except:
                print("Error")
                main()
    main()
    print("In sleep")
    time.sleep(delay)
