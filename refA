import wlib
import requests
import urllib.request
import urllib.parse
import re
import os

temlist = ["FootnotesSmall"
,"註腳"
,"注脚"
,"參考資料"
,"RefList"
,"References"
,"Refs"
,"REFLIST" 
,"参考列表"
,"脚注"
,"reflist"
,"Reflist"
,"refList"
,"refs"
,"references"
,"rEFLIST"
,"footnotesSmall"]

URL = "https://zh.wikipedia.org/w/api.php"

rdt = wlib.login()
CSRF_TOKEN = rdt[0]
S = rdt[1]

rstr = r"https://checkwiki.toolforge.org/cgi-bin/checkwiki.cgi?project=zhwiki&view=bots&id=3&offset=0"
n1 = urllib.request.urlopen(rstr)
raw = n1.read()
listr = raw.decode("utf-8").split('\n')
listx = []
for item in listr:
    if(item != ""):
        if(item[0] != '<'):
            listx.append(item)
    else:
        continue
flag = 0
for item in listx:
    #print(item)
    wt = wlib.getwt(urllib.parse.quote(item),S)
    count = 0
    while count < len(temlist):
        re1 = r'\{\{(Template:)?(T:)?(template:)?(t:)?' + temlist[count]
        re2 = re.compile(re1)
        try:
            found = (re2.search(wt).group())[0:]
            print("FOUND: " + temlist[count] + " in " + item)
            os.system('echo * ' + item + ' >> list.txt')
            flag = 0
            break
        except AttributeError:
            #print("NOT FOUND: " + item)
            flag = 1
        count += 1
    if flag == 1:
        print("NOT FOUND: " + item)
        flag = 0
