"""给你一个正整数列表 L, 判断列表内所有数字乘积的最后一个非零数字的奇偶性。如果为奇数输出1,偶数则输出0.。

例如：L=[2,8,3,50]

则输出：0"""
L=[2,8,3,50]
i2 = 0
i5 = 0
for item in L:
    while item % 2 ==0:
        i2 += 1
        item = item // 2
    while item % 5 ==0:
        i5 += 1
        item = item //5
if i2 > i5:
    print(0)
else:
    print(1)
