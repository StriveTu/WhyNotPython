#Python内置了字典：dict的支持，dict全称dictionary，
# 在其他语言中也称为map，使用键-值（key-value）存储，具有极快的查找速度。
dict1 = {'key1':'value1','key2':'value2'}
print(dict1)
print(dict1['key1'],dict1['key2'])
print(dict1.get('key1'))

#加键值对(没有set方法,直接用dict['key']加)
dict1['name'] = 'tuyf'
print(dict1)
#减
dict1.pop('name')
print(dict1)

#用in判断key是否存在
m = 'key10' in dict1
n = 'key1' in dict1
print(m,n)

#如果key不存在，可以返回None，或者自己指定的value：
print(dict1.get('key3'))
print(dict1.get('key3','不存在'))
print(dict1)

#set集合
set1 = {1,'2',3.0,'tuyf',1,2,'2','yf','tuyf'}
print(set1)

#加减
set1.add(10)
set1.remove(3.0)
print('加减',set1)

#交集和并集操作
s1 = {1,2,3,4}
s2 = {3,4,5,6}
print('交集',s1 & s2)
print('并集',s1 | s2)