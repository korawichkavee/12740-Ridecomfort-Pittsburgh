# 12740-Ridecomfort-Pittsburgh
Ride comfort of different modes of transportation in Pittsburgh
You can click this link to the report page
https://korawichkavee.github.io/12740-Ridecomfort-Pittsburgh/

# Introduction and Motivation
Depending on how close you live to CMU, getting to campus can take many forms. Regardless of which mode of transport is used, each has its benefits. Taking a car might save time, taking a bus might save money, and riding a bike or scooter might be the most practical. While these measures can be quantified based on time, cost, or both, one of the most critical aspects of these rides cannot be easily quantified: comfort. Attempting to measure the comfort of each of these rides is crucial in ultimately understanding the full range of benefits and disadvantages of each most of transportation. This analysis will use quantitative data to evaluate the comfort of each mode of public or private transport to campus.

# Goals
We will quantify the comfort of a ride based on three primary factors:
  1. Vibrations within the vehicle
  2. Sound volumes throughout the ride
  3. Temperature and humidity of the vehicle

We will conduct sensing for three modes of transportation:
  1. Bus 
  2. Car
  3. Scooter/bike 
  
For each measured aspect and mode of transportation, we will analyze and compare obtained values to determine the comfort levels of each ride.

# Sensors
We will use the following sensors to measure data:
  1. Vibration sensor to measure vibrations/accelerations.
  2. Sound detection sensor to measure the noise of the vehicle.
  3. Temperature and humidity sensor to measure temperature and humidity.
We will fix our sensors to each vehicle while in motion and take samples.
Note that a more in depth description of these sensors is outlined later, below.

# Progress
## Current Progress
Our main goal at the moment is to successfully code and build the circuit for the sensors to the RaspberryPi. Our vibration sensor was not functional so we had to buy a new one, which was finally delivered on 10/4.
We are still working out bugs in our code because the vibration sensor (accelerometer) measurements are not outputting correctly.

10/5/2021 update

We tried to run the accelerometer and sound sensor that arrived yesterday with the Raspberry Pi, and we are having trouble in interpreting the data that the AD converter is giving us. Although we detect variation in the voltage when the sensors are stimulated, we still cannot convert that parameter into a magnitude of our interest, like m/s2 or g for acceleration and db for sound.

We saw a transformation function for the accelerometer provided by the manufacturer (Adafruit) but is in terms of the digital raw values, which are very erratic and we suspect that something is not working properly with those values. 

## Future Plan
After the code and circuit has been fine-tuned, we need to test our sensors on rides on each mode of transport. Then, we will need to post-process data to compare the comfort levels form each ride.

# Methods


# Experiment and Results


# Discussion


# Sensors Used - In Depth
