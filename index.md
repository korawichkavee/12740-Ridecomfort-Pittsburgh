# Ride comfort of different modes of transportation in Pittsburgh

**Members: Korawich Kavee, Jacobo Kirsch Tornell, Guillermo Montero, and Albin Wells**

#### TO DO: (1) Finish sensor spec sheet (with citations), (2) add graphs and discussion on results, (3) add final conclusions, (4) read over full report and review writing and formatting

**To delete later: [Canvas project rubric link](https://canvas.cmu.edu/courses/25498/discussion_topics/362646)

Website Link: [Github Project](https://korawichkavee.github.io/12740-Ridecomfort-Pittsburgh/)

Video Link: [Ride Comfort Video](https://www.youtube.com/watch?v=bcNrlpfi9SA&ab_channel=KorawichKavee)

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
One of the main aspects that one can attribute to comfort is a smooth ride. That is why adding a vibration sensor to measure accelerations differences during the traveling time would be able to determine if the ride was pleasant. The accelerometer sensor we decided to use is **ADXL335 - 5V ready triple axis accelerometer**. (Figure 1).

### Noise and Sound 
Who has not had the annoying situation of having to hear a car blasting off music while going to a place. Noises, especially loud and sharp, irritate someone very easily. Hence, detecting the noise while travelling can also quantify comfort. The microphone sensor (**Electret Microphone Amplifier MAX9814**) is shown in Figure 1 below. 

### Temperature and humidity 
Temperature and humidity can affect how a human feels during a ride. For instance, a warm and humid sensation would make someone start to sweat more easily and make a ride unpleasant. Thus, using **DHT11 Temperature and Humidity Sensor** to measure temperature and humidity would give us an outcome that one can measure if the temperature and humidity is inside the human comfort location (See Figure 1 below).

*Figure 1: Sensors used to obtain data to determine comfort in different modes of transportation. From left to right, ADXL335 sensor, MAX9814 sensor, and DHT11 sensor.*[^1][^2][^3]

![3 sensors used. From left to right, ADXL335 sensor, MAX9814 sensor, and DHT11 sensor!](https://github.com/korawichkavee/12740-Ridecomfort-Pittsburgh/blob/gh-pages/footage%20and%20picture/3sensors.jpg)

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
As mentioned above, the interest of this project is to quantify and compare the comfort of various modes of transportation. We identified a few contributing factors to comfort, which include noise level, vibrations, temperature, and humidity. Ultimately, these are the phenomena we are sensing.

#### Temperature and Humidity
The temperature and humidity are both relatively static signals. Especially considering the short time scale of our study (~2 to 5 minutes), these signals are unlikely to change. If they do, they are unlikely to change by very much. Thus, a low sampling frequency can adequately capture and characterize these signals. Sampling one point might be sufficient to understand the temperature and humidity in each mode of transportation, although it is still better to obtain multiple samples throughout the ride. Theoretically, depending on the weather conditions, the temperature in a car could change with heating or air conditioning over the 2-5 minute time period of our test. It is crucial to keep in mind that the optimal human comfort zone is between 22°C to 27°C and 40-60% relative humidity during this analysis. [^4]

*Figure 2: Human comfort requires the right combination of temperature and humidity. The comfort zone diagram gives an estimated insight about the ranges where the human feel the most comfortable.* [^5]

![Human comfort requires the right combination of temperature and humidity!](https://github.com/korawichkavee/12740-Ridecomfort-Pittsburgh/blob/gh-pages/footage%20and%20picture/comfort%20zone.png)

#### Vibrations and Movement
Sensing vibrations is much more challenging. This is a dynamic, aperiod signal. The accelerometer can measure movement, shock, or shake in the X, Y, and Z-axis. Sensors of this type measure capacitance changes based on the deflection between fixed plates and plates attached to a dangled structure. As acceleration is detected in each axis, the difference in capacitance is converted to an output voltage proportional to it. [^6] While we expect the signal to be 'centered' around 1g, sporadic motion from the vehicles causes it to vary at random intervals. These variations tend to be a function of external sources, such as potholes and road conditions, stops and traffic lights, other cars, driving habits, etc. Thus, we cannot expect a consistent, periodic signal. Instead, we sample the signal at a rate high enough to capture these sudden variations in acceleration and use this to quantify the vibrations during the ride.

*Figure 3: An accelerometer is used where linear motion such as shock, vibration, and movement is needed. Diagram shows the structure of measuring movement, shock, or shake within an axis.* [^5]

![Diagram of Principle of Accelerometer!](https://github.com/korawichkavee/12740-Ridecomfort-Pittsburgh/blob/gh-pages/footage%20and%20picture/Principle%20of%20accelerometer.jpg)

#### Sound and Noises
Sound sensing poses and entirely new set of challenges. Sound signals are dynamic, periodic signals that cover a very large range of frequencies (up to and above 1kHz). Due to limitations of the sensors and equipment, sampling rate is severely limited to the point where effectively all sound signals are aliased. Thus, trying to determine the sound wave frequencies is futile. Instead, we focus our efforts on measuring volume: magnitude of the sound waves. This magnitude is converted into decibels to easily compare to human comfort levels. For this analysis, it is important to note that normal speech is around 60 dB and any sound above 120 dB is perceived as discomfort. [^7]

*Figure 4: Defining the maximum frequency-intensity range that can be audible to the human ear. Denoting human speech and music range for comparison.* [^8]

![Diagram of Sound!](https://github.com/korawichkavee/12740-Ridecomfort-Pittsburgh/blob/gh-pages/footage%20and%20picture/sound.jpg)

### Sensors - In Depth
An outline of the sensor descriptions and specifications is show in Table 1. The final setup of the sensor with the RaspberryPi is shown in Figure 5 below.

*Table 1: Sensor descriptions and specifications*
| Sensor | Description | Physical Principle | Characteristics |
| ----------- | ----------- | ----------- | ----------- |
| Sound and Noise Sensor | Electret Microphone Amplifier - MAX9814 | Electret condenser microphones function by utilizing a diaphragm as a capacitor plate. Vibrations by the diaphragm generated by sound produce changes the distance between the diaphragm and the second plate. Thus, causing a difference in voltage, which is amplified and converted to reflect audio signal at the output. [^9], [^10] | <ul><li>Supply Voltage: 2.7v-5.5v @ 3mA current</li><li>Output: 2Vpp on 1.25V bias</li><li>Frequency Response: 20Hz - 20 KHz</li><li> Temperature Range: −55°C to +125°C</li></ul> [^9] |
| Accelerometer Sensor | ADXL335 - 5V ready triple axis accelerometer | This accelerometer measures capacitance changes based on the deflection of fixed plates and plates attached to a suspended structure. A proportional output voltage is generated for each axis when acceleration is detected.[^6] | <ul><li>Supply Voltage: 1.8v-3.6v @ 350 μA current</li><li>Output: 0.1V-2.8V with ±0.01 %/°C sensitivity change</li><li>Frequency Response: 0.5Hz-1600Hz (X, Y-axes), 0.5Hz-550Hz (Z-axis)</li><li> Temperature Range: −55°C to +125°C</li></ul>[^11] |
| Temperature and Humidity | Add description here | Add the phyisical principle of the sensor here | Add specs here |

*Figure 5. The final sensor setup with the RaspberryPi*

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
Figure 6 (below) shows raw data results for the amplitude of accelerations during the trip for each mode of transportation. Figure 7 shows the acceleration for each mode of transportation during the trip on the frequency domain. As can be clearly seen, the scooter has by far the most vibrations. The ride is much 'bumpier' than for the bus or car, with amplitudes frequently eclipsing 1g. Particularly interesting is the lapse in vibrations on the scooter at around 100 seconds. This period of low vibrations reflects a red light, when the scooter was stopped for a short period of time. There is no discernable difference in vibrations on the car or the bus: both are relatively low with a few spikes where acceleration peaks.

*Figure 6: Acceleration for each mode of transportation during a ride from S Negley Ave to Morewood Ave on Fifth Ave*
![Acceleration record!](https://github.com/korawichkavee/12740-Ridecomfort-Pittsburgh/blob/gh-pages/footage%20and%20picture/Acceleration%20Records.png)
From the frequency domain graph, it can be seen that in all transportation methods, there are not any clearly predominant frequency content from others, it seems like if they were almost uniformly distributed. This may probably be because of the low sampling of the sensor equipment, compared with the actual frequencies of vibration and there might be a considerable amount of aliasing in this data. So, the only reliable information that can be obtained is that the acceleration amplitudes of the scooter ride are much larger than the car and the bus.

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


Overall, the project succeeded and the obtained data provided a clear picture on the levels of comfort for each ride. This would be especially insightful if we could repeat the test throughout the year (varying outdoor weather conditions) and at various times of day (varying bus crowdedness and street traffic). However, from simply testing on one day we can still make valuable deductions. In order to do this, we calculated the root-mean-square deviation from all the collected data with respect to each measurment type and transportation method. This way we can comparatively identify for each measurment category which was the most un comfortable transportation method by identifying the greatest deviation.

*Table 2: Measurments Comfort Zone and root-mean-square deviation*
| Sensor | Comfot Zone | Car | Bus | Scooter |
| ----------- | ----------- | ----------- | ----------- | ----------- |
| Acceleration [g] | 0 | 0.05 | 0.05 | 0.77 |
| Noise [db] | 0 | 64.46 | 82.92 | 82.92 |
| Temperature [°C] | 24.5 | 0.52 | 0.54 | 3.45 |
| Humidity [%] | 40 | 1.46 | 1.62 | 31.11 |

With respect to acceleration, the scooter is the most uncomfortable transportation method since it is the one with the most accelerations amplitudes and clearly the bumpiest ride (it can be easily identified by viewing Figures 6 and 7). As for the bus and the car, there is a difference in the fourth decimal place of the deviations, but for practical purposes it can be considered as a tie. As for the noise level, the most comfortable or quietest was the car ride, then we have another technical tie, but this time it is between the bus and the scooter, whose difference is only noticeable in the third decimal place of the comfort deviation values.

In temperature the winner is again the car trip, which has a deviation from the comfort zone only slightly lower than the bus. In other words, we could say that the temperature of the car is only slightly more comfortable than that of the bus.  But as for the scooter, it is at a temperature well below the comfort temperature and takes third place in this category. Finally in terms of humidity, the car trip is almost perfectly above the comfort humidity, taking the first place, then follows the bus trip, which deviates a little more from the optimum and the scooter is the one with the highest humidity and is further away from the comfort zone.

Analizing the results it can be easyly determined that is by far the least comfortable of three, but comparing between the car and the bus is more difficult. Both performed well and proved to be comfortable modes of transportation. The temperature and humidity were nearly identical for the car and the bus, and both fell within the human comfort levels. Vibrations from both rides were also comparable and low, each with minimal vibrations and occasional spikes. But for the volume of sound, the car was quieter than the bus. The ambient noise of the car around 60 dB is roughly equivalent to normal speech, while the bus was only slightly louder at 80 dB. For this reason, the car was slightly more comfortable than the bus. Based on our results, the following lists the comfort of each mode of transportation in order from most comfortable to least:

1. Car
2. Bus
3. Scooter

While our conclusions are based in our assumptions of comfortness, with more testing we would expect a larger difference in the comfort of the bus and the car to appear. In general, cars are better equipped to control temperature, especially during the summer. Furthermore, testing was carried out on a Saturday when the bus was relatively quiet and empty. If we tested during a ride home from school during the week, we might expect the bus to be louder. That said, the vibrations showed no discernable difference between the car and the bus, and that would not be likely to change very much even in different temperature or during a busier time of day.

-------------------------------------------------------------------
## References and Footnotes
[^1]: Earl, B. (2021). Sensors ADXL335 Lrg. Adafruit. Adafruit. Retrieved 2021, from https://cdn-learn.adafruit.com/assets/assets/000/002/469/small360/sensors_ADXL335_LRG.jpg?1396783433. 
[^2]: Adafruit. (2021). MAX9814. Digi-Key Electronics. Adafruit. Retrieved 2021, from https://www.digikey.com/en/products/detail/adafruit-industries-llc/1713/4990777?s=N4IgjCBcoLQBxVAYygMwIYBsDOBTANCAPZQDa4ArAEwIC6AvvYVWeAOxgDMIDQA. 
[^3]: Roboshop.com. (2020). DHT11 Temperature Humidity Sensor Module. Roboshop.com. Retrieved 2021, from https://www.robotshop.com/media/catalog/product/cache/image/1350x/9df78eab33525d08d6e5fb8d27136e95/d/h/dht11-temperature-humidity-sensor-module.jpg. 
[^4]: Maplesoft. (n.d.). Conditioning Air into the Human Comfort Zone. Maplesoft. https://www.maplesoft.com/products/maple/app_gallery/pdf/Condition_Air_into_the_Human_Comfort_Zone.pdf
[^5]: Datta, A. K. (2017). Equilibrium, Energy Conservation and Temperature. In Heat and mass transfer: A biological context (2nd ed., pp. 11–14). essay, CRC press. 
[^6]: Earl, B. (2012, November 5). Adafruit analog accelerometer breakouts. Adafruit Learning System. Retrieved October 10, 2021, from https://learn.adafruit.com/adafruit-analog-accelerometer-breakouts. 
[^7]: Noisequest. (2018). Noise Basics. PSU Noisequest. Retrieved October 11, 2021, from https://www.noisequest.psu.edu/noisebasics-basics.html. 
[^8]: Vaisberg, J., Folkeard, P., Parsa, V., et al. (2017, August 17). Comparison of music sound quality between hearing aids and music programs. AudiologyOnline. Retrieved October 12, 2021, from https://www.audiologyonline.com/articles/comparison-music-sound-quality-between-20872. 
[^9]: Ada, L. (2014, February 13). Adafruit AGC Electret microphone amplifier - MAX9814. Adafruit Learning System. Retrieved October 13, 2021, from https://learn.adafruit.com/adafruit-agc-electret-microphone-amplifier-max9814/. 
[^10]: CUI Devices. (2021). Product spotlight: Electret condenser microphones. CUI Devices. Retrieved October 13, 2021, from https://www.cuidevices.com/product-spotlight/electret-condenser-microphones. 
[^11]: ADXL335. Datasheet and Product Info | Analog Devices. (2010). Retrieved October 13, 2021, from https://www.analog.com/en/products/adxl335.html#product-overview. 

