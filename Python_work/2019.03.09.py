# -*- coding: utf-8 -*-

#嵌套
#将字典嵌套到列表里
alien_0 = {'color' : 'green', 'point' : 5}
alien_1 = {'color' : 'yellow', 'point' : 10}
alien_2 = {'color' : 'red', 'point' : 15}
aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    print(alien)
#自动创建字典
aliens = []
for alien_number in range(30):
    new_alien = {'color' : 'green', 'point' : 5, 'speed' : 'slow'}
    aliens.append(new_alien)
#显示前五个
for alien in aliens[:5]:
    print(alien)
print('Total number of aliens: ', str(len(aliens)))
#修改前三个数据
for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['point'] = 10
        alien['speed'] = 'medium'
for alien in aliens[:5]:
    print(alien)

#字典里嵌套列表
favorite_languages = {
        'tom' : ['C', 'Python'], 
        'john' : ['Java'], 
        'lily' : ['C++', 'C'], 
        'alice' : ['php', 'Python'], 
        }
#打印嵌套的列表，用两个for循环实现
for name, value in favorite_languages.items():
    print('\n' + name.title() + ' favorite languages are : ')
    for language in value : 
        print(language.title())
#优化输出，加一个if语句，如果列表内只有一个，更改输出内容
for name, languages in favorite_languages.items():
    if len(languages) <= 1:
        print('\n' + name.title() + ' favorite language is : ')
    else:
        print('\n' + name.title() + ' favorites languages are : ')
    for language in languages:
        print('\t' + language.title())

#
















