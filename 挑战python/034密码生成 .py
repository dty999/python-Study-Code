"""生活在当代社会，我们要记住很多密码，银行卡，qq，人人，微博，邮箱等等。\
    小P经过一番思索之后，发明了下面这种生成密码方法：\
        给定两个正整数a和b, 利用a / b我们会得到一个长度无限的小数\
            (若a / b不是无限小数，比如1/2=0.5,我们认为0.5是0.5000000...，同样将其看做无限长的小数），\
                小P将该小数点后第x位到第y位的数字当做密码，\
                    这样，无论密码有多长，小P只要记住a,b,x,y四个数字就可以了，牢记密码再也不是那么困难的事情了\
                        。现在告诉你a,b,x,y（0 < a,b <= 20132013, 0 < x <= y < 100000000000),请你输出密码。\
    例如：a = 1, b = 2, x = 1, y = 4, 则 a / b = 0.5000000..., 输出小数点后第1到4位数字，即5000"""


a,b = 1,2
x,y = 1,8
#求最大公约数,不知道为什么用math.gcd()报错?
def mygcd(num1,num2):
    if num1 < num2:
        temp = num1
        num1 = num2
        num2 = temp  
    if  num1%num2 ==0:
        return num2
    else:
        num2 = num1%num2
        return mygcd(num1,num2)
#求这个数的所有质因数
def get_num_factors(num):
    list0=[]
    tmp=2
    if num==tmp:
        list0.append(2)
        return list0
    else:
        while (num>=tmp):
            k=num%tmp
            if( k == 0):
                list0.append(str(tmp))
                num=num/tmp  #更新
            else:
                tmp=tmp+1  #同时更新除数值，不必每次都从头开始
    return list(set(list0))
#判断a/b是否为有限小数
#原理:如果约分后除数除了2,5之外还有其他质因子,则为无限小数
def isYouXian(a,b):
    c = mygcd(a,b)#约分
    b = b//c
    list1 = get_num_factors(b)
    if 2 in list1:
        list1.remove(2)
    if 5 in list1:
        list1.remove(5)
    if list1:
        return False#如果不为空说明除了2,5之外还有其他质因子,则为无限小数
    else:
        return True

def Chufa(a,b,x,y):
    s  = []
    st = []
    #能够整除的情况
    if a%b == 0:
        return '0'*(y-x+1)
    if isYouXian(a,b):#如果是有限小数就除尽并在后面添加足够的0
        a = a %b
        while True:
            s.append(a//b)
            a = (a%b)*10
            if a%b == 0:
                s.append(a//b)
                break
        del s[0]
        s += [0 for i in range(y)]
        return ''.join(map(str,s[x-1:y]))
    else:
        a = a%b
        flag1 = 0
        while True:
            s.append(a//b)
            a = (a%b)*10
            if a in st:
                flag1 = st.index(a)
                break
            else:
                st.append(a)
        del s[0]
        st2 = s[flag1:]
        while y> len(st2):
            st2 += st2
        s += st2
        return ''.join(map(str,s[x-1:y]))


#别人的算法---------------

def f(a,b,x,y): #remainder即每次进行除法时的余数
    remainder = a*pow(10,x-1,b)%b #由除法性质，除数不变，被除数是原来的多少倍，商也是原来的多少倍。这步就是为了算出原来商的第x-1位小数进行除法后的余数
    result = ""
    
    for i in range(y-x+1):
        
        remainder *= 10
        result += str(remainder/b)
        remainder %= b
    
    return result

import time
time.clock()
print(f(a,b,x,y)) 
print(time.clock())


print(Chufa(a,b,x,y))
print(time.clock())