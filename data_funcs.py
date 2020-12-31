import requests
from bs4 import BeautifulSoup
import wikipedia
import json
import time


def get_data(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")

    title = soup.find(attrs={"id": "firstHeading"}).text
    try:
        summary = wikipedia.summary(title)
    except:
        get_data(url)

    article = {
        "_date": time.strftime(r"%d.%m.%Y %H:%M:%S", time.localtime()),
        "title": title,
        "desc": summary
    }
    return article


def save_json(_object, path="./data.json"):
    with open(path) as lof:
        loaded_file = json.load(lof)

    loaded_file["articles"].append(_object)
    print(loaded_file)

    with open(path, "w") as f:
        json.dump(loaded_file, f, indent=4)
