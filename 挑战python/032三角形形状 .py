"""给以一个三角形的三边长a,b和c(边长是浮点数),请你判断三角形的形状。
若是锐角三角形，输出R,
若是直角三角形，输出Z，
若是钝角三角形，输出D，
若三边长不能构成三角形，输出W."""
a,b,c = 3,4,5
l = [a,b,c]
l.sort()
rs = 'W'
flag = l[0]**2 + l[1]**2 - l[2]**2
if a < b+c and b < a+c and c < b+a:
    if flag == 0:
        rs = 'Z'
    elif flag > 0:
        rs = 'R'
    else:
        rs = 'D'
print(rs)

