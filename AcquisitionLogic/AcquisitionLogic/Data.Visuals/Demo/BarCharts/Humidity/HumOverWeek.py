import numpy as npy
import matplotlib.pyplot as plt

from random import randint as rand

week = 7
weekDataList = list()
# demo data
for x in range(0,7):
    hum = rand(0,100)
    weekDataList.append(hum)

index = npy.arange(week)
width = 0.40

fig, ax = plt.subplots()
barSet1 = ax.bar(index, weekDataList, width, color='r')

ax.set_ylabel('Humidity (%)')
ax.set_title('Humidity Data Captured Over Current Week')
ax.set_xticks(index + width)
ax.set_xticklabels(('Monday','Tuesday','Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'))

ax.legend(barSet1, ('DHT11 - Main'))

def autolabel(bars):
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width(),
                1.05*height,
                '%d' % int(height),
                ha='center', va='bottom')

autolabel(barSet1)

plt.show()