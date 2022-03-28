# -*- coding: utf-8 -*-
from flask import render_template, request
from sense_hat import SenseHat
import RPi.GPIO as gpio
from flask import Flask
import os, time
 
sense = SenseHat()
app = Flask(__name__)
 
#no colour
b = [0, 0, 0] 
#setting colours
red = [255, 0, 0]
white = [255,255,255]
blue = [0, 0, 255]
green = [0, 255, 0] 
pink = [228, 35, 157] 
 
def heart():
    sense.set_pixels([b, red, b, b, b, b, red, b,
                    red, red, red, b, b, red, red, red,
                    red, red, red, red, red, red, red, red,
                    b, red, red, red, red, red, red, b,
                    b, b, red, red, red, red, b, b,
                    b, b, b, red, red, b, b, b,
                    b, b, b, b, red, b, b, b,
                    b, b, b, b, b, b, b, b])
 
@app.route("/temp/")
def temp():
    '''print("Inside temp not action")'''
    #creating temp variable and rounding it to 2 decimal places
    temp = round(sense.get_temperature(), 2)
    #rounding the temp_value that will be used to light up pixels
    temp_value = round(temp)
    #setting temerature to light up equivalent amount of pixels
    pixels = [red if i < temp_value else white for i in range(64)]
    sense.set_pixels(pixels)
    #display message in text box
    return("Temperature is: " + str(temp))
 
@app.route("/humidity/")
def humidity():
    humidity = round(sense.get_humidity(), 2)
    #multiplying range of sense_hat pixels to display equivalent
    #amount of blue pixels in humidity percentage
    humidity_value = 64 * humidity / 100
    pixels = [blue if i < humidity_value else white for i in range(64)]
    sense.set_pixels(pixels)
    return("Humidity is: " + str(humidity))
    
@app.route("/pressure/")
def pressure():
    pressure = round(sense.get_pressure(), 2)
    #dividing by 20 to display the pixels in sense_hat range 
    #max 1260hPa / 20 = 63 pixels
    pressure_value = pressure / 20
    pixels = [green if i < pressure_value else white for i in range(64)]
    sense.set_pixels(pixels)
    return("Pressure is: " + str(pressure))
 
'''
@app.route to accept multiple actions
before each action, board is cleared
and specified action is applied
'''
@app.route("/<action>")
def action(action):
    if action == "green":
        sense.clear(green)
        return("Green")
    elif action == "red":
        sense.clear(red)
        return("Red")
    elif action == "blue":
        sense.clear(blue)
        return("Blue")
    elif action == "pink":
        sense.clear(pink)
        return("Pink")
    elif action == "smile":
        sense.clear()
        sense.show_message(":)")
        return("Smile :)")
    elif action == "heart":
        sense.clear()
        heart()
        return("Heart <3")
    elif action == "off":
        sense.clear()
        return("Screen reset")
'''
    These possible actions are redundand
    as they have their own dedicated app routes above
    
    elif action == "temp":
        print("Inside temp action")
        sense.clear()
        temp()
    elif action == "pressure":
        sense.clear()
        pressure()
    elif action == "humidity":
        sense.clear()
        humidity()
'''
        
if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 5002, debug = True)