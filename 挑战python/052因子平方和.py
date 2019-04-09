"""6 的因子有 1, 2, 3 和 6, 它们的平方和是 1 + 4 + 9 + 36 = 50. 如果 f(N) 代表正整数 N 所有因子的平方和, 那么 f(6) = 50.
现在令 F 代表 f 的求和函数, 亦即 F(N) = f(1) + f(2) + .. + f(N), 显然 F 一开始的 6 个值是: 1, 6, 16, 37, 63 和 113.
那么对于任意给定的整数 N (1 <= N <= 10^8), 输出 F(N) 的值."""

N = 20
l = []
def f(n):
    res = []
    for i in range(1,int(n/2 +1)+1):
        if n % i ==0:
            res.append(i)
            res.append(n//i)
    return set(res)
def F1(N):
    from collections import defaultdict
    dic = defaultdict(int)
    for i in range(1,N+1):
        res = f(i)
        for i in res:
            dic[i] += 1
    return dic


def F(N):
    res = 0
    for i in range(1,N//2 + 1):
        res  += i**2*(N//i-1)#每个数拿出来留到后面给平方和用
    res += N*(N+1)*(2*N+1)/6
    return res
print(int(F(6)))
