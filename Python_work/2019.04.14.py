# -*- coding: utf-8 -*-

#Using def to define a function 
def greet_user(username):
    """Showing a simple greeting."""
    print("Hello, " + username.title() + '!')

greet_user('john')

#transmit the argument
    #position the arguments (It is important that the arguments' order)
def describe_pet(animal_type, pet_name):
    """Showing the pets' imformation"""
    print("\nI have a " + animal_type + ".")
    print('My' + animal_type + "'s name is " + pet_name.title() + '.')

describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')
describe_pet('willie', 'dog')#The order is very important!

    #Keyword argument (When you input arguments, you can use Keyword argument)
def describe_pet(animal_type, pet_name):
    """Showing the pets' imformation"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet(animal_type = 'dog', pet_name = 'willie')
describe_pet(pet_name = 'harry', animal_type = 'hamster')

    #Using defult value (Attention!defult value must be placed at the end!)
def describe_pet(pet_name, animal_type = 'dog'):#defult is at the end!
    """Showing the pets' imformation"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

# 一条名为Willie的小狗
describe_pet('willie')
describe_pet(pet_name='willie')
# 一只名为Harry的仓鼠
describe_pet('harry', 'hamster')
describe_pet(pet_name='harry', animal_type='hamster')
describe_pet(animal_type='hamster', pet_name='harry')

#return value
    #return a simple value
def get_formatted_name(first_name, last_name):
    """Return a neat name"""
    full_name = first_name + " " + last_name
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

    #Make the actual argument optional
def get_formatted_name(first_name, last_name, middle_name = ''):
    """Return a neat name"""
    if middle_name:
        full_name = first_name + " " + middle_name + " " + last_name
    else:
        full_name = first_name + " " + last_name
    return full_name.title()

musician0 = get_formatted_name('jimi', 'hendrix')
musician1 = get_formatted_name('john', 'hokker', 'lee')
print(musician0)
print(musician1)

    #Return dictionary
def build_person(first_name, last_name, age = ''):
    """Returning a dictionary, which include the information of one person"""
    person = {'first' : first_name, 'last' : last_name}
    if age:
        person['age'] = age
    return person

musician = build_person('jimi', 'hendrix', age = 27)
print(musician)

#function and while loop
def get_formatted_name(first_name, last_name, middle_name = ''):
    """Return a neat name"""
    if middle_name:
        full_name = first_name + " " + middle_name + " " + last_name
    else:
        full_name = first_name + " " + last_name
    return full_name.title()

while True:
    print("\nplease tell me your name:")
    print("(enter 'q' at any time to quit)")
    
    f_name = input('First name: ')
    if f_name == 'q':
        break
   
    l_name = input('Last name: ')
    if l_name == 'q':
        break
    
    m_name = input("If you don't have middle_name," +
                   "please press Enter.\nMiddle name: ")
    if m_name:
        if m_name == 'q':
            break
        else:
            full_name = f_name + " " + m_name + " " + l_name
    else:
        full_name = f_name + " " + l_name

    formatted_name = get_formatted_name(f_name, l_name, m_name)
    print("\nHello, " + formatted_name + "!")

#transfer list to a function
def greet_users(names):
    """Send a simple greeting to every user in the list"""
    for name in names:
        print("Hello, " + name.title() + "!")

usernames = ['john', 'ty', 'margot']
greet_users(usernames)

    #Modify the list in the function
      
        #Don't use function
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

while unprinted_designs:
    current_design = unprinted_designs.pop()
    print("printing model: " + current_design + ".")
    completed_models.append(current_design)

print("\nThe following models have been printed: ")
for completed_model in completed_models:
    print(completed_model)
        
        #use function
