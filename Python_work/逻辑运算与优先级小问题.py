# -*- coding: utf-8 -*-
'''
逻辑运算符包含'and', 'or', 'not'
分别表示‘逻辑与’， ‘逻辑或’， ‘逻辑非’
但是我在代码中使用or的时候却遇到了问题
因此深入探究一下逻辑运算符的用法与规则
'''
#下面这段代码是我在做用 while 循环改编字典的练习时写的
responses = {}
polling_active = True
while polling_active:
    name = input('What is your name? ')
    response = input("Which mountain would you like to climb someday? ")
    responses[name] = response
    repeat = input("Would you like to let another person respond? (Yes/ No) ")
    if repeat == "no" or "No" :#这里为了使'no' 和 'No'都能生效，所以采用了or运算符
        polling_active = False#若if为真，则标志变为False，循环中止。
print("\n---Poll Results---")
for name, response in responses.items():
    print(name.title() + ' would like to climb ' + response.title() + '.')
#运行代码，我发现即便我输入了Yes，循环依然中止。
#再次运行，我发现不管我输入什么，循环都会被中止。

#我重新查阅了逻辑运算符的定义，定义如下
a = 10
b = 20
#and	
#x and y 布尔"与" 
#如果 x 为 False 或者 为 0 ，x and y 返回 x，否则它返回 y 的计算值。
print(a and b) #返回 20。


#or	
#x or y	布尔"或" 
#如果 x 是 True 或者 非0 ，它返回 x 的值，否则它返回 y 的计算值。	
print(a or b) #返回 10。


#not	
#not x 布尔"非" 
#如果 x 为 True，返回 False 。如果 x 为 False，它返回 True。	
print(not a) #返回 False

a = 0
b = 20#改变 a 的值
print(a and b) #返回为 0 
print(a or b) #返回为20
print(not a) #返回为True

#看来逻辑运算符没什么问题
#找老师看过代码之后才找到了问题的关键所在
#关键在于运算优先级
#'no' == 'no' or 'No'中 ‘==’的优先级高于‘or’所以if判断的只是‘no’ == ‘no’
#后面的or对if语句没有影响
#例如：
if 1 == 1 or 2:
    print('true')
else:
    print('false')

if 1 == 2 or 1:
    print('true')
else:
    print('false')
#不适用if语句更加直观
1 == 1
1 == 2
#再把or放入对比
1 == 2 or 1
1 == 1 or 2
#事实证明or的优先级低于‘==’
#对于字符串同样适用
'no' == 'no'
'no' == 'No'

'no' == 'no' or 'No'
'no' == 'No' or 'no'

'no' == ('No' or 'no')
'no' == ('no' or 'No')

#回到最初的问题，若我想让比较repeat与‘no’，‘No’，‘NO’三个，
#只要与三个中的任意一个相同就可以中止循环，我该怎么办呢？
#我可以创建一个列表，用‘in’ 或者 ‘not in’来实现
polling_active = True
nos = ['no', 'No', 'NO']
repeat = input("Would you like to let another person respond? (Yes/ No) ")
if repeat in nos:
    polling_active = False
print(polling_active)





































