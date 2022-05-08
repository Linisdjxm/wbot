import requests
import urllib.request
import re
def login(lgun,lgpw,URL="https://zh.wikipedia.org/w/api.php"):
    S = requests.Session()
    
# Retrieve login token first
    PARAMS_0 = {
        'action':"query",
        'meta':"tokens",
        'type':"login",
        'format':"json"
    }

    R = S.get(url=URL, params=PARAMS_0)
    DATA = R.json()

    LOGIN_TOKEN = DATA['query']['tokens']['logintoken']

    print(LOGIN_TOKEN)

# Send a post request to login. Using the main account for login is not
# supported. Obtain credentials via Special:BotPasswords
# (https://www.mediawiki.org/wiki/Special:BotPasswords) for lgname & lgpassword

    PARAMS_1 = {
        'action':"login",
        'lgname':lgun,
        'lgpassword':lgpw,
        'lgtoken':LOGIN_TOKEN,
        'format':"json"
    }

    R = S.post(URL, data=PARAMS_1)
    DATA = R.json()

    print(DATA)

    PARAMS_2 = {
        "action": "query",
        "meta": "tokens",
        "format": "json"
    }

    R = S.get(url=URL, params=PARAMS_2)
    DATA = R.json()

    CSRF_TOKEN = DATA['query']['tokens']['csrftoken']
    return [CSRF_TOKEN,S]
