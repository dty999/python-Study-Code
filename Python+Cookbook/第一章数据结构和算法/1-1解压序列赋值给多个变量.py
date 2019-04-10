"""
现在有一个包含 N 个元素的元组或者是序列，怎样将它里面的值解压后同时赋值
给 N 个变量？
"""
"""
任何的序列（或者是可迭代对象）可以通过一个简单的赋值语句解压并赋值给多
个变量。唯一的前提就是变量的数量必须跟序列元素的数量是一样的。

"""

p = (4, 5)
x, y = p
data = ['ACME', 50, 91.1, (2012, 12, 21)]
name, shares, price, date = data
print(name, shares, price, date)
record = ('Dave', 'dave@example.com', '773-555-1212', '345-888-9899')
name, email, *phone_numbers = record
print(name, email, phone_numbers)
