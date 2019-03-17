"""
for循环：
操作列表
"""
toothpastes = ["佳洁士", "舒客", "高露洁", "中华", "冷酸灵",
               "两面针", "纳爱斯"]

print(toothpastes[0])
print(toothpastes[1])
...
"""
1.toothpaste相当于中间变量，换成其他变量名也是可以的。
2.冒号问题。冒号不能省略。
3.缩进问题。
"""

for toothpaste in toothpastes:    
    print(toothpaste)
print("牙膏")

for a in toothpastes:
    print(a)

i = 1
for toothpaste in toothpastes:
    print("周{}用".format(i) + toothpaste + ".")
    i+=1
































