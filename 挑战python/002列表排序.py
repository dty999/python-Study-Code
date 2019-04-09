



L = [2,5,1,4,9,5,4,6,3]
print(sorted(L))#生成一个新的列表
L.sort()#不会生成新列表,会改变原列表,没有返回值
print(L)
#倒序
L.reverse()
print(L)

print(L[::-1])#通过切片实现倒序,没有改变原列表
print(L)