# -*- coding: utf-8 -*-

name = "John"
print(name)
name = 123
print(name)

#output and some mode in common use
name = "ada lovelace"
print(name.title())
print(name.upper())
print(name.lower())

#combine character string
first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name
print("Hello, " + full_name.title() + "!")

#use \n or \t to add blank
print("python".title())
print("\tpython".title())
print("I love\nPython!")


#Delete useless blank

#Use .rstrip() to delete the char str of blank of back
language = " python "
language.rstrip()
language#The change is just temporary!
language = language.rstrip()#You can change it permanently by assignment
language

message = (" I love Python ! ")
print(message)
print(message.rstrip())#Only delete the back of blank

#Use .lstrip() to delete the char str of blank of foregoing
language = " python "
language.lstrip()

#Use .strip() to delete the char str of blank of both side
language = " python "
language.strip()


#Use .str() to avoid type error
age = 23
message = "Happy " + str(age) + "rd Birthday!"
print(message)


#List
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

#Access list elements
print(bicycles[0].title())
print(bicycles[2].title())
print(bicycles[3].title())

#Revise list elements
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
bicycles[0] = 'xdx'
print(bicycles)

#Add list elements
    #Use .append() to add new element to the end of list
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
bicycles.append('xdx')
print(bicycles)

    #Use .insert() to add new element to where you want in list
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
bicycles.insert(0, 'xdx')
bicycles.insert(2,  'ganta')
print(bicycles)

#Delete list elements
    #Use del(It is a function) to delete everyone you want to delete
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
del bicycles[0]
print(bicycles)

    #Use .pop() to popping element of the end
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
popped_bicycle = bicycles.pop()
print(bicycles)
        #If you use .pop(), you could also use what you delete.
print(popped_bicycle)

    #Use .pop() to popping element of where you want
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
first_owned = bicycles.pop(1)
print('The first bichcle I owned was a ' + first_owned.title() + '.')

    #Use .remove() to delete element on the basis of value
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
bicycles.remove('redline')
print(bicycles)
        #You can also use what you delete
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
too_expensive = 'trek'
bicycles.remove(too_expensive)
print(bicycles)
print('\nA ' + too_expensive.title() + ' is too expensive for me.')


#Sort your list

    #Use sort() to sort your list permanently
cars = ['Bmw', 'audi', 'toyota', 'subaru', '3ling']
cars.sort()
print(cars)#nums are above, capitals and lowercase is following.
    #use .sort(reverse = True) to reversely sort your list permanently
cars = ['Bmw', 'audi', 'toyota', 'subaru', '3ling']
cars.sort(reverse = True)
print(cars)

    #Use sorted() (It is a function) to sort your list temporary
cars = ['Bmw', 'audi', 'toyota', 'subaru', '3ling']
print('Here is the sorted list:')
print(sorted(cars))
print(cars)

    #Use reverse() to sort your list permanently
cars = ['Bmw', 'audi', 'toyota', 'subaru', '3ling']
cars.reverse()
print(cars)
        #You can recover your list simply by use .reverse() again
cars.reverse()
print(cars)

#Measure the length of list by function : len()
cars = ['Bmw', 'audi', 'toyota', 'subaru', '3ling']
len(cars)


#Traversing the entire list
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)
    #Operations of for loop
magicians = ['alice', 'david', 'carolina']
for magician in magicians:#Don't forget the indent and ':'!
    print(magician.title() + ', that was a greak trick!')
    print("I can't wait to see your next trick, " + magician.title() + '.\n')
print('Thank you everyone, that was a great magic show!')


#Creat digital list
    #function range()  {It is a type of [ ) }
for value in range(1,5):#1~4
    print(value)
for value in range(1,5):
    print(value - 1)#output 0~3

    #Use range() function to creat digital list
numbers = list(range(1,6))
print(numbers)
        #limit step length\size
odds = list(range(1,11,2))#output odds in 1~10
print(odds)
evens = list(range(2,11,2))
print(evens)

#Use range() fleliblely
#for example:Creat a squares list
squares = []
for value in range(1,11):
    squares.append(value ** 2)  #'**' on behalf of squares 乘方
print(squares)

#Simple calculation on the list
    #function min(), max(), sum()
digits = list(range(10)) #0~9
print(min(digits))
print(max(digits))
print(sum(digits))

#Use List of analytical to simplify your code
squates = [value ** 2 for value in range(1,11)]
print(squates)


