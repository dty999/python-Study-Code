"""还记得中学时候学过的杨辉三角吗？具体的定义这里不再描述，你可以参考以下的图形：

1

1 1

1 2 1

1 3 3 1

1 4 6 4 1

1 5 10 10 5 1

..............

先在给你一个正整数n，请你输出杨辉三角的前n层

注意：层数从1开始计数,每层数字之间用一个空格隔开，行尾不要有空格。

如n=2,则输出：

1

1 1


杨辉三角最本质的特征是，它的两条斜边都是由数字1组成的，而其余的数则是等于它肩上的两个数之和。


"""

n = 8
L = []

for i in range(1,n+1):
    l = []
    if i == 1:
        L.append([1])
        continue
    if i == 2:
        L.append([1,1])
        continue
    for j in range(0,i):
        if j==0:
            l.append(1)
            continue
        if j == i-1:
            l.append(1)
            continue
        l.append(L[-1][j-1] + L[-1][j])
    L.append(l)
    

for l in L:
    print(' '.join(map(str,l)))