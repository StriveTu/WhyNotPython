"""
sorted 会返回一个经过排序的列表，不会改变原可迭代对象的顺序。
sorted(iterable, key=None, reverse=False)
iterable：一个可迭代对象，例如列表、元组、字符串、字典等。
key：一个函数，用于指定排序的依据。默认为 None，表示直接比较元素的值。
reverse：布尔值，True 表示降序排序，False 表示升序排序（默认）。
返回一个 新的排序列表。
"""
#排序列表
numbers = [4, 2, 8, 1]
sorted_numbers = sorted(numbers)
print(sorted_numbers)  # 输出 [1, 2, 4, 8]

#降序
numbers = [4, 2, 8, 1]
sorted_numbers = sorted(numbers, reverse=True)
print(sorted_numbers)  # 输出 [8, 4, 2, 1]

#按字符串长度
words = ["apple", "banana", "pear", "kiwi"]
sorted_words = sorted(words, key=len)
print(sorted_words)  # 输出 ['kiwi', 'pear', 'apple', 'banana']

#按dict中的某个key排序
people = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 20},
    {"name": "Eve", "age": 30},
]
sorted_people = sorted(people, key=lambda person: person["age"])
print(sorted_people)# 输出 [{'name': 'Bob', 'age': 20}, {'name': 'Alice', 'age': 25}, {'name': 'Eve', 'age': 30}]


