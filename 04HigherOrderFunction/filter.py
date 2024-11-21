"""
filter 用于根据指定的函数过滤可迭代对象中的元素，只保留函数返回值为 True 的元素
filter(function, iterable)
返回值
返回一个 filter 对象（迭代器），需要通过 list()、tuple() 等转换为具体的数据结构。
function：用于判断每个元素是否保留的函数，返回值需为布尔值。
如果为 None，会筛选出所有在布尔上下文中为 True 的元素。
iterable：一个可迭代对象，如列表、元组、集合、字符串等。
"""
def o2(x):
    flag = x%2==0
    return flag
iter1 = filter(o2,[1,2,3,4,5,6])
print(list(iter1)) #[2, 4, 6]

#筛选非空字符串
strings = ["hello", "", "world", None, "python"]
non_empty = filter(None, strings)
print(list(non_empty))  # 输出 ['hello', 'world', 'python']

#筛选大写字符
chars = "aBcDeFg"
uppercase = filter(str.isupper, chars)
print("".join(uppercase))  # 输出 "BDF"

