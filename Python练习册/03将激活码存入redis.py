import string
import random
import redis

def cdkey(num):
    s = set()
    while len(s) < num:
        code = random.sample(string.ascii_uppercase + string.digits, 6)
        s.add(''.join(code))
    return s


conn = redis.Redis(host='localhost',port = 6379,decode_responses=True)

cdkey_dict = {key:value for key,value in enumerate(list(cdkey(200)))}


flag = conn.hmset('num',cdkey_dict)

print(conn.hvals("num"))

