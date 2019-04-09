"""银行在打印票据的时候，常常需要将阿拉伯数字表示的人民币金额转换为大写表示，现在请你来完成这样一个程序。

在中文大写方式中，0到10以及100、1000、10000被依次表示为：    零 壹 贰 叁 肆 伍 陆 柒 捌 玖 拾 佰 仟 万

以下的例子示范了阿拉伯数字到人民币大写的转换规则：

1	壹圆

11	壹拾壹圆

111	壹佰壹拾壹圆

101	壹佰零壹圆

-1000	负壹仟圆

1234567	壹佰贰拾叁万肆仟伍佰陆拾柒圆

现在给你一个整数a(|a|<100000000), 请你打印出人民币大写表示.

例如：a=1

则输出：壹圆

注意：请以Unicode的形式输出答案。提示：所有的中文字符，在代码中直接使用其Unicode的形式即可满足要求，中文的Unicode编码可以通过如下方式获得：u'壹'。

注意：代码无需声明编码！！不要在代码头部声明文件编码，否则会导致语法错误！

Note：数据已于2013-11-19日加强，原来通过的代码可能不能再次通过。"""
import time
def wode(a):
    voice=[u'零',u'壹',u'贰',u'叁',u'肆',u'伍',u'陆',u'柒',u'捌',u'玖']
    unit=[u'',u'拾',u'佰',u'仟',u'万',u'拾',u'佰',u'仟']
    s = u''
    if a == 0: 
        return s + u'零圆'
    else:
        if a < 0:
            s += u'负'
            a = -a
    length = len(str(a))
    zeroflag = 0
    for i in range(length,0,-1):
        i = i -1#一万有长度是五要除以10的四次方,所以要减一
        v = a // (10**i)
        if v == 0 and zeroflag==1:
            if i == 4:
                s = s[0:-1]
                s += unit[4]
                zeroflag = 0
            if i == 0:
                s = s[0:-1]
        elif v == 0 and zeroflag == 0:
            if i == 4:
                s += unit[4]
                zeroflag = 0
            else:
                if i != 0:
                    s += voice[0]
                    zeroflag = 1
        elif v != 0:
            s += voice[v]
            s += unit[i]
            zeroflag = 0
        a = a % (10**i)
    return s + u'圆'



def tade1(a):
    num_list=u"零壹贰叁肆伍陆柒捌玖"
    wei_list=u'万圆拾佰仟万拾佰仟亿拾佰仟'
    def GetDX(num):
        s=''
        flag=0
        if num<0:
            num=-num
            flag=1
        wei=len(str(num))
        for i in str(num):
            s=s+num_list[int(i)]+wei_list[wei]
            wei=wei-1
        s=Modify(s)
        if num==0:
            s=u'零圆'
        if flag:
            s=u'负'+s
        return s
    def Modify(s):
        if u'零仟' in s:
            s=s.replace(u'零仟',u'零')
        if u'零佰' in s:
            s=s.replace(u'零佰',u'零')
        if u'零拾' in s:
            s=s.replace(u'零拾',u'零')
        while u'零零' in s:
            s=s.replace(u'零零',u'零')
        if u'零万' in s:
            s=s.replace(u'零万',u'万')
        if u'零圆' in s:
            s=s.replace(u'零圆',u'圆')
        return s
    ans=GetDX(a)
    return ans



if __name__ == "__main__":

    time1 = 0
    time3 = 0
    for i in range(0,200000):

        start = time.clock()
        s1 = wode(i)
        time1 += time.clock()-start 

        start = time.clock()
        s3 = tade1(i)
        time3 += time.clock()-start

        if s1 != s3:
            print(s1,s3)
    print(time1,time3)

