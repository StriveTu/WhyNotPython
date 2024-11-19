'''
生成器是一个返回迭代器的函数，使用 yield 关键字来生成值，而不是一次性返回所有值。
每次调用生成器的 __next__() 方法（或者使用 for 循环时），生成器会暂停，直到下次迭代时继续执行。
'''
#用yield生成值
def my_generator():
    yield 1
    yield 'hello'
    yield 3

gen = my_generator()
print(next(gen))  # 输出 1
print(next(gen))  # 输出 hello

for x in my_generator():
    print(x) #依次输出 1 hello 3

#生成器表达式
gen_expr = (x * x for x in range(5))
for num in gen_expr:
    print(num)  # 输出 0, 1, 4, 9, 16


#外部通信用send传值
def echo():
    while True:
        received = yield
        print(f'Received: {received}')

gen = echo()
next(gen)  # 启动生成器
gen.send('Hello')  # 输出 "Received: Hello"
gen.send('world')  # 输出 "Received: world"


#读取文件
def read_file(file_path):
    with open(file_path, 'r',encoding='utf-8') as file:
        for line in file:
            yield line.strip()

for line in read_file('tuyf.txt'):
    print(line)




