import requests
import hmac
import hashlib
import base64
import time
import random
import re
 
def general_basicOCR(appid,bucket,secret_id,secret_key,picpath):
   """" 通用印刷字体识别 """
   appid = appid
   bucket = bucket #参考本文开头提供的链接
   secret_id = secret_id #参考官方文档
   secret_key = secret_key #同上
   expired = time.time() + 2592000
#   onceExpired = 0
   current = time.time()
   rdm = ''.join(random.choice("0123456789") for i in range(10))
#   userid = "0"
#   fileid = "tencentyunSignTest"
   info = "a=" + appid + "&b=" + bucket + "&k=" + secret_id + "&e=" + str(expired) + "&t=" + str(current) + "&r=" + str(
   rdm) + "&u=0&f="
   signindex = hmac.new(bytes(secret_key,'utf-8'),bytes(info,'utf-8'), hashlib.sha1).digest() # HMAC-SHA1加密
   sign = base64.b64encode(signindex + bytes(info,'utf-8')) # base64转码，也可以用下面那行转码
   #sign=base64.b64encode(signindex+info.encode('utf-8'))


   url = "http://recognition.image.myqcloud.com/ocr/general"
   headers = {'Host': 'recognition.image.myqcloud.com',
      "Authorization": sign,
      }
   files = {'appid': (None,appid),
   'bucket': (None,bucket),
   'image': (picpath,open(picpath,'rb'),'image/' + picpath.split('.')[-1])
   }


   r = requests.post(url, files=files,headers=headers)
   responseinfo = r.content
   data = responseinfo.decode('utf-8')
   r_index = r'itemstring":"(.*?)"' # 做一个正则匹配
   result = re.findall(r_index, data)
   return '\r\n'.join(result)




