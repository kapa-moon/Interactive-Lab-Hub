# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT
from __future__ import print_function
import qwiic_joystick

import board
import busio
import adafruit_ssd1306

from luma.core.interface.serial import i2c
from luma.core.render import canvas
from luma.oled.device import ssd1306

import qwiic_oled_display
import sys

    
#proximity
import time
from adafruit_apds9960.apds9960 import APDS9960

# Create the I2C interface.
i2c = busio.I2C(board.SCL, board.SDA)

#proximity
i2c = board.I2C()
apds = APDS9960(i2c)

apds.enable_proximity = True

# OLED Display
myOLED = qwiic_oled_display.QwiicOledDisplay()
myOLED.begin()

myOLED.clear(myOLED.PAGE)  #  Clear the display's buffer
myOLED.print("Hello World")
myOLED.display()
print(myOLED.is_connected())

    
# Create the SSD1306 OLED class.
# The first two parameters are the pixel width and pixel height.  Change these
# to the right size for your display!
oled = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c)
# serial = i2c(port=1, address=0x3C)
# oled = ssd1306(serial,width=128, height=32, rotate=2) 

# Helper function to draw a circle from a given position with a given radius
# This is an implementation of the midpoint circle algorithm,
# see https://en.wikipedia.org/wiki/Midpoint_circle_algorithm#C_example for details
def draw_circle(xpos0, ypos0, rad, col=1):
    x = rad - 1
    y = 0
    dx = 1
    dy = 1
    err = dx - (rad << 1)
    while x >= y:
        oled.pixel(xpos0 + x, ypos0 + y, col)
        oled.pixel(xpos0 + y, ypos0 + x, col)
        oled.pixel(xpos0 - y, ypos0 + x, col)
        oled.pixel(xpos0 - x, ypos0 + y, col)
        oled.pixel(xpos0 - x, ypos0 - y, col)
        oled.pixel(xpos0 - y, ypos0 - x, col)
        oled.pixel(xpos0 + y, ypos0 - x, col)
        oled.pixel(xpos0 + x, ypos0 - y, col)
        if err <= 0:
            y += 1
            err += dy
            dy += 2
        if err > 0:
            x -= 1
            dx += 2
            err += dx - (rad << 1)


# Joystick
joy_pos = 0
joy_move = False
joy_count = 0
joy_x = 0
prev_joy_x = 0
# myJoystick = qwiic_joystick.QwiicJoystick()
# myJoystick.begin()
def runJoystick():

	print("\nSparkFun qwiic Joystick   Example 1\n")
	myJoystick = qwiic_joystick.QwiicJoystick()
    

	if myJoystick.connected == False:
		print("The Qwiic Joystick device isn't connected to the system. Please check your connection", \
			file=sys.stderr)
		return

	myJoystick.begin()

	print("Initialized. Firmware Version: %s" % myJoystick.version)

	while True:

		print("X: %d, Y: %d, Button: %d" % ( \
					myJoystick.horizontal, \
					myJoystick.vertical, \
					myJoystick.button))

		time.sleep(.5)


while True:
    joy_move = True
    print(apds.proximity)
    current_prox = apds.proximity
    if current_prox > 100:
        print("warning!")
        myOLED.clear(myOLED.PAGE)  #  Clear the display's buffer
        myOLED.print("Win!")
        # draw.text((x, 15), "to start the game.", font=font, fill="#FFFFFF")
        myOLED.display()
    
    runJoystick()
    
    elif joy_count > 3:
        myOLED.clear(myOLED.PAGE)  #  Clear the display's buffer
        myOLED.print("Win!!")
        # draw.text((x, 15), "to start the game.", font=font, fill="#FFFFFF")
        myOLED.display()

    time.sleep(0.2)   
# Joystick

# if __name__ == '__main__':
# 	try:
# 		runJoystick()
# 	except (KeyboardInterrupt, SystemExit) as exErr:
# 		print("\nEnding Example 1")
# 		sys.exit(0)
