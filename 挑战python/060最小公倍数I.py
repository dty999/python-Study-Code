"""给你一个正整数list L, 如 L=[2,8,3,50], 求列表中所有数的最小公倍数(不用考虑溢出问题）。
如L=[3,5,10], 则输出30"""
L=[3,5,10]
def gbs(a,b):
    a,b = max(a,b),min(a,b)
    var1 = a*b
    c = a % b
    while c != 0:
        a = b
        b = c
        c = a % b
    return var1 / b
temp = L[0]
for i in range(0,len(L)):
    temp = gbs(temp,L[i])

print(temp)