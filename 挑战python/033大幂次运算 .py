"""给你两个正整数a(0 < a < 100000)和n(0 <= n <=100000000000)，计算(a^n) % 20132013并输出结果"""

import time
a = 9999933
n = 234567894

def pow_mod(a,n,mod):
    res = 1
    while n > 0 :
        if n % 2 == 1: res = res * a % mod
        a = a * a % mod
        n >>= 1
    return res

start = time.clock()
print(pow(a,n,20132013))
print(time.clock()-start)
start = time.clock()
print(pow_mod(a,n,20132013))
print(time.clock()-start)
