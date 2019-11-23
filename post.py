import tweepy, json

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


def post(text):
    try:
        # loads json details file and saves in variables
        filename = 'keys'
        key = 'DETAILS'
        file = load_file(filename, key)
        cKey = file["CONSUMER_KEY"]
        cSecret = file["CONSUMER_SECRET"]
        key1 = file["KEY1"]
        key2 = file["KEY2"]

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

