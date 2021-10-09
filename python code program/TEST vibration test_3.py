import busio
import digitalio
import board
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn
import time
import numpy as np

import matplotlib.pyplot as plt

spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)
cs = digitalio.DigitalInOut(board.D5)

# Create an MCP3008 object
mcp = MCP.MCP3008(spi, cs)
# Create an analog input channel on the MCP3008 pin 0
channel_x = AnalogIn(mcp, MCP.P0)
channel_y = AnalogIn(mcp, MCP.P1)
channel_z = AnalogIn(mcp, MCP.P2)


def accel_value(axis):
    val = axis/6339.663
    val -= 5.1493 
    # Convert to gravities.
    return val

data_RAW =[[],[],[]]
data_V =[[],[],[]]
data_accel=[[],[],[]]

#while True:
for i in range (0,300):
    data_RAW[0].append(channel_x.value)
    data_V[0].append(channel_x.voltage)
    data_accel[0].append(accel_value(channel_x.value))
    
    data_RAW[1].append(channel_y.value)
    data_V[1].append(channel_y.voltage)
    data_accel[1].append(accel_value(channel_y.value))
    
    data_RAW[2].append(channel_z.value)
    data_V[2].append(channel_z.voltage)
    data_accel[2].append(accel_value(channel_z.value))
    
    time.sleep(0.001)

data_RAW=np.array(data_RAW)
print("this is RAW")
print(np.average(data_RAW[0]))
print(np.average(data_RAW[1]))
print(np.average(data_RAW[2]))
Fig2 = plt.figure(figsize=(9, 3))
plt.plot(data_RAW[0],label ="x axis")
plt.plot(data_RAW[1],label ="y axis")
plt.plot(data_RAW[2],label ="z axis")
plt.legend()
plt.show(Fig2)

data_V=np.array(data_V)
print(np.average(data_V))
Fig1 = plt.figure(figsize=(9, 3))
plt.plot(data_V[0],label ="x axis")
plt.plot(data_V[1],label ="y axis")
plt.plot(data_V[2],label ="z axis")
plt.legend()
plt.show(Fig1)

data_accel=np.array(data_accel)
print(np.average(data_accel))
Fig3 = plt.figure(figsize=(9, 3))
plt.plot(data_accel[0],label ="x axis")
plt.plot(data_accel[1],label ="y axis")
plt.plot(data_accel[2],label ="z axis")
plt.legend()
plt.show(Fig3)
