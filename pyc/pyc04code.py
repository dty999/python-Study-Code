import re
import urllib.request as request
import socket

socket.setdefaulttimeout(180)
next = '80109'
url = ''
myresponse = ''
while next:
    url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=" + next
    res = request.urlopen(url)
    myresponse = res.read().decode('utf-8')
    if re.findall(r'\.html$',myresponse):
        break
    code = re.findall(r'\d+$',myresponse)
    if (code):
        next = code[0]
    else:
        next = str(int(next)//2)
    print(next)
print(url)
print(myresponse)


