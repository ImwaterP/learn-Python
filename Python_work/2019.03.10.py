# -*- coding: utf-8 -*-

#嵌套小练习
#列表内嵌套字典
person_0 = {'name' : 'peter', 'age' : 24, 
            'gender' : 'male', 'location' : 'bei jing'}
person_1 = {'name' : 'lisa', 'age' : 20, 
            'gender' : 'male', 'location' : 'he nan'}
person_2 = {'name' : 'tom', 'age' : 28, 
            'gender' : 'male', 'location' : 'shang hai'}
people = [person_0,person_1, person_2]
for person in people:
    print(person)
people[1]

#字典中嵌套列表
favorite_places = {
        'tom' : ['bei jing', 'nan jing', 'shang hai'], 
        'john' : ['gui lin', 'cheng du', 'chong qing'], 
        'lisa' : ['san ya', 'xi zang', 'yun nan'], 
        }
for name, places in favorite_places.items():
    print('\n' + name.title() + "'s favorite places :")
    for place in places:
        print('\t' + place.title())

#字典中嵌套字典
cities = {
        'shang hai' : {'country' : 'china', 'population' : '150w', 
                       'fact': 'bf'}, 
        'lundon' : {'country' : 'england', 'population' : '90w', 
                       'fact': 'fh'}, 
        'washington' : {'country' : 'america', 'population' : '200w', 
                       'fact': 'ml'}, 
        }
for city, facts in cities.items():
    print('\ncity: ' + city.title())
    for fact, answer in facts.items():
        print('\t' + fact.title() + ' : ' + answer.title())

#input 输入 (输入的都为字符串类型)
name = input("please enter your name: ")
print('Hello, ' + name + '!')
#当提示信息超过一行时，将提示输入一个变量里在输出
prompt = 'If you tell us who you are, we can personalize the messages you see.'
prompt += '\nWhat is your name? '
name = input(prompt + '\n')
print('Hello, ' + name + '!')

#将字符串类型转换为int类型
height = input('How tall are you, in inches? ')
height = int(height)
if height >= 36:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older.")

#取模 % ,判断奇偶
number = input('Please enter a number: ')
number = int(number)
if number % 2 == 0:
    print('It is even.')
else:
    print('It is odd.')

#while 循环，并插入标志
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
active = True#插入了一个标志
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    elif message == '0':
        active = False
#当必须同时满足多个条件才能继续循环时可以插入标志
#只要有一个条件不满足，就将标志变为False停止循环
    else:
        print(message)

#小练习
prompt = 'Please enter what you want to topping.'
prompt += '\nEnter quit to end the program'
message = ''
while message != 'quit':
    message = input(prompt + '\n')
    if message != 'quit':
        print("We'll topping " + message.title() + ' in your pizza.')
    else:
        break

#用while循环处理列表和字典

#列表之间移动元素
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print("Verifying user: " + current_user.title())
    confirmed_users.append(current_user)
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

#处理字典
responses = {}
polling_active = True
while polling_active:
    name = input('What is your name? ')
    response = input("Which mountain would you like to climb someday? ")
    responses[name] = response
    repeat = input("Would you like to let another person respond? (Yes/ No) ")
    if repeat == "no" :
        polling_active = False
print("\n---Poll Results---")
for name, response in responses.items():
    print(name.title() + ' would like to climb ' + response.title() + '.')

#小练习1
sandwich_orders = ['jiamo', 'latiao', 'biededongxi']
finished_sandwiches = []
while sandwich_orders:
    finished_sandwich = sandwich_orders.pop()
    print("I made your " + finished_sandwich.title() + ' sandwich.')
    finished_sandwiches.append(finished_sandwich)
print(finished_sandwiches)

#小练习二
sandwich_orders = ['jiamo', 'pastrami', 'latiao',  'pastrami', 'biededongxi', 'pastrami']
finished_sandwiches = []
print('Sorry the Pastrami is none')
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
while sandwich_orders:
    finished_sandwich = sandwich_orders.pop()
    print("I made your " + finished_sandwich.title() + ' sandwich.')
    finished_sandwiches.append(finished_sandwich)
print(finished_sandwiches)

#小练习三
responsed = {}
active = True
answer = ['no', 'No', 'NO']
while active:
    name = input("What's your name?\n")
    response = input('If you could visit one place in the world,\
                     where would you go?\n')
    responsed[name] = response
    repeat = input('Anyone else? (yes / no) ' )
    if repeat in answer:
        active = False
        print(active)
for name, response in responsed.items():
    print('\n' + name.title() + ' Would like to visit ' + \
          response.title() + '.')











































