'''
Created on 2018年3月19日
你有一个字典或者实例的序列，然后你想根据某个特定的字段比如 date 来分组迭代访问。
@author: Administrator
'''
# itertools.groupby() 函数对于这样的数据分组操作非常实用。
from collections import defaultdict

# 为了演示，假设你已经有了下列的字典列表：
rows = [
        {'address': '5412 N CLARK', 'date': '07/01/2012'},
        {'address': '5148 N CLARK', 'date': '07/04/2012'},
        {'address': '5800 E 58TH', 'date': '07/02/2012'},
        {'address': '2122 N CLARK', 'date': '07/03/2012'},
        {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
        {'address': '1060 W ADDISON', 'date': '07/02/2012'},
        {'address': '4801 N BROADWAY', 'date': '07/01/2012'},
        {'address': '1039 W GRANVILLE', 'date': '07/04/2012'},
        ]

# 如果你仅仅只是想根据 date 字段将数据分组到一个大的数据结构中去，
# 并且允许随机访问，那么你最好使用 defaultdict() 来构建一个多值字典，
# 关于多值字典已经在 1.6 小节有过详细的介绍。比如：

rows_by_date = defaultdict(list)
for row in rows:
    rows_by_date[row['date']].append(row)

print(rows_by_date)
print()
for r in rows_by_date['07/01/2012']:
    print(r)

# 在上面这个例子中，我们没有必要先将记录排序。
# 因此，如果对内存占用不是很关心，这种方式会比先排序然后再通过 groupby() 函数迭代的方式运行得快一些。
