import busio
import digitalio
import board
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn
import time
import numpy as np
from datetime import datetime, timedelta

import matplotlib.pyplot as plt

spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)
cs = digitalio.DigitalInOut(board.D5)

# Create an MCP3008 object
mcp = MCP.MCP3008(spi, cs)
# Create an analog input channel on the MCP3008 pin 0
channel_x = AnalogIn(mcp, MCP.P0)
channel_y = AnalogIn(mcp, MCP.P1)
channel_z = AnalogIn(mcp, MCP.P2)


def dB_value(input):
    val = input*(-0.0297)+756.73
    return val

data_RAW =[[],[],[]]
data_V =[[],[],[]]
data_dB=[[],[],[]]
time_rec=[]

freq = 10
duration = 5
duration_adj = timedelta(days = 0, seconds = duration*1.35,microseconds = 0,milliseconds = 0,minutes = 0, hours = 0,weeks = 0)
begining =datetime.now()
current_time =datetime.now()
#while True:
while current_time-begining < duration_adj:
    data_RAW[0].append(channel_x.value)
    data_V[0].append(channel_x.voltage)
    data_dB[0].append(dB_value(channel_x.value))
    current_time = datetime.now()
    time_rec.append(datetime.now())
    time.sleep(1/freq)
end=datetime.now()
print(end-begining)

data_RAW=np.array(data_RAW)
print("this is RAW")
print(np.average(data_RAW[0]))
Fig2 = plt.figure(figsize=(9, 3))
plt.plot(data_RAW[0],label ="RAW")
plt.legend()
plt.show(Fig2)

data_V=np.array(data_V)
#print(np.average(data_V[0]))
Fig1 = plt.figure(figsize=(9, 3))
plt.plot(data_V[0],label ="Volt")
plt.legend()
plt.show(Fig1)

data_dB=np.array(data_dB)
print("this is data_dB")
print(np.average(data_dB[0]))
Fig3 = plt.figure(figsize=(9, 3))
plt.plot(data_dB[0],label ="dB")
plt.legend()
plt.show(Fig3)
