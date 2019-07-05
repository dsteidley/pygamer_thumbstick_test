"""
thumbstick_test.py
Hardware: Adafruit PyGamer Advanced
IDE: Mu-editor
Author: David Steidley
Date: 5 July 2019

Description:
I wanted to play around with using the thumbstick.  In the end I came up with a script
that allows you to scale and flip, as well as apply an offset to the value that comes
out of the ADC.  Using the Plotter in Mu was nice in allowing me to visualize the output.
It wasn't until I applied a 1/16 factor that the results were fairly smooth.

Another goal of the project was to convert this to an digital stick.  Most of the games
I would like to write do not require the analog information, just the direction.  Which,
by the way, has it's X and Y axis swapped.  I checked the GitHub repo and it looks like
this issue is being addressed.

Copyright (c) 2019 David Steidley

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

#import the modules
import board
import analogio
import time

#set up the ADC to the correct pins
adc = analogio.AnalogIn(board.JOYSTICK_X)

# Flip, Scale, and Offset values obtained from ADC
polarity = -1
scale = .0625
offset = 2056

# Smooth the output
sample_count = 10

# Convert the signal to digital-ish?
# If so, set up a null spot that will represent 0
read_as_analog = 1
x_null = 1000
x_null_neg = x_null * -1

if read_as_analog:
    """
    Empty buffer, take several readings and compute average, then apply scale and offset
    """
    while True:
        x_buffer = 0.0
        for i in range(0,sample_count):
            x_buffer = x_buffer + adc.value
            time.sleep(0.01)
        x_avg = x_buffer / sample_count
        x_val = (x_avg * polarity * scale) + offset
        print((x_val,))
        time.sleep(0.1)
else:
    """
    Take a reading and convert it to -1, 0, or 1
    """
    while True:
        x_buffer = (adc.value * polarity * scale) + offset
        if x_buffer > x_null:
            x_val = 1
        elif x_buffer < x_null_neg:
            x_val = -1
        else:
            x_val = 0
        print((x_val,))
        time.sleep(0.1)