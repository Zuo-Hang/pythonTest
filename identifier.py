# encoding: utf-8

# 在 Python 里，标识符有字母、数字、下划线组成。
# 在 Python 中，所有标识符可以包括英文、数字以及下划线（_），但不能以数字开头。
# Python 中的标识符是区分大小写的。
# 以下划线开头的标识符是有特殊意义的。以单下划线开头（_foo）的代表不能直接访问的类属性，需通过类提供的接口进行访问，不能用"from xxx import *"而导入；
# 以双下划线开头的（__foo）代表类的私有成员；以双下划线开头和结尾的（__foo__）代表python 里特殊方法专用的标识，如__init__（）代表类的构造函数。
# 可以编写一个脚本用python xxx.py来运行
# python使用锁进来定义代码块，在方法之间预留空行
# print 默认输出是换行的，如果要实现不换行需要在变量末尾加上逗号 ,
# 像 if、while、def 和 class 这样的复合语句，首行以关键字开始，以冒号( : )结束，该行之后的一行或多行代码构成代码组。
# 变量

counter = 100  # 赋值整型变量
miles = 1000.0  # 浮点型
name = "John"  # 字符串

print counter
print miles
print name

a = b = c = 1
print a,b,c
a, b, c = 1, 2, "john"
print a,b,c

# Python 有五个标准的数据类型：
#
# Numbers（数字）
# String（字符串）
# List（列表）
# Tuple（元组）
# Dictionary（字典）

# 数字数据类型用于存储数值。
#     Python 支持四种不同的数值类型：
#     int（有符号整型）
#     long（长整型[也可以代表八进制和十六进制]）
#     float（浮点型）
#     complex（复数）
#
# 他们是不可改变的数据类型，这意味着改变数字数据类型会分配一个新的对象。
#
# 当你指定一个值时，Number 对象就会被创建：

var1 = 1
var2 = 10
# 可以使用 del 语句删除一些对象引用
del var1

# 列表
list = ['abcd', 786, 2.23, 'john', 70.2]
tinylist = [123, 'john']
print "-----------------list--------------------"
print list  # 输出完整列表
print list[0]  # 输出列表的第一个元素
print list[1:3]  # 输出第二个至第三个的元素
print list[2:]  # 输出从第三个开始至列表末尾的所有元素
print tinylist * 2  # 输出列表两次
print list + tinylist  # 打印组合的列表


# 元组
# 元组用"()"标识。内部元素用逗号隔开。但是元素不能二次赋值，相当于只读列表。
tuple = ('abcd', 786, 2.23, 'john', 70.2)
tinytuple = (123, 'john')
print "--------------------元组-----------------"
print tuple  # 输出完整元组
print tuple[0]  # 输出元组的第一个元素
print tuple[1:3]  # 输出第二个至第三个的元素
print tuple[2:]  # 输出从第三个开始至列表末尾的所有元素
print tinytuple * 2  # 输出元组两次
print tuple + tinytuple  # 打印组合的元组