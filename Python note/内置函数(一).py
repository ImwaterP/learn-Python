"""
abs
"""
print(-50)
print(abs(-50))
print(abs(-50.123))

"""
all()
作用对象：列表或者元组
"""
print(all(["a", "b", "c"]))
print(all(["a", "b", ""]))
print(all(["a", "b", 0]))
print(all(["a", "b", "0"]))

"""
any()
作用对象：列表或者元组
"""
print(any(["a", "b", "c"]))
print(any([0, "", False]))
print(any([0, "b", False]))
print(any([0, "0", False]))

"""
float:
"""
a = "apple"
print(a)
print(float(a))

b = 25
print(b)
print(float(b))

"""
format函数
保留百分比格式
"""
print("{:.1%}".format(1.23456789))
print("{:.2%}".format(1.23456789))
print("{:.3%}".format(1.23456789))
print("{:.4%}".format(1.23456789))



















