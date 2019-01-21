'''
Created on 2018年3月20日
你有一个数据序列，想利用一些规则从中提取出需要的值或者是缩短序列
@author: Administrator
'''
# 列表推导和生成器表达式通常情况下是过滤数据最简单的方式。
# 其实它们还能在过滤的时候转换数据。比如：
mylist = [1, 4, -5, 10, -7, 2, 3, -1]
import math
list1 = [math.sqrt(n) for n in mylist if n > 0]
print(list1)

# 过滤操作的一个变种就是将不符合条件的值用新的值代替，而不是丢弃它们。
# 比如，在一列数据中你可能不仅想找到正数，而且还想将不是正数的数替换成指定的数。
# 通过将过滤条件放到条件表达式中去，可以很容易的解决这个问题，就像这样：
clip_neg = [n if n > 0 else 0 for n in mylist]
print(clip_neg)
clip_pos = [n if n < 0 else 0 for n in mylist]
print(clip_pos)
