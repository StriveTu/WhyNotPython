"""
偏函数（Partial Function）是 Python 中 functools 模块提供的一个功能，用于固定某些函数的参数值，从而创建一个新的函数。它是一种函数式编程技巧，能简化调用时的代码。
from functools import partial

partial(func, *args, **kwargs)
func：要被包装的原始函数。
*args：固定的定位参数。
**kwargs：固定的关键字参数。
"""
from functools import partial

# 原函数
def power(base, exp):
    return base ** exp

# 创建偏函数，固定参数 exp=2
square = partial(power, exp=2)

# 使用偏函数
print(square(4))  # 输出: 16
print(square(5))  # 输出: 25

#创建日志打印工具
def log(message, level):
    print(f"[{level}] {message}")

info = partial(log, level="INFO")
error = partial(log, level="ERROR")

info("System is running")       # 输出: [INFO] System is running
error("System error occurred")  # 输出: [ERROR] System error occurred

#生成函数用于统计单词长度
from functools import partial

def count_words(text, separator):
    return len(text.split(separator))

# 固定分隔符为空格
word_counter = partial(count_words, separator=" ")

print(word_counter("Python is awesome!"))  # 输出: 3


