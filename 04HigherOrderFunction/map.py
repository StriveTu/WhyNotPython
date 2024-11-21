'''
map(function, iterable, ...)
map 用于将一个函数应用到一个或多个可迭代对象（如列表、元组）中的每个元素上，返回一个新的迭代器
'''
def abc(x):
    return x+x

list1 = [1,2,3,4]
res = map(abc,list1)
print('res',res)# res <map object at 0x00000233C9D86F20>
#返回一个 map 对象（迭代器），可以用 list() 或 tuple() 转换为具体的集合
result = list(res)
print('result',result)# result [2, 4, 6, 8]

def dou(x,y):
    return x+y
list2 = [5,10,15,20]
list3 = [50,100,150,200]
res2 = map(dou,list2,list3)
print('res2',list(res2))# res2 [55, 110, 165, 220]


