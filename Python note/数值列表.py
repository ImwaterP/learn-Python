"""
数值列表
"""
#range()函数【左闭右开】
for i in range(1,11):
    print(i)

#list函数与range函数结合
num = list(range(1,11))
print(num)

#生成1到10的偶数

values=[]
for i in range(1,6):
    value = 2*i
    values.append(value)
#    print(value)
print(values)


for i in range(2,11,2):
    print(i)

#计算数字1到10的平方和
result = []
for i in range(1,11):
    value = i**2
    result.append(value)
    
print(sum(result))
































