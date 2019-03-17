"""
列表：
由一系列按特定顺序排列的元素组成;

python:
用[]来表示列表;并且用逗号（必须是英文逗号）进行分隔元素
"""
drinks = ['脉动', '可乐', 'fenda', 'qi xi']
print(drinks)

#查
#访问列表内的某个元素
drinks[2]
print(drinks[2].title())

#访问某些元素【切片】
drinks[0:2]

#增
#在列表末尾添加元素
drinks.append('啤酒')

#在任意位置添加元素
drinks.insert(1, '啤酒')

#删除
#删除列表内的某个元素
del drinks[1]

#pop()删除元素
drinks.pop()
drinks.pop(1)

#根据值删除元素
drinks.remove("脉动")

#改
drinks[0] = ("可乐")

#排序
cars = ['bmw', 'tesla', 'audi']
print(cars)
#sort()方法[升序]
cars.sort()

#sort()方法【降序】
cars.sort(reverse = True)
print(cars)



















