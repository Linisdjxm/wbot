import re
import time
import wlib
import os
import requests

URL=r"https://zh.moegirl.org.cn/api.php"
URL2=r"https://zh.moegirl.org.cn/zh/"

re1 = r'(?<=<a class="mw-selflink selflink">)[\S\s]*?(?=<)'
new_ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36"
#sorry!
headers = {"User-Agent": new_ua}
rdt = wlib.login(URL)
CSRF_TOKEN = rdt[0]
S = rdt[1]
titles = ["Example"]
for item in titles:
    text = wlib.getwt(item,S,URL=URL,URL2=URL2,debug=1)
    text2 = requests.get(r"https://zh.moegirl.org.cn/zh/" + item,headers=headers)
    text2.encoding = "utf-8"
    text2 = text2.text
    resultA = re.findall(re1,text2)
    if(resultA):
        print(item + ": TRUE")
        for item2 in resultA:
            print(item2)
            resultB = re.findall(r'\[\[[\S\s]*?' + item2 + r"\]\]",text)
            #print(resultB)
            #text = re.sub(r"\[\[(?P<tag1>" + item + r")\]\]",r"\g<tag1>",text)
            text = text.replace(resultB[0],item2)
        wlib.wrwt(item,S,text,r"test",CSRF_TOKEN,URL)
        print(text)
        break
    else:
        print(item + ": FALSE")
