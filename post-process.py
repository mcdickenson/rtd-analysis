# Post-process RTD tweets
# 1. Exclude all @-replies
# 2. Exclude all tweets from before 2016-04-22 when the A Line launched (http://www.rtd-denver.com/a-line.shtml)

import csv
from datetime import datetime

filename = 'RideRTD_tweets'
fieldnames = ['id', 'created_at', 'text']
date_fmt = '%Y-%m-%d %H:%M:%S'
min_date = datetime.strptime('2016-04-22 00:00:00', date_fmt)

print('min_date is {}'.format(min_date))


with open('{}.csv'.format(filename), 'r') as infile:
  with open('{}_processed.csv'.format(filename), 'wb') as outfile:
    reader = csv.DictReader(infile)
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    writer.writeheader()

    for row in reader:

      # skip @-replies
      if row['text'][0] == '@':
        continue

      # skip tweets before the A Line launched
      if datetime.strptime(row['created_at'], date_fmt) < min_date:
        continue

      writer.writerow(row)