# Ride comfort of different modes of transportation in Pittsburgh

**Members: Korawich Kavee, Jacobo Kirsch Tornell, Guillermo Montero, and Albin Wells**

## TO DO: (1) Finish sensor spec sheet (with citations), (2) add graphs and discussion on results, (3) add final conclusions, (4) read over full report and review writing and formatting

To delete later: [Canvas project rubric link](https://canvas.cmu.edu/courses/25498/discussion_topics/362646)

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
One of the main aspects that one can attribute to comfort is a smooth ride. That is why adding a vibration sensor to measure accelerations differences during the traveling time would be able to determine if the ride was pleasant. The accelerometer we used is shown in Figure 1 below.

### Noise and Sound 
Who has not had the annoying situation of having to hear a car blasting off music while going to a place. Noises, especially loud and sharp, irritate someone very easily. Hence, detecting the noise while travelling can also quantify comfort. The microphone sensor measuring these noises can be seen in Figure 1 below. 

### Temperature and humidity 
Temperature and humidity can affect how a human feels during a ride. For instance, a warm and humid sensation would make someone start to sweat more easily and make a ride unpleasant. Thus, using sensor to measure temperature and humidity would give us an outcome that one can measure if the temperature and humidity is inside the human comfort location (See Figure 2 below).

### Sensor Images
*Figure 1: The microphone (left) and accelerometer (right)*

![The microphone (left) and accelerometer (right)!](https://github.com/korawichkavee/12740-Ridecomfort-Pittsburgh/blob/gh-pages/footage%20and%20picture/0577d09c-f731-45a8-9509-2cb6770de479.jpeg)

*Figure 2: The temperature and humidity sensor*

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

The temperature and humidity are both relatively static signals. Especially considering the short time scale of our study (~2 to 5 minutes) these signals are unlikely to change, and, if they do, they are unlikely to change by very much. Thus, a very low sampling frequency can adequetely capture and characterize these signals. In fact, sampling one point might be sufficient to understand the temperature and humidity in each mode of transportation, although it is still better to obtain multiple samples throoughout the ride. Theoretically, depending on the weather conditions, the temperature in a car could change with heating or air conditioning over the 2-5 minute time period of our test. During this analysis, it is important to keep in mind the optimal human comfort zome between 22 C to 27 C and 40-60% relative humidity. [^1]

Sensing vibrations is much more challenging. This is a dynamic, aperiod signal. While we expect the signal to be 'centered' around 1g, sporadic motion from the vehicles causes it to vary at random intervals. These variations tend to be a function of external sources, such as potholes and road conditions, stops and traffic lights, other cars, driving habits, etc. Thus, we cannot expect a consistent, periodic signal. Instead, we sample the signal at a rate high enough to capture these sudden variations in acceleration and use this to quantify the vibrations during the ride.

Sound sensing poses and entirely new set of challenges. Sound signals are dynamic, periodic signals that cover a very large range of frequencies (up to and above 1kHz). Due to limitations of the sensors and equipment, sampling rate is severely limited to the point where effectively all sound signals are aliased. Thus, trying to determine the sound wave frequencies is futile. Instead, we focus our efforts on measuring volume: magnitude of the sound waves. This magnitude is converted into decibels to easily compare to human comfort levels.

### Sensors Used - In Depth
An outline of the sensor descriptions and specifications is show in Table 1. The final setup of the sensor with the RaspberryPi is shown in Figure 3 below.

*Table 1: Sensor descriptions and specifications*
| Sensor | Description | Physical Principle | Characteristics | Additional Notes |
| ----------- | ----------- | ----------- | ----------- | ----------- |
| Microphone | Adafruit AGC Electret Microphone Amplifier - MAX9814 [^2] | The working principle of an electret condenser microphone is that the diaphragm acts as one plate of a capacitor. Vibrations produce changes in the distance between the diaphragm and the back plate. ... This change in voltage is amplified by the FET and the audio signal appears at the output, after a dc-blocking capacitor. [^3] | <ul><li>Supply Voltage: 2.7v-5.5v @ 3mA current</li><li>Output: 2Vpp on 1.25V bias</li></li><li>Frequency Response: 20Hz - 20 KHz</ul> | Add notes here |
| Accelerometer | Add description here | Add the phyisical principle of the sensor here | Add specs here | Add notes here |
| Temperature and Humidity | Add description here | Add the phyisical principle of the sensor here | Add specs here | Add notes here |

*Figure 3: The final sensor setup with the RaspberryPi*

![Final sensor and RaspberryPi setup!](https://github.com/korawichkavee/12740-Ridecomfort-Pittsburgh/blob/gh-pages/footage%20and%20picture/WhatsApp%20Image%202021-10-08%20at%203.13.27%20PM.jpeg)

### Signal Conditioning and Processing
In order to collect, condition, and process signal data, we set up a Python code. This source code can be accessed through the link at the top of this page. The smart comfort file is used to run our experiment, while the test codes are only used for initial calibration and testing of individual sensors. When running the experiment, we first create a new csv file to store the time and all sensor outputs. Then, we create a button parameter that links to the RaspberryPi to control the start and stop of sensing on the breadboard, instead of solely through the computer. While the temperature and humidity sensor gives a digital output and connects straight to the RaspberryPi, the sound and vibration sensors are passed through an A/D converter before reaching the RaspberryPi.

We define a samply frequency of 20 Hz, which actually samples at 6.8 Hz due to limitations of the hardware and CPU. While this sampling frequency is not nearly high enough to detect sound freqeuncies and might miss some subtle vibrations, the frequency still captures the general trends of the rides and the magnitudes of sounds and accelerations. Ultimately, this is sufficient for capturing the volume of noise, which is a more critical aspect of assessing comfort from sound. As temperature and humidity are static signals, this sampling rate is appropriate for those signals.

The accelerometer was then calibrated to convert raw data into actual acceleration. This was done using three known points by placing the accelerometer flat facing upwards, sideways, and upside down. The z-axis value of the accelerometer was converted in relation to gravity in each position: g, 0, and -g, respectively. The microphone was similarly calibrated by testing the sensor at a constant sound loudness. A smartphone was used to measure the volume of sound in decibels at various loudnesses, and compared to the raw data. A linear function was used to derive a conversion from the raw data into a decibel output for volume.

When running the code, the RaspberryPi takes the values from each sensor and writes it into our initially created file. Then, it waits for the time period determined by the frequency, and repeats the process immediately after this wait. When the button is pressed again or the program is stopped on the computer, the RaspberryPi stops taking measurements. The file is closed and saved into the desired folder, and we have the obtained data for each sensor in a csv file format.

**Reminder: to see the source code used, follow the link at the top of this page**

## Experiment and Results
We measured the comfort of each type of ride for a stretch of road from the corner of S Negley Ave and Fifth Ave to the corner of Morewood Ave and Fifth Ave. This is a common route for students from Shadyside to travel to school. To carry out our tests, we securely fastened the RaspberryPi and breadboard with sensors in an open box. For each mode of tranportation, we placed and firmly held or taped the box in place on the ground between the feet of where we would sit or stand. We started and ended sampling at the same location for each mode of transportation, so the amount of time varied for slower modes of transportation (the scooter especially). In each case, we did not talk or make noise during testing so that any sound levels were from the surrounding environment.

### Noise Results
Figure 4 (below) displays the raw data results for the noise during the trips for each mode of transportation. While the low sampling rate causes the signal to be very erratic and difficult to draw conclusions to, the following Figure 5 shows a moving window average of the raw data using 136 points (20 seconds). In Figure 5, a few trends can be easily observed.

First and foremost, the length of each graph shows how long each of the rides took. The result is not at all surprising: the car was the fastest, taking about 120 seconds, while the bus was only marginally slower, taking about 135 seconds. The scooter, however, took much longer to reach the destination: over 260 seconds. While this observation has little to do with the sensor itself, this is the reason the plots all vary in length and it is important to keep in mind.

From Figure 5, we can also make deductions about the level of noise on each mode of transportation. The car is evidently the quietest, hovering around 60 dB during the ride. The bus was noticeably louder than the car, with most values just below the 80 dB range. Finally, the noise from the scooter was by far the most inconsistent. This is likely due to the fact that the noise from the scooter comes almost exclusively from the surrounding environment, not anything heppning 'inside' the vehicle. Thus, it depends largely on the traffic around it. At times, the moving window average reached over 120 dB and below 40 dB. During the full ride, however, the scooter was overall the loudest mode of transportation with an average of **THISAVERAGENUMBER** dB.

*Figure 4: Volume of sounds for each mode of transportation during a ride from S Negley Ave to Morewood Ave on Fifth Ave*
![db record!](https://github.com/korawichkavee/12740-Ridecomfort-Pittsburgh/blob/gh-pages/footage%20and%20picture/Sound%20Records.png)

*Figure 5: Moving window average of the volume of sounds while riding each mode of transportation*
![SMA db record!](https://github.com/korawichkavee/12740-Ridecomfort-Pittsburgh/blob/gh-pages/footage%20and%20picture/SMA_20%20SoundRecords.png)

### Vibrations Results
Figure 6 (below) shows raw data results for the amplitude of accelerations during the trip for each mode of transportation. Figure 7 shows the acceleration for each mode of transportation during the trip on the frequency domain. As can be clearly seen, the scooter has by far the most vibrations. The ride is much 'bumpier' than for the bus or car, with amplitudes frequently eclipsing 1g. Particularly interesting is the lapse in vibrations on the scooter at around 100 seconds. This period of low vibrations reflects a red light, when the scooter was stopped for a short period of time. There is no discernable difference in vibrations on the car or the bus: both are relatively low with a few spikes where acceleration peaks. **WRITE SOMETHING ABOUT FREQUENCY DOMAIN GRAPH**

*Figure 6: Acceleration for each mode of transportation during a ride from S Negley Ave to Morewood Ave on Fifth Ave*
![Acceleration record!](https://github.com/korawichkavee/12740-Ridecomfort-Pittsburgh/blob/gh-pages/footage%20and%20picture/Acceleration%20Records.png)

*Figure 7: Amplitude of acceleration on the frequency domain for each mode of transportation*
![Acceleration Fourier!](https://github.com/korawichkavee/12740-Ridecomfort-Pittsburgh/blob/gh-pages/footage%20and%20picture/Frequency%20Content%202.png)

### Temperature and Humidity Results
In Figure 8, the humidity for each mode of transportation during the ride is shown. Note that this experiment was carried out shortly after a brief rain, so the outdoor humidity was high. In Figure 8, the scooter reflects this high outdoor humidity. The relative humidity of over 70% is likely precisely the outdoor humidity, which confirms the notion that the comfort of the scooter depends largely on the weather. In this case, high humidity makes the scooter ride less comfortable. By contrast, the car and bus rides had substantially lower relative humidity values–around 41%. This is a much more comfortable relative humidity.

*Figure 8: Humidity for each mode of transportation during a ride from S Negley Ave to Morewood Ave on Fifth Ave*
![Humidity Record!](https://github.com/korawichkavee/12740-Ridecomfort-Pittsburgh/blob/gh-pages/footage%20and%20picture/Humidity%20Records.png)

Figure 9 (below) shows the temperature on each mode of transportation during the ride. The car and bus had comparable values of 24 C and 25 C, respectively. The scooter was slightly cooler, for an average value of 21 C. Similar to the relative humidity, this temperature value for the scooter matches the weather at the time. As the temperature was in a comfortable range, the temperature while riding the scooter was also comfortable. However, on a hot or cold day, this value would  change to reflect this. On the other hand, the bus and car were both slightly warmer than the outdoor temperature. This is not surprising for a partly sunny day, as the sun heats up the car and bus a bit above the outdoor temperature.

*Figure 9: Temperature for each mode of transportation during a ride from S Negley Ave to Morewood Ave on Fifth Ave*
![Temperature Record!](https://github.com/korawichkavee/12740-Ridecomfort-Pittsburgh/blob/gh-pages/footage%20and%20picture/Temperature%20Records.png)

## Discussion
Overall, the project succeeded and the obtained data provided a clear picture on the levels of comfort for each ride. This would be especially insightful if we could repeat the test throughout the year (varying outdoor weather conditions) and at various times of day (varying bus crowdedness and street traffic). However, from simply testing on one day we can still make valuable deductions. The scooter was clearly the noisiest and bumpiest ride. The humidity for the scooter was also uncomfortably high. While the temperature was comfortable, this was not only at the bottom of the human comfort range but also only comfortable because the weather happened to be comfortable on that day. All in all, while a scooter might be a low-cost or convenient mode of transportation, it is by far the least comfortable.

Comparing between the car and the bus is more difficult. Both performed well and proved to be comfortable modes of transportation. The temperature and humidity were nearly identical for the car and the bus, and both fell within the human comfort levels. Vibrations from both rides were also comparable and low, each with minimal vibrations and occasional spikes

compare modes of transport and make conclusion
maybe lets mention how it was saturday to the bus was empty and perhaps quieter than usual




-------------------------------------------------------------------
## References and Footnotes
[^1]: https://www.maplesoft.com/products/maple/app_gallery/pdf/Condition_Air_into_the_Human_Comfort_Zone.pdf
[^2]: https://www.cuidevices.com/product-spotlight/electret-condenser-microphones
[^3]: https://learn.adafruit.com/adafruit-agc-electret-microphone-amplifier-max9814/

