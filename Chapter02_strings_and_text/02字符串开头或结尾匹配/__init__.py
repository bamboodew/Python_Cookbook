# data structure

# 列表的方法
a = [66.25, 333, 333, 1, 1234.5]
print(a.count(333))  # list.count(x)：返回x在列表中出现的次数。
a.insert(2, -1)  # 在指定位置插入一个元素。第一个参数是准备插入到其前面的那个元素的索引
print(a)
a.append(222)
print(a)
print(a.index(333))
a.remove(333)
print(a)
a.reverse()  # 倒排列表中的元素
print(a)
a.sort()  # 对列表中的元素进行排序
print(a)
