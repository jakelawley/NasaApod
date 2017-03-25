import requests, json
import tingbot
from HTMLParser import HTMLParser
from tingbot import *

date = ''
explanation = ''
title = ''
hdurl = ''
showImage = 1

@every(hours=12)
def get_data():
    req = requests.get('https://api.nasa.gov/planetary/apod?api_key=5MYmeCSEVNnYaOhZJYXDt4ZlmuEDQWM6DXZackWf&hd=true')
    jsonResp = req.json()
   
    #PARSE CONTENT
    global hdurl
    hdurl = HTMLParser().unescape(jsonResp['hdurl'])
    global explanation
    explanation = HTMLParser().unescape(jsonResp['explanation'])
    global date
    date = HTMLParser().unescape(jsonResp['date'])
    global title
    title = HTMLParser().unescape(jsonResp['title']) 

@right_button.press
def on_right():
    global showImage
    showImage = 0
    
@left_button.press
def on_left():
    global showImage
    showImage = 1

@every(seconds=1.0/30)
def loop():
    if (showImage):
        screen.fill(color='black')
        if(hdurl!=''):
            screen.image(hdurl)
        screen.brightness = 100
    else:
        screen.brightness = 100
        screen.fill(color='black')
        screen.text(title, font_size=13, align='topleft')
        screen.text(explanation, font_size=11, align='bottomleft')

tingbot.run()
