import re
import time
import wlib
import os
import requests

URL=r"https://zh.moegirl.org.cn/api.php"
URL2=r"https://zh.moegirl.org.cn/"

rdt = wlib.login("Example",r"Example",URL)

CSRF_TOKEN = rdt[0]
S = rdt[1]
todo = []
ttext = {}
titles = ["TEST"]
for item in titles:
    text = wlib.getwt(item,S,URL=URL,URL2=URL2)
    ttext[item] = text
    if((r"[[" + item + r"]]") in text):
        print(item + ": TRUE")
        todo.append(item)
    else:
        print(item + ": FALSE")

for item in todo:
    text = ttext[item]
    text = re.sub(r"\[\[(?P<tag1>" + item + r")\]\]",r"\g<tag1>",text)
    wlib.wrwt(item,S,text,r"Auto: Replace \[\[" + item + "\]\] -> " + item,CSRF_TOKEN,URL)
    
