# Observant Systems

For lab this week, we focus on creating interactive systems that can detect and respond to events or stimuli in the environment of the Pi, like the Boat Detector we mentioned in lecture. 
Your **observant device** could, for example, count items, find objects, recognize an event or continuously monitor a room.



A) [Play](#part-a)

B) [Fold](#part-b)

C) [Flight test](#part-c)

D) [Reflect](#part-d)

---

### Part A
### Play with different sense-making algorithms.

#### Pytorch for object recognition

#### MediaPipe

#### Teachable Machines

### Part B
### Construct a simple interaction.

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
