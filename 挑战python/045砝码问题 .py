"""有一组砝码，重量互不相等，分别为m1、m2、m3……mn；它们可取的最大数量分别为x1、x2、x3……xn。 
现要用这些砝码去称物体的重量,问能称出多少种不同的重量。 
现在给你两个正整数列表w和n， 列表w中的第i个元素w[i]表示第i个砝码的重量，列表n的第
i个元素n[i]表示砝码i的最大数量。i从0开始，请你输出不同重量的种数。
如：w=[1,2], n=[2,1], 则输出5（分析：共有五种重量：0,1,2,3,4）"""
import copy

w = [3,11]
n = [5,5]
q = []
for i in range(len(w)):
    q += [w[i] for j in range(n[i])]
aw = [0]
for i in range(0,len(q)):
    for j in range(0,len(aw)):
        t = q[i] + aw[j]
        if t not in aw:
            aw.append(t)

print(sorted(aw))






    