#Use a part of list
    #Use slice(切片)
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[2:4])#output 3nd to 4th
print(players[:3])#output 1st to 3nd
print(players[1:])#output 2nd to the end
print(players[-3:])#output 3nd from bottom to the end

    #Traversing slice
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print('Here are the first three players on my team:')
for player in players[:3]:#traversing the first three
    print(player.title())

#Copy your list
    #Using slice to copy list must!
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]#Amount to slice the entire list
print(my_foods)
print(friend_foods)
my_foods.append('hamburger')
friend_foods.append('dumpling')
print(my_foods)
print(friend_foods)
    #If you don't use slice
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods
print(my_foods)
print(friend_foods)
my_foods.append('hamburger')
friend_foods.append('dumpling')
print(my_foods)
print(friend_foods)#friend_foods list like chain to my_foods list
#So must use slice to copy list!!!


#tuple(元组),which is that you can't change it's elements
dimensions = (200, 50)
dimensions[0] = 250#It is an typeError

#Redefine the tuple to support tuple assignment
dimensions = (200, 50)
print('Original dimensions:')
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)#redefinition
print('\nModified dimensions:')
for dimension in dimensions:
    print(dimension)


#if statement(if 语句)
cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':#Attention! '==' is not '='
        print(car.upper())
    else:
        print(car.title())
    #'==' is to detect, which is don't consider letter Case(大小写)

    #Check the condition of multiple
        #'and'
age_0 = 22
age_1 = 18
age_0 >= 21 and age_1 >= 21

age_1 = 22
age_0 >= 21 and age_1 >= 21
        #'or'
age_0 = 22
age_1 = 18
age_0 >= 21 or age_1 >= 21

age_0 = 18
age_0 >= 21 or age_1 >= 21

#Check whether a particular value in the list
banned_users = ['andrew', 'carolina', 'david'] 
user = 'marie'
user in banned_users
'marie' in banned_users
'david' in banned_users
'David' in banned_users#Attent the letter case

if user not in banned_users:
    print(user.title() + ', you can post a response if you wish.')

#if-elif-else statement
age = 12
if age < 4:
    print('Your admission cost is $0.')
elif age < 18:
    print('Your admission cost is $5.')
else:
    print('Your admission cost is $10.')
    
    #You can make your code more simpler
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 5
else:
    price = 10
print('Your admission cost is $' + str(price) + '.')

    #omit the else code block
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
elif age >= 65:
    price = 5
print('Your admission cost is $' + str(price) + '.')


#Using for statement to check particular elements
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print('Sorry, we are out of green peppers right now.')
    else:
        print('Adding' + requested_topping + '.')
print('\nFinished making your pizza!')

#Using for statement to make sure the list is not blank
requested_toppings = []
if requested_toppings:
    for requested_topping in requested_toppings:
        print("Adding " + requested_topping + '.')
    print('\nFinished making your pizza!')
else:
    print("Are you sure you want a plain pizza?")


