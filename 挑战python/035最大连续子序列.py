"""给你一个整数list L, 如 L=[2,-3,3,50], 求L的一个连续子序列，使其和最大，输出最大子序列的和。
例如，对于L=[2,-3,3,50]， 输出53（分析：很明显，该列表最大连续子序列为[3,50])."""

L = [2,-3,3,50]
sum1 = 0
for i in range(len(L)):
    for j in range(i,len(L)):
        print(i,j,L[i:j+1])
        if sum1 < sum(L[i:j+1]):
            sum1 = sum(L[i:j+1])
print(sum1)


