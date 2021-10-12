# Ride comfort of different modes of transportation in Pittsburgh

**Members: Korawich Kavee, Jacobo Kirsch Tornell, Guillermo Montero, and Albin Wells**

Video Link: [Ride Comfort Video](https://www.youtube.com/watch?v=bcNrlpfi9SA&ab_channel=KorawichKavee)

Website Link: [Github Project](https://korawichkavee.github.io/12740-Ridecomfort-Pittsburgh/)

Source Code: [Ride Comfort Code](https://github.com/korawichkavee/12740-Ridecomfort-Pittsburgh/tree/main/python%20code%20program)

## Introduction and Motivation
There are many travel options to and from the Carnegie Mellon University Pittsburgh Campus. Depending on how close you live to CMU, your mode of transportation, or your budget, a specific option usually fits your needs. For instance, taking a car might save time, but riding the bus might save money, and riding a bike or scooter might be more practical. While these measures can be quantified by time, cost, or both, one of the most critical aspects to consider that different transportation options cannot easily quantify: **comfort**. Attempting to measure the comfort of each of these rides is crucial in ultimately understanding the full range of benefits and downfalls of most transportation options.

The objective is to create a framework to better estimate comfort using different variables related to it. Hence, the outcomes will aid in determining better the advantages and disadvantages of different modes of transportation. Furthermore, based on the results, one will be able to ascertain the gaps in accessibility of transportation to campus when the privilege to own any vehicle, including bikes and scooters, is lacking. Thus, the following analysis will use quantitative data obtained from an array of sensors to evaluate the comfort of each mode of public or private transport to and from campus.


## Goals
The overall goal of this project is to create a framework to measure passenger comfort from different types of transportation. In order to quantify the comfort of a ride based on three primary factors:
  1. Vibrations and movement within the vehicle
  2. Noises present throughout the ride
  3. Temperature and humidity of the vehicle

To understand the benefits and hindrances of different types of transportation, three different vehicles were sensed to obtain an array of results. The three modes of transportation are the bus (encompassing the public transportation type of vehicles), car (comprising private ride and ride-share options), and scooter (which embodies alternatives to traditional transport, including the bicycle). 
  
For each measured aspect and type of transportation, there will be an analysis and comparison discussion based on obtained values to quantify the comfort levels of a *ride*.

## Sensors
The following sensors were chosen to measure data, and get an assessment of comfort that can be quantifiable.

### Vibration and Movement
One of the main aspects that one can attribute to comfort is a smooth ride. That is why adding a vibration sensor to measure accelerations differences during the traveling time would be able to determine if the ride was pleasant.

### Noise and Sound 
Who has not had the annoying situation of having to hear a car blasting off music while going to a place. Noises, especially loud and sharp, irritate someone very easily. Hence, detecting the noise while travelling can also quantify comfort. 

### Temperature and humidity 
Temperature and humidity can affect how a human feels during a ride. For instance, a warm and humid sensation would make someone start to sweat more easily and make a ride unpleasant. Thus, using sensor to measure temperature and humidity would give us an outcome that one can measure if the temperature and humidity is inside the human comfort location.

### Sensor Images
The microphone (left) and accelerometer (right) are shown in the figure below.

![The microphone (left) and accelerometer (right)!](https://github.com/korawichkavee/12740-Ridecomfort-Pittsburgh/blob/gh-pages/footage%20and%20picture/0577d09c-f731-45a8-9509-2cb6770de479.jpeg)

The temperature and humidity sensor is show in the photo below.

![The temperature and humidity sensor!](https://github.com/korawichkavee/12740-Ridecomfort-Pittsburgh/blob/gh-pages/footage%20and%20picture/Screen%20Shot%202021-10-12%20at%2012.13.28%20PM.png)

**In order to take relevant measurements, the sensors were fixed to each vehicle while in motion, near the human position (where someone normally sits/stands on) to take samples during the trip and assess the differences between types of transportation.**

**Note that a more in depth description of these sensors is outlined later, below.**

## Progress
### Current Progress
Our main goal at the moment is to successfully code and build the circuit for the sensors to the RaspberryPi. Our vibration sensor was not functional so we had to buy a new one, which was finally delivered on 10/4.

We are still working out bugs in our code because the vibration sensor (accelerometer) measurements are not outputting correctly.


*10/5/2021 update*

We tried to run the accelerometer and sound sensor that arrived yesterday with the Raspberry Pi, and we are having trouble in interpreting the data that the AD converter is giving us. Although we detect variation in the voltage when the sensors are stimulated, we still cannot convert that parameter into a magnitude of our interest, like m/s2 or g for acceleration and db for sound.

We saw a transformation function for the accelerometer provided by the manufacturer (Adafruit) but is in terms of the digital raw values, which are very erratic and we suspect that something is not working properly with those values. 


*10/6/2021 update*

After checking connections and circuit wiring, testing sensors, and checking code, we still could not resolve the issues we were seeing yesterday. However, we soldered the accelerometer to the pins to ensure a strong, sustained electrical connection between the sensor and the breadboard. This seems to finally have resolved the issue, as we obtained values that made sense: a range of positive and negative accelerations when we vibrated the sensor.

We also callibrated the z-axis of the accelerometer.


*10/7/2021 update*

We successfully wired the sound sensor (microphone): identifying and addressing potential issues with sampling frequency associated with the sensor. We then calibrated the sensor output to a loudness. Another calibration had to be done to convert the micropone output into decibels, which was particularly challenging. This was validated by comparing sensor output to measured sound from an iPhone app.


*10/9/2021 update*

We went out and successfully obtained data from each mode of transportation today. We measured sound, vibration, temperature, and humidity of the bus, car, and scooter over a designated route. We initially had some trouble with the portable battery connecting to the RaspberryPi, but we replaced a faulty USB-c cable and it worked out well in the end.

## Methods

### Phenomena of Interest
As mentioned above, we are interested in quantifying and comparing the comfort of various modes of transportation. We identified a few contributing factors to comfort, which include noise level, vibrations, temperature, and humidity. Ultimately, these are the phenomena we are sensing.

The temperature and humidity are both relatively static signals. Especially considering the short time scale of our study (~2 to 8 minutes) these signals are unlikely to change, and, if they do, they are unlikely to change by very much. Thus, a very low sampling frequency can adequetely capture and characterize these signals. In fact, sampling one point might be sufficient to understand the temperature and humidity in each mode of transportation, although it is still better to obtain multiple samples throoughout the ride. Theoretically, depending on the weather conditions, the temperature in a car could change with heating or air conditioning over the 2-8 minute time period of our test.

Sensing vibrations is much more challenging. This is a dynamic, aperiod signal. While we expect the signal to be 'centered' around 1g, sporadic motion from the vehicles causes it to vary at random intervals. These variations tend to be a function of external sources, such as potholes and road conditions, stops and traffic lights, other cars, driving habits, etc. Thus, we cannot expect a consistent, periodic signal. Instead, we sample the signal at a rate high enough to capture these sudden variations in acceleration and use this to quantify the vibrations during the ride.

Sound sensing poses and entirely new set of challenges. Sound signals are dynamic, periodic signals that cover a very large range of frequencies (up to and above 1kHz). Due to limitations of the sensors and equipment, sampling rate is severely limited to the point where effectively all sound signals are aliased. Thus, trying to determine the sound wave frequencies is futile. Instead, we focus our efforts on measuring volume: magnitude of the sound waves. This magnitude is converted into decibels to easily compare to human comfort levels.

### Sensors Used - In Depth
| Sensor | Description | Physical Principle | Characteristics | Additional Notes |
| ----------- | ----------- | ----------- | ----------- | ----------- |
| Microphone | Adafruit AGC Electret Microphone Amplifier - MAX9814 [^1] | The working principle of an electret condenser microphone is that the diaphragm acts as one plate of a capacitor. Vibrations produce changes in the distance between the diaphragm and the back plate. ... This change in voltage is amplified by the FET and the audio signal appears at the output, after a dc-blocking capacitor. [^2] | <ul><li>Supply Voltage: 2.7v-5.5v @ 3mA current</li><li>Output: 2Vpp on 1.25V bias</li></li><li>Frequency Response: 20Hz - 20 KHz</ul> | Add notes here |
| Accelerometer | Add description here | Add the phyisical principle of the sensor here | Add specs here | Add notes here |
| Temperature and Humidity | Add description here | Add the phyisical principle of the sensor here | Add specs here | Add notes here |

The final sensor setup with the RaspberryPi is displayed in the figure below.

![Final sensor and RaspberryPi setup!](https://github.com/korawichkavee/12740-Ridecomfort-Pittsburgh/blob/gh-pages/footage%20and%20picture/WhatsApp%20Image%202021-10-08%20at%203.13.27%20PM.jpeg)

### Signal Conditioning and Processing
Describe the signal conditioning and processing procedure

LETS ALSO TALK ABOUT THE SAMPLING FREQUENCY AND HOW THAT WAS CHOSEN

## Experiment and Results
We measured the comfort of each type of ride for a stretch of road from the corner of S Negley Ave and Fifth Ave to the corner of Morewood Ave and Fifth Ave. This is a common route for students from Shadyside to travel to school. To carry out our tests, we securely fastened the RaspberryPi and breadboard with sensors in an open box. For each mode of tranportation, we placed and firmly held or taped the box in place on the ground between the feet of where we would sit or stand. We started and ended sampling at the same location for each mode of transportation, so the amount of time varied for slower modes of transportation (the scooter especially). In each case, we did not talk or make noise during testing so that any sound levels were from the surrounding environment.

### Noise Results



### Vibrations Results



### Temperature and Humidity Results



## Discussion
Discuss the insights from the project




-------------------------------------------------------------------
## References and Footnotes
[^1]: https://www.cuidevices.com/product-spotlight/electret-condenser-microphones
[^2]: https://learn.adafruit.com/adafruit-agc-electret-microphone-amplifier-max9814/
