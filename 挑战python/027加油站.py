"""一个环形的公路上有n个加油站，编号为0,1,2,...n-1,
每个加油站加油都有一个上限，保存在列表limit中，即limit[i]为第i个加油站加油的上限，
而从第i个加油站开车开到第(i+1)%n个加油站需要cost[i]升油,cost为一个列表。
现在有一辆开始时没有油的车，要从一个加油站出发绕这个公路跑一圈回到起点。
给你整数n，列表limit和列表cost,你来判断能否完成任务。
如果能够完成任务，输出起始的加油站编号，如果有多个,输出编号最小的。
如果不能完成任务，输出-1。"""

n = 5
limit = [3,2,3,5,2]
cost = [3,4,2,2,1]
def f1(n,limit,cost):
    for start in range(n):
        shengyu = 0
        print('从第%d个加油站出发----------' % (start,))
        for i in range(start,start+n):
            shengyu += limit[i%n]
            print('在第%d个加油站加了%d油,剩余%d油,将花费%d油'%(i%n,limit[i%n],shengyu,cost[i%n]))
            shengyu -= cost[i%n]
            if shengyu < 0:
                break
            if (i+1)%n == start and i+1 != start:
                print(start)
                return
    print(-1)

f1(n,limit,cost)