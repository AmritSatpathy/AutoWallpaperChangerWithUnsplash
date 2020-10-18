import threading
import requests
import urllib.request as url
import ctypes
import os
from os import listdir
from os.path import isfile, join
import time
import datetime

def wallpaper():
    f = open("date.txt", "r")
    if (f.read() != datetime.today().strftime('%m/%d/%Y')):
        onlyfiles = [f for f in listdir("C:\\Users\\red_tomato\\PycharmProjects\\autowallpaperchanger") if isfile(join("C:\\Users\\red_tomato\\PycharmProjects\\autowallpaperchanger", f))]
        for f in onlyfiles:
            if (os.path.splitext(f)[1] == ".jpg"):
                os.remove(f)
                print("deleting..")
        r = requests.get("https://api.unsplash.com/search/collections?query=wallpaper&page=1&per_page=48&client_id=os6QVPyOEnV7FWHPx-CmTpWA2JF8qEACv5VMwu1_BOo")
        data = r.json()
        for img_data in data['results']:
            file_name = str(img_data['id']) + ".jpg"
            img_url = img_data['cover_photo']['urls']['raw']
            suffix = '&q=100&fm=jpg&crop=entropy&cs=tinysrg&w=1920&fit=max'
            img_url = img_url + suffix
            url.urlretrieve(img_url,file_name)
        print("downloaded")
        x = datetime.today()
        q = open("date.txt", "w")
        q.write(x.strftime('%m/%d/%Y'))
        q.close()
        return
    else:
        return
def set():
    listimage = []
    onlyfiles = [f for f in listdir("C:\\Users\\red_tomato\\PycharmProjects\\autowallpaperchanger") if
                 isfile(join("C:\\Users\\red_tomato\\PycharmProjects\\autowallpaperchanger", f))]
    for f in onlyfiles:
        if (os.path.splitext(f)[1] == ".jpg"):
            listimage.append(f)
    dirname = "C:\\Users\\red_tomato\\PycharmProjects\\autowallpaperchanger\\"
    for image in listimage:
        ctypes.windll.user32.SystemParametersInfoW(20, 0, dirname + image, 0)
        time.sleep(1800)


if __name__ == "__main__":
    curtime = datetime.datetime.now()
    download_thread = threading.Thread(target=set, name="set")
    download_thread.start()
    while True:
        time.sleep(1)
        diff = (datetime.datetime.now() - curtime).total_seconds()
        if diff > 14400: wallpaper()
        curtime = datetime.datetime.now()
