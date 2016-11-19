# rtd-analysis

Analysis of RTD (Denver-area public transit) reliability

## Motivation

- A line opened in April to great fanfare
- lots of delays and closures
- gained a reputation for unreliability
- Aurora line hasn't opened because it's operated by same company, want to get issues worked out

## Process

1. Collect all tweets from the RTD Twitter account [@RideRTD](twitter.com/RideRTD) (`twitter-collect.py`)
2. Filter out irrelevant tweets (`post-process.py`)
3. Use tweets to generate data on delays by line
  - delays or closures
  - if a delay is expressed as a range (e.g. "15-30 minutes"), the upper bound was used
  - when URLs were given in the tweet they were referenced for additional details
  - if there is a scheduled delay that did not occur (according to a subsequent tweet), not recorded
4. Analyze frequency and duration of delays (`analysis.py`)
  - what is the average frequency (days/month) of delays by line?
    - hypothesis: the A line has more frequent delays than other lines
  - what is the average duration (in minutes) of delays by line?
    - hypothesis: the A line has longer delays than other lines
  - what is the average extent (in hours) of delays by line?
    - hypothesis: the A line has more extensive than other lines
  - what is the average frequency of closures (days/month) by line?
    - hypothesis: the A line has more frequent closures than other lines
  - have delays become more or less frequent since the A line opened? (e.g. Oct vs. May)
  - assume that every mile of track has a failure rate, where any delay or closure on a day is a failure, and estimate this rate for each line
  - future:
    - are certain lines correlated (for occurrence and duration)?
      - hypothesis: geographically colocated lines will have correlated delays
      - correlation could also be indicated by an outage reported in the same tweet


## Setup

1. Go to https://apps.twitter.com/
2. Sign in
3. Create new app (if necessary)
4. Put the following four values in a dotfile in your project:
  - Consumer Key (`export TWITTER_CONSUMER_KEY=foo`)
  - Consumer Secret (`export TWITTER_CONSUMER_SECRET=foo`)
  - Access Token Key (`export TWITTER_ACCESS_KEY=foo`)
  - Access Token Secret (`export TWITTER_ACCESS_SECRET=foo`)
5. Source the dotfile (and make sure it's in your .gitignore)
6. Install TwitterAPI module: `pip install TwitterAPI`
7. Modify `twitter-collect.py` for the username whose tweets you wish to collect


## Acknowledgements

- Twitter code adapted from code by [Charley Frazier](https://gist.github.com/cfrazier91/1c6708a83c6c09b0ee20e0ee6e0ec7ce) and [yanofsky](https://gist.github.com/yanofsky/5436496).
