import time
import board
import neopixel
import displayio
from adafruit_bitmap_font import bitmap_font
from adafruit_display_text import label

# Boiler Plate NeoPixel setup from Adafruit examples:
# On CircuitPlayground Express, and boards with built in status NeoPixel -> board.NEOPIXEL
# Otherwise choose an open pin connected to the Data In of the NeoPixel strip, i.e. board.D1
pixel_pin = board.NEOPIXEL

# The number of NeoPixels
num_pixels = 5

# The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
# For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.
ORDER = neopixel.GRB

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.2, auto_write=False,
                           pixel_order=ORDER)

# I wanted to put something on the display besides the standard
# CircuitPython status text
# Boiler Plate Displayio setup from Adafruit Examples
display = board.DISPLAY
text = "Cylon searching ..."
font = bitmap_font.load_font("fonts/Helvetica-Bold-16.bdf")
color = 0xFF00FF
text_area = label.Label(font, text=text, color=color)
text_area.x = 0
text_area.y = 60
display.show(text_area)

#Set up some values for eye color and scan speed
color = (255,0,255) # The center of the eye
dim_color = (8,0,0) # The edge of the eye
delay = .125

# Make the "eye" do it's thing
while True:
   # Travel to the right
    for i in range(0, num_pixels):
        pixels.fill((0,0,0))
        pixels[i] = color
        # I want the center of the eye to go edge to edge
        # so, do not display the sides of the eye if they are
        # outside the range of the neopixels.
        if i > 0:
            pixels[i - 1] = dim_color
        if i < num_pixels - 1:
            pixels[i + 1] = dim_color
        pixels.show()
        time.sleep(delay)

    # Travel to the left
    for i in range(num_pixels -2, 0, -1):
        pixels.fill((0,0,0))
        pixels[i] = color
        pixels[i + 1] = dim_color
        pixels[i - 1] = dim_color
        pixels.show()
        time.sleep(delay)