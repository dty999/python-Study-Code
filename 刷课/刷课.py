import pyautogui
import time
import json

def findone(pic):
    while True:
        time.sleep(2)
        try:
            x, y = pyautogui.locateCenterOnScreen(pic, confidence=0.8)
        except:
            continue
        else:
            return x, y


def finall(pic):
    while True:
        time.sleep(2)
        try:
            L = [(i[0], i[1])
                 for i in pyautogui.locateAllOnScreen(pic, confidence=0.8)]

        except:
            continue
        else:
            return L


webbrowser.open('https://mooc1-1.chaoxing.com/mycourse/studentstudy?chapterId=143053440&courseId=203660835&clazzid=7299927&enc=2c2a45ed22545e029f15cb758438d97a')

with open("ini.json", "rt", encoding='utf-8') as f:
    zhangjie = json.load(f)['zhangjie']
    print(zhangjie)

findone('cgjz.png')
time.sleep(3)
pyautogui.moveTo(100, 100)
pyautogui.press('down', presses=2, interval=0.25)
time.sleep(2)
pyautogui.click(500, 500)  # 开始播放
findone('rwdwc.png')
L = finall('2.png')
pyautogui.click(L[zhangjie])
x, y = findone('xxmb.png')
pyautogui.click(x+100, y)
time.sleep(3)
pyautogui.press('down', presses=2, interval=1)
pyautogui.click(500, 500)
