'''
迭代
大部分使用for循环
也可以使用 iter() 将可迭代对象转换为迭代器，用 next() 获取元素
'''
#for循环
list1 = [1,2,3,4,5,6]
for a in list1:
    print(a)
#带下标的用enumerate()函数
for i,a in enumerate(list1):
    print(i,a)

#迭代器
list1Iter = iter(list1)
print(next(list1Iter))
print(next(list1Iter))
print(next(list1Iter))

#迭代字典
d = {'a': 1, 'b': 2, 'c': 3}
for key in d:  # 默认迭代键
    print(key)

for value in d.values():  # 迭代值
    print(value)

for key, value in d.items():  # 迭代键值对用 d.items()
    print(key, value)

#迭代多个序列,使用 zip()：
names = ['Alice', 'Bob', 'Charlie']
scores = [85, 90, 95]
for name, score in zip(names, scores):
    print(f"{name}: {score}") # Alice: 85    Bob: 90    Charlie: 95


