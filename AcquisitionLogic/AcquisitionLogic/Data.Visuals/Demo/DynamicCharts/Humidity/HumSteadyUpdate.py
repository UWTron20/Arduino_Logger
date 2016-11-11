import matplotlib.pyplot as plt
from random import randint as rand
from drawnow import *

hum = []

def makePlot():
    plt.ylim(0,100)
    plt.title("Live Stream")
    plt.grid(True)
    plt.ylabel('Humidity')
    plt.xlabel('Time (s)')  
    plt.plot(hum, "ro-")

def genHum():
    hum.append(rand(0,100))
    if(len(hum) == 100):
        for x in range(0,40):
            hum.pop(x)

while True:
    genHum()
    drawnow(makePlot)
    plt.pause(.00000001)