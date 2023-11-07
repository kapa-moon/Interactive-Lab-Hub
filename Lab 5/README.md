# Observant Systems

**NAMES OF COLLABORATORS HERE**


For lab this week, we focus on creating interactive systems that can detect and respond to events or stimuli in the environment of the Pi, like the Boat Detector we mentioned in lecture. 
Your **observant device** could, for example, count items, find objects, recognize an event or continuously monitor a room.

This lab will help you think through the design of observant systems, particularly corner cases that the algorithms need to be aware of.

## Prep

1.  Install VNC on your laptop if you have not yet done so. This lab will actually require you to run script on your Pi through VNC so that you can see the video stream. Please refer to the [prep for Lab 2](https://github.com/FAR-Lab/Interactive-Lab-Hub/blob/-/Lab%202/prep.md#using-vnc-to-see-your-pi-desktop).
2.  Install the dependencies as described in the [prep document](prep.md). 
3.  Read about [OpenCV](https://opencv.org/about/),[Pytorch](https://pytorch.org/), [MediaPipe](https://mediapipe.dev/), and [TeachableMachines](https://teachablemachine.withgoogle.com/).
4.  Read Belloti, et al.'s [Making Sense of Sensing Systems: Five Questions for Designers and Researchers](https://www.cc.gatech.edu/~keith/pubs/chi2002-sensing.pdf).

### For the lab, you will need:
1. Pull the new Github Repo
1. Raspberry Pi
1. Webcam 

### Deliverables for this lab are:
1. Show pictures, videos of the "sense-making" algorithms you tried.
1. Show a video of how you embed one of these algorithms into your observant system.
1. Test, characterize your interactive device. Show faults in the detection and how the system handled it.

## Overview
Building upon the paper-airplane metaphor (we're understanding the material of machine learning for design), here are the four sections of the lab activity:

A) [Play](#part-a)

B) [Fold](#part-b)

C) [Flight test](#part-c)

D) [Reflect](#part-d)

---

### Part A
### Play with different sense-making algorithms.

#### Pytorch for object recognition

For this first demo, you will be using PyTorch and running a MobileNet v2 classification model in real time (30 fps+) on the CPU. We will be following steps adapted from [this tutorial](https://pytorch.org/tutorials/intermediate/realtime_rpi.html).

![torch](Readme_files/pyt.gif)


To get started, install dependencies into a virtual environment for this exercise as described in [prep.md](prep.md).

Make sure your webcam is connected.

You can check the installation by running:

```
python -c "import torch; print(torch.__version__)"
```

If everything is ok, you should be able to start doing object recognition. For this default example, we use [MobileNet_v2](https://arxiv.org/abs/1801.04381). This model is able to perform object recognition for 1000 object classes (check [classes.json](classes.json) to see which ones.

Start detection by running  

```
python infer.py
```

The first 2 inferences will be slower. Now, you can try placing several objects in front of the camera.

Read the `infer.py` script, and get familiar with the code. You can change the video resolution and frames per second (fps). You can also easily use the weights of other pre-trained models. You can see examples of other models [here](https://pytorch.org/tutorials/intermediate/realtime_rpi.html#model-choices). 


### Machine Vision With Other Tools
The following sections describe tools ([MediaPipe](#mediapipe) and [Teachable Machines](#teachable-machines)).

#### MediaPipe

A recent open source and efficient method of extracting information from video streams comes out of Google's [MediaPipe](https://mediapipe.dev/), which offers state of the art face, face mesh, hand pose, and body pose detection.

![Media pipe](Readme_files/mp.gif)

To get started, install dependencies into a virtual environment for this exercise as described in [prep.md](prep.md):

Each of the installs will take a while, please be patient. After successfully installing mediapipe, connect your webcam to your Pi and use **VNC to access to your Pi**, open the terminal, and go to Lab 5 folder and run the hand pose detection script we provide:
(***it will not work if you use ssh from your laptop***)


```
(venv-ml) pi@ixe00:~ $ cd Interactive-Lab-Hub/Lab\ 5
(venv-ml) pi@ixe00:~ Interactive-Lab-Hub/Lab 5 $ python hand_pose.py
```

Try the two main features of this script: 1) pinching for percentage control, and 2) "[Quiet Coyote](https://www.youtube.com/watch?v=qsKlNVpY7zg)" for instant percentage setting. Notice how this example uses hardcoded positions and relates those positions with a desired set of events, in `hand_pose.py`. 

Consider how you might use this position based approach to create an interaction, and write how you might use it on either face, hand or body pose tracking.

(You might also consider how this notion of percentage control with hand tracking might be used in some of the physical UI you may have experimented with in the last lab, for instance in controlling a servo or rotary encoder.)



#### Teachable Machines
Google's [TeachableMachines](https://teachablemachine.withgoogle.com/train) is very useful for prototyping with the capabilities of machine learning. We are using [a python package](https://github.com/MeqdadDev/teachable-machine-lite) with tensorflow lite to simplify the deployment process.

![Tachable Machines Pi](Readme_files/tml_pi.gif)

To get started, install dependencies into a virtual environment for this exercise as described in [prep.md](prep.md):

After installation, connect your webcam to your Pi and use **VNC to access to your Pi**, open the terminal, and go to Lab 5 folder and run the example script:
(***it will not work if you use ssh from your laptop***)


```
(venv-tml) pi@ixe00:~ Interactive-Lab-Hub/Lab 5 $ python tml_example.py
```


Next train your own model. Visit [TeachableMachines](https://teachablemachine.withgoogle.com/train), select Image Project and Standard model. The raspberry pi 4 is capable to run not just the low resource models. Second, use the webcam on your computer to train a model. *Note: It might be advisable to use the pi webcam in a similar setting you want to deploy it to improve performance.*  For each class try to have over 150 samples, and consider adding a background or default class where you have nothing in view so the model is trained to know that this is the background. Then create classes based on what you want the model to classify. Lastly, preview and iterate. Finally export your model as a 'Tensorflow lite' model. You will find an '.tflite' file and a 'labels.txt' file. Upload these to your pi (through one of the many ways such as [scp](https://www.raspberrypi.com/documentation/computers/remote-access.html#using-secure-copy), sftp, [vnc](https://help.realvnc.com/hc/en-us/articles/360002249917-VNC-Connect-and-Raspberry-Pi#transferring-files-to-and-from-your-raspberry-pi-0-6), or a connected visual studio code remote explorer).
![Teachable Machines Browser](Readme_files/tml_browser.gif)
![Tensorflow Lite Download](Readme_files/tml_download-model.png)

Include screenshots of your use of Teachable Machines, and write how you might use this to create your own classifier. Include what different affordances this method brings, compared to the OpenCV or MediaPipe options.

#### (Optional) Legacy audio and computer vision observation approaches
In an earlier version of this class students experimented with observing through audio cues. Find the material here:
[Audio_optional/audio.md](Audio_optional/audio.md). 
Teachable machines provides an audio classifier too. If you want to use audio classification this is our suggested method. 

In an earlier version of this class students experimented with foundational computer vision techniques such as face and flow detection. Techniques like these can be sufficient, more performant, and allow non discrete classification. Find the material here:
[CV_optional/cv.md](CV_optional/cv.md).

### Part B
### Construct a simple interaction.

* Pick one of the models you have tried, and experiment with prototyping an interaction.
* This can be as simple as the boat detector showen in a previous lecture from Nikolas Matelaro.
* Try out different interaction outputs and inputs.


**\*\*\*Describe and detail the interaction, as well as your experimentation here.\*\*\***
 
 I picked the Teachable Machine as the model for prototyping an interaction.

 Model trained for the Bunny to become a traffic police officer.
 The rule is explained in the figure below.
 <img alt="Traffic-Police-Hand-Signals" src="https://github.com/kapa-moon/Interactive-Lab-Hub/assets/100012430/99db4e26-a807-4dc2-ab64-b4beecdda9a7" width="400">

Begin the training on the Teachable Machine interface:
<img width="600" alt="Screenshot 2023-11-07 at 8 25 47 AM" src="https://github.com/kapa-moon/Interactive-Lab-Hub/assets/100012430/dc5cdedb-76af-4caf-9ea5-debc5af0ace9">
<img width="332" alt="trainBunny1" src="https://github.com/kapa-moon/Interactive-Lab-Hub/assets/100012430/9e68a736-ad5f-4172-87e9-10036c5fcf9a">

After training:

Output signal: 1) stop_all 2) stop_front 3) stop_left

<img width="150" alt="stop3" src="https://github.com/kapa-moon/Interactive-Lab-Hub/assets/100012430/d4b223dd-29a3-4a71-a3fe-394e7a13e3b3">
<img width="150" alt="stop2" src="https://github.com/kapa-moon/Interactive-Lab-Hub/assets/100012430/453bf0fb-dbe5-4fd8-9c44-0bd40a1c55b8">
<img width="150" alt="stop1" src="https://github.com/kapa-moon/Interactive-Lab-Hub/assets/100012430/ba37f7ac-6a06-43bb-9e06-1cb8da0f9eb4">





### Part C
### Test the interaction prototype

<img width ="600" src="https://github.com/kapa-moon/Interactive-Lab-Hub/assets/100012430/8c0d8805-58ae-478d-a143-2bac93ab6489">
<img width ="600" src="https://github.com/kapa-moon/Interactive-Lab-Hub/assets/100012430/ba039461-5839-4b1d-8a76-a92e9532c42a">
<img width ="600" src="https://github.com/kapa-moon/Interactive-Lab-Hub/assets/100012430/197b59f2-8195-4a47-b5bb-c755f0b15327">


Now flight test your interactive prototype and **note down your observations**:
For example:
1. When it is supposed to do?
1. When does it fail?
1. When it fails, why does it fail?
1. Based on the behavior you have seen, what other scenarios could cause problems?

**\*\*\*Think about someone using the system. Describe how you think this will work.\*\*\***
1. Are they aware of the uncertainties in the system?
1. How bad would they be impacted by a miss classification?
1. How could change your interactive system to address this?
1. Are there optimizations you can try to do on your sense-making algorithm.

In this setting, the interaction is dealing with an authentication problem. False verification will potentially let uncleared individuals (spies, enemies, random neighbors, etc) enter the Forte town (which was introduced in Lab 4). Adding several "no-pass" categories can improve the performance compared to binary classificaiton. It could also be addressed with a "back-up" passcode, but this is less ideal. (Note that each passsheet is unique and only the entering villager has the complete information of the passsheet (i.e. the Sheet Ghost and its 2D coordinate on the sheet.) At the same time, the concept of zero-knowledge proof could be confusing and villagers need to understand it to a practical extent.



### Part D
### Characterize your own Observant system

Now that you have experimented with one or more of these sense-making systems **characterize their behavior**.
During the lecture, we mentioned questions to help characterize a material:
* What can you use X for?
* What is a good environment for X?
* What is a bad environment for X?
* When will X break?
* When it breaks how will X break?
* What are other properties/behaviors of X?
* How does X feel?


* Retrain the model to classify a valid Sheet Ghost, in addition to the gesture function.
  <img width="1352" alt="trainGhost1" src="https://github.com/kapa-moon/Interactive-Lab-Hub/assets/100012430/357c2e7b-748b-4fa4-96b4-e350cab2f1f8">
  
  <img width="200" alt="ghost6" src="https://github.com/kapa-moon/Interactive-Lab-Hub/assets/100012430/281aef88-9cfa-4b79-8f80-834a11ff2f6e">
  <img width="200" alt="ghost2" src="https://github.com/kapa-moon/Interactive-Lab-Hub/assets/100012430/cba1c6dd-9892-4b18-b186-bcd16539654c">

  * Several "partial" categories are added to improve the performance of classification (compared to pass/no-pass binary classification).

<img width="200" alt="ghost5" src="https://github.com/kapa-moon/Interactive-Lab-Hub/assets/100012430/47e365a9-9896-4494-8600-b95f601921e9">
<img width="200" alt="ghost4" src="https://github.com/kapa-moon/Interactive-Lab-Hub/assets/100012430/04a45bbb-3719-46c0-a771-3496e0de6103">
<img width="200" alt="ghost3" src="https://github.com/kapa-moon/Interactive-Lab-Hub/assets/100012430/2d475e93-2237-4751-93f2-e554cf0317f2">

  * Test the model with the setting of the Forte town's Defense Wall.
  
    <img width="200" alt="theWall" src="https://github.com/kapa-moon/Interactive-Lab-Hub/assets/100012430/00c58617-3214-4b07-be42-f21cce36b2fe">


[Test Process](https://drive.google.com/file/d/1wu_QEWYs669UqLiSY8HTz5xt0zNIm1aZ/view?usp=sharing)


### Part 2.

Following exploration and reflection from Part 1, finish building your interactive system, and demonstrate it in use with a video.

[Video Link](https://drive.google.com/file/d/1Z99x21RU-i3uAEOOp3XYs6GpVRxNSQ4n/view?usp=sharing)

**\*\*\*Include a short video demonstrating the finished result.\*\*\***
