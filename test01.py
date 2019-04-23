import requests
from bs4 import BeautifulSoup
import string


def getcontent(url):

    html = requests.get(url).content.decode('utf-8')

    soup = BeautifulSoup(html, 'lxml')
    print(url)
    if soup.title is None:
        with open('errlink.txt','a+',encoding='utf-8') as f :
            f.write(url + '\n')



    if soup.title is None or '历史人物_历史名人_中国历史人物大全_历史人物百科_名人介绍与评价' in str(soup.title.string) or str(soup.title.string) == 'None':
        return None,None,None

    shengzu = '【生卒】：不详'
    jieshao = '不详'
    name = None

    name = soup.find('div', id='ArtContent').find_next().string
    name = '【姓名】：'+str(name)
    for i in soup.find('span').find_all('p'):
        content = str(i)
        if content != None:
            if '【生卒】' in content:
                shengzu = str(i.string)
                continue
            if '【介绍】' in content:
                jieshao = '【介绍】：' + str(i.next_sibling)
                break
            if len(content) > 30:
                jieshao = '【介绍】：' + str(i)
                break
    return name, shengzu, jieshao


startnum = 0

def linkgen():
    global startnum
    with open('num.txt','rt',encoding='utf-8') as f:
        startnum = int(f.read())
    for i in range(startnum,10,1):
        for j in range(24):
            link = str(i) + string.ascii_lowercase[j]
            yield link
        startnum = i
    return


for i in linkgen():
    url = 'http://www.guoxuedashi.com/renwu/' + str(i) + '/'
    name, shengzu, jieshao  = getcontent(url)
    with open('num.txt','wt',encoding='utf-8') as f:
        f.write(str(startnum))


    if name == None:
        continue
    print(name)
    print(shengzu)
    print(jieshao)
