def loadMostRecentTweet():
    with open("lastTweet") as f:
        lastID = f.read()
        return int(lastID)

def saveMostRecentTweet(id):
    with open ("lastTweet", "w") as f:
        f.write(id)

def getBowisTweets(tAPI):
    tweets = tAPI.user_timeline(user_id=3131144855, since_id=loadMostRecentTweet(), count=20)
    bodies  = []
    mostRecent = 0
    for tweet in tweets:
        if tweet.id > mostRecent:
            mostRecent = tweet.id
        bodies.append(tweet.text)
    saveMostRecentTweet(id)
    return bodies