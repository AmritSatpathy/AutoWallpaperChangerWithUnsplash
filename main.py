import threading
import requests
import urllib.request as url
import ctypes
import os
from datetime import datetime as dt
from os import listdir
from os.path import isfile, join
import time
global date
date = "10/18/2020"
def wallpaper():
    global date
    if (date != dt.today().strftime('%m/%d/%Y')):
        onlyfiles = [f for f in listdir("C:\\Users\\red_tomato\\PycharmProjects\\autowallpaperchanger\\") if isfile(join("C:\\Users\\red_tomato\\PycharmProjects\\autowallpaperchanger\\", f))]
        for f in onlyfiles:
            if (os.path.splitext(f)[1] == ".jpg"):
                os.remove(f)
        r = requests.get("https://api.unsplash.com/search/collections?query=wallpaper&page=1&per_page=48&client_id=os6QVPyOEnV7FWHPx-CmTpWA2JF8qEACv5VMwu1_BOo")
        data = r.json()
        for img_data in data['results']:
            file_name = str(img_data['id']) + ".jpg"
            img_url = img_data['cover_photo']['urls']['raw']
            suffix = '&q=100&fm=jpg&crop=entropy&cs=tinysrg&w=1920&fit=max'
            img_url = img_url + suffix
            url.urlretrieve(img_url,file_name)
        x = dt.today()
        date = dt.today().strftime('%m/%d/%Y')
        print(date)
        return
    else:
        return
def set():
    time.sleep(15)
    listimage = []
    onlyfiles = [f for f in listdir("C:\\Users\\red_tomato\\PycharmProjects\\autowallpaperchanger\\") if
                 isfile(join("C:\\Users\\red_tomato\\PycharmProjects\\autowallpaperchanger\\", f))]
    for f in onlyfiles:
        if (os.path.splitext(f)[1] == ".jpg"):
            listimage.append(f)
    dirname = "C:\\Users\\red_tomato\\PycharmProjects\\autowallpaperchanger\\"
    for image in listimage:
        ctypes.windll.user32.SystemParametersInfoW(20, 0, dirname + image, 0)
        time.sleep(1800)


if __name__ == "__main__":
    update_thread = threading.Thread(target=set, name="set")
    update_thread.start()
    download_thread = threading.Thread(target=wallpaper(), name="wallpaper")
    download_thread.start()

