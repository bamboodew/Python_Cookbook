'''
Created on 2018年7月8日

@author: Administrator
'''

from collections import ChainMap

# 作为 ChainMap 的替代，你可能会考虑使用 update() 方法将两个字典合并。比如：
a = {'x': 1, 'z': 3 }
b = {'y': 2, 'z': 4 }
merged = dict(b)
merged.update(a)
print(merged['x'])
print(merged['y'])
print(merged['z'])

# 这样也能行得通，但是它需要你创建一个完全不同的字典对象（或者是破坏现有
# 字典结构）。同时，如果原字典做了更新，这种改变不会反应到新的合并字典中去。比如：
a['x'] = 13
print(merged['x'])

# ChainMap 使用原来的字典，它自己不创建新的字典。所以它并不会产生上面所说
# 的结果，比如：
merged1 = ChainMap(a, b)
print(merged1['x'])
a['x'] = 42
print(merged1['x'])  # Notice change to merged dicts
