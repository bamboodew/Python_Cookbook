'''
Created on 2018年3月23日
你有一段通过下标访问列表或者元组中元素的代码，
但是这样有时候会使得你的代码难以阅读，于是你想通过名称来访问元素。
@author: Administrator
'''
# _replace() 方法还有一个很有用的特性，
# 就是当你的命名元组拥有可选或者缺失字段时候，
# 它是一个非常方便的填充数据的方法。
# 你可以先创建一个包含缺省值的原型元组，
# 然后使用 _replace() 方法创建新的值被更新过的实例。比如：
from collections import namedtuple
Stock = namedtuple('Stock', ['name', 'shares', 'price', 'date', 'time'])

stock_prototype = Stock('', 0, 0.0, None, None)
def dict_to_stock(s):
    return stock_prototype._replace(**s)
# 下面是它的使用方法:
a = {'name': 'ACME', 'shares': 100, 'price': 123.45}
print(dict_to_stock(a))
b = {'name': 'ACME', 'shares': 100, 'price': 123.45, 'date': '12/17/2012'}
print(dict_to_stock(b))

# 最后要说的是，如果你的目标是定义一个需要更新很多实例属性的高效数据结构，
# 那么命名元组并不是你的最佳选择。
# 这时候你应该考虑定义一个包含 __slots__ 方法的类（参考 8.4 小节）。
