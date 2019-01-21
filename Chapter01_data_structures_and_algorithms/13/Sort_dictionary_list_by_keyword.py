'''
Created on 2018年3月19日
你有一个字典列表，你想根据某个或某几个字典字段来排序这个列表。
@author: Administrator
'''
# 通过使用 operator 模块的 itemgetter 函数，可以非常容易的排序这样的数据结构。

# 假设你从数据库中检索出来网站会员信息列表，并且以下列的数据结构返回：
rows = [
        {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
        {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
        {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
        {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
        ]
# 根据任意的字典字段来排序输入结果行是很容易实现的，代码示例：
from operator import itemgetter
rows_by_fname = sorted(rows, key=itemgetter('fname'))
rows_by_uid = sorted(rows, key=itemgetter('uid'))
print(rows_by_fname)
print(rows_by_uid)

# itemgetter() 函数也支持多个 keys，比如下面的代码
rows_by_lfname = sorted(rows, key=itemgetter('lname', 'fname'))
print(rows_by_lfname)

# 在上面例子中，rows 被传递给接受一个关键字参数的 sorted() 内置函数。
# 这个参数是 callable 类型，并且从 rows 中接受一个单一元素，然后返回被用来排序的值。
# itemgetter() 函数就是负责创建这个 callable 对象的。