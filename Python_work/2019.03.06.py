# -*- coding: utf-8 -*-

#元组，元素不能被修改
dimensions = (200,50)
print(dimensions[0])#注意括号
#遍历元组
dimensions = (200,50)
for dimension in dimensions:
    print(dimension)

#修改元素变量的方法，重新定义元组
dimensions = (200,50)
for dimension in dimensions:
    print(dimension)
dimensions = (400,100)
for dimension in dimensions:
    print(dimension)

#比较字符时，大小写会有影响
car = 'Audi'
car == 'audi'
#如果比较时大小写不重要，可以加上.lower()函数
car.lower() == 'audi'

#小测试1
alien_color = ('green', 'yellow', 'red')
if alien_color == 'green':
    print('You got 5 points!')
else:
    print('')

if alien_color == 'green':
    print('You got 5 points!')
elif alien_color == 'yellow':
    print('You got 10 points!')
elif alien_color == 'red':
    print('You got 15 points!')
#小测试2
age = 55
if age < 2:
    print('He is a baby.')
elif age >= 2 and age < 4:
    print('He is learn how to walk.')
elif age >= 4 and age< 13:
    print('He is a child.')
elif age >= 13 and age < 20:
    print('He is a teenage.')
elif age >= 20 and age < 65:
    print('He is an adult.')
elif age >=65:
    print('He is an old.')
#小测试三
favorite_fruites = ['apple', 'banana', 'pear', 'orange', 'yeeze']
if 'apple' in favorite_fruites:
    print('You really like apple!')
if 'bee' not in favorite_fruites:
    print("You really don't like bee!")

#用if语句判断列表是不是空的
requested_toppings = []
if requested_toppings:#列表非空就为真，空为假
    for requested_topping in requested_toppings:
        print("Adding " + requested_topping +'.')
    print('Finished making your pizza!')
else:
    print('Are you sure you want a plain pizza?')

#多个列表的处理
available_toppings = ['mushrooms', 'olives', 'green peppers',
'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print('Adding ' + requested_topping + '.')
    else:
        print("Sorry, we don't have " + requested_topping +'.')
print('\nFinished making your pizza!')

#小练习1
user_names = ['tom', 'tony', 'admin', 'lily', 'shedlon']
for user_name in user_names:
    if user_name == 'admin':
        print('Hello ' + user_name.title() + ',\
              would you like to see a status report?')
    else:
        print('Hello ' + user_name.title() + ', \
              thank you for logging in again.')
        
#小练习2
user_names = []        
for user_name in user_names:
    if user_names:
        if user_name == 'admin':
            print('Hello ' + user_name + ', would you like to see a status\
                  report?')
        else:
            print('Hello ' + user_name + ', thank you for logging in again.')
    else:
        print('We need to find some users!')
        
#小练习3  有点小问题
#引入中间列表解决
current_users = ['alien', 'Tom', 'tonY', 'lisa', 'lIly']
new_users = ['lili', 'tom', 'liyang', 'Tony', 'liu']
a = []
for current_user in current_users:    
    a.append(current_user.lower())
for new_user in new_users:
    if new_user.lower() in a:
        print(new_user + ' has been used.please use other names.')
    else:
        print(new_user + ' has not been used.')
#用布尔函数求解
current_users = ['alien', 'Tom', 'tonY', 'lisa', 'lIly']
new_users = ['lili', 'tom', 'liyang', 'Tony', 'liu']
for new_user in new_users:
    used = False
    for current_user in current_users:
        if new_user.lower() == current_user.lower():
            used = True
    if used:
        print(new_user + ' has been used.please use other names.')
    else:
        print(new_user + ' has not been used.')

#小练习4
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#nums = list(range(1,10))  更简便
for num in nums:
    if num == 1:
        print('1st')
    elif num == 2:
        print('2nd')
    elif num == 3:
        print('3rd')
    else:
        print(str(num) + 'th') #要注意变量类型转换













