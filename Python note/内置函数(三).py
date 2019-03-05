"""
range():
返回值是一个可迭代对象
"""
a = range(0,10,2)
print(a)

#常用来设定循环次数
for i in range(5):
    print("a")

"""
sort()
排序函数，永久排序
"""
a = [1,2,34,5,6,73,23,45,57]
a.sort()
print(a)

"""
sorted()
排序函数，临时排序
"""
b = [1,2,34,5,6,73,23,45,57]
sorted(b)
print(b)

"""
sum()
求和函数
"""
a = [1,2,3,4,5]
print(sum(a))

"""
tuple()函数
将列表转为元组
"""
a = [5,4,3,2,1]
b = tuple(a)
print(b)
print(a)









































































































