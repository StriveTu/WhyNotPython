#if 注意条件不需要括号，else后面冒号，其余后面不跟
s = input('if匹配：')
age = int(s)
if age >= 18:
    print('adult')
elif age >= 6:
    print('teenager')
else:
    print('kid')

#match 匹配
a = input('match匹配：')
match a:
    case 'A':
        print('score is A.')
    case 'B':
        print('score is B.')
    case 'C':
        print('score is C.')
    case _: # _表示匹配到其他任何情况
        print('score is ???.')

#匹配条件、匹配多个
age = 15
match age:
    case x if x < 10:
        print(f'< 10 years old: {x}')
    case 10:
        print('10 years old.')
    case 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18:
        print('11~18 years old.')
    case 19:
        print('19 years old.')
    case _:
        print('not sure.')


#匹配列表(有点类似contains)
list2 = ['gcc', 'hello.c', 'world.c','1','2']
# list2 = ['clean']
# list2 = ['gcc']

match list2:
    # 如果仅出现gcc，报错:
    case ['gcc']:
        print('gcc: missing source file(s).')
    # 出现gcc，且至少指定了一个文件:
    case ['gcc', a, *b]:
        print('gcc compile: ' + a + ', ' + ', '.join(b))
    # 仅出现clean:
    case ['clean']:
        print('clean')
    case _:
        print('invalid command.')