# ISP Speed Shamer
This is a very simple script that can be deployed to any Raspberry Pi in order to test, track, and tweet to the appropriate Twitter account, whenever internet speeds reach a certain point. It can be used for any ISP that has a public Twitter account.

# Requirements
* Python 3
* speedtest-cli
* tweepy
* Twitter API keys

Any required packages can be downloaded from the appropriate repository or using pip. Twitter API keys can be obtained from [here](https://dev.twitter.com).

# Restrictions
At the current time, the code requires that the API keys for Twitter, along with other variables be inserted directly into the code. This will be fixed in later editions. For the current time code comments explaining what should be inserted where should suffice.

The best way to track speeds is to directly connect to your router using ethernet. Using this script to test WiFi speeds does not produce the best results.
