g# -*- coding: utf-8 -*-


#函数小练习
'''
编写一个函数，它接受顾客要在三明治中添加的一系列食材
。这个函数只有一个形参（它收集函数调用中提供的所有食材），并打印一条消息，
对顾客点的三明治进行概述。调用这个函数三次，每次都提供不同数量的实参。
'''
def sandwich_toppings(*toppings):
    """描述三明治选的配料"""
    print('Making a sandwich with following toppings : ')
    for topping in toppings:
        print('- ' + topping)
#这里我本身创建了一个列表或者元组，并将其当作实参，但是报错。
#toppings = ('onion', 'mushroon')
#sandwich_toppings(toppings)
sandwich_toppings('onion', 'mushroom', 'green papper')
#所以当用*做形参的时候，不能用列表或者元组做实参

"""
用户简介 ：复制前面的程序user_profile.py，在其中调用build_profile() 
来创建有关你的简介；调用这个函数时，指定你的名和姓，以及三个描述你的键-值
对。
"""
def build_profile(first, last, **user_info):
    """创建一个字典，里面包含了我们知道的用户的资料"""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('chen', 'zhuo', 
                             location = 'China', 
                             language = 'chinese')
print(user_profile)

"""
：编写一个函数，将一辆汽车的信息存储在一个字典中。这个函数总是接受制造商和型号，
还接受任意数量的关键字实参。这样调用这个函数：提供必不可少的信息，
以及两个名称—值对，如颜色和选装配件。
"""
def car_message(make, model, **user_info):
    message = {}
    message['make shop'] = make
    message['car model'] = model
    for key, value in user_info.items():
        message[key] = value
    return message

user_car = car_message('auto', 'A6', color = 'black', tow_package = True)


#模块，在该项目文件夹中创建一个pizza.py文件，里面的函数称为模块

#调用整个模块
import pizza#使用import + 文件名，就可调用pizza中所有的函数
pizza.make_pizza(16, "pepperoni")#文件名 + 函数名即可调用函数
pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

#单独调用某个模块中特定函数
from pizza import make_pizza#from + 文件名 + 函数名,即可调用
make_pizza(16, 'pepperoni')

#用as给函数或者模块指定别名
from pizza import make_pizza as mp#给函数指定别名
mp(16, "mushroom")

import pizza as p#给模块指定别名
p.make_pizza(16, "mushroom")

#导入模块中所有函数,用*，相当于将模块中所有函数都复制到该文件夹中。
from pizza import *
make_pizza(16, "mushroom")
"""
#因为你导入的是全部，他提示你不能检测一些没有定义的名称，
#练习的话，可以Import *，但是实际中千万不要全部倒入，很浪费时间，
#因为定义的一个库可能有非常多的函数，一般是用哪个导入哪个就行了
"""


"""
pip命令
库，包，模块下载（.whl格式）
https://www.lfd.uci.edu/~gohlke/pythonlibs/

"""

"""
给定一个x，经过模块或者包或者库中的函数关系，就可以得到y
相当于黑匣子，很多是由C语言写的

模块：
一个.py文件就是一个模块

包（package）：在模块之上的集合
很多个模块就是一个包

库：
是具有相关功能模块的集合
"""

"""
time:
时间模块
unix时间：从1970年1月1日到现在的秒数
"""
import time

print(time.time())#time模块下的time（）函数
dir(time)#用dir查看time模块中的所有函数

"""
random
随机模块
"""
import random

num = random.randrange(1, 51)#random模块中的randrange()函数
print(num)
dir(random)


"""
局部变量与全局变量
整体与C语言相似：

全局变量不能被改变
局部变量优先
global 能把局部变量变为全局变量

"""

"""
局部变量：
函数内部的变量名如果第一次出现，并且出现在=前面，那么这个变量
会被视为局部变量
"""

num = 100
def func():
    num = 200
    num += 200
    print(num)
func()

#num = 100
#def func():
#    num += 100
#    print(num)
#func() 
"""
会报错，因为局部变量优先，函数体中num第一次出现在等号左边，判定为局部变量，
却又没有定义num的值，因此编译器不知道num的数值是多少
"""

"""
函数内部的变量名第一次出现，并且出现在=号后面，
且该变量在全局中已定义，那么在函数内部就会引用全局变量的值
"""
num = 100
def func():
    a = num + 100
    print(a)
func()
#不会报错，因为num在函数中第一次没有出现在等号左边，
#因此会用全局变量

"""
用global改变局部变量为全局变量
"""
num = 100
def func():
    num = 200
    num += 200
    print(num)
func()

#这里从数值框中看到num的值还是100，因为局部变量的值不会显示
num = 100
def func():
    global num
    num = 200
    num += 200
    print(num)
func()
#可以看到num 的值不再是100，而是400



"""
用debug调试代码
能够看到局部变量的值
断点：能直接调到想调试的地方
"""
def add(a, b):
    x = a
    y = b
    z = x+y
    print(z)
add(1, 2)
add(2, 3)
add(3, 4)


"""
匿名函数：lambda
f(x, y) = x+y
"""
#正常函数：
def func1(x, y, z):
    sum = x + y * z
    print(sum)
func1(2, 3, 2)
#匿名函数：
sum = lambda x, y, z : x + y * z
print(sum(2, 3, 2))

"""
#添加条件表达式：
#只能添加条件表达式，无法使用更复杂的表达
"""
#正常函数：
def func1(x):
    if x == 0:
        print("ok")
    else:
        print("no")
func1(0)
func1(1)
#匿名函数
func2 = lambda x:"ok" if x == 1 else "no"
func2(0)
func2(1)

"""
map()
语法：
map(function, iterable, ...)
function:函数
iterable:添加一个或者多个序列
"""
def square(x):
    return x**2

data = list(range(0, 11))
print(list(map(square, data)))
#将map()函数与lambda函数结合起来
print(list(map(lambda x: x**2, data)))
#更复杂的例子
print(list(map(lambda x, y: x+y, data, data)))
#list()的作用:取出内存地址
print(map(lambda x: x**2, data))


"""
读取txt文件
with
"""
#相对路径（读取的文件与就在当前代码所在文件夹内）
with open("word.txt") as f:
    contents = f.read()
    print(contents)
#绝对路径（读取的文件在其他文件夹内）
with open(r"C:\Users\Administrator\Desktop\word.txt") as f:
    contents = f.read()
    print(contents)
#逐行读取
with open(r"C:\Users\Administrator\Desktop\word.txt") as f:
    for line in f:
        #print(line)
#取消行与行之间的换行
        print(line, end = "")

"""
写入文件
w:写入模式（wb表示二进制写入）
r：读取模式（rb表示二进制读取）
r+：读取写入模式
a：附加模式
"""
#with open没有的文件，会自动创建一个新的文件
#w：写入模式，将内容写入指定文件中，并覆盖文件原有内容
with open("content.txt", "w") as f:
    f.write("Python\n")
    f.write("Java\n")
#a：附加模式，会在保留文件原始数据条件下，写入新的内容
with open("content.txt", "a") as f:
    f.write("Python\n")
    f.write("Java\n")
    
with open("content.txt", "r") as f:
    
    
    



































