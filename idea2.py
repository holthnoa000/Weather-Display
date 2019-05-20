#!/usr/bin/python

#matrix_libraries
from rgbmatrix import graphics
import time
from PIL import Image
from PIL import ImageDraw
from rgbmatrix import RGBMatrix, RGBMatrixOptions
import os

#weather_apis
switch_time = 12

from requests import get
from pprint import pprint
import json
import sys
import time
import pigpio
import random
pi = pigpio.pi()

#Copy and paste JSON file url
url = 'https://api.darksky.net/forecast/fcb5dfb979848fcc9296545128ea1823/37.8267,-122.4233'

myweather_sum = get(url).json()['currently']['icon']
conditions = {"cloudy" : "cloudy", "partly-cloudy-day" : "cloudy", "partly-cloudy-night" : "cloudy", "fog" : "cloudy", "clear-day" : "sunny", "clear-night" : "sunny" , "snow" : "snowy", "sleet" : "snowy", "hail" : "snowy" , "rain" : "rainy" , "thunderstormstorm" : "stormy"}

# Configuration for the matrix
options = RGBMatrixOptions()
options.rows = 32
options.chain_length = 2
options.parallel = 1
options.hardware_mapping = 'adafruit-hat'

matrix = RGBMatrix(options = options)
font = graphics.Font()
font.LoadFont("../../../fonts/8x13B.bdf")
offscreen_canvas = matrix.CreateFrameCanvas()

#Colors
green = graphics.Color(0,150,0)
red = graphics.Color(150,0,0)
purple = graphics.Color(255,0,255)

while True:
    current_time = time.strftime("%I:%M")
    ampm = time.strftime("%p")
    current_weather = conditions[myweather_sum]

#Clock Face:
    graphics.DrawText(offscreen_canvas, font, 2, 2, red, current_time)
    graphics.DrawText(offscreen_canvas, font, 2, 15, green, ampm)
    graphics.DrawText(offscreen_canvas, font, 2, 30, green,current_weather)
    offscreen_canvas = matrix.SwapOnVSync(offscreen_canvas)

    time.sleep(30)

    offscreen_canvas.Clear()
