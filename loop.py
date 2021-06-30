# encoding: utf-8

print "-----------while loop1----------"
count = 0
while (count < 9):
  print 'The count is:', count
  count = count + 1
print "Good bye!"

print "-----------while loop2----------"
i = 1
while i < 10:
    i += 1
    if i % 2 > 0:  # 非双数时跳过输出
        continue
    print i  # 输出双数2、4、6、8、10

i = 1
while 1:  # 循环条件为1必定成立
    print i  # 输出1~10
    i += 1
    if i > 10:  # 当i大于10时跳出循环
        break
print "-----------while loop3----------"

# while … else 在循环条件为 False 时执行 else 语句块
count = 0
while count < 5:
   print count, " is  less than 5"
   count = count + 1
else:
   print count, " is not less than 5"

print "-----------while loop4----------"
flag = 1

# while (flag): print 'Given flag is really true!'

print "Good bye!"


print "-----------for loop1----------"
for letter in 'Python':     # 第一个实例
   print '当前字母 :', letter

fruits = ['banana', 'apple',  'mango']
for fruit in fruits:        # 第二个实例
   print '当前字母 :', fruit

print "Good bye!"

print "-----------for loop2----------"
fruits = ['banana', 'apple',  'mango']
for index in range(len(fruits)):
   print '当前水果 :', fruits[index]

print "Good bye!"
# 内置函数 len() 和 range(),函数 len() 返回列表的长度，即元素的个数。 range 返回一个序列的数
print range(len(fruits))

# for … else 表示这样的意思，for 中的语句和普通的没有区别，else 中的语句会在循环正常执行完（即 for 不是通过
# break 跳出而中断的）的情况下执行，while … else 也是一样。
print "-----------for loop3----------"
for num in range(10,20):  # 迭代 10 到 20 之间的数字
   for i in range(2,num): # 根据因子迭代
      if num%i == 0:      # 确定第一个因子
         j=num/i          # 计算第二个因子
         print '%d 等于 %d * %d' % (num,i,j)
         break            # 跳出当前循环
   else:                  # 循环的 else 部分
      print num, '是一个质数'

print range(10,20)