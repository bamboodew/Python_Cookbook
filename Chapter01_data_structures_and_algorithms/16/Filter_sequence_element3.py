'''
Created on 2018年3月20日
你有一个数据序列，想利用一些规则从中提取出需要的值或者是缩短序列
@author: Administrator
'''
# 另外一个值得关注的过滤工具就是 itertools.compress() ，
# 它以一个 iterable对象和一个相对应的 Boolean 选择器序列作为输入参数。
# 然后输出 iterable 对象中对应选择器为 True 的元素。
# 当你需要用另外一个相关联的序列来过滤某个序列的时候，
# 这个函数是非常有用的。比如，假如现在你有下面两列数据：
addresses = [
            '5412 N CLARK',
            '5148 N CLARK',
            '5800 E 58TH',
            '2122 N CLARK',
            '5645 N RAVENSWOOD',
            '1060 W ADDISON',
            '4801 N BROADWAY',
            '1039 W GRANVILLE',
            ]
counts = [ 0, 3, 10, 4, 1, 7, 6, 1]
# 现在你想将那些对应 count 值大于 5 的地址全部输出，那么你可以这样做：
from itertools import compress
more5 = [n > 5 for n in counts]
print(more5)
l=list(compress(addresses, more5))
for n in l:
    print(n)
# 这里的关键点在于先创建一个 Boolean 序列，指示哪些元素符合条件。
# 然后compress() 函数根据这个序列去选择输出对应位置为 True 的元素。
# 和 filter() 函数类似，compress() 也是返回的一个迭代器。
# 因此，如果你需要得到一个列表，那么你需要使用 list() 来将结果转换为列表类型。