# 单行注释

"""
多行注释
"""


'''
占位符	替换内容
%d	整数
%f	浮点数
%s	字符串
%x	十六进制整数
f'xxx{a}xxx'变量a替换
'''
print("整数:%d,浮点数:%f,字符串:%s,十六进制整数:%x"%(12,9.3,'中文',100))
a = 12
b = '20度'
print(f'今天是{a}号，气温有{b}')

#转义字符
str1 = 'I\'m \"OK!\"'
print("str1=",str1)

#换行
str2 = ''' 第一行   
...第二行
...第三行'''
print("str2=",str2)

#布尔需要大小写True Flase
str3 = True
str4 = False
if str3:
    print(str3)
if not str4:
    print(str4)

'''
/是浮点数除法，结果始终是浮点数
//是地板除，结果是整数
%是取余数
'''
print(9/3)
print(9//3)
print(10/3)
print(10//3)
print(9%3)
print(10%3)

#1字节8比特，1个字符占字节数不确定
str5 = '中国中文'
print(str5.encode('utf-8'))
print(b'\xe4\xb8\xad\xe5\x9b\xbd\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))


