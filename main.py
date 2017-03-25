import requests, json
import tingbot
from HTMLParser import HTMLParser
from tingbot import *

date = ''
explanation = ''
title = ''
hdurl = ''
showImage = 1
screenBrightness = 75

@every(hours=12)
def get_data():
    req = requests.get('https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY&hd=true')
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
    
@midleft_button.press
def on_midleft():
    global screenBrightness
    if(screenBrightness > 0):
        screenBrightness = screenBrightness -5
    
@midright_button.press
def on_midright():
    global screenBrightness
    if(screenBrightness < 100):
        screenBrightness = screenBrightness +5

@every(seconds=1.0/30)
def loop():
    if (showImage):
        screen.fill(color='black')
        if(hdurl!=''):
            screen.image(hdurl)
        screen.brightness = screenBrightness
    else:
        screen.brightness = screenBrightness
        screen.fill(color='black')
        screen.text(title, font_size=13, align='topleft')
        screen.text(explanation, font_size=11, align='bottomleft')

tingbot.run()
