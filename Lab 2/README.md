# Interactive Prototyping: The Clock of Pi

Does it feel like time is moving strangely during this semester?

For our first Pi project, we will pay homage to the [timekeeping devices of old](https://en.wikipedia.org/wiki/History_of_timekeeping_devices) by making simple clocks.

It is worth spending a little time thinking about how you mark time, and what would be useful in a clock of your own design.



## Overview
For this assignment, you are going to 

A) [Connect to your Pi](#part-a)  

B) [Try out cli_clock.py](#part-b) 

C) [Set up your RGB display](#part-c)

D) [Try out clock_display_demo](#part-d) 

E) [Modify the code to make the display your own](#part-e)

F) [Make a short video of your modified barebones PiClock](#part-f)

G) [Sketch and brainstorm further interactions and features you would like for your clock for Part 2.](#part-g)


## Part A. 

Completed.


## Part B. 

Completed.


## Part C. 

Completed


## Part D. 
### Set up the Display Clock Demo
Work on `screen_clock.py`, try to show the time by filling in the while loop (at the bottom of the script where we noted "TODO" for you). You can use the code in `cli_clock.py` and `stats.py` to figure this out.
#### Default clock and image display
<img width="400" alt="Part D" src="https://github.com/kapa-moon/Interactive-Lab-Hub/assets/100012430/fb13cc6d-8da0-4b97-9565-dfd0d9eb8953">


### How to Edit Scripts on Pi
Option 1. One of the ways for you to edit scripts on Pi through terminal is using [`nano`](https://linuxize.com/post/how-to-use-nano-text-editor/) command. You can go into the `screen_clock.py` by typing the follow command line:
```
(venv) pi@raspberrypi:~/Interactive-Lab-Hub/Lab 2 $ nano screen_clock.py
```
You can make changes to the script this way, remember to save the changes by pressing `ctrl-o` and press enter again. You can press `ctrl-x` to exit the nano mode. There are more options listed down in the terminal you can use in nano.

Option 2. Another way for you to edit scripts is to use VNC on your laptop to remotely connect your Pi. Try to open the files directly like what you will do with your laptop and edit them. Since the default OS we have for you does not come up a python programmer, you will have to install one yourself otherwise you will have to edit the codes with text editor. [Thonny IDE](https://thonny.org/) is a good option for you to install, try run the following command lines in your Pi's ternimal:

  ```
  pi@raspberrypi:~ $ sudo apt install thonny
  pi@raspberrypi:~ $ sudo apt update && sudo apt upgrade -y
  ```

Now you should be able to edit python scripts with Thonny on your Pi.

Option 3. A nowadays often preferred method is to use Microsoft [VS code to remote connect to the Pi](https://www.raspberrypi.com/news/coding-on-raspberry-pi-remotely-with-visual-studio-code/). This gives you access to a fullly equipped and responsive code editor with terminal and file browser.  

Pro Tip: Using tools like [code-server](https://coder.com/docs/code-server/latest) you can even setup a VS Code coding environment hosted on your raspberry pi and code through a web browser on your tablet or smartphone! 

## Part E.
### Modify the barebones clock to make it your own
#### Circadian Rhythm and Time Perception
<img width="400" alt="Part D" src = "https://github.com/kapa-moon/Interactive-Lab-Hub/assets/100012430/3d6890a9-72ca-4376-832b-682a8f1869d8" width = 400>

Does time have to be linear?  How do you measure a year? [In daylights? In midnights? In cups of coffee?](https://www.youtube.com/watch?v=wsj15wPpjLY)

Can you make time interactive? You can look in `screen_test.py` for examples for how to use the buttons.

Please sketch/diagram your clock idea. (Try using a [Verplank digram](http://www.billverplank.com/IxDSketchBook.pdf)!

**We strongly discourage and will reject the results of literal digital or analog clock display.**


\*\*\***A copy of your code should be in your Lab 2 Github repo.**\*\*\*

After you edit and work on the scripts for Lab 2, the files should be upload back to your own GitHub repo! You can push to your personal github repo by adding the files here, commiting and pushing.

```
(venv) pi@raspberrypi:~/Interactive-Lab-Hub/Lab 2 $ git add .
(venv) pi@raspberrypi:~/Interactive-Lab-Hub/Lab 2 $ git commit -m 'your commit message here'
(venv) pi@raspberrypi:~/Interactive-Lab-Hub/Lab 2 $ git push
```

After that, Git will ask you to login to your GitHub account to push the updates online, you will be asked to provide your GitHub user name and password. Remember to use the "Personal Access Tokens" you set up in Part A as the password instead of your account one! Go on your GitHub repo with your laptop, you should be able to see the updated files from your Pi!


## Part F. 
## Make a short video of your modified barebones PiClock

\*\*\***Take a video of your PiClock.**\*\*\*

[Video Link](https://drive.google.com/file/d/1aIAAsFDrw_CKgRw7gMzVpnvwm9Xlb0LT/view?usp=drive_link)

<img width="300" alt="Screenshot 2023-09-19 at 11 18 19 AM" src="https://github.com/kapa-moon/Interactive-Lab-Hub/assets/100012430/9f1b1dd8-60ee-4262-8453-f37b180fbb28">

<img width="300" alt="Screenshot 2023-09-19 at 11 18 28 AM" src="https://github.com/kapa-moon/Interactive-Lab-Hub/assets/100012430/5a13b576-4362-40ff-95f2-3603b39851eb">

<img width="300" alt="Screenshot 2023-09-19 at 11 18 41 AM" src="https://github.com/kapa-moon/Interactive-Lab-Hub/assets/100012430/ee13c487-563b-49db-89bf-555d266bdf47">

<img width="300" alt="Screenshot 2023-09-19 at 11 18 51 AM" src="https://github.com/kapa-moon/Interactive-Lab-Hub/assets/100012430/77e17a23-d7bd-42c9-9205-3ce3bfd37ab9">

## Part G. 
#### Sketch and brainstorm further interactions and features you would like for your clock for Part 2.
#### Synthesized in Part 2

# Prep for Part 2

1. Pick up remaining parts for kit on Thursday lab class. Check the updated [parts list inventory](partslist.md) and let the TA know if there is any part missing.
  

2. Look at and give feedback on the Part G. for at least 2 other people in the class (and get 2 people to comment on your Part G!)

# Lab 2 Part 2

Pull Interactive Lab Hub updates to your repo.

Modify the code from last week's lab to make a new visual interface for your new clock. You may [extend the Pi](Extending%20the%20Pi.md) by adding sensors or buttons, but this is not required.

#### Augment perception of time with colors

<img alt="color time" src="https://github.com/kapa-moon/Interactive-Lab-Hub/assets/100012430/54dd289e-cffc-411b-885a-4e1af307f75c" width="300">

- A day is filled with the happenings, the activities we individuals carry out. Different people may have different perceptions of "the progress" of the day. People who work during evening times may not call 6 pm "the end of the day". People who enjoy night life may call 8pm "the right time to begin".

- Coloring of different times of the day gives a sense of the actual hour and provide a mapping between "perception" and "reality".
  
- In the video, I prototyped a routine clock based on my normal schedule as a student.
  
[Video Link](https://drive.google.com/file/d/1JU2mjb2XlyPsxoDlZaJgv7Gap6eOMK94/view?usp=drive_link)

