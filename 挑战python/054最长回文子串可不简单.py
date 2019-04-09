"""记得一副有趣的对联: "雾锁山头山锁雾, 天连水尾水连天", 上联和下联都是回文的.

当然类似的还有: "上海自来水水来自海上, 山西悬空寺寺空悬西山".

回文是什么意思? 就是把内容反过来读也是和原来一样的, 譬如 abccba, xyzyx, 这些都是回文的.

然而我们更感兴趣的是在一个英文字符串 L 中, 怎么找出最长的回文子串.

例如 L = "caayyhheehhbbbhhjhhyyaac", 那么它最长的回文子串是 "hhbbbhh".

这个任务看似简单, 但是如果我告诉你 L 的长度可能会接近 10^4, 问题似乎就变麻烦了.

不管怎么说, 加油吧骚年."""

from collections import deque

s = 'abccba'
q = deque()
length = len(s)
anwer = ''
#去除s太短的情况
if length ==1 or length == '':
    anwer = s
if length ==2:
    if s[0] == s[1]:
        anwer = s
    else:
        anwer = s[0]

#s > 2时

if length  > 2:
    #先将所有两个三个形成的回文串找出来加入到队列中,
    for i in range(0,length-2):
        if s[i] == s[i+1]:
            q.appendleft((i,i+1))
        if s[i] == s[i+2]:
            q.appendleft((i,i+2))
    if s[-1] == s[-2]:
        q.append((length-2,length-1))
    
    maxlen = 0
    res = []
    while len(q) > 0:
        tr = q.pop()
        start,end = tr
        res = (start,end+1)
        if end+1<=length-1 and start-1 >= 0 :
            if s[end+1] == s[start-1]:
                q.appendleft((start-1,end+1))

    anwer = s[res[0]:res[1]]

print(anwer)
