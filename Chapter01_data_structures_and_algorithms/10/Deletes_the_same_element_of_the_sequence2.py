'''
Created on 2018年3月12日
怎样在一个序列上面保持元素顺序的同时消除重复的值?
@author: Administrator
'''


# 这个方法仅仅在序列中元素为 hashable 的时候才管用。
# 如果你想消除元素不可哈希（比如 dict 类型）的序列中重复元素的话，
# 你需要将上述代码稍微改变一下，就像这样：
def dedupe(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)

# 这里的 key 参数指定了一个函数，将序列元素转换成 hashable 类型。
# 下面是它的用法示例：
a = [ {'x':1, 'y':2}, {'x':1, 'y':3}, {'x':1, 'y':2}, {'x':2, 'y':4}]
print(list(dedupe(a, key=lambda d:(d['x'], d['y']))))
print(list(dedupe(a, key=lambda d:(d['x']))))
print(list(dedupe(a, key=lambda d:(d['y']))))
# 如果你想基于单个字段、属性或者某个更大的数据结构来消除重复元素，此方案同样可以胜任。