""" 输出100以内的所有素数，素数之间以一个空格区分（注意，最后一个数字之后不能有空格）。"""
a = []
for i in range(1,100):
    for t in range(1,i):
        if i % t == 0 and t != 1:
            break
        if t >= (i-1):
            a.append(i)
print(" ".join(map(str,a)))