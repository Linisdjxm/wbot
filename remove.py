import wlogin
import requests
import urllib.request
import re

#S = requests.Session()

URL = "https://zh.wikipedia.org/w/api.php"
#URL2 = "https://www.wikidata.org/w/api.php"
#URL3 = "localhost/api.php"

rdt = wlogin.login()
CSRF_TOKEN = rdt[0]
S = rdt[1]
#S2 = rdk[1]
while True:
    PARAMS = {
    "action": "query",
    "cmtitle": "Category:带有简短描述的條目",
    "cmlimit": "500",
    "list": "categorymembers",
    "format": "json"
    }
    
    R = S.get(url=URL, params=PARAMS)
    DATA = R.json()
    
    PAGES = DATA['query']['categorymembers']
    if(PAGES == []):
        print("Done")
        break
    for page in PAGES:
        paget = page["title"]
        urlstr1 = r"https://zh.wikipedia.org/w/api.php?action=query&prop=revisions&titles="
        urlstr2 = r"&rvslots=*&rvprop=content&formatversion=2&format=json"
        rec = re.compile(r'\{\{(?P<name>[Ss]hort description[\S]*?)\}\}')
        urlstr3 = urlstr1 + paget + urlstr2
        html = dict((S.get(urlstr3)).json())
        html2 = html["query"]["pages"][0]["revisions"][0]["slots"]["main"]["content"]
        html3 = re.sub(rec,r'<!--\g<name>-->',html2)
        PARAMS_3 = {
            "action": "edit",
            "title": paget,
            "token": CSRF_TOKEN,
            "format": "json",
            "text": html3,
            "summary": "Remove Template:Short description"
        }
        #xs = re.findall(rec,html2)[0][18:]
        #print(xs)
        R = S.post(URL, data=PARAMS_3)
        DATA = R.json()
        print(DATA)

