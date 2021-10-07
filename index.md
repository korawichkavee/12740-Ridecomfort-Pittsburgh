# Ride comfort of different modes of transportation in Pittsburgh

**Members: Korawich Kavee, Jacobo Kirsch Tornell, Guillermo Montero, and Albin Wells**

Video Link:

Website Link: [Github Project](https://korawichkavee.github.io/12740-Ridecomfort-Pittsburgh/)

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

**In order to take relevant measurements, the sensors were fixed to each vehicle while in motion, near the human position (where someone normally sits/stands on) to take samples during the trip and assess the differences between types of transportation.**

**Note that a more in depth description of these sensors is outlined later, below.**

## Progress
### Current Progress
Our main goal at the moment is to successfully code and build the circuit for the sensors to the RaspberryPi. Our vibration sensor was not functional so we had to buy a new one, which was finally delivered on 10/4.

We are still working out bugs in our code because the vibration sensor (accelerometer) measurements are not outputting correctly.


10/5/2021 update

We tried to run the accelerometer and sound sensor that arrived yesterday with the Raspberry Pi, and we are having trouble in interpreting the data that the AD converter is giving us. Although we detect variation in the voltage when the sensors are stimulated, we still cannot convert that parameter into a magnitude of our interest, like m/s2 or g for acceleration and db for sound.

We saw a transformation function for the accelerometer provided by the manufacturer (Adafruit) but is in terms of the digital raw values, which are very erratic and we suspect that something is not working properly with those values. 


10/6/2021 update

After checking connections and circuit wiring, testing sensors, and checking code, we still could not resolve the issues we were seeing yesterday. However, we soldered the accelerometer to the pins to ensure a strong, sustained electrical connection between the sensor and the breadboard. This seems to finally have resolved the issue, as we obtained values that made sense: a range of positive and negative accelerations when we vibrated the sensor.

We also began to callibrate the accelerometer.


10/7/2021 update



### Future Plan
After the code and circuit has been fine-tuned, we need to test our sensors on rides on each mode of transport. Then, we will need to post-process data to compare the comfort levels form each ride.

## Methods


## Experiment and Results


## Discussion


## Sensors Used - In Depth
| Sensor | Description | Physical Principle | Characteristics | Additional Notes |
| ----------- | ----------- | ----------- | ----------- | ----------- |
| Microphone | Adafruit AGC Electret Microphone Amplifier - MAX9814 [^1] | The working principle of an electret condenser microphone is that the diaphragm acts as one plate of a capacitor. Vibrations produce changes in the distance between the diaphragm and the back plate. ... This change in voltage is amplified by the FET and the audio signal appears at the output, after a dc-blocking capacitor. [^2] | <ul><li>Supply Voltage: 2.7v-5.5v @ 3mA current</li><li>Output: 2Vpp on 1.25V bias</li></li><li>Frequency Response: 20Hz - 20 KHz</ul> | Add notes here |
| Accelerometer | Add description here | Add the phyisical principle of the sensor here | Add specs here | Add notes here |
| Temperature and Humidity | Add description here | Add the phyisical principle of the sensor here | Add specs here | Add notes here |



-------------------------------------------------------------------
## References and Footnotes
[^1]: https://www.cuidevices.com/product-spotlight/electret-condenser-microphones
[^2]: https://learn.adafruit.com/adafruit-agc-electret-microphone-amplifier-max9814/
