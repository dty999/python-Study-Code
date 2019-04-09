"""有两堆石子，数量任意，可以不同。游戏开始由两个人轮流取石子。游戏规定，每次有两种不同的取法，
一是可以在任意的一堆中取走任意多的石子；二是可以在两堆中同时取走相同数量的石子。最后把石子全部取完者为胜者。
现在给出初始的两堆石子的数目a和b，如果轮到你先取，假设双方都采取最好的策略，问最后你是胜者还是败者。
如果你是胜者，输出Win,否则输出Loose。
例如，a=3,b=1, 则输出Win(你先在a中取一个，此时a=2，b=1,此时无论对方怎么取，你都能将所有石子都拿走).

威佐夫博弈
即 a[k] = (int)  （(b[k] - a[k])*1.618） 注：这里的int是强制类型转换，注意这不是简单的四舍五入，假如后面的值是3.9，转换以后得到的不是4而是3，也就是说强制int类型转换得到的是不大于这个数值的最大整数。

"""

import math
a,b = 3,5

a,b = min(a,b),max(a,b)

r = (math.sqrt(5.0)+1)/2
print(r)
if int((b-a) * r) != a:#注意取整
    print('Win')
else:
    print('Loose')

def wythoff_gen(start = 0,last = 10):
    a,b,n = 0,0,0
    all_num = set()
    all_num.add(0)
    while n < last:
        yield (a,b)
        n = n+1
        all_num.add(a)
        all_num.add(b)
        for i in range(a,b):
            if i not in all_num:
                a,b = i,i+n
                break
        else:
            a,b = b+1,b+1+n


for i in wythoff_gen(0,11):
    print(i)




