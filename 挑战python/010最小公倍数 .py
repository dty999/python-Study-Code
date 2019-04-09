"""给你两个正整数a和b， 输出它们的最小公倍数。

例如：a = 3, b = 5

则输出：15"""
a = 3
b = 5
max = a if a > b else b
while 1:
    if max % a ==0 and max %b == 0:
        break
    max += 1
print(max)