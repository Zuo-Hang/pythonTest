# encoding: utf-8

# 任何非0和非空（null）值为true，0 或者 null为false。

flag = False
name = 'luren'
if name == 'python':         # 判断变量否为'python'
    flag = True          # 条件成立时设置标志为真
    print 'welcome boss'    # 并输出欢迎信息
else:
    print name  # 条件不成立时输出变量名称

# python 并不支持 switch 语句，所以多个条件判断，只能用 elif 来实现
num = 5
if num == 3:            # 判断num的值
    print 'boss'
elif num == 2:
    print 'user'
elif num == 1:
    print 'worker'
elif num < 0:           # 值小于零时输出
    print 'error'
else:
    print 'roadman'     # 条件均不成立时输出

# 同一行的位置上使用if条件判断语句
var = 100

if (var == 100): print "变量 var 的值为100"

print "Good bye!"