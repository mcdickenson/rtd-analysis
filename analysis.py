from pandas import Series, DataFrame
from collections import OrderedDict
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


path_to_data = '~/rtd_delays.csv'
colors = OrderedDict([
  ('A', '#56C2E7'),
  ('B', '#4CA02E'),
  ('C', '#FF932D'),
  ('D', '#037E48'),
  ('E', '#58268B'),
  ('F', '#F13D28'),
  ('H', '#007DCE'),
  ('W', '#02A2A4')
])

path_to_data = '/home/mcdickenson1/rtd_delays.csv'
data = pd.read_csv(path_to_data)

data = pd.read_csv(path_to_data, index_col='date')
data.index = pd.to_datetime(data.index)

data.head()
data.describe()


##########
# - what is the frequency of delays by line?
#   - hypothesis: the A line has more frequent delays than other lines

delays = data[data['type'] == 'delay']

lines_total = delays.groupby('line')
lines_total.size()
# A       44
# B        1
# C        3
# D       10
# E        6
# F       10
# H        8
# W        2

# parameters for plots
n = 8
ind = np.arange(n)
width = 1

fig1, ax = plt.subplots()
rects1 = ax.bar(ind, lines_total.size(), width, color=colors.values())
ax.set_xticks(ind + 0.5)
ax.set_xticklabels(lines_total.size().index)
ax.set_ylabel('Total delays')
ax.set_title('RTD Delay Counts by Line')
fig1.savefig('rtd1.png')

# conclusion: A line had more delays than all other lines ~combined~


##########
# - what is the average duration (in minutes) of delays by line?
#   - hypothesis: the A line has longer delays than other lines
avg_delays = lines_total.mean()

fig2, ax = plt.subplots()
rects1 = ax.bar(ind, avg_delays['delay_minutes'], width, color=colors.values())
ax.set_xticks(ind + 0.5)
ax.set_xticklabels(lines_total.size().index)
ax.set_ylabel('Average delay duration (minutes)')
ax.set_title('RTD Delay Durations by Line')
fig2.savefig('rtd2.png')

# conclusion: the A line does *not* have the longest delays


##########
# - what is the average extent (in hours) of delays by line?
#   - hypothesis: the A line has more extensive than other lines
fig3, ax = plt.subplots()
rects1 = ax.bar(ind, avg_delays['duration_hours'], width, color=colors.values())
ax.set_xticks(ind + 0.5)
ax.set_xticklabels(lines_total.size().index)
ax.set_ylabel('Average delay extent (hours)')
ax.set_title('RTD Delay Extents by Line')
fig3.savefig('rtd3.png')

# conclusion: when a line has a delay, those delays occur for longer portions of the day on the A line


##########
# - what is the frequency of closures by line?
#   - hypothesis: the A line has more frequent closures than other lines

# Note - the W line had no closures for the period under consideration

n = 7
ind = np.arange(n)

closures = data[data['type'] == 'closure']
closures_total = closures.groupby('line')

fig4, ax = plt.subplots()
rects1 = ax.bar(ind, closures_total.size(), width, color=colors.values()[0:n-1])
ax.set_xticks(ind + 0.5)
ax.set_xticklabels(closures_total.size().index)
ax.set_ylabel('Total closures')
ax.set_title('RTD Closure Counts by Line')
fig4.savefig('rtd4.png')

# conclusion: A line is about middle-of-the pack for closure counts


##########
# - have delays become more or less frequent since the A line opened? (e.g. Oct vs. May)
aline_delays = delays[delays['line'] == 'A'].groupby(pd.TimeGrouper(freq='M'))

# subset to complete months
subset = aline_delays.size()
subset = subset[1:7]


n = 6
ind = np.arange(n)

fig5, ax = plt.subplots()
rects1 = ax.bar(ind, subset.values, width, color=colors['A'])
ax.set_xticks(ind + 0.5)
ax.set_xticklabels(['May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct'])
ax.set_ylabel('Delays by month')
ax.set_title('RTD A Line Delay Counts by Month')
fig5.savefig('rtd5.png')

# conclusion: delays on the A line are becoming less frequent
