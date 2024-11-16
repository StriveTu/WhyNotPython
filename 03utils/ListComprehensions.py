'''
列表生成式即List Comprehensions，用来创建list
[expression for item in iterable if condition]
expression：列表中的每个元素的表达式，表示如何计算列表中的值。
item：从可迭代对象中取出的元素。
iterable：被迭代的对象（如列表、字符串、range等）。
if condition（可选）：条件过滤，仅当条件为 True 时才执行。
'''
list1 = list(range(1,11))
print(list1) #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

list2 = [x for x in range(1,11)]
print(list2) #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 只生成偶数
evens = [x for x in range(10) if x % 2 == 0]
print(evens)  # 输出: [0, 2, 4, 6, 8]

# 生成笛卡尔积
pairs = [(x, y) for x in range(3) for y in range(3)]
print(pairs)  # 输出: [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]

#同理字典生成式
squares = {x: f'{x}' for x in range(5)}
print(squares)  # 输出: {0: '0', 1: '1', 2: '2', 3: '3', 4: '4'}



