# -*- coding: utf-8 -*-
'''
今天在学习函数的默认值形参时，遇到一个小问题

'''

#再写下面这条代码的时候报错
def describe_pet(animal_type = 'dog', pet_name):
     '''显示宠物的信息'''
     print('\nI have a ' + animal_type + '.')
     print('My ' + animal_type + "'s name is " + pet_name.title() + '.')

describe_pet('lili')
#去掉默认值形参的形式就没有错误
def describe_pet(animal_type, pet_name):
     '''显示宠物的信息'''
     print('\nI have a ' + animal_type + '.')
     print('My ' + animal_type + "'s name is " + pet_name.title() + '.')


describe_pet('dog', 'lili')

#经过多次尝试，我发现必须先将普通的位置形参全部列出来之后才能列默认值参数
def describe_pet(pet_name, animal_type = 'dog'):
     '''显示宠物的信息'''
     print('\nI have a ' + animal_type + '.')
     print('My ' + animal_type + "'s name is " + pet_name.title() + '.')
 
describe_pet(pet_name = 'lili')
describe_pet('lili')
describe_pet('lili', 'er ha')#再次输入位置实参会覆盖默认值形参



































