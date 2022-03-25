# -*- coding: utf-8 -*-
from flask import render_template, request
from sense_hat import SenseHat
import RPi.GPIO as gpio
from flask import Flask
import os, time

sense = SenseHat()
app = Flask(__name__)
#sense.show_message("test 1")

r = [255, 0, 0]
b = [0, 0, 0]

#def heart():
#    sense.set_pixels(b, r, b, b, b, b, r, b,
#                     r, r, r, b, b, r, r, r,
#                    r, r, r, r, r, r, r, r,
#                    b, r, r, r, r, r, r, b,
#                     b, b, r, r, r, r, b, b,
#                     b, b, b, r, r, b, b, b,
#                     b, b, b, b, r, b, b, b]

@app.route("/temp/")
def temp():
    temp = sense.get_temperature()
    #round it to 2 decimal places
    temp = round(temp, 2)
    #return string of temperature
    temp = str(temp)
    #get temperatue from sensehat
    return("Temperature is: " + temp)

@app.route("/<action>")
def action(action):
    if action == "green":
        #use clear to light it up as it also clears every possible left overs
        sense.clear(0, 255, 0)
    if action == "red":
        sense.clear(255, 0, 0)
    if action == "blue":
        sense.clear(0, 0, 255)
    if action == "pink":
        sense.clear(228, 35, 157)
    if action == "purple":
        sense.clear(84, 22, 180)
    if action == "smile":
        sense.clear()
        sense.show_message(":)")
#    if action == "heart":
#        sense.clear()
#        heart()
    if action == "temp":
        temp = sense.get_temperature()
        print(temp)
        #round it to 2 decimal places
        temp = round(temp, 2)
        #return string of temperature
        temp = str(temp)
        sense.clear()
        sense.show_message(temp)
    if action == "off":
        sense.clear()
if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 5002, debug = True)