def print_models(unprinted_designs, completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print("printing model: " + current_design + ".")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    print("\nThe following models have been printed: ")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

    #Prohibit modify the list in the function(use slice)
def print_models(unprinted_designs, completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print("printing model: " + current_design + ".")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    print("\nThe following models have been printed: ")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs[:], completed_models)#use slice
show_completed_models(completed_models)

print(unprinted_designs)

#Pass any number of arguments
def make_pizza(*toppings):
    """print all the toppings for customers' point"""
    print(toppings)

make_pizza('mushroom', 'green peppers', 'extra cheese')

    #If you want the function to accept different types of arguments,
    #you must put the formal parameters that accept any number of arguments
    #in the function definition.
def make_pizza(size, *toppings):
    """Outline the pizz to be made"""
    print("\nMaking a " + str(size) +
          "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)

make_pizza(16, 'mushroom', 'green peppers', 'extra cheese')

#Use any number of keyword arguments
def build_profile(first, last, **user_info):
    """Create a dictionary that contains users' everything we know"""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('albert', 'einstein',
                            location='princeton',
                            field='physics')
print(user_profile)

#import function
    #import the entire module
import pizza

pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

    #Import specific functions
from pizza import make_pizza

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

    #Use as to specify an alias for the function
from pizza import make_pizza as mp

mp(16, 'pepperoni')

     #Use as to assign an alias for the module
import pizza as p

p.make_pizza(16, 'pepperoni')

#Use * to import all functions in the module
from pizza import *

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

#class
    #define a class
class Dog():
    """Try to simulate a puppy"""
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def sit(self):
        """Try to simulate sit down"""
        print(self.name.title() + " is now sitting.")
    def roll_over(self):
        """Try to simulate roll"""
        print(self.name.title() + ' rolled over!')

    #transfer the class
my_dog = Dog('willie', 4)
print("My dog's name is " + my_dog.name.title() + '.')
my_dog.roll_over()

your_dog = Dog('lucy', 6)
print("\nYour dog is " + str(your_dog.age) + " years old.")
your_dog.sit()



#定义一个描述汽车的类
class Car():
    """"一次模拟汽车的简单尝试"""
    def __init__(self, make, model, year):
        """初始化汽车的属性"""
        self.make = make 
        self.model = model
        self.year = year
        #默认属性
        self.odometer = 0
    def get_description_name(self):
        """返回汽车的完整信息"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name
    def read_odometer(self):
        """打印汽车的里程信息"""
        print("This car has " + str(self.odometer) + ' km')
#输入参数
my_car = Car('audi', 'a6', '2016')
#调用参数
my_car.make
my_car.model
my_car.odometer
#调用类中的方法
my_car.get_description_name()
my_car.read_odometer()

#修改类中属性的值
    #直接修改
my_car.odometer = 23
my_car.read_odometer()

    #通过方法修改
class Car():
    """"一次模拟汽车的简单尝试"""
    def __init__(self, make, model, year):
        """初始化汽车的属性"""
        self.make = make 
        self.model = model
        self.year = year
        #默认属性
        self.odometer = 20
    def get_description_name(self):
        """返回汽车的完整信息"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name
    def read_odometer(self):
        """打印汽车的里程信息"""
        print("This car has " + str(self.odometer) + ' km')
    #在这里插入一个方法用来修改里程数
    def update_odometer(self, mileage):
        """
        将里程表读数设置为指定值
        并禁止把里程数往回调
        """
        if mileage >= self.odometer:
            self.odometer = mileage
        else:
            print("You can't roll back an odometer!")
                        
my_car = Car('audi', 'a6', '2016')  
my_car.get_description_name()
my_car.read_odometer()

my_car.update_odometer(18)
my_car.read_odometer()


#继承
    #创建一个父类,父类必须与子类在同一文件夹中，且父类必须在子类前面
class Car():
    """一次模拟汽车的简单尝试"""
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def fill_gas_tank(self):
        """汽车有油箱"""
        print("This car need a gas tank!")
    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")
    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    def increment_odometer(self, miles):
        self.odometer_reading += miles
        
    #创建子类继承父类的功能
class ElectricCar(Car):
    def __init__(self, make, model, year):
        """初始化父类的类型"""
        super().__init__(make, model, year)
        #super()函数使得子类和父类联系起来，使得子类继承父类的方法
        
my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.read_odometer()
my_tesla.increment_odometer(235)
my_tesla.read_odometer()

    #给子类定义属性和方法
class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    def __init__(self, make, model, year):
        """
        初始化父类的类型
        再初始化电动车特有的类型
        """
        super().__init__(make, model, year)
        self.battery_size = 70
    def describe_battery(self):
        """打印一条描述电瓶容量的信息"""
        print("This car has a " + str(self.battery_size) + "-kWh battery")

my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()

    #子类修改父类的方法()
class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    def __init__(self, make, model, year):
        """
        初始化父类的类型
        再初始化电动车特有的类型
        """
        super().__init__(make, model, year)
        self.battery_size = 70
    def describe_battery(self):
        """打印一条描述电瓶容量的信息"""
        print("This car has a " + str(self.battery_size) + "-kWh battery")
    def fill_gas_tank(Car):#在这里直接定义新的方法，但是括号里要引用父类名
            """电动车没有油箱"""
            print("This car doesn't need a gas tank!")

my_tesla = ElectricCar('tesla', 'model s', 2016)
my_tesla.fill_gas_tank()


#将实例用作属性（类的嵌套）
class Car():
    """一次模拟汽车的简单尝试"""
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def fill_gas_tank(self):
        """汽车有油箱"""
        print("This car need a gas tank!")
    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")
    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    def increment_odometer(self, miles):
        self.odometer_reading += miles

class Battery():
    """一次模拟电动车电瓶的简单尝试"""
    def __init__(self, battery_size = 70):
        """初始化电瓶的属性"""
        self.battery_size = battery_size
    def describe_battery(self):
        """打印一条描述电瓶容量的消息"""
        print("This car has a " + str(self.battery_size) + "-kWh battery")
    def get_range(self):
        """打印一条消息，指出电瓶的续航里程"""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)
        
class ElectricCar(Car):
    """电动车的独特之处"""
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()
        
my_tesla = ElectricCar('tesla', 'model s', 2016)
my_tesla.get_descriptive_name()
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()




#打开文件
with open('word.txt') as file_object:
    contents = file_object.read()
    print(contents)
    #删除多出来的空行
    print(contents.rstrip())
#打开其他文件夹的文件
    #要注意反斜杠与斜杠，直接复制的路径可以加 r 来避免反斜杠的问题
file_path = r'C:/Python work/learn Python/test.txt.txt'
with open(file_path) as file_object:
    contents = file_object.read()
    print(contents.rstrip())

with open('C:/Python work/learn Python/test.txt.txt') as file_object:#不加 r ，要用斜杠，而不是反斜杠
    contents = file_object.read()
    print(contents.rstrip())    
     
with open(r'C:\Python work\learn Python\test.txt.txt') as file_object:#加上r可以自动转译
    contents = file_object.read()
    print(contents.rstrip())    
     
#逐行读取文件
with open('word.txt') as file_object:
    for line in file_object:
        print(line)#空行会变的很多
        print(line.rstrip())


#创建一个包含文件各行的列表
filename = r'C:\Python work\learn Python\test.txt.txt'
with open(filename) as file_object:
    lines = file_object.readlines()
for line in lines:
    print(line.rstrip())

#使用文件中的数据
filename = r'C:\Python work\learn Python\test.txt.txt'
with open(filename) as file_object:
    lines = file_object.readlines()
    pi_string = ''
for line in lines:
    pi_string += line.rstrip()
print(pi_string)
print(len(pi_string))

#写入文件
filename = 'programming.txt'
with open(filename, 'w') as file_object:
    file_object.write("I love Python" + str(3.0) + '\n')
    file_object.write('I love programming\n')

#添加到文件
filename = 'programming.txt'
with open(filename, 'a') as file_object:
    file_object.write("I also love finding meaning in large datasets.\n")


#异常： try-except
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")

    #用try-except-else提高代码抵御错误的能力
print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")
while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by zero!")
    else:
        print(answer)

#计算一本书中有多少个单词
filename = 'alice.txt'
try:
    with open(filename) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    message = "Sorry, the file " + filename + " does not exist."
    print(message)
else:
    #计算文件有多少个字，以空格为分隔符
    words = contents.split()
    num_words = len(words)
    print("The file " + filename + " has about " + str(num_words) + " words.")

#储存数据
import json
numbers = [2, 3, 5, 7, 11, 29, 12]
filename = 'numbers.json'
with open(filename,'w') as f_obj:
    json.dump(numbers, f_obj)

#读取数据
import json
filename = 'numbers.json'
with open(filename) as f_obj:
    numbers = json.load(f_obj)
print(numbers)

#储存用户输入的内容
import json
username = input('What is your name? ')
filename = 'username.json'
with open(filename, 'w') as f_obj:
    json.dump(username, f_obj)
    print("We'll remember you when you come back, " + username + "!")

#使用上面储存的内容输出
import json
filename = 'username.json'
with open(filename) as f_obj:
    username = json.load(f_obj)
    print("Welcome back, " + username + '!')


# 如果以前存储了用户名，就加载它
# 否则，就提示用户输入用户名并存储它
import json
filename = 'username.json'
try:
    with open(filename) as f_obj:
        username = json.load(f_obj)
except FileNotFoundError:
    username = input("what is your name?")
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
        print("We'll remember you when you come back, " + username + "!")
else:
    print("Welcome back, " + username + '!')

#重构上述代码
import json
def get_stored_username():
    """如果储存了用户名，则获取他"""
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    """提示用户输入用户名"""
    username = input("what is your name?")
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
        
def greet_user():
    """问候用户，并指出名字"""
    username = get_stored_username()
    if username:
         print("Welcome back, " + username + '!')
    else:
        username = get_new_username()
        print("We'll remember you when you come back, " + username + "!")

greet_user()








