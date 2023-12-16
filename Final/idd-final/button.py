from __future__ import print_function
import qwiic_button 
import time
import sys

def buttonPress():
    my_button = qwiic_button.QwiicButton()

    if my_button.begin() == False:
        print("\nThe Qwiic Button isn't connected to the system. Please check your connection", \
            file=sys.stderr)
        return
    print("\nButton ready!")
    
    while True:   
        if my_button.is_button_pressed() == True:
            print("\nThe button is pressed!")

        else:    
            print("\nThe button is not pressed!")
            
        time.sleep(0.02)

if __name__ == '__main__':
    try:
        buttonPress()
    except (KeyboardInterrupt, SystemExit) as exErr:
        print("\nEnding Example 1")
        sys.exit(0)