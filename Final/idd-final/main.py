
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
from oled import writeToScreen
from proximity import Sensors
import qwiic_proximity
import time
import sys

# button lib
import qwiic_button 

import board
import busio
import adafruit_mpr121
import ssl
from speechRec import SpeechRecognizer
from tts import createAudio
import pygame


i2c = busio.I2C(board.SCL, board.SDA)
mpr121 = adafruit_mpr121.MPR121(i2c)
# for i in range(12):
# 	if mpr121[i].value: val = f"Twizzler {i} touched!"; print(val)
    
button = qwiic_button.QwiicButton()
speechRecognizer = SpeechRecognizer()
pygame.mixer.init()
sound_welcome_ONE = pygame.mixer.Sound('welcome_ONE.wav')
sound_welcome_TWO = pygame.mixer.Sound('welcome_TWO.wav')
sound_keys = pygame.mixer.Sound('reminder_key.wav')
sound_id = pygame.mixer.Sound('reminder_id.wav')
sound_good = pygame.mixer.Sound('reminder_good.wav')
sound_confirm = pygame.mixer.Sound('confirm.wav')
sound_wait = pygame.mixer.Sound('wait.wav')
sensors = Sensors()

sound_reminder_ONE = pygame.mixer.Sound('section_one.wav') # Some BS variables!!!
sound_reminder_TWO = pygame.mixer.Sound('section_two.wav')

# section = 0


def runBox():
    
    def welcome_sec(section):
        global sound_reminder_ONE, sound_reminder_TWO
        if (section == 1):
            sound_welcome = sound_welcome_ONE
            file_name = "section_one"
        else:
            sound_welcome = sound_welcome_TWO
            file_name = "section_two"
            
        sound_welcome.play()

        print('button pressed!')
        
        text = speechRecognizer.getTranscript(writeToScreen, button)
        sound_wait.play()
        createAudio("You forgot your "+text, file_name)
        
        if (section == 1):
            sound_reminder_ONE = pygame.mixer.Sound(file_name+'.wav')
        else:
            sound_reminder_TWO = pygame.mixer.Sound(file_name+'.wav')

        print("The text is: ", text)
        sound_confirm.play()
        
    
    # global section
    print("\nSparkFun Proximity Sensor VCN4040 Example 1\n")
    oProx = qwiic_proximity.QwiicProximity()
    

    if oProx.connected == False:
        print("The Qwiic Proximity device isn't connected to the system. Please check your connection", \
            file=sys.stderr)
        return
    oProx.begin()
    
    section = 1
    going_out = False
    setting_finished = True
    
    while True:
        if button.is_button_pressed() == True:
            # going_out = True
            print(section)
            time.sleep(1)
            
            if section == 3:
                setting_finished = True
               

            else:            
                welcome_sec(section)
                section += 1
        

        for i in range(12):            
            if mpr121[i].value: 
                going_out = True
        
        done = False
            
        if going_out == True:  
            while (True):

                if (sensors.is_there_one()):
                    sound_reminder_ONE.play()
                    time.sleep(3)
                    
                if (sensors.is_there_two()):
                    sound_reminder_TWO.play()
                    time.sleep(3)
                    
                if not sensors.is_there_one() and not sensors.is_there_two():
                    writeToScreen("Bye-bye! Have a good one!")
                    sound_good.play()
                    time.sleep(10)
                    going_out = False
                    done = True
                    break
        
        # if done == True:
        #     break
                    
                
        # going_out = False
        #         if proxValue > 100: sound_keys.play(); time.sleep(3)
        #         elif proxValue > 41: sound_id.play(); time.sleep(3)
        #         if proxValue <= 41: sound_good.play(); time.sleep(5); print("DONE!"); done = True; return   
            
        # else:
        #     going_out = False
        #     proxValue = oProx.get_proximity()
            
        #     for i in range(12):
        #         if mpr121[i].value: 
        #             going_out = True
        #     # First condition to trigger the thing
            
        #     if going_out == True:
        #         done = False 
                
        #         while (~done):
        #             proxValue = oProx.get_proximity()
        #             print(proxValue)
        #             if proxValue > 100: sound_keys.play(); time.sleep(3)
        #             elif proxValue > 41: sound_id.play(); time.sleep(3)
        #             if proxValue <= 41: sound_good.play(); time.sleep(5); print("DONE!"); done = True; return

            # if abs(proxValue - prevValue) > 10: # change detected
            #     if proxValue > 100: sound_keys.play(); time.sleep(3)
            #     elif proxValue > 60: sound_id.play(); time.sleep(3)
            #     if proxValue < 60: sound_good.play(); time.sleep(5); return
                
            
            # for i in range(12):
            #     if mpr121[i].value: 
            #         going_out = True
            #         #    val = f"Twizzler {i} touched!"
            #         #    print(val)
        
            # if going_out:
            #         if proxValue > 100: sound_keys.play(); time.sleep(3)
            #         elif proxValue > 60: sound_id.play(); time.sleep(3)
            #         elif proxValue < 60: sound_good.play(); time.sleep(5); return

            time.sleep(.4)
    


if __name__ == '__main__':
    try:
        runBox()
    except (KeyboardInterrupt, SystemExit) as exErr:
        print("\nEnding Example 1")
        sys.exit(0)