"""把一个偶数拆成两个不同素数的和，有几种拆法呢？
现在来考虑考虑这个问题，给你一个不超过10000的正的偶数n，
计算将该数拆成两个不同的素数之和的方法数，并输出。
如n=10，可以拆成3+7，只有这一种方法，因此输出1."""
import math
n = 10
num = 0
def isSuShu(n):
    for i in range(2,int(math.sqrt(n)+2)):
        if n%i == 0:
            return False
    return True

for i in range(3,int(n//2),2):
    if isSuShu(i) and isSuShu(n-i):
        num += 1
print(int(num))

#注意1不是素数......................