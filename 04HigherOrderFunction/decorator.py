"""
装饰器（Decorator）是 Python 中的一种设计模式，用于在不改变函数定义的情况下，动态地为函数或方法添加功能。装饰器本质上是一个高阶函数，它接收一个函数作为参数并返回一个新的函数
1.在函数调用前后动态添加功能。
2.提高代码的可复用性和可读性。
3.实现逻辑分离，增强代码的清晰性。
"""
def dec1(func):
    def wrapper(*args, **kwargs):
        print("---Before---")
        result = func(*args, **kwargs)
        print("---After---")
        return result
    return wrapper

@dec1
def test1(name):
    print(f"Hello, {name}!")

test1("Alice")
