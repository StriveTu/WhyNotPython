'''
在Python中，定义一个函数要
使用def语句，依次写出函数名、括号、括号中的参数和冒号:，
然后，在缩进块中编写函数体，函数的返回值用return语句返回。
'''
def swap(a,b):
    a = f'xxx{a}xxx'
    b = f'***{b}***'
    return a,b


m = 10
n = 5
print(m,n)
(m,n)=swap(m,n)
print(m,n)

#Python的函数返回多值其实就是返回一个tuple
h=swap(m,n)
print(h)

#参数可以赋默认值，必填参数在前，默认参数在后
def power(a,n=2):
    s = 1
    while n > 0:
        s = a * s
        n = n - 1
    return s

b = power(4)
print(b)
b = power(4,3)
print(b)

#当不按顺序提供部分默认参数时，需要把参数名写上
# 定义默认参数要牢记一点：默认参数必须指向不变对象！
def mArg(a,b,c=1,d=5):
    print(a,b,c,d)

mArg(9,8,7)# 9 8 7 5
mArg(9,8,d=7)# 9 8 1 7

#可变参数 *a,a为list或tuple
def anyParams(*a):
    print(a)
anyParams(1, 2, 3, 4)# (1, 2, 3, 4)
anyParams(1)# (1,)
anyParams()# ()

#关键字参数,**c传键值对或dict
def keyParams(a,b,**c):
    print(a,b,c)
keyParams(1,2,key1=3,v='tuyf',m=0)# 1 2 {'key1': 3, 'v': 'tuyf', 'm': 0}

#命名关键字参数，需要一个特殊分隔符*，*后面的参数被视为命名关键字参数
#如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要特殊分隔符*了：
def keyNameParams(a,b,*,c,d):
    print(a,b,c,d)
keyNameParams(1,2,c=3,d=4)# 1 2 3 4

def keyMParams(a,*b,c,d):
    print(a,b,c,d)
keyMParams(1,3,5,0,c='v',d='f')# 1 (3, 5, 0) v f

#参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数
