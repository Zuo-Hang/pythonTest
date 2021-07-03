# encoding: utf-8
import cmath
import math
import json

l = dir(math)
dir1 = dir(cmath)

# 数字、字符串、列表、元组、字典

print l
print dir1
print "--------------number---------------"
# note
# 数据类型是不允许改变的、 del 语句删除一些数字对象引用

# 整型 (Int) - 通常被称为是整型或整数，是正或负整数，不带小数点。
# 长整型 (long integers) - 无限大小的整数，整数最后是一个大写或小写的L。
# 浮点型( floating point real values) - 浮点型由整数部分与小数部分组成，浮点型也可以使用科学计数法表示（2.5e2 = 2.5 x 102 = 250）
# 复数 ( complex numbers) - 复数的虚部以字母J 或 j结尾 。如：2+3i

# python 内置了很多的数学函数，可以直接调用

print "--------------字符串----------------"

print "--------------list-----------------"
list1 = ['physics', 'chemistry', 1997, 2000]
list2 = [1, 2, 3, 4, 5, 6, 7]

print "list1[0]: ", list1[0]
print "list2[1:5]: ", list2[1:5]

# 其实在python中是有一个list的类的，这个类提供类一些工具方法。
list.append()
print "--------------输出汉字-----------------"
list_words = ['你', '我', '他']
print(list_words)  # 无法正常显示汉字
print(str(list_words).decode('string_escape'))  # 正常显示汉字

list_words_result = json.dumps(list_words, encoding='UTF-8', ensure_ascii=False)
print(list_words_result)

print "--------------元组-----------------"
# 元组和list类似，但是元组是不可变的
tup1 = ('physics', 'chemistry', 1997, 2000);
tup2 = (1, 2, 3, 4, 5, 6, 7);

print "tup1[0]: ", tup1[0]
print "tup2[1:5]: ", tup2[1:5]
# 元组和列表的相互转换
list_to_tuple = tuple(tup2)
tuple_to_list = list(tup2)
print list_to_tuple
print tuple_to_list

print "--------------字典-----------------"
# 字典的键是要求不可变的,键必须不可变，所以可以用数，字符串或元组充当，所以用列表就不行
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

print "dict['Name']: ", dict['Name']
print "dict['Age']: ", dict['Age']
print dict
del dict['Name'] # 删除键是'Name'的条目
dict.clear()     # 清空词典所有条目
del dict         # 删除词典
print dict
