## Welcome to GitHub Pages [Data Acq: Ride comfort of different modes of transportation in Pittsburgh]

Members = [Korawich, Jacobo, Guillermo, and Albin].

video link:

website link: [Github Project](https://korawichkavee.github.io/12740-Ridecomfort-Pittsburgh/)

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
## Future Plan
After the code and circuit has been fine-tuned, we need to test our sensors on rides on each mode of transport. Then, we will need to post-process data to compare the comfort levels form each ride.

# Methods


# Experiment and Results


# Discussion


# Sensors Used - In Depth





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
