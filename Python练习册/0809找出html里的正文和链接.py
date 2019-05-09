#一个HTML文件，找出里面的正文
from bs4 import BeautifulSoup
import requests





def sechBodyUrl(path):
    with open(path,encoding='utf-8') as fp:
        text = BeautifulSoup(fp, 'lxml')
        urls = text.findAll('a')
        for u in urls:
            print(u['href'])
        content = text.get_text().strip('\n')
    return content


f1 = requests.get('https://www.baidu.com/')
f1.encoding = 'utf-8'
f = f1.text
text = BeautifulSoup(f,'lxml')
content = text.get_text().strip('\n')
print(content)


urls = text.findAll('a')
for u in urls:
    print(u['href'])




