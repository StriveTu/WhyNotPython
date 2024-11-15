#for x in list
names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print(name)

sum = 0
list1 = list(range(11))
for e in list1:
    sum = sum + e
print(sum)

#while
sum1 = 1
a = 3
t = 0
while sum1 < 50:
    sum1 = sum1 + a
    t = t+1
print(sum1,t)

#break
n = 1
while n <= 15:
    if n > 10: # 当n = 11时，条件满足，执行break语句
        break # break语句会结束当前循环
    print(n)
    n = n + 1
print('break , END')

#continue
n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0: # 如果n是偶数，执行continue语句
        continue # continue语句会直接继续下一轮循环，后续的print()语句不会执行
    print(n)

