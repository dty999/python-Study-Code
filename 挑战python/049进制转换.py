"""给你一个十进制数a，将它转换成b进制数,如果b>10,用大写字母表示（10用A表示，等等）
a为32位整数，2 <= b <= 16
如a=3,b = 2, 则输出11"""
a,b = -17,2
l = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
lstr = []
sign = ''
if a < 0:
    a = -a
    sign = '-'
elif a == 0:
    lstr.append('0')

while a != 0:
    lstr.append(l[a % b])
    a = a // b

lstr.append(sign)
print(''.join(lstr[::-1]))
