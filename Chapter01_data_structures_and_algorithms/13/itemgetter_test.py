'''
Created on 2018年3月19日

@author: Administrator
'''
# operator.itemgetter() 函数有一个被 rows 中的记录用来查找值的索引参数。
# 可以是一个字典键名称，一个整形值或者任何能够传入一个对象的 __getitem__() 方法的值。
# 如果你传入多个索引参数给 itemgetter() ，
# 它生成的 callable 对象会返回一个包含所有元素值的元组，
# 并且 sorted() 函数会根据这个元组中元素顺序去排序。
# 但你想要同时在几个字段上面进行排序（比如通过姓和名来排序，也就是例子中的那样）的时候这种方法是很有用的。
from _operator import itemgetter
rows = [
        {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
        {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
        {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
        {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
        ]
# itemgetter() 有时候也可以用 lambda 表达式代替，比如：
rows_by_fname = sorted(rows, key=lambda r:r['fname'])
rows_by_lfname = sorted(rows, key=lambda r:(r['lname'], r['fname']))
print(rows_by_fname)
print(rows_by_lfname)

# 这种方案也不错。但是，使用 itemgetter() 方式会运行的稍微快点。
# 因此，如果你对性能要求比较高的话就使用 itemgetter() 方式。

# 最后，不要忘了这节中展示的技术也同样适用于 min() 和 max() 等函数。比如：
print(min(rows, key=itemgetter('uid')))
print(max(rows, key=itemgetter('uid')))
