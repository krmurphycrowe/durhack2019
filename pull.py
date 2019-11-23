import tweepy, json

def loadMostRecentTweet():
    try:
        with open("lastTweet") as f:
            lastID = f.read()
            return int(lastID)
    except FileNotFoundError:
        return 0

def saveMostRecentTweet(id):
    with open ("lastTweet", "w") as f:
        f.write(str(id))

def getBowisTweets(tAPI):
    """Returns list of text bodies of Boris Johnson's twitter feed."""
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