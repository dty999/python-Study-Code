"""给你两个正整数a和b， 输出它们的最大公约数。

例如：a = 3, b = 5

则输出：1"""
a = 3
b = 5
min = b if a>b else a
for i in range(1,min+1):
    if b%i==0 and a%i == 0:
        c = i
print(c)