import tweepy, json

def loadMostRecentTweet():
    with open("lastTweet") as f:
        lastID = f.read()
        return int(lastID)

def saveMostRecentTweet(id):
    with open ("lastTweet", "w") as f:
        f.write(str(id))

def getBowisTweets(tAPI):
    tweets = tAPI.user_timeline(user_id=3131144855, since_id=loadMostRecentTweet(), count=20, tweet_mode="extended")
    # Gets up to the 20 most recent tweets from bojo's twitter
    bodies = [] # Creates an empty list to store the bodies (not as suspicious as it sounds)
    mostRecent = loadMostRecentTweet() # Gets the most recent tweet from the file
    for tweet in tweets: # For every tweet
        if tweet.id > mostRecent: # If the tweet is more recent than the most recent
            mostRecent = tweet.id # Update the most recent tweek
        try: # So basically tweepy is really dumb and the only way to tell if it's a retweet or not is to use try/except
            bodies.append(tweet.retweeted_status.full_text) # Append the retweeted status
        except AttributeError: # Yada yada tweepy is dumb
            bodies.append(tweet.full_text) # Append the text of the tweet
    saveMostRecentTweet(mostRecent)
    newbod = [] # Creates a list for the processed bodies (again not as sus as it sounds)
    for body in bodies: # For every tweet body we have
        if not body.startswith(".@BorisJohnson"): # If it's not funky retweet
            newbod.append(body) # Append the body
    return newbod[::-1] # Tweepy fetches them most-recent first and we want most-recent last, so we flip the list

def load_file(to_load, key):
    # this is a method to load a file, used in loading the twitter key details file
    try:
        with open(to_load + '.json', 'r') as loadFile:
            # loads file, uses main key
            return json.load(loadFile)[key]

    except FileNotFoundError:
        print('File doesn\'t exist.')
        return 0

    except KeyError:
        print('File is in an invalid format')
        return 0

def test():
    try:
        filename = 'keys'
        key = 'DETAILS'
        file = load_file(filename, key)
        cKey = file["CONSUMER_KEY"]
        cSecret = file["CONSUMER_SECRET"]
        key1 = file["KEY1"]
        key2 = file["KEY2"]

        auth = tweepy.OAuthHandler(cKey, cSecret)
        auth.secure = True
        auth.set_access_token(key1, key2)

        api = tweepy.API(auth)
        print(getBowisTweets(api))
    except tweepy.error.TweepError:
        pass