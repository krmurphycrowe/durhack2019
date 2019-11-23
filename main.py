import tweepy, json, pull, post, uwu, time

filename = 'keys'
key = 'DETAILS'
file = post.load_file(filename, key)
cKey = file["CONSUMER_KEY"]
cSecret = file["CONSUMER_SECRET"]
key1 = file["KEY1"]
key2 = file["KEY2"]


def makeTweets(tweetBodies):
    i = 0
    while i < len(tweetBodies):
        try:
            post.post(tweetBodies[i])
            i += 1
        except tweepy.RateLimitError:
            print("Ratelimited - sleeping for 1s")
            time.sleep(60)


if __name__ == '__main__':

    auth = tweepy.OAuthHandler(cKey, cSecret)
    auth.secure = True
    auth.set_access_token(key1, key2)

    api = tweepy.API(auth)

    while True:

        newTweets = pull.getBowisTweets(api)

        owoTweets = []

        for tweet in newTweets:
            owoTweets.append(uwu.uwuMe(tweet))

        makeTweets(owoTweets)

        time.sleep(600)

