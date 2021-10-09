#import some library
import pandas as pd
import numpy as np
import os
import time
from time import sleep
from datetime import datetime, timedelta
import RPi.GPIO as GPIO
import busio
import digitalio
import board
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn
import dht11
import sys

#create empty dataframe csv
#col_list = ['Timestamp', 'Vibration', 'Sound','Temp','Humid']
#df = pd.DataFrame(columns = col_list)
current_time =datetime.now()
file = open("/home/pi/data_log"+str(current_time)+".csv", "a")
if os.stat("/home/pi/data_log"+str(current_time)+".csv").st_size == 0:
        file.write("Timestamp,Sensor1,Sensor2,Sensor3,Sensor4,Sensor5\n")
print('my data log file is created !!!')

#create a parameter to get GPIO reading
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(25,GPIO.IN) #switch button

spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)
cs = digitalio.DigitalInOut(board.D5)
# Create an MCP3008 object
mcp = MCP.MCP3008(spi, cs)
# Create an analog input channel on the MCP3008 pin 0
channel_0 = AnalogIn(mcp, MCP.P0) #sound
channel_1 = AnalogIn(mcp, MCP.P1) #accel z

#define function for each sensor
freq = 20
duration = 5
duration_adj = timedelta(days = 0, seconds = duration*1.35,microseconds = 0,milliseconds = 0,minutes = 0, hours = 0,weeks = 0)
begining =datetime.now()

def accel_value(axis):
    val = axis/6339.663
    val -= 5.1493 
    # Convert to gravities.
    return val

def dB_value(i):
    val = i*(-0.0297)+756.73
    return val

instance = dht11.DHT11(pin = 14)

#define function for date and time
#tstamp = "{0:%Y}-{0:%m}-{0:%d}_{0:%H}.{0:%M}.{0:%S}".format(now)

#write a record of all sensor to csv
#https://www.instructables.com/Raspberry-Pi-Data-Logging/
#for index, row in df.iterrows():
#   df['Timestamp'] = tstamp
sound_data= []
#while current_time-begining < duration_adj:
run=True
while run:
    if GPIO.input(25):
        time.sleep(1/freq)
    else:
        run=False
time.sleep(3)        
run=True
print("I am sampling data")
while run:
    if GPIO.input(25):
        accel = accel_value(channel_1.value)
        sound = dB_value(channel_0.value)
        result = instance.read()
        temp  = result.temperature
        humid = result.humidity
        current_time =datetime.now()
        #file.write(str(now)+","+str(accel)+","+str(sound)+","+str(temp)+","+str(humid)+","+"\n")
        file.write(str(current_time)+","+str(accel)+","+str(sound)+","+str(temp)+","+str(humid)+"\n")
        sound_data.append(sound)
        #I think we also should do this flush thing
        #https://stackoverflow.com/questions/7127075/what-exactly-is-pythons-file-flush-doing
        #file.flush()
        time.sleep(1/freq)
    else:
        run=False
        
    
file.close()
for i in range(0,len(sound_data)):
    sound_data[i]=sound_data[i]*sound_data[i]
dB_RMS=(np.average(sound_data))**(1/2)
print(dB_RMS)
print("The python code is done")