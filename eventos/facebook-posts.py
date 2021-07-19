import os
import re
import requests
import config
import facebook as fb
import glob
from datetime import datetime, timedelta, time
import schedule


def canvas():

    time_today = datetime.now()

    time_x = time_today + timedelta(days=+10) 

    time2 = time_x.strftime("%Y-%m-%d")

    canvas_list = glob.glob('C:/Users/gonca/Downloads/*evento-canvas*')                  

    item = [[canvas] for canvas in canvas_list if time2 in canvas]

    string = ''.join(item[0])
    
    print(string)

    name = string.split('\\')

    print(name[1])

    x = name[1]

    print(item)
    item.pop()

    
    print(canvas_list)

    access_token ="EAAEZAZAyZC4tuYBAPRZAne4fsz8SS7v8ZCHzFiZBA5yurcwQPGxLvXyZA4iWjsDe80GE4mZBsWO9Eu2usPlQo89yUXkp1zhQokRpdvkUL28L0MdJhT1YaZCs9eZApU7Pktk6aII4oei4yNZAFk29W2oeFUnM3j2BU4KS0SbTyLpZC6LFaaXG3icZA80f2";

    facebook = fb.GraphAPI(access_token)

    facebook.put_photo(open(string, 'rb'))


