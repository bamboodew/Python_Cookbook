'''
Created on 2018年3月12日
怎样在一个序列上面保持元素顺序的同时消除重复的值?
@author: Administrator
'''


# 如果序列上的值都是 hashable 类型，
# 那么可以很简单的利用集合或者生成器来解决这个问题。比如：
def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)


a = [1, 5, 2, 1, 9, 1, 5, 10]
print(list(dedupe(a)))
