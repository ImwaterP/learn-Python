# names = ['Michael', 'Bob', 'Tracy']
# scores = [95, 75, 85]
# d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
# print(d['Michael'])

# 'Thomas' in d

# d.get('Thomas',-1)
# # d['Adam'] = 67
# # print(d['Adam'])

# s1 = (1, 'a1', [2, 'a2'])#list
# s2 = [1, 2, 3,[4, 5, 6]]#tuple
# s3 = {'b1': 11, 'b2': 12}#dict
# s4 = set([1, 2, 3, 3, 5])#set()
# print(s1)
# print(s2)
# print(s3)
# print(s4)

# n1 = 255
# n2 = 1000
# print(hex(n1))
# print(hex(n2))

# def my_abs(x):
	# if not isinstance(x,(int, float)):
		# raise TypeError('bad openrand type')
	# if x >= 0:
		# return x
	# else:
		# return -x

import math
# def move(x, y, step, angle = 0):
	# nx = x + step * math.cos(angle)
	# ny = y - step * math.sin(angle)
	# return nx, ny
	
# def quadratic(a, b, c):
	# if a == 0:
		# x1 = -c / b
		# x2 = x1
		# return x1, x2
	# Y = b * b - 4 * a * c
	# if Y < 0:
		# print('no answer')
		# return
	# elif Y == 0:
		# x1 = -b / 2 * a
		# x2 = x1
		# return x1, x2
	# else:
		# x1 = (-b + math.sqrt(Y)) / (2 * a)
		# x2 = (-b - math.sqrt(Y)) / (2 * a)
		# return x1, x2
		
		# # 测试:
# print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
# print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))

# if quadratic(2, 3, 1) != (-0.5, -1.0):
    # print('测试失败')
# elif quadratic(1, 3, -4) != (1.0, -4.0):
    # print('测试失败')
# else:
    # print('测试成功')

# def power(x, n = 2):
	# s = 1
	# while n > 0:
		# s = s * x
		# n = n - 1
	# return s
	
# print(power(5))
# print(power(5,3))

# def add_end(L = None):
	# if L == None:
		# L = []
	# L append('End')
	# return L
		
# def calm(*num):
	# sum = 0
	# for n in num:
		# sum = sum + num * num
	# return sum
	
# def person(name, age, **kw):
	# print('name :', name, 'age :', age, 'other :', kw)
	
# print(person('Tom', 66))

# def person(name, age, **kw):
	# print('name :',name, 'age :', age, 'other :', kw)
	
# extra = {'home':'China', 'sexal':'Yes'}
# a = person('Tony', 18 , **extra)
# print(a)

# def print_Hello(name, sex):
	# sex_dict = {1 : '先生', 2 :'女士'}
	# print('Hello,%s %s,welcome to Python world!'% (name, sex_dict.get(sex, '先生')))
# print(print_Hello(sex = 2, name = 'tont'))

# def test_some(name, sex, age, **kw):
	# print(name ,sex, age, kw)
# a = test_some(sex = 'man', address = 'China', age = 29, name = 'Tony')

# def test_some(name, sex, *wife_name, address = 'China'):
	# print(name, sex, wife_name, address)
# # a = test_some('Tony', 'man', address = 'China')
# b = test_some('Tony', 'man', 'Lilly', 'Bob', address = 'US')

# def product(*x):
# #要考虑没有输入的情况
	# if len(x) == 0:
		# raise TypeError('Your are wrong')
	# else:
		# s = 1
		# i = 0
		# for i in x:
			# s = s * i
		# return s
	# # 测试
# print('product(5) =', product(5))
# print('product(5, 6) =', product(5, 6))
# print('product(5, 6, 7) =', product(5, 6, 7))
# print('product(5, 6, 7, 9) =', product(5, 6, 7, 9))
# if product(5) != 5:
    # print('测试失败!')
# elif product(5, 6) != 30:
    # print('测试失败!')
# elif product(5, 6, 7) != 210:
    # print('测试失败!')
# elif product(5, 6, 7, 9) != 1890:
    # print('测试失败!')
# else:
    # try:
        # product()
        # print('测试失败!')
    # except TypeError:
        # print('测试成功!')
		
def trim(s):

	if len(s) == 0:
		return s
	elif s[0] == ' ':
		return trim(s[1:])
	elif s[-1] == ' ':
		return trim(s[:-1])
	return s
	
# 测试:
if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')	
	
	
	
	
