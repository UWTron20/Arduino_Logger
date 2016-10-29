import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as ny
import datetime

from random import randint as rand
from matplotlib import style

style.use('fivethirtyeight')

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

# Y - Data
dataL = []

# X - Time
timeL = []

#ensures only 7 copies of the array kept
def clearList(dataList):
    size = len(dataList)
    if(size >= 7):
        dataList.pop(0)


# For Testing Purposes
def generate_Data(dataList):
    data = rand(0,100)
    dataList.append(data);
    clearList(dataList)

def get_Time(timeList):
    currTime = datetime.datetime.now()
    timeList.append(currTime.second)
    clearList(timeList)

def check_Time(dataList, timeList):
    if(datetime.datetime.now().second == 60 ):
        dataList = ny.zeros(shape=(1,7))
        timeList = ny.zeros(shape=(1,7))

def animate_graph(i, dList, tList):
    generate_Data(dList)
    get_Time(tList)
    ax1.clear()
    # test = [1,2,3,5]
    ax1.plot(tList, dList)


ani = animation.FuncAnimation(fig, animate_graph, interval=10, fargs=(dataL, timeL))
plt.xlim(0,60)
plt.ylim(0,101)
plt.xlabel('time (s)')
plt.ylabel('Humidity (%)')
plt.title('Humidity Time Update')
plt.grid(True)
plt.show()