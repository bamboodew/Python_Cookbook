'''
Created on 2018年7月8日

@author: Administrator
'''
# 问题：
# 现在有多个字典或者映射，你想将它们从逻辑上合并为一个单一的映射后执行某些操作，
# 比如查找值或者检查某些键是否存在。

# 解决方案
# 假如你有如下两个字典:
a = {'x':1, 'z':3}
b = {'y':2, 'z':4}
# 现在假设你必须在两个字典中执行查找操作（比如先从 a 中找，如果找不到再在 b
# 中找）。一个非常简单的解决方案就是使用 collections 模块中的 ChainMap 类。比如：

from collections import ChainMap
c = ChainMap(a, b)
print(c['x'])
print(c['y'])
print(c['z'])
print()
# 讨论
# 一个 ChainMap 接受多个字典并将它们在逻辑上变为一个字典。然后，这些字典并
# 不是真的合并在一起了，ChainMap 类只是在内部创建了一个容纳这些字典的列表并重
# 新定义了一些常见的字典操作来遍历这个列表。大部分字典操作都是可以正常使用的，
# 比如：
print(len(c))
print(list(c.keys()))
print(list(c.values()))

# 如果出现重复键，那么第一次出现的映射值会被返回。因此，例子程序中的 c['z']
# 总是会返回字典 a 中对应的值，而不是 b 中对应的值。
# 对于字典的更新或删除操作总是影响的是列表中第一个字典。比如：
c['z'] = 10
c['w'] = 40
del c['x']
print(a)
# del c['y']

# ChainMap 对于编程语言中的作用范围变量（比如 globals , locals 等）是非常有
# 用的。事实上，有一些方法可以使它变得简单：
values = ChainMap()
values['x'] = 1
values = values.new_child()
values['x'] = 2
values = values.new_child()
values['x'] = 3
print(values)
print(values['x'])
values = values.parents  # Discard last mapping
print(values['x'])
values = values.parents
print(values['x'])
print(values)
