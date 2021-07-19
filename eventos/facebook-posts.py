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

    access_token ="EAAEZAZAyZC4tuYBAF7kvNXwhYGraZB79EfRHsIYfDwxwO7UtexUu9y1C5pvlOLJjxasK0oTVYJBV0P9uZAPxt1fMZAHh226mwCM0zvxpNkrwagyPrbzMLfTL5TcHZC34sQ5cnaf5jhNZB2Rqfny1f349cbH1P08yxCwRBuIfGATZB5mJHYH4zVSPA1UuFeJqwCZCJEZBsQ2iqWhFwZDZD";

    facebook = fb.GraphAPI(access_token)

    facebook.put_photo(open(string, 'rb'))


schedule.every().day.at("20:30").do(canvas)

while True:
    schedule.run_pending()
    