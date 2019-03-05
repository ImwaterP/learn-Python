# -*- coding: utf-8 -*-

name = 'tom jeon'
print(name.title())

name = 'lisa LILY'
print(name.upper())
print(name.lower())

first_name = 'lisa'
next_name = 'lily'
full_name = first_name + ' ' + next_name
print('Hello, ' + full_name.title() + '.')

print('languange:\t\npython\t\nc\t\njava'.title())

a = '  Python  '
print(a.strip())
print(a.lstrip())
print(a.rstrip())

print('Albert Einstein once said,"A person who never made a mistake never tried anything new."')

famous_person = 'albert einstein'
print(famous_person.title() + ' ' + 'once said,"A person who never made a mistake never tried anything new."')

#练习rstrip(),lstrip(),strip()
name = " \tAlbert    \n Eistein   "
print(name)
print(name.rstrip())
print(name.lstrip())
print(name.strip())

#把age转换成str类型才能不出错
age = 23
message = "Happy " + str(age) + 'rd Birthday!'
print(message)

import this

#title()不能用于整个list，只能用于list中的某一项
names = ['tom', 'jack', 'tony', 'lily']
print(names[0].title())
print("Hello", names[0].title(), ",my friend.") #这样输出会让name两侧都含有空格

#给list插入元素
names.append("liu")
print(names)
names.insert(1, "wang")
print(names)

#删除list的元素
del names[0]  #直接删除指定位置的元素
print (names)

pop_names = names.pop()#将list的最后一位“弹出”，被弹出的变量仍然可以使用
print(names)
print(pop_names)

names.pop(2)#将list指定位置的元素“弹出”
print(names)

names.remove('jack')#根据值删除元素
print(names)

#嘉宾的小练习
#列出嘉宾名单，并发出邀请
guest = ['wang', 'li', 'sun', 'qu', 'liu']
print('Hello ' + guest[0].title() + ',may I invite you to eat a dinner with me?')

#嘉宾sun不能来了，将其从明天中删除，并打印出来
no_guest = guest.pop(2)
print("Sorry," + no_guest.title() + " can't come here.")

#有了更大的餐桌，可以邀请更多的人，用三种语法再邀请三个人
names.insert(0) = 'chen'
names.insert(2) = 'liu'
names.append() = 'yang'
print(names)

#对列表进行排序
cars = ['bmw', 'audi', 'toyota', 'bench']
cars.sort()#对list永久的排序
print(cars)
cars.sort(reverse = True)#倒叙排序,也是永久的
print(cars)

cars = ['bmw', 'audi', 'toyota', 'bench']
print(cars)
print(sorted(cars))#临时排序
print(cars)


cars = ['bmw', 'audi', 'toyota', 'bench']
print(cars)
cars.reverse()#倒着输出，但是并不进行排序，永久的
print(cars)

#确定list的长度（从1开始计数）
len(cars)

#排序小练习
locations = ['beijing', 'nanjing', 'shanghai', 'yunnan', 'Amarica']
print(locations)
print(sorted(locations))#使用sorted正序输出
print(locations)
print(sorted(locations, reverse = True))#使用sorted倒序输出
print(locations)
#print(locations.reverse) 这种写法不可行
locations.reverse()
print(locations)
locations.reverse()
print(locations)
locations.sort()
print(locations)
locations.sort(reverse = True)
print(locations)

len(locations)

#遍历整个列表
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title() + ', that was a great trick!')

#range()函数
for value in range(1,5):
    print(value)
    
#用range()创建列表
numbers = list(range(1,6))
print(numbers)

#range()指定步长
even_numbers = list(range(2,20,2))
print(even_numbers)

#用range()函数创建其他数字集
squares = []
for value in range(1,10):
    square = value ** 2
    squares.append(square)
    print(squares)
#也可以不用中间变量
squares = []
for value in range(1,10):
    squares.append(value ** 2)
print(squares)
#列表解析法创建
squares = [value**2 for value in range(1,10)]
print(squares)

#对列表进行统计计算
print(max(squares))
print(min(squares))
print(sum(squares))


#小练习
num = list(range(1,1000000))#从一到一百万的列表
print(min(num))
print(max(num))
print(sum(num))

#能被3整除的数
odds = []
for odd in range(3,30,3):
    odds.append(odd)
    print(odd)
print(odds)

#立方
cubes = []#for循环法
for value in range(1,11):
    cube = value **3
    cubes.append(cube)
    print(cube)
print(cubes)
#列表解析法
cubes = [value ** 3 for value in range(1,11)]
print(cubes)

#切片
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])#注意这里的括号
print(players[1:4])#输出编号为1的元素到编号为3的元素
print(players[:2])#默认从第一个开始到编号为1的元素
print(players[2:])#从编号为2的元素到最后一个元素
print(players[-3:])#后三位元素

#遍历切片
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print('Here are the first three players on my team:')
for player in players[:3]:
    print(player.title())

#复制列表
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
print(my_foods)
print(friend_foods)
#证明这是两个不同的列表
my_foods.append('ice cream')
friend_foods.append('apple')
print(my_foods)
print(friend_foods)
#错误的复制方法
friend_foods = my_foods#相当于让两个列表同步更新
my_foods.append('cannoli')
friend_foods.append('face')
print(my_foods)
print(friend_foods)

for my_food in my_foods[:]:
    print(my_food)

#元组

























