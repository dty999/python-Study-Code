"""给你两个整数a和b（-10000<10000），请你判断是否存在两个整数，他们的和为a，乘积为b。 
若存在，输出Yes,否则输出No
例如：a=9,b=15, 此时不存在两个整数满足上述条件，所以应该输出No。"""
a = 5
b = 6
import math
def jie(a,b,c):

    x1 = (-b + math.sqrt(b**2 - 4*a*c))/2*a
    if x1-int(x1) == 0:
        return 'Yes'
    else:
        return 'No'

print(jie(1,-a,b))