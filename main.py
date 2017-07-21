# Speed tester for Comcast/Xfinity internet service.
# I'm paying for 150Mbits/sec, and I'd be darned if I get any less than what's reasonable!
import tweepy
import speedtest


def tweet_send(simpleDownload, simpleUpload):
    # Variables that contains the user credentials to access Twitter API.
    # Should probably make this a lot easier to use before putting on GitHub.
    # Also,
    # TODO: REMOVE KEYS BEFORE POSTING ON GITHUB!
    consumer_key = "" # Twitter consumer key
    consumer_secret = "" # Twitter secret key
    access_token = "" # Twitter account access token
    access_token_secret = "" # Twitter account secret access token

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    api.update_status("Hey, @ComcastCares, I'm paying for 150Mbps service. I'm only getting {}Mbps down/{}Mbps up. All is good on my end. What gives?".format(simpleDownload, simpleUpload))
    print("Tweet posted!")
    return 0


def speed_test():
    print("Starting speed test...")
    serverArray = []

    # Conduct speed test.
    s = speedtest.Speedtest()
    s.get_servers(serverArray)
    s.get_best_server()
    # Results are returned back as bits/second, as a double.
    downloadSpeedRaw = s.download()
    print("Download test completed.")
    uploadSpeedRaw = s.upload()
    print("Upload test completed.")

    # Stores raw data in .json for later use...
    resultsDict = s.results.dict()
    storeFile = open("dataFile.json", "a+")
    storeFile.write(str(resultsDict) + "\n")
    storeFile.close()
    print("Test data written to file.")

    # Math to determine if threshhold is met/not met
    TARGET_SPEED = 150  # Advertised speed they gave to you on signup for service
    MARGIN_OF_ERROR = 0.5  # Percentage, in decimal format, you're willing to compromise on
    # Because, let's face it, you won't get full speed all the time
    # But if it's really bad (Think, 50% worse than advertised, for example), that's bad
    simpleDownload = round(downloadSpeedRaw / 1000000, 2)
    simpleUpload = round(uploadSpeedRaw / 1000000, 2)
    if (downloadSpeedRaw) < ((TARGET_SPEED * 1000000) * MARGIN_OF_ERROR):
        print("SLOW SPEEDS DETECTED!\nI'm telling the world!\nDownload: {}\nUpload: {}".format(simpleDownload, simpleUpload))
        tweet_send(simpleDownload, simpleUpload)
    else:
        print("All is good.\nDownload: {}\nUpload: {}".format(simpleDownload, simpleUpload))
        return 0

print("Comcast/Xfinity Speed Tester, Version 1.0")
speed_test()