#Using list multiple
available_toppings = ['mushrooms', 'olives', 'green peppers',
                      'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print('Adding ' + requested_topping + '.')
    else:
        print("Sorry, we don't have " + requested_topping + '.')
print("\nFinished making your pizza!")


#dictionary
alien_0 = {'color' : 'green', 'points' : 5}
print(alien_0['color'])
print(alien_0['points'])

#Adding Key-Value
alien_0 = {'color' : 'green', 'points' : 5}
print(alien_0)

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

#Change the value
alien_0 = {'color' : 'green', 'points' : 5}
alien_0['color'] = 'yellow'
print('The alien is now ' + alien_0['color'] + '.')

    #There is a little more complicated but interesting example.
        #Define a alien's original position
alien_0 = {'x_position' : 0, 'y_position' : 25, 'speed' : 'medium'}
print("Original x-position: " + str(alien_0['x_position']))

        #Let's move the alien to the left along the x axis
        #According to the speed level to decide how far should the alien move
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

        #New x-position is Original x-position add to x-increment
alien_0['x_position'] = alien_0['x_position'] + x_increment
print("New x-position: " + str(alien_0['x_position']))

#Deleting Key-Value with function del()
alien_0 = {'color' : 'green', 'points' : 5}
print(alien_0)

del alien_0['points']
print(alien_0)

#Travising the dictionary
    #Travising the entire dictionary with .items()
user_0 = {
        'usernames' : 'efermi',
        'first' : 'enrico',
        'last' : 'fermi',
        }
for key, value in user_0.items():
    print("\nkey: " + key)
    print("value: " + value)

    #Travising all the key of the dictionary with .keys()
favorite_languages = {
        'jen': 'python',
        'sarah': 'c',
        'edward': 'ruby',
        'phil': 'python',
        }
for name in favorite_languages.keys():
    print(name.title())
      
        #Something interesting example
favorite_languages = {
        'jen': 'python',
        'sarah': 'c',
        'edward': 'ruby',
        'phil': 'python',
        }
friends = ['jen', 'john', 'edward']
for friend in friends:
    print('\n' + friend)
    if friend in favorite_languages.keys():
        print("  Hi " + friend.title() + ', I see your favorite language is ' +
              favorite_languages[friend].title() + '!')
        
    #Travising all the value of the dictionary with .values()
favorite_languages = {
        'jen': 'python',
        'sarah': 'c',
        'edward': 'ruby',
        'phil': 'python',
        }
print('The following languages have been mentioned:')
for language in favorite_languages.values():
    print(language.title())
     
        #Remove the dumplicates with function set()
favorite_languages = {
        'jen': 'python',
        'sarah': 'c',
        'edward': 'ruby',
        'phil': 'python',
        }
print('The following languages have been mentioned:')
for language in set(favorite_languages.values()):
    print(language.title())       
    
#nest
#dictionary in list
aliens = []
for alien_number in range(30):
    new_alien = {'color' : 'green', 'points' : 5, 'speed' : 'slow'}
    aliens.append(new_alien)

for alien in aliens[:5]:#Just show the first three
    print(alien)
print("Total number of aliens: " + str(len(aliens)))

    #Modify the values in the dictionary(批量修改字典中的值)
aliens = []
for alien_number in range(30):
    new_alien = {'color' : 'green', 'points' : 5, 'speed' : 'slow'}
    aliens.append(new_alien)

for alien in aliens[:3]:
    if(alien['color'] == 'green'):
        alien['points'] = 10
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'

for alien in aliens[:5]:
    print(alien)

#list in dictionary
pizza = {
        'crust' : 'thick',
        'toppings' : ['mushrooms', 'extra cheese'],
        }
print("You ordered a " + pizza['crust'] + '-crust pizza ' +
      "with the following toppings.")
for topping in pizza['toppings']:
    print('\t' + topping)

#dictionary iin dictionary
users = {
    'aeinstein' : {
            'first' : 'albert',
            'last' : 'einstein',
            'location' : 'princeton',
            },
    'mcurie' : {
            'first' : 'marie',
            'last' : 'curie',
            'location' : 'paris',
            },
        }
for username, user_info in users.items():
    print("\nusername: " + username)
    full_name = user_info['first'] + user_info['last']
    location = user_info['location']
    print('\tFull_name: ' + full_name.title())
    print('\tLocation: ' + location.title())



#input() to get input
name = input('Tell me what is your name:')
print(name.title())

#Using function int() to get input of numbers
age = input('How old are you?')
age#The type is char

age = int(input('How old are you?'))
age

#While loop
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1
    
#Using Flag
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program."

active = True#This is a flag
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)

#Using break to quit the entire while loop
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program."

while active:
    message = input(prompt)
    if message == 'quit':
        break#quit loop
    else:
        print(message)

#Using continue to only quit while loop this time
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)        

#Using while loop to deal with dictionary and list
    #move elements in different lists
unconfirmed_name = ['alice', 'brian', 'candace']
confirmed_users = []
while unconfirmed_name:
    current_user = unconfirmed_name.pop()
    print('Verifying user: ' + current_user.title())
    confirmed_users.append(current_user)

print('\nThe following users have been confirmed:')
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

    #delete the element of list, which has particular value
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)
while 'cat' in pets:
    pets.remove('cat')
print(set(pets))

    #Use the user input to populate the dictionary
responses = {}

polling_active = True

while polling_active:
    name = input('\n What is your name?')
    response = input("Which mountain would you like to climb someday? ")
    
    responses[name] = response
    
    repeat = input("Would you like to let another person respond? (yes/ no) ")
    
    Nos = ['no', 'No', 'NO']
    if repeat in Nos:
        polling_active = False

print("\n--- Poll Results ---")
for name, response in responses.items():
    print(name.title() + 'would like to climb ' + response + '.')























