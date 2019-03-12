# -*- coding: utf-8 -*-

#定义函数
#def + 函数名 + (形参) + :
    #函数体
#调用函数
#函数名 + (实参)
def greet_user():
    """显示简单的问候语"""
    print('Hello!')

greet_user()

#函数的调用
def greet_user(username):
    print('Hello, ' + username.title() + '!')

greet_user('tom')

#小练习1
def display_message(learning):
    print('本章我学的是:' + learning)

learning = input('输入本章你学了什么\n')
display_message(learning)

#小练习2
def favorite_book(title):
    print('One of my favorite books is ' + title)

book = 'Alice in Wonderland'
favorite_book(book)

#实参类型：位置实参和关键字实参
#位置实参
def describe_pet(animal_type, pet_name):
    '''显示宠物的信息'''
    print('\nI have a ' + animal_type + '.')
    print('My ' + animal_type + "'s name is " + pet_name.title() + '.')

describe_pet('二哈', '普拉达')#实参的顺序要与形参的顺序相同。
describe_pet('金毛', '多多')

#关键字实参
def describe_pet(animal_type, pet_name):
    '''显示宠物的信息'''
    print('\nI have a ' + animal_type + '.')
    print('My ' + animal_type + "'s name is " + pet_name.title() + '.')

describe_pet(pet_name = '普拉达', animal_type = '二哈')

#形参的默认值
def describe_pet(pet_name, animal_type = 'dog'):
     '''显示宠物的信息'''
     print('\nI have a ' + animal_type + '.')
     print('My ' + animal_type + "'s name is " + pet_name.title() + '.')
 
describe_pet(pet_name = 'lili')
describe_pet('lili')
describe_pet('lili', 'er ha')#再次输入位置实参会覆盖默认值形参

#小练习
def make_shirt(size, pattern):
    print("This T-shirt's size is " + size + ' , pattern is ' + pattern + '.')

make_shirt('3XL', 'apple')

def make_shirt(pattern, size = '3XL'):
    print("This T-shirt's size is " + size + ' , pattern is ' + pattern + '.')

make_shirt('apple')

#函数的返回值
#简单的返回值
def get_formatted_name(first_name, last_name):
    """返回整洁的姓名"""
    full_name = first_name.title() + ' ' + last_name.title()
    return full_name

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

#返回字典
def build_person(first_name, last_name, age = ''):
    """返回一个字典，其中包含一个人的信息"""
    person = {'first' : 'first_name', 'last' : 'last_name'}
    if age:
        person['age'] = age
    return person
musician = build_person('jimi', 'hendrix',age = 29)
print(musician)

#while与函数
def get_formatted_name(first_name, last_name):
    '''返回一个整洁的姓名'''
    full_name = first_name + ' ' + last_name
    return full_name

while 1:
    a = input('输入任意键开始循环，输入q推出循环')
    if a == 'q':
        break
    first_name = input('输入first_name: ')
    last_name = input('输入last_name: ')
    formatted_name = get_formatted_name(first_name, last_name)
    print('Hello, ' + formatted_name.title() + '.')


#用函数改变列表
def print_models(unprint_designs, completed_models):
    """
    打印每个设计，知道没有未打印的设计为止
    打印每个设计后，都将其移动到completed_models中
    """
    while unprint_designs:
        current_design = unprint_designs.pop()
        #根据设计打印模型
        print('Printing model: ' + current_design)
        #将打印好的模型移动到completed_models中
        completed_models.append(current_design)
        
def show_completed_models(completed_models):
    """
    显示所有已经打印的模型
    """
    print('\nThe following models have been printed: ')
    for completed_model in completed_models:
        print(completed_model)

unprint_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
print_models(unprint_designs[:], completed_models)#这里用了切片表示副本
'''
unprint_designs[:]表示列表的副本，对列表内的元素进行改变只是对副本的操作
对原列表没有影响
'''
show_completed_models(completed_models)
print(unprint_designs)#打印原列表可以看到元素没有改变。

#小练习  
#1.创建一个包含魔术师名字的列表，并将其传递给一个名为show_magicians() 的函数，这个函数打印列表中每个魔术师的名字。
def show_magicians(magicians_name):
    print("Magicians' name are: ")
    for magician_name in magicians_name:
        print(magician_name.title())

magicians_name = ['liu qian', 'davida', 'dong qing']
show_magicians(magicians_name)

#2.编写一个名为make_great() 的函数，对魔术师列表进行修改，在每个魔术师的名字中都加入字样“the Great”。
#调用函数show_magicians() ，确认魔术师列表确实变了。

#引入中间变量，不用创建心的列表
def make_great(magicians_name):
    for magician_name in magicians_name:
        current_magician = 'the Great ' + magicians_name.pop(0)#必须从第一个开始更改
        magicians_name.append(current_magician)
magicians_name = ['liu qian', 'davida', 'dong qing']
make_great(magicians_name)
show_magicians(magicians_name)

'''
3.修改你为完成练习8-10而编写的程序，在调用函数make_great() 时，向它传递魔术师列表的副本。
由于不想修改原始列表，请返回修改后的列表，并将其存储到另一个列表中。
分别使用这两个列表来调用show_magicians() ，确认一个列表包含的是原来的魔术师名字，
而另一个列表包含的是添加了字样“the Great”的魔术师名字。
'''
#创建一个新列表great_magicians       
def make_great(magicians_name, great_magicians):
    while magicians_name:
        current_magician = 'the Great ' + magicians_name.pop()
        great_magicians.append(current_magician)
    
magicians_name = ['liu qian', 'davida', 'dong qing']
great_magicians = []
make_great(magicians_name[:], great_magicians)
show_magicians(great_magicians)
print('\n')
show_magicians(magicians_name)

#传递任意数量的参数
# * + 形参， 表示创建一个以 形参 为名的空元组
def make_pizza(size, *toppings):
    """打印顾客点的所有配料"""
    print('\nMaking a ' + str(size) + 
          "-inch pizza with the following toppings: ")
    for topping in toppings:
        print('- ', topping)
    
make_pizza(16, 'pepperni')
make_pizza(25, 'mushrooms', 'green peppers', 'extra cheese')











































    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    