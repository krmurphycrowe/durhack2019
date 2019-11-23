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
        status = api.update_status(text)
        api.update_status(status=status)
    except tweepy.error.TweepError:
        pass

post('first tweet uwu')

