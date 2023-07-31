import re
import time
import dateparser
import wlib
import requests

URL = "https://zh.wikipedia.org/w/api.php"
CSRF_TOKEN = rdt[0]
S = rdt[1]
limit = 10

month = "(?:January|February|March|April|May|June|July|August|September|October|November|December)"
re1 = r'''\|[^|]*?date[\s]*=[\s]*''' + month + r''' [0-9]+,[\s]*[0-9][0-9][0-9][0-9]'''
re2 = r'''\|[^|]*?date[\s]*=[\s]*''' + month + r''' [0-9][0-9][0-9][0-9]'''
re3 = r'''\|[^|]*?date[\s]*=[\s]*''' + r'''[0-9]+ ''' + month + r'''[\s]*[0-9][0-9][0-9][0-9]'''
re1a = month + r''' [0-9]+,[\s]*[0-9][0-9][0-9][0-9]'''
re2a = month + r''' [0-9][0-9][0-9][0-9]'''
re3a = r'''[0-9]+ ''' + month + r'''[\s]*[0-9][0-9][0-9][0-9]'''

re1c = re.compile(re1)
re2c = re.compile(re2)
re3c = re.compile(re3)

re1ac = re.compile(re1a)
re2ac = re.compile(re2a)
re3ac = re.compile(re3a)

PARAMS = {
    "action": "query",
    "format": "json",
    "list": "search",
    "srsearch": 'insource:/date=' + month + '/',
    "srlimit": limit
}

R = S.get(url=URL, params=PARAMS)
DATA = R.json()
print(DATA)
offsetl= 0
while "continue" in DATA.keys():
    offsetl += limit
    for item in DATA["query"]["search"]:
        title = item["title"]
        text = wlib.getwt(title,S)
        #print (text)
        #print(re1)
        res = re.findall(re1c,text)
        res2 = re.findall(re2c,text)
        res3 = re.findall(re3c,text)
        print(title + " : " + str(len(res) + len(res2) + len(res3)))
        for item2 in res:
            src = re.findall(re1ac,item2)[0]
            text = re.sub(src,dateparser.parse(src).isoformat()[:-9],text)
            print(src + " --> " + dateparser.parse(src).isoformat()[:-9])
        for item3 in res2:
            src = re.findall(re2ac,item3)[0]
            text = re.sub(src,dateparser.parse(src).isoformat()[:-12],text)
            print(src + " --> " + dateparser.parse(src).isoformat()[:-12])
        for item4 in res3:
            src = re.findall(re3ac,item4)[0]
            text = re.sub(src,dateparser.parse(src).isoformat()[:-9],text)
            print(src + " --> " + dateparser.parse(src).isoformat()[:-9])
        #print(text)
        wlib.wrwt(title,S,text,"Date Correct Test",CSRF_TOKEN,URL)
        
    
    PARAMS = {
    "action": "query",
    "format": "json",
    "list": "search",
    "srsearch": 'insource:/date=' + month + '/',
    "srlimit": limit,
    "sroffset": offsetl
    }
    R = S.get(url=URL, params=PARAMS)
    DATA = R.json()
