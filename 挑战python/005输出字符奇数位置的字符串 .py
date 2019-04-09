"""
给你一个字符串 a， 输出a中奇数位置字符构成的字符串（位置编号从1开始）。

例如：a=‘xyzwd’

则输出:xzd

"""

a = "abcdefghilmnopqrstxyz"
print(a[0:len(a):2])
"""最优解"""
print(a[::2])

print(a[0:-1:2])#这样不可以,因为不包括最后一个字符