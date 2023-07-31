plist = ["User:Ning-Bot/Task/Example"]

import wlib
import re

URL = "https://zh.wikipedia.org/w/api.php"

rdt = wlib.login()

CSRF_TOKEN = rdt[0]
S = rdt[1]
re3 = re.compile(r'ikisource')
re4 = re.compile(r'==[\s]*?(?P<q>((参考)|(參考))[^=]*?)==(?!=)')
re5 = re.compile(r'==[\s]*?((延伸阅读)|(延伸閱讀))[^=]*?==(?!=)')
count0 = 0
for item in plist:
    '''if item in dnlist:
        print(item + ": Skip")
        continue'''
    wt = wlib.getwt(item,S)
    if(wt == "NULL"):
        print("Error")
        continue
    chapters = re3.findall(wt)
    if chapters != []:
        print(item + ": False A")
    else:
        ch2 = re4.search(wt)
        flag1 = 0
        flag2 = 0
        if(ch2 != None):
            flag1 = 1
        ch3 = re5.findall(wt)
        if(ch3 != []):
            flag2 = 1
        if(flag1 == 0 and flag2 == 0):
            print(item + ": False B")
        elif(flag2 == 0):
            print(item + ": True   Type: A")
            D = wlib.wrwt(item,S,re.sub(re4,r'== 延伸阅读 ==\n{{Wikisource further reading}} \n\n== \g<q> ==\n',wt,count=1),'使用维基数据',CSRF_TOKEN)
            print(D)
        else:
            print(item + ": B")
            continue
