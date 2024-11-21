"""
reduce 将一个函数应用到可迭代对象的所有元素上，将其逐步归约为一个单一的值。

reduce(function, iterable, [initializer])

function：一个带两个参数的函数，用于逐步归约。
iterable：需要归约的可迭代对象。
initializer（可选）：初始值。
适用于需要将一组值累积成单个结果的场景（如求和、乘积）。
每次迭代时，将前一次的结果作为第一个参数，当前元素作为第二个参数。
"""
from functools import reduce

#累加计算
nums = [1, 2, 3, 4]
result = reduce(lambda x, y: x + y, nums)
print(result)  # 输出 10

#使用初始值
nums = [1, 2, 3, 4]
result = reduce(lambda x, y: x + y, nums, 10)
print(result)  # 输出 20

#求最大值
nums = [1, 5, 3, 9, 2]
result = reduce(lambda x, y: x if x > y else y, nums)
print(result)  # 输出 9


#map reduce的综合案例
def price(x):
    return x['price']
def sumPrice(x,y):
    return x+y

products = [{'name': 'A', 'price': 10}, {'name': 'B', 'price': 20}, {'name': 'C', 'price': 15}]
# 用 map 提取价格
prices = map(price, products)
# 用 reduce 计算总价
total_price = reduce(sumPrice, prices)

print(total_price)  # 输出 45


