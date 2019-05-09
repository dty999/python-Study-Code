import pyautogui
import time
from threading import Timer
from PIL import Image


fangwan = False


def shuaxin():
    if bofang == True:
        pyautogui.click(465, 340)

        pyautogui.click(800, 550)

    t = Timer(600, shuaxin)
    t.start()


def panduan():
    try:
        x, y = pyautogui.locateCenterOnScreen('刷课\\pic\\tijiao.png')
    except:
        pass
    else:
        pyautogui.click(160, 177)
        time.sleep(2)
        pyautogui.click(x, y)
        print('提交')
        time.sleep(2)
        print('继续。。')
        pyautogui.click(x, y)
        try:
            i, j = pyautogui.locateCenterOnScreen('刷课\\pic\\cuowu.png')
        except:
            pass
        else:
            print("回答错误。。。")
            pyautogui.click(170, 206)
            time.sleep(3)
            print('......')
            pyautogui.click(924, 506)
            time.sleep(3)
            pyautogui.click(924, 506)

    finally:
        t = Timer(30, panduan)
        t.start()


#如果播放结束返回False
def shotpoint():
    im = pyautogui.screenshot(region=(300,200, 700, 500))
    time.sleep(10)
    im2 = pyautogui.screenshot(region=(300,200, 700, 500))
    for i in range(100,110):
        p = im.getpixel((i,100))
        print(p)
        p2 = im2.getpixel((i,100))
        print(p2)
        if p == p2 :
            continue
        else:
            return True
    else:
        return False



def back():
    print('进入返回函数')
    try:
        x, y = pyautogui.locateCenterOnScreen('刷课\\pic\\zhangjie.png')
    except :
        print('没有找到播放，尝试退一下')
        pyautogui.click(300,300)
        time.sleep(1)
        pyautogui.click(22,62)
        time.sleep(3)
        try:
            x, y = pyautogui.locateCenterOnScreen('刷课\\pic\\zhangjie.png')
        except:
            print('找不到播放界面了')
        else:
            pyautogui.click(27,88)#退到列表
            print('退回播放列表')
    else:
        pyautogui.click(27,88)#退到列表
        print('退回播放列表')


def next():
    print('进入next')
    global bofang
    try:
        x, y = pyautogui.locateCenterOnScreen('刷课\\pic\\two.png')
    except:
        print('没找到two。。。')
        bofang = False
    else:
        pyautogui.click(x,y)
        
        time.sleep(3)
        pyautogui.click(465,313)
        bofang = True
    print('结束next')
    



#判断是否结束并返回播放列表
def jieshu():
    print('进入结束函数。。。')
    global fangwan
    fangwan = shotpoint()
    if fangwan == False:
        back()
        time.sleep(5)
        next()
    else:
        pass
    print('完成结束函数。。。')
    t = Timer(600, jieshu)
    t.start()






jieshu()
time.sleep(50)


shuaxin()

time.sleep(50)

panduan()

