"""给你一个正整数列表 L, 输出L内所有数字的乘积末尾0的个数。(提示:不要直接相乘,数字很多,相乘得到的结果可能会很大)。

例如： L=[2,8,3,50],

将L里的数字全部相乘，得到的数中末尾有几个零
[分解成2*5]
则输出：2"""

L = [2,5,10,8,40]
i2 = 0
i5 = 0
for item in L:
    while item % 2 == 0:
        i2 +=1
        item = item // 2
    while item % 5 == 0:
        i5 +=1
        item = item // 5
print(min(i2,i5))