#!/usr/bin/env python
#-----------------------------------------------------------------------------
# qwiic_proximity_ex1.py
#
# Simple Example for the Qwiic Proximity Device
#------------------------------------------------------------------------
#
# Written by  SparkFun Electronics, May 2019
# 
# This python library supports the SparkFun Electroncis qwiic 
# qwiic sensor/board ecosystem on a Raspberry Pi (and compatable) single
# board computers. 
#
# More information on qwiic is at https://www.sparkfun.com/qwiic
#
# Do you like this library? Help support SparkFun. Buy a board!
#
#==================================================================================
# Copyright (c) 2019 SparkFun Electronics
#
# Permission is hereby granted, free of charge, to any person obtaining a copy 
# of this software and associated documentation files (the "Software"), to deal 
# in the Software without restriction, including without limitation the rights 
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell 
# copies of the Software, and to permit persons to whom the Software is 
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all 
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR 
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, 
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE 
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER 
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, 
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE 
# SOFTWARE.
#==================================================================================
# Example 1
#
# - Setup the device
# - Output the proximity value

from __future__ import print_function
import qwiic_proximity
import time
import sys

import board
from adafruit_apds9960.apds9960 import APDS9960


class Sensors:
    def __init__(self):
        # Sensor two
        i2c = board.I2C()
        self.sensor_TWO = APDS9960(i2c)
        self.sensor_TWO.enable_proximity = True
  
        # Sensor one
        self.sensor_ONE = qwiic_proximity.QwiicProximity()

        if self.sensor_ONE.connected == False:
            print("The Qwiic Proximity device isn't connected to the system. Please check your connection", \
                file=sys.stderr)
            return

        self.sensor_ONE.begin()
        
        self.prev_ONE = False
        self.prev_TWO = False
        
        self.last_to_change = 1
        
    def is_there_one(self):
        value_ONE = self.sensor_ONE.proximity
        
        curr_value = value_ONE > 50
        
        print("SENSOR TWO IS", curr_value)
        
        # if (curr_value != self.prev_ONE):
        #     self.change_ONE = time.now()
        #     self.prev_ONE = curr_value
        
        return curr_value

    def is_there_two(self):
        value_TWO = self.sensor_TWO.proximity
        
        curr_value = value_TWO > 50
        
        print("SENSOR ONE IS", curr_value)
        
        # if (curr_value != self.prev_ONE):
        #     self.change_TWO = time.now()
        #     self.prev_TWO =curr_value
        
        return curr_value
    
    def last_to_change(self):
        if (self.change_TWO > self.change_ONE):
            return 2
        else:
            return 1
        
    
    
        
    


if __name__ == '__main__':
    try:
        sensors = Sensors()
        sensors.runExample()
    except (KeyboardInterrupt, SystemExit) as exErr:
        print("\nEnding Example 1")
        sys.exit(0)