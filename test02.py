import csv

l = [
	['姓名','年龄','性别'],
	['丁老大','22','男'],
	['王老五','8'],
	['赵九','90','男']

]

with open('csvfile.csv','rt',encoding='utf-8') as f:
	csvf = csv.reader(f)
	for row in csvf:
		print(row)
