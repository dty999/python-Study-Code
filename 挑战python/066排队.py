"""全班N（2<=N<=45）个人排成一排，但因为高矮不齐，需要进行调整。调整的方法是，不调换左右次序，只让若干人后退一步变为第2排，使第一排留下的人从左到右的身高按降序排列，即右边的人不比左边的人高。如果第2排的人还不按降序排列，则照此办理，即再让第2排的若干人后退一步变为第3排，这样继续下去，直到所有排的人都按身高从高到低排列。
现在将每个人的身高保存在列表L中，给你L，请你找出一种使第一排留下的人数尽可能多的调整方法，输出第一排留下的人数P及最后调整完共有几排数K，P和K之间以一个空格隔开。
如，L=[130, 122, 112, 126, 126, 125, 120, 100],则输出6 2。"""