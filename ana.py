import wlib
import requests
import urllib.request
import re

#S = requests.Session()

URL = "https://zh.wikipedia.org/w/api.php"

rdt = wlib.login()
CSRF_TOKEN = rdt[0]
S = rdt[1]

year = 2021
mon = 1
la = []
rdic = {}
rea = re.compile(r"'''\[\[[\S]*?\|")
reb = re.compile(r"\| type = [^\f\n\r\t\v\.]*")
rec = re.compile(r"(?P<nameA>\[\[[^\]]*?)\|'''(?P<nameB>[\S]*?)'''\]\]")

while mon <= 12:
    pname = 'Wikipedia:新条目推荐/存档/' + str(year) + '年' + str(mon) + '月'
    #text = wlib.getwt(pname,S).replace(r"]]'''","").replace(r"''']]","")
    text = wlib.getwt(pname,S)
    text = re.sub(rec,r"'''\g<nameA>|\g<nameB>]]'''",text)
    #text = re.sub(rec,r"",text)
    text = wlib.getwt(pname,S).replace(r"]]'''","")
    la += re.findall(rea,text)
    mon += 1
    #print(la)
index = 0
print("NOTICE: STAGE 1 DONE.")
while index < len(la):
    la[index] = la[index][5:-1]
    index += 1
#print(la)
index = 0
for item in la:
    #print(item)
    tpage = 'Talk:' + wlib.dwred(item,S,debug=1)
    text = wlib.getwt(tpage,S,debug=2)
    try:
        tpa = re.findall(reb,text)[0][9:].lower()
    except:
        tpa = "NULL"
    if(tpa == ""):
        tpa = "NULL"
    if tpa in rdic:
        rdic[tpa].append(item)
    else:
        rdic[tpa] = [item,]
    #print(tpa)
    index += 1
    if(index % 10 == 0):
        print("NOTICE: " + str(index) + " PAGES.")
print(rdic)
