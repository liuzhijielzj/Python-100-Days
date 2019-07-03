#变量和类型
#整型, 处理任意大小的整数
print(0b100)
print(0o100)
print(0x100)
#浮点
print(1.2345e2)
#字符串
#原始字符串表示法、字节字符串表示法、Unicode字符串表示法
print('''
this is multi-line string
line 2
''')
#布尔
print(True)
print(False)
#复数
print(3 + 5j)




'''
变量命名:
1. 字母（广义的Unicode字符，不包括特殊字符）
、数字和下划线构成，数字不能开头.
2. 大小写敏感（大写的a和小写的A是两个不同的变量）。
3. 不要跟关键字（有特殊含义的单词，后面会讲到）和系统保留字（如函数、模块等的名字）冲突。
PEP 8要求：
用小写字母拼写，多个单词用下划线连接。
受保护的实例属性用单个下划线开头（后面会讲到）。
私有的实例属性用两个下划线开头（后面会讲到）。
'''
a = 321
b = 123
print(a // b) # 整除
print(a / b)
print(a % b)
print(a ** b) # 阶乘




'''
input: input from console
int: convert to int
用占位符格式化输出的字符串
'''
a = int(input('a = '))
b = int(input('b = '))
print('%d + %d = %d' % (a, b, a // b))



'''
type: check variable type
'''
print(type(100))
print(type(True))



'''
int()：将一个数值或字符串转换成整数，可以指定进制。
float()：将一个字符串转换成浮点数。
str()：将指定的对象转换成字符串形式，可以指定编码。
chr()：将整数转换成该编码对应的字符串（一个字符）。
ord()：将一个字符转换成对应的编码（整数）。
'''
print(ord('t'))
print(chr(116))






