import tweepy, json, pull, post, uwu, time


if __name__ == '__main__':
    pass

def makeTweets(tweetBodies):
    i = 0
    while i < len(tweetBodies):
        try:
            post.post(tweetBodies[i])
            i += 1
        except tweepy.RateLimitError:
            time.sleep(60)
