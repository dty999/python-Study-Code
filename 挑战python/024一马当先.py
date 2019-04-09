"""下过象棋的人都知道，马只能走'日'字形（包括旋转90°的日），现在想象一下，给你一个n行m列网格棋盘，
棋盘的左下角有一匹马，请你计算至少需要几步可以将它移动到棋盘的右上角，若无法走到，则输出-1.
如n=1，m=2,则至少需要1步；若n=1，m=3,则输出-1。"""
#广度优先遍历
from collections import deque
n,m=2,3
def steps(n, m):
	dx = [-1, -2, -2, -1, +1, +2, +2, +1]
	dy = [+2, +1, -1, -2, -2, -1, +1, +2]
	v = {(x, y) : False for x in range(0,n+1) for y in range(0,m+1)}
	v[(0, 0)] = True
	q = deque([(0, 0, 0)])
	while len(q)>0:
		p = q.popleft()
		for i in range(0, 8):
			x = p[0] + dx[i]
			y = p[1] + dy[i]
			if x < 0 or x > n or y < 0 or y > m:
				continue
			if v[(x, y)]:
				continue
			v[(x, y)] = True
			q.append((x, y, p[2]+1))
			if x == n and y == m:
				return p[2]+1
	return -1






