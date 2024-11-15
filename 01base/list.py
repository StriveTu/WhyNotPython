sp = ','
list1 = [1,'a',9.3,1,1,'s','k']
print(list1[0],sp,list1[1],sp,list1[2],sp,list1[-1],sp,list1[-2])
l=len(list1)
print(f'list1为{list1},长度是{l}')

#加元素
list1.append('Tuyf')
print('末尾加Tuyf：',list1)
list1.insert(2,9.333)
print('在索引2插入9.333：',list1)
list1[2]=10
print('把索引2元素换成10：',list1)

#减元素
list1.pop()
print('减去末尾元素：',list1)
list1.pop(2)
print('减去第三个元素',list1)