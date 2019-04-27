#你有一个目录，装了很多照片，把它们的尺寸变成都不大于 iPhone5 分辨率的大小
import os
from PIL import Image



dir = "C:\\Users\\22512\\Pictures\\Saved Pictures"


def getpicdir_list(dir):
	l = [os.path.join(dir,i) for i in os.listdir(dir) if i.endswith('.png') or i.endswith('.jpg')]
	return l


pic_list = getpicdir_list(dir)


for i in pic_list:
	pic = Image.open(i)
	w,h = pic.size
	n = w/1366 if (w/1366) >= (h/640) else h/640
	pic.thumbnail((w/n, h/n))
	pic.save('_new.'.join(i.split('.')))


 