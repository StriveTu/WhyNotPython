"""
返回函数的基本概念
一个函数可以将另一个函数作为返回值返回，并在需要时调用。
返回函数的核心思想是：延迟执行逻辑 或 动态生成新函数。
"""
def outer_function():
    print('out')
    def inner_function():
        return "Hello from inner function!"
    return inner_function

# 调用 outer_function，得到 inner_function 的引用
func1 = outer_function()
print(func1())  # 输出:out  "Hello from inner function!"

#闭包：带状态的返回函数
#返回函数可以捕获父函数中的局部变量，这种特性称为闭包。
def power_factory(exponent):
    def power(base):
        return base ** exponent
    return power

func2 = power_factory(2)  # 创建平方函数
func3 = power_factory(3)    # 创建立方函数

print(func2(4))  # 输出: 16
print(func3(3))    # 输出: 27



