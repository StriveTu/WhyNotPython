'''
切片操作
param[start:stop:step]
start: 切片开始的索引（包括该索引）。默认值为 0。
stop: 切片结束的索引（不包括该索引）。默认值为序列长度。
step: 步长（默认为 1）。可以为负值实现逆序切片。
'''
list1 = ['a','b','c',1,2,3]

print(list1[2:4]) #['c', 1]

print(list1[::]) # ['a', 'b', 'c', 1, 2, 3]

print(list1[0:6:1]) # ['a', 'b', 'c', 1, 2, 3]

print(list1[::2]) # ['a', 'c', 2]

print(list1[:-1:]) #['a', 'b', 'c', 1, 2]

print(list1[::-1]) # [3, 2, 1, 'c', 'b', 'a']

str1 = 'tuyufeng'
print(str1[:2]) # 'tu'
print(str1[2:])# 'yufeng'


'''一些其它用法'''
#切片赋值（仅适用于可变序列，如列表）
list2 = [5,6,7,8,9]
list2[1:-1] = [60,70,80]
print(list2) #[5, 60, 70, 80, 9]
#清空list
list2[:] = []
print(list2) # []

