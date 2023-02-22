import matplotlib.pyplot as plt
import numpy as np
from pandas import read_csv
import pandas as pd
import matplotlib.dates as md

et = []  # EnergyTake Data
temp = []
flow = []
I =[]
date = []
time = []

df = read_csv(r'C:\Users\gabeh\Desktop\shed12hr.csv') # CSV read

for i, row in df.iterrows():
    et.append(df.iloc[i,8])
    temp.append(120-(df.iloc[i,8]/(50*2.44))) # Change 50 gal if using different sized WH. 2.44 Wh to heat 1 gal by 1 degree.
    I.append(df.iloc[i,10]/240)
    date.append(df.iloc[i,0])
    time.append(date[i][10:19])
    if i > 721: # 721 data points for 12 hours, any data beyond 721 in the csv is ignored
        break

print(time)
# flow = [0,0,0,0,0,0,0,2,2,2,2,2,2,2,2,2,2,2,2]
# flowrate = np.diff(flow)
# print(len(flowrate))

fig, ax1 = plt.subplots(2,1,figsize = (8,6))

dt = pd.DataFrame({'Time': pd.date_range(start = '2021-01-01 09:00', end = '2021-01-01 21:00', freq = '1min')})
ax1[0].xaxis.set_major_locator(md.MinuteLocator(byminute = [0, 60]))
ax1[0].xaxis.set_major_formatter(md.DateFormatter('%H:%M'))
plt.setp(ax1[0].xaxis.get_majorticklabels(), rotation = 45)
ax1[1].xaxis.set_major_locator(md.MinuteLocator(byminute = [0, 60]))
ax1[1].xaxis.set_major_formatter(md.DateFormatter('%H:%M'))
plt.setp(ax1[1].xaxis.get_majorticklabels(), rotation = 45)
dt = dt.set_index('Time')


ax1[0].plot(dt.index, et,linewidth=1.2, color='blue')
ax1[1].plot(dt.index, I,linewidth=1.2, color='red')

ax1[1].set_xlabel('Time (Hours:Minutes)')
ax1[0].set_title('EnergyTake and Current')
ax1[0].set_ylabel('EnergyTake (Wh)')
ax1[1].set_ylabel('Current (A)')

ax1[0].grid(True)
ax1[1].grid(True)


plt.show()
