# Welcome to GitHub Pages [Data Acq: Ride comfort of different modes of transportation in Pittsburgh]

Members = [Korawich, Jacobo, Guillermo, and Albin].

video link:

website link: [Github Project](https://korawichkavee.github.io/12740-Ridecomfort-Pittsburgh/)

## Introduction and Motivation
There are many travel options to and from the Carnegie Mellon University Pittsburgh Campus. Depending on how close you live to CMU, your mode of transportation, or your budget, a specific option usually fits your needs. For instance, taking a car might save time, but riding the bus might save money, and riding a bike or scooter might be more practical. While these measures can be quantified by time, cost, or both, one of the most critical aspects to consider that different transportation options cannot easily quantify: **comfort**. Attempting to measure the comfort of each of these rides is crucial in ultimately understanding the full range of benefits and downfalls of most transportation options.

The objective is to create a framework to better estimate comfort using different variables related to it. Hence, the outcomes will aid in determining better the advantages and disadvantages of different modes of transportation. Furthermore, based on the results, one will be able to ascertain the gaps in accessibility of transportation to campus when the privilege to own any vehicle, including bikes and scooters, is lacking. Thus, the following analysis will use quantitative data obtained from an array of sensors to evaluate the comfort of each mode of public or private transport to and from campus.


## Goals
We will quantify the comfort of a ride based on three primary factors:
  1. Vibrations within the vehicle
  2. Sound volumes throughout the ride
  3. Temperature and humidity of the vehicle

We will conduct sensing for three modes of transportation:
  1. Bus 
  2. Car
  3. Scooter/bike 
  
For each measured aspect and mode of transportation, we will analyze and compare obtained values to determine the comfort levels of each ride.

## Sensors
We will use the following sensors to measure data:
  1. Vibration sensor to measure vibrations/accelerations.
  2. Sound detection sensor to measure the noise of the vehicle.
  3. Temperature and humidity sensor to measure temperature and humidity.

We will fix our sensors to each vehicle while in motion and take samples.
Note that a more in depth description of these sensors is outlined later, below.

## Progress
### Current Progress
Our main goal at the moment is to successfully code and build the circuit for the sensors to the RaspberryPi. Our vibration sensor was not functional so we had to buy a new one, which was finally delivered on 10/4.

We are still working out bugs in our code because the vibration sensor (accelerometer) measurements are not outputting correctly.


10/5/2021 update

We tried to run the accelerometer and sound sensor that arrived yesterday with the Raspberry Pi, and we are having trouble in interpreting the data that the AD converter is giving us. Although we detect variation in the voltage when the sensors are stimulated, we still cannot convert that parameter into a magnitude of our interest, like m/s2 or g for acceleration and db for sound.

We saw a transformation function for the accelerometer provided by the manufacturer (Adafruit) but is in terms of the digital raw values, which are very erratic and we suspect that something is not working properly with those values. 

### Future Plan
After the code and circuit has been fine-tuned, we need to test our sensors on rides on each mode of transport. Then, we will need to post-process data to compare the comfort levels form each ride.

## Methods


## Experiment and Results


## Discussion


## Sensors Used - In Depth





-------------------------------------------------------------------
You can use the [editor on GitHub](https://github.com/korawichkavee/12740-Ridecomfort-Pittsburgh/edit/gh-pages/index.md) to maintain and preview the content for your website in Markdown files.

Whenever you commit to this repository, GitHub Pages will run [Jekyll](https://jekyllrb.com/) to rebuild the pages in your site, from the content in your Markdown files.

### Markdown

Markdown is a lightweight and easy-to-use syntax for styling your writing. It includes conventions for

```markdown
Syntax highlighted code block

# Header 1
## Header 2
### Header 3

- Bulleted
- List

1. Numbered
2. List

**Bold** and _Italic_ and `Code` text

[Link](url) and ![Image](src)
```

For more details see [GitHub Flavored Markdown](https://guides.github.com/features/mastering-markdown/).

### Jekyll Themes

Your Pages site will use the layout and styles from the Jekyll theme you have selected in your [repository settings](https://github.com/korawichkavee/12740-Ridecomfort-Pittsburgh/settings/pages). The name of this theme is saved in the Jekyll `_config.yml` configuration file.

### Support or Contact

Having trouble with Pages? Check out our [documentation](https://docs.github.com/categories/github-pages-basics/) or [contact support](https://support.github.com/contact) and we’ll help you sort it out.
