"""记得有一次全班去唱K, 其中有个活动是情歌对唱. 具体操作流程是这样的:
准备好 21 个阄(我们班 15 男 6 女), 其中只有两个是有标记的, 每人随意抓取一个, 最后取到有标记的阄的两个人去点首情歌对唱.
旁边一哥们儿幽幽地对我说, 看来搅基真是神的安排啊, 你看我们班的男女人数, 搅基的几率 C(15,2)/C(21,2) 刚好是 1/2.
给跪了, 这哥们儿对数字太敏感了, 简直是拉马努金转世啊. 不过我随之想到一个问题: (21, 15) 真的是神的唯一安排吗? 其实不是的,
神还有很多类似的安排. 比如 (4, 3), 显然 C(4,2)/C(3,2) 也等于 1/2, 当然还有 (120, 85) 等等等等.
神的安排太多太多了, 如果我们定义 (n, m) 是一个安排(其中 1 < m < n), 而如果 C(m,2)/C(n,2) = 1/2, 它就是神的安排.
现在的问题是, 给你一个不大于 10^9 的正整数 N, 有多少组神的安排 (n, m) 满足 n <= N 呢?"""
#佩尔方程
N = 10**9
l = []
x = 1
y = 1
while x<=N:
    l.append((x,y))
    x = 3*l[-1][0] + 4*l[-1][1]
    y = 2*l[-1][0] + 3*l[-1][1]
print(l)
x=1
y=1
n=0
while (x+1)/2<=N:
    a=x
    b=y
    x=3*a+4*b
    y=2*a+3*b
    n+=1
print(n-1)