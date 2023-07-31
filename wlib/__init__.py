import requests
from urllib import request
from urllib.parse import unquote
import re
import time

headers={'User-Agent':'Ning-Bot/0.0'}

def login(lgun,lgpw,URL="https://zh.wikipedia.org/w/api.php"):
    S = requests.Session()
    
# Retrieve login token first
    PARAMS_0 = {
        'action':"query",
        'meta':"tokens",
        'type':"login",
        'format':"json"
    }

    R = S.get(url=URL, params=PARAMS_0,headers=headers)
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

    R = S.post(URL, data=PARAMS_1,headers=headers)
    DATA = R.json()

    print(DATA)

    PARAMS_2 = {
        "action": "query",
        "meta": "tokens",
        "format": "json"
    }

    R = S.get(url=URL, params=PARAMS_2,headers=headers)
    DATA = R.json()

    CSRF_TOKEN = DATA['query']['tokens']['csrftoken']
    return [CSRF_TOKEN,S]

def getwt(pagename,S,debug = 0):
    url1 = r"https://zh.wikipedia.org/w/api.php?action=query&prop=revisions&titles="
    url2 = r"&rvslots=*&rvprop=content&formatversion=2&format=json"
    try:
        html = dict((S.get(url1 + pagename + url2,headers=headers)).json())
    except ConnectionResetError:
        print("ERROR: RST")
        time.sleep(5)
        html = dict((S.get(url1 + pagename + url2,headers=headers)).json())
    if debug == 1:
        print (html)
    try:
        html2 = html["query"]["pages"][0]["revisions"][0]["slots"]["main"]["content"]
    except:
        try:
            pagenamex = unquote(requests.get("https://zh.wikipedia.org/wiki/" + pagename).url[30:],'utf-8')
            if (debug == 2):
                print("REDIRECT(A):" + pagenamex)
            html = dict((S.get(url1 + pagenamex + url2,headers=headers)).json())
        except ConnectionResetError:
            print("ERROR: RST")
            time.sleep(5)
            pagenamex = unquote(requests.get("https://zh.wikipedia.org/wiki/" + pagename).url[30:],'utf-8')
            if (debug == 2):
                print("REDIRECT(A):" + pagenamex)
            html = dict((S.get(url1 + pagenamex + url2,headers=headers)).json())
        try:
            html2 = html["query"]["pages"][0]["revisions"][0]["slots"]["main"]["content"]
        except:
            print("ERROR: " + pagenamex)
            html2 = "NULL"
    return html2
def dwred(title, S, debug=0):
    url1 = r'https://zh.wikipedia.org/w/api.php?action=query&format=json&titles='
    url2 = r'&redirects=1&formatversion=2'
    try:
        html = dict((S.get(url1 + title + url2,headers=headers)).json())
    except ConnectionResetError:
        print("ERROR: RST")
        time.sleep(5)
        html = dict((S.get(url1 + title + url2,headers=headers)).json())
    if ('redirects' in html["query"]):
        ntitle = html["query"]["redirects"][0]["to"]
    else:
        ntitle = title
    if(ntitle != title and debug != 0):
        print("REDIRECT(B): " + ntitle)
    return ntitle
def wrwt(page,S,text,summary,CSRF_TOKEN):
    URL = "https://zh.wikipedia.org/w/api.php"

    PARAMS_3 = {
    "action": "edit",
    "title": page,
    "token": CSRF_TOKEN,
    "format": "json",
    "bot": True,
    "summary":summary,
    "text": text
    }

    R = S.post(URL, data=PARAMS_3)
    DATA = R.json()
    
    return(DATA)