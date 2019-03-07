'''
今天我在对字典里的键用sorted排序时发现并没有按照预期排序
研究后发现字母大小写会影响排序
'''
#创建一个字典，键里面的首字母有大写有小写
favorite_digit = {
        'john' : 4, 
        'Tom' : 5, 
        'Lisa' : 9, 
        'liu' : 5, 
        'alice' : 0, 
        }
for name in sorted(favorite_digit.keys()):
    print(name.title())
#运行后发现与预期不符合
#我不使用title函数又进行排序
for name in sorted(favorite_digit.keys()):
    print(name)
#结果发现，sorted先对首字母大写进行排序，
#然后才对小写字母排序
#正因为我使用了title，使得排序看起来十分混乱

#避免此类情况的发生
#先创建一个字典将原先字典键小写化储存
favorite_digit_lower = {}
#然后遍历原先的字典，将键转化为小写
#同时将数据储存在新的字典中
for name, digit in favorite_digit.items():
    name = name.lower()
    #print(name)
#这里也可以加一个print检查name是否成功写入小写
#将原来字典的内容复制到新字典里
    favorite_digit_lower [name] = digit
#再次打印，结果为预期结果
for name in sorted(favorite_digit_lower.keys()):
    print(name.title())












