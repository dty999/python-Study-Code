"""给你一个整数列表L, 输出L的中位数（若结果为小数，则保留一位小数）。

例如： L=[0,1,2,3,4]

则输出：2"""
L = [0,1,2,3,4]
L = sorted(L)
if len(L)%2 !=0:
    print(L[len(L)//2])
else:
    if (L[len(L)//2-1]+L[len(L)//2])%2 == 0:
        print((L[len(L)//2-1]+L[len(L)//2])//2)
    else:

        print((L[len(L)//2-1]+L[len(L)//2])/2.0)
print(5/2.0)