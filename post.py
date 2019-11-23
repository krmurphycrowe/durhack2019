import tweepy, json, os


def post(text):
    try:
        # loads json details file and saves in variables

        cKey = os.environ['cKey']
        cSecret = os.environ['cSecret']
        key1 = os.environ['key1']
        key2 = os.environ['key2']

        # creates auth, which is needed to access the api
        auth = tweepy.OAuthHandler(cKey, cSecret)
        auth.secure = True
        auth.set_access_token(key1, key2)

        # accesses api and posts status
        api = tweepy.API(auth)
        status = api.update_status(text)
        api.update_status(status=status)
    except tweepy.error.TweepError:
        pass

