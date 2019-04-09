"""给你一个字符串a和一个正整数n,判断a中是否存在长度为n的回文子串。如果存在，则输出YES，否则输出NO。
回文串的定义：记串str逆序之后的字符串是str1，若str=str1,则称str是回文串，如"abcba"."""
a = 'abchhdfgfbca'
n = 3
length = len(a)
ret = 'NO'
for i in range(0,length - n +1):
    if a[i:i+n] == a[i:i+n][::-1]:
        ret = 'YES'
        break
print(ret)

