"""
类与对象
继承封装多态和java一样
私有用__a,让内部属性不被外部访问
继承：class Son(Father)
"""

#1.类
class MyClass:
    # 类属性
    class_variable = "I am a class variable"
    # 初始化方法（构造函数）
    def __init__(self, instance_variable):
        self.instance_variable = instance_variable  # 实例属性
    # 实例方法
    def instance_method(self):
        return f"字符串是: {self.instance_variable}"

# 2.对象
obj = MyClass("obj hello")
# 访问属性
print(obj.instance_variable)
# 调用方法
print(obj.instance_method())

#3.类中的属性
"""
类属性：
定义在类体中的变量，属于整个类共享。
通过 类名.属性 或 对象.属性 访问。

实例属性：
由 __init__ 方法创建，属于每个对象独立。
"""

class Example:
    class_variable = "类属性"  # 类属性

    def __init__(self, value):
        self.instance_variable = value  # 实例属性

obj1 = Example("对象1")
obj2 = Example("对象2")

print(obj1.class_variable) #类属性
print(obj2.class_variable) #类属性
print(obj1.instance_variable) #对象1
print(obj2.instance_variable) #对象2


#4.方法
"""
实例方法：
第一个参数为 self，用于访问实例属性和方法。
只能通过实例调用。

类方法：
使用 @classmethod 装饰，第一个参数为 cls，用于操作类属性。
通过类或实例调用。

静态方法：
使用 @staticmethod 装饰，不需要 self 或 cls 参数。
通过类或实例调用
"""
class Example:
    class_variable = "类属性"
    def __init__(self,v1,v2,v3):
        self.a = v1
        self.b = v2
        self.c = v3

    def m1(self):
        print('m1被调用',self.a,self.b,self.c)

    @classmethod
    def m2(cls):
        return f"Class method: {cls.class_variable}"

    @staticmethod
    def m3():
        return "静态方法"


print(Example.m2())
print(Example.m3())
ex1 = Example('j','k','l')
ex1.m1()
print(ex1.m2())
print(ex1.m3())

