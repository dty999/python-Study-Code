"""互联网上的每台计算机都有一个IP，合法的IP格式为：A.B.C.D。
其中A、B、C、D均为位于[0, 255]中的整数。为了简单起见，我们规定这四个整数中不允许有前导零存在，如001这种情况。
现在给你一个字符串s(s不含空白符),请你判断s是不是合法IP，若是，输出Yes,否则输出No.
如：s="202.115.32.24", 则输出Yes;  
    s="a.11.11.11", 则输出No."""

s="255.11.11.0"
l = s.split('.')
out = 'Yes'
if len(l) != 4:
    out = 'No'
else:
    for i in l:
        if i.isdigit():
            if int(i) == 0:
                continue
            if i.find('0') == 0 or int(i) < 0 or int(i) > 255:
                out = 'No'
                break
            continue
        else:
            out = 'No'
            break  
print(out)