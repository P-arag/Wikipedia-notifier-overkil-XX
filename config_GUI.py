import PySimpleGUI as sg
import json


sg.theme('DarkTeal2')

config = json.load(open("./config.json"))
uName = config["username"]
iTime = config["time"]
iIcon = config["icon"]

heading = [sg.Image("./wikipedia.png", size=(100, 100)), sg.Text(
    "Welome to Wikipedia Random Article Config Settings", font="NotoSans 25", text_color="black", pad=(50, 50))]

username = [sg.Text('Enter Your Username', size=(20, 1),
                    font="Arial 15"), sg.InputText(default_text=uName, size=(50, 4), font="15", key="-UN-", pad=(284, 10))]

time = [sg.Text("Enter the time delay between the notifications (seconds)",
                font="Arial 15"), sg.InputText(size=(35, 4), default_text=iTime, enable_events=True, font="15", key="-TIME-")]

icon = [sg.Text("Enter the icon path", size=(20, 1),
                font="Arial 15"), sg.FileBrowse(key="-ICO-", initial_folder=iIcon, file_types=(("Images", "*.jpeg"), ("Images", "*.jpg"), ("Images", "*.png")), pad=(0, 0))]


layout = [heading,
          username,
          time,
          icon,
          [sg.Submit(), sg.Cancel()]]

window = sg.Window('Configure Your Notifier', layout,
                   size=(1200, 300))


out = {}
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel' or event == "Submit":

        out = {
            "username": values["-UN-"],
            "time": float(values["-TIME-"]),
            "icon": values["-ICO-"]
        }

        break

    if len(values['-TIME-']) and values['-TIME-'][-1] not in ('0123456789'):
        window['-TIME-'].update(values['-TIME-'][:-1])


window.close()

json.dump(out, open("config.json", "w"), indent=4)
