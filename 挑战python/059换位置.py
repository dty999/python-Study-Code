"""M个人围成一圈，每分钟相邻的两个人可以交换位置（只能有一对交换）。
现在给你一个正整数n(0 < n < 1000)，求使n个人的顺序颠倒(即每个人左边相邻的人换到右边，右边相邻的人换到左边）所需的最少时间（分钟数）。
如：n=4, 输出2."""

n = 4
def myf(n):
    print (sum([min(i,n-1-i) for i in range(1,n)]))


def otherf(n):
    if n%2 == 0:
        return (n-2)/2*((n-2)/2+1)
    else:
        return ((n-1)/2)*((n-1)/2)

for i in range(1,1000):
    if myf(i) == otherf(i):
        pass