"""
复制列表
"""
stock1 = ["同花顺", "东方财富", "大智慧"]
stock2 = stock1
stock2.append("雪球")
print(stock2)
print(stock1)

#使用列表切片
stock1 = ["同花顺", "东方财富", "大智慧"]
stock2 = stock1[:]
stock2.append("雪球")
print(stock2)
print(stock1)

#使用copy()函数
stock1 = ["同花顺", "东方财富", "大智慧"]
stock2 = stock1.copy()
stock2.append("雪球")
print(stock2)
print(stock1)




































