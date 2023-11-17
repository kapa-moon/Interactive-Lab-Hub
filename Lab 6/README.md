# Little Interactions Everywhere

**NAMES OF COLLABORATORS HERE**

## Prep

1. Pull the new changes from the class interactive-lab-hub. (You should be familiar with this already!)
2. Install [MQTT Explorer](http://mqtt-explorer.com/) on your laptop. If you are using Mac, MQTT Explorer only works when installed from the [App Store](https://apps.apple.com/app/apple-store/id1455214828).
3. Readings before class:
   * [MQTT](#MQTT)
   * [The Presence Table](https://dl.acm.org/doi/10.1145/1935701.1935800) and [video](https://vimeo.com/15932020)


## Overview

The point of this lab is to introduce you to distributed interaction. We have included some Natural Language Processing (NLP) and Generation (NLG) but those are not really the emphasis. Feel free to dig into the examples and play around the code which you can integrate into your projects if wanted. However, we want to emphasize that the grading will focus on your ability to develop interesting uses for messaging across distributed devices. Here are the four sections of the lab activity:

A) [MQTT](#part-a)

B) [Send and Receive on your Pi](#part-b)

C) [Streaming a Sensor](#part-c)

D) [The One True ColorNet](#part-d)

E) [Make It Your Own](#part-)

## Part 1.

### Part A
### MQTT

MQTT is a lightweight messaging portal invented in 1999 for low bandwidth networks. It was later adopted as a defacto standard for a variety of [Internet of Things (IoT)](https://en.wikipedia.org/wiki/Internet_of_things) devices. 

#### The Bits

* **Broker** - The central server node that receives all messages and sends them out to the interested clients. Our broker is hosted on the far lab server (Thanks David!) at `farlab.infosci.cornell.edu/8883`. Imagine that the Broker is the messaging center!
* **Client** - A device that subscribes or publishes information to/on the network.
* **Topic** - The location data gets published to. These are *hierarchical with subtopics*. For example, If you were making a network of IoT smart bulbs this might look like `home/livingroom/sidelamp/light_status` and `home/livingroom/sidelamp/voltage`. With this setup, the info/updates of the sidelamp's `light_status` and `voltage` will be store in the subtopics. Because we use this broker for a variety of projects you have access to read, write and create subtopics of `IDD`. This means `IDD/ilan/is/a/goof` is a valid topic you can send data messages to.
*  **Subscribe** - This is a way of telling the client to pay attention to messages the broker sends out on the topic. You can subscribe to a specific topic or subtopics. You can also unsubscribe. Following the previouse example of home IoT smart bulbs, subscribing to `home/livingroom/sidelamp/#` would give you message updates to both the light_status and the voltage.
* **Publish** - This is a way of sending messages to a topic. Again, with the previouse example, you can set up your IoT smart bulbs to publish info/updates to the topic or subtopic. Also, note that you can publish to topics you do not subscribe to. 


**Important note:** With the broker we set up for the class, you are limited to subtopics of `IDD`. That is, to publish or subcribe, the topics will start with `IDD/`. Also, setting up a broker is not much work, but for the purposes of this class, you should all use the broker we have set up for you!


#### Useful Tooling

Debugging and visualizing what's happening on your MQTT broker can be helpful. We like [MQTT Explorer](http://mqtt-explorer.com/). You can connect by putting in the settings from the image below.


![input settings](imgs/mqtt_explorer.png?raw=true)


Once connected, you should be able to see all the messages under the IDD topic. , go to the **Publish** tab and try publish something! From the interface you can send and plot messages as well. Remember, you are limited to subtopics of `IDD`. That is, to publish or subcribe, the topics will start with `IDD/`.


<img width="1026" alt="Screen Shot 2022-10-30 at 10 40 32 AM" src="https://user-images.githubusercontent.com/24699361/198885090-356f4af0-4706-4fb1-870f-41c15e030aba.png">



### Part B
### Send and Receive on your Pi

[sender.py](./sender.py) and and [reader.py](./reader.py) show you the basics of using the mqtt in python. Let's spend a few minutes running these and seeing how messages are transferred and shown up. Before working on your Pi, keep the connection of `farlab.infosci.cornell.edu/8883` with MQTT Explorer running on your laptop.

**Running Examples on Pi**

* Install the packages from `requirements.txt` under a virtual environment:

  ```
  pi@raspberrypi:~/Interactive-Lab-Hub $ source circuitpython/bin/activate
  (circuitpython) pi@raspberrypi:~/Interactive-Lab-Hub $ cd Lab\ 6
  (circuitpython) pi@raspberrypi:~/Interactive-Lab-Hub/Lab 6 $ pip install -r requirements.txt
  ...
  ```
* Run `sender.py`, fill in a topic name (should start with `IDD/`), then start sending messages. You should be able to see them on MQTT Explorer.

  ```
  (circuitpython) pi@raspberrypi:~/Interactive-Lab-Hub/Lab 6 $ python sender.py
  >> topic: IDD/AlexandraTesting
  now writing to topic IDD/AlexandraTesting
  type new-topic to swich topics
  >> message: testtesttest
  ...
  ```
* Run `reader.py`, and you should see any messages being published to `IDD/` subtopics. Type a message inside MQTT explorer and see if you can receive it with `reader.py`.

  ```
  (circuitpython) pi@raspberrypi:~ Interactive-Lab-Hub/Lab 6 $ python reader.py
  ...
  ```

<img width="890" alt="Screen Shot 2022-10-30 at 10 47 52 AM" src="https://user-images.githubusercontent.com/24699361/198885135-a1d38d17-a78f-4bb2-91c7-17d014c3a0bd.png">


**\*\*\*Consider how you might use this messaging system on interactive devices, and draw/write down 5 ideas here.\*\*\***

1. Under a social context, take the system as a shortcut to send a "code word" to your friends. A "code word" might mean "change the signal" please.
   
   <img width="300" alt="Screenshot 2023-11-17 at 1 46 30 PM" src="https://github.com/kapa-moon/Interactive-Lab-Hub/assets/100012430/dbaf60e2-403b-4d60-ba51-61dc37c7c137">

2. An easier version of the two-person mode of Nintendo game Cup Head.

  <img width="300" alt="Screenshot 2023-11-17 at 1 46 13 PM" src="https://github.com/kapa-moon/Interactive-Lab-Hub/assets/100012430/95900408-2cd8-4ad0-a74a-3de88a0a7fb6">

3. Tic-tac-toe

   <img width="300" alt="Screenshot 2023-11-17 at 1 46 21 PM" src="https://github.com/kapa-moon/Interactive-Lab-Hub/assets/100012430/f2c28dd1-5533-4b5a-b886-d0c1eb541241">

4. A communication system that respond to the request from your roommate when you're in your room and don't want to get out of bed.

   <img width="300" alt="Screenshot 2023-11-17 at 1 46 39 PM" src="https://github.com/kapa-moon/Interactive-Lab-Hub/assets/100012430/1bcb84fd-2c06-412e-8513-a0883689c448">

5. A controller of an investment game. Game rule: A starts with $10. A sends B $X. B will have $3X (triple). B sends back $Y as they want to.

   <img width="300" alt="Screenshot 2023-11-17 at 1 46 34 PM" src="https://github.com/kapa-moon/Interactive-Lab-Hub/assets/100012430/8ebd91e4-5fb0-42e0-811d-468b36720cea">

### Part C
### Streaming a Sensor

We have included an updated example from [lab 4](https://github.com/FAR-Lab/Interactive-Lab-Hub/tree/Fall2021/Lab%204) that streams the [capacitor sensor](https://learn.adafruit.com/adafruit-mpr121-gator) inputs over MQTT. 

Plug in the capacitive sensor board with the Qwiic connector. Use the alligator clips to connect a Twizzler (or any other things you used back in Lab 4) and run the example script:

<p float="left">
<img src="https://cdn-learn.adafruit.com/assets/assets/000/082/842/large1024/adafruit_products_4393_iso_ORIG_2019_10.jpg" height="150" />
<img src="https://cdn-shop.adafruit.com/970x728/4210-02.jpg" height="150">
<img src="https://cdn-learn.adafruit.com/guides/cropped_images/000/003/226/medium640/MPR121_top_angle.jpg?1609282424" height="150"/>
<img src="https://media.discordapp.net/attachments/679721816318803975/823299613812719666/PXL_20210321_205742253.jpg" height="150">
</p>

 ```
 (circuitpython) pi@raspberrypi:~ Interactive-Lab-Hub/Lab 6 $ python distributed_twizzlers_sender.py
 ...
 ```

**\*\*\*Include a picture of your setup here: what did you see on MQTT Explorer?\*\*\***
<img width="500" alt="Screenshot 2023-11-17 at 12 54 38 AM" src="https://github.com/kapa-moon/Interactive-Lab-Hub/assets/100012430/c3be6a6b-22c3-4d20-b4ff-18c8243192c8">


**\*\*\*Pick another part in your kit and try to implement the data streaming with it.\*\*\***

I used the button and implemented the data streaming following the capacitor sensor example. Here is what shows on the MQTT Explorer.

<img width="600" alt="button" src="https://github.com/kapa-moon/Interactive-Lab-Hub/assets/100012430/51dc3aed-3e9d-4a12-8602-413a74ab2b6b">


<img width="600" alt="Screenshot 2023-11-16 at 10 49 07 PM" src="https://github.com/kapa-moon/Interactive-Lab-Hub/assets/100012430/3f49258e-cde2-4fc6-bd70-2e18a3186530">


### Part D
### The One True ColorNet

It is with great fortitude and resilience that we shall worship at the altar of the *OneColor*. Through unity of the collective RGB, we too can find unity in our heart, minds and souls. With the help of machines, we can overthrow the bourgeoisie, get on the same wavelength (this was also a color pun) and establish [Fully Automated Luxury Communism](https://en.wikipedia.org/wiki/Fully_Automated_Luxury_Communism).

The first step on the path to *collective* enlightenment, plug the [APDS-9960 Proximity, Light, RGB, and Gesture Sensor](https://www.adafruit.com/product/3595) into the [MiniPiTFT Display](https://www.adafruit.com/product/4393). You are almost there!

<p float="left">
  <img src="https://cdn-learn.adafruit.com/assets/assets/000/082/842/large1024/adafruit_products_4393_iso_ORIG_2019_10.jpg" height="150" />
  <img src="https://cdn-shop.adafruit.com/970x728/4210-02.jpg" height="150">
  <img src="https://cdn-shop.adafruit.com/970x728/3595-03.jpg" height="150">
</p>


The second step to achieving our great enlightenment is to run `color.py`. We have talked about this sensor back in Lab 2 and Lab 4, this script is similar to what you have done before! Remember to activate the `circuitpython` virtual environment you have been using during this semester before running the script:

 ```
 (circuitpython) pi@raspberrypi:~ Interactive-Lab-Hub/Lab 6 $ systemctl stop mini-screen.service
 (circuitpython) pi@raspberrypi:~ Interactive-Lab-Hub/Lab 6 $ python color.py
 ...
 ```

By running the script, wou will find the two squares on the display. Half is showing an approximation of the output from the color sensor. The other half is up to the collective. Press the top button to share your color with the class. Your color is now our color, our color is now your color. We are one.

(A message from the previous TA, Ilan: I was not super careful with handling the loop so you may need to press more than once if the timing isn't quite right. Also, I haven't load-tested it so things might just immediately break when everyone pushes the button at once.)

The result of showing color

<img width="300" alt="color" src="https://github.com/kapa-moon/Interactive-Lab-Hub/assets/100012430/9cd88e7b-abc3-417d-8816-b7b413b8485a">



### Part E
### Make it your own

Find at least one class (more are okay) partner, and design a distributed application together based on the exercise we asked you to do in this lab.

**\*\*\*1. Explain your design\*\*\*** 

The purpose of the design is to offer two music buddies an convinient way to study cords progressions and improvise collaboratively with the device.
(Piano keyboards are not always available. Not to mention two co-exsiting keyboards.) The physical user interface will also make the chords usable in a more intuitive and novice-friendly way.

**\*\*\*2. Diagram the architecture of the system.\*\*\*** 

<img src="https://github.com/kapa-moon/Interactive-Lab-Hub/assets/100012430/d0ea7d41-aa03-422f-b02f-4c2476ec9fd7" width=300>

The following will take the 1-4-5 (C-F-G) progression as an example.

The music box concept diagram:

<img width="300" alt="Screenshot 2023-11-17 at 12 53 47 PM" src="https://github.com/kapa-moon/Interactive-Lab-Hub/assets/100012430/006c7f66-fe69-48ac-bc27-42e41dd389ba">

The concept is to make music instrument interface "malleable" and suitable for people from different music backgrounds (e.g. traning in different instruments such as guitar and piano, or no music training at all). For example, piano people might be more used to parallel keyboard, while guitar people hold the instrument in a totally different way. The position of each key can be changed to make the music box more friendly to different types of hand postures.

"Guitar-version arrangement"

<img width="300" alt="Screenshot 2023-11-17 at 12 53 55 PM" src="https://github.com/kapa-moon/Interactive-Lab-Hub/assets/100012430/eb05d317-97cd-4736-9835-ea0d07db7a5c">
<img width="300" alt="Screenshot 2023-11-17 at 12 58 45 PM" src="https://github.com/kapa-moon/Interactive-Lab-Hub/assets/100012430/eecba2b5-9bfd-4949-bd4e-eb9a7727aba7">


"Piano-version arrangement"

<img width="300" alt="Screenshot 2023-11-17 at 12 54 00 PM" src="https://github.com/kapa-moon/Interactive-Lab-Hub/assets/100012430/f6675b85-1e25-4b1b-89c5-11897e3518f2">
<img width="300" alt="Screenshot 2023-11-17 at 12 59 18 PM" src="https://github.com/kapa-moon/Interactive-Lab-Hub/assets/100012430/549cc0d8-4f39-4fe7-bb5d-5d9635ee7924">



**\*\*\*3. Build a working prototype of the system.\*\*\*** 

Process:
Communicate over the MQTT Explorer example:

<img width="600" alt="Screenshot 2023-11-16 at 11 30 31 PM" src="https://github.com/kapa-moon/Interactive-Lab-Hub/assets/100012430/59734bde-5082-407d-8d1b-1823e022c646">


**\*\*\*4. Document the working prototype in use.\*\*\*** It may be helpful to record a Zoom session where you should the input in one location clearly causing response in another location.

[Video Link](https://drive.google.com/file/d/16Ds7MKKXLaF9_PG5947COl0ZWBNEkKR4/view?usp=sharing)
<!--**\*\*\*5. BONUS (Wendy didn't approve this so you should probably ignore it)\*\*\*** get the whole class to run your code and make your distributed system BIGGER.-->

