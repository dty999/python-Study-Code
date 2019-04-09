"""故事背景和“单身狗”相同，只不过这次Party中混进了两只单身狗，请你输出这两只单身狗的编号，小编号在前，大编号在后，以一个空格隔开。
例如：L=[1,1,4,4,3,5,5,7]
则输出：3 7

"""
from collections import Counter
L=[1,1,4,4,3,5,5,7]
L_counter = Counter(L).most_common()
l = []
if L_counter[-1][1] == 1 and L_counter[-2][1] == 1:
    if L_counter[-1][1] < L_counter[-2][1]:
        l = [L_counter[-1][0],L_counter[-2][0]]
    else:
        l = [L_counter[-2][0],L_counter[-1][0]]

    print(' '.join(map(str,l)))
else:
    print('')