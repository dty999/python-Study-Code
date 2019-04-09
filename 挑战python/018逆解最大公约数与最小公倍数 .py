"""我们经常遇到的问题是给你两个数，要你求最大公约数和最小公倍数。\
    今天我们反其道而行之，给你两个数a和b，计算出它们分别是哪两个数的最大公约数和最小公倍数。\
        输出这两个数，小的在前，大的在后，以空格隔开。若有多组解，输出它们之和最小的那组。\
            注：所给数据都有解，不用考虑无解的情况。

例如：a=3, b = 60

则输出：12 15"""

def my_gcd(i,j):
    if i < j:
        i,j = j,i
    while j != 0:
        temp = i % j 
        i = j
        j = temp
    return i

a = 3
b = 60
s = [0,0,0]

if a > b:
    max,min = a,b
else:
    max,min = b,a

for i in range(min,max+1):
    for j in range(i,max+1):
        if my_gcd(i,j) == min and i*j == min*max:
            if s[0] > i+j or s[0] == 0:
                s = [i+j,i,j]
print(str(s[1])+' '+str(s[2]))
