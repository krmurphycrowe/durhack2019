import flask, tweepy, os, json, uwu, datetime
from flask import request
from flask_cors import CORS

app = flask.Flask(__name__)
CORS(app)

def getBowisTweets():
    print("Regenerating cache")
    """Returns list of text bodies of Boris Johnson's twitter feed."""
    cKey = os.environ['cKey']
    cSecret = os.environ['cSecret']
    key1 = os.environ['key1']
    key2 = os.environ['key2']

    # creates auth, which is needed to access the api
    auth = tweepy.OAuthHandler(cKey, cSecret)
    auth.secure = True
    auth.set_access_token(key1, key2)

    # accesses api and posts status
    tAPI = tweepy.API(auth)
    tweets = tAPI.user_timeline(user_id=3131144855, count=200, tweet_mode="extended")
    # Gets up to the 20 most recent tweets from bojo's twitter
    bodies = [] # Creates an empty list to store the bodies (not as suspicious as it sounds)
    times = []
    for tweet in tweets: # For every tweet
        try: # So basically tweepy is really dumb and the only way to tell if it's a retweet or not is to use try/except
            bodies.append(tweet.retweeted_status.full_text) # Append the retweeted status
        except AttributeError: # Yada yada tweepy is dumb
            bodies.append(tweet.full_text) # Append the text of the tweet
        ttime = tweet.created_at

        if len(str(ttime.minute)) == 1:
            newtime = str(ttime.hour) + ":0" + str(ttime.minute) + ", " + str(ttime.day) + "/" + str(ttime.month) + "/" + str(ttime.year)
        else:
            newtime = str(ttime.hour) + ":" + str(ttime.minute) + ", " + str(ttime.day) + "/" + str(ttime.month) + "/" + str(ttime.year)
        times.append(newtime)
    newbod = [] # Creates a list for the processed bodies (again not as sus as it sounds)
    for body in bodies: # For every tweet body we have
        if not body.startswith(".@BorisJohnson"): # If it's not funky retweet
            newbod.append(body) # Append the body
    uwus = []
    for body in newbod:
        uwus.append(uwu.uwuMe(body))
    return (uwus, times) # Tweepy fetches them most-recent first and we want most-recent last, so we flip the list

cachedTweets = getBowisTweets()
cachedTime = datetime.datetime.now()

@app.route("/api/v1/tweets", methods=["GET"])
def api_id():
    global cachedTweets
    global cachedTime
    if "page" in request.args:
        page = int(request.args["page"])
    else:
        return "Error: no page specified"

    if datetime.datetime.now().timestamp() - cachedTime.timestamp() > 300:
        cachedTweets = getBowisTweets()
        cachedTime = datetime.datetime.now()

    selected = (cachedTweets[0][(page-1)*20:page*20],cachedTweets[1][(page-1)*20:page*20])

    return json.dumps(selected)

@app.route("/")
def index():
    return "<h1> LOL LIMEWIRE SERVER IS UP XDDDDD UWU</h1>"

if __name__ == '__main__':
    app.run()