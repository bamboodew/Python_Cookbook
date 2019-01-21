'''
Created on 2018年3月9日
怎样从一个集合中获得最大或者最小的 N 个元素列表？
@author: Administrator
'''

# heapq模块有两个函数：nlargest()和 nsmallest()，可以完美解决这个问题。
import heapq
nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
print('最大的3个数是', heapq.nlargest(3, nums))
print('最小的3个数是', heapq.nsmallest(3, nums))

# 两个函数都能接受一个关键字参数，用于更复杂的数据结构中：
portfolio = [
            {'name': 'IBM', 'shares': 100, 'price': 91.1},
            {'name': 'AAPL', 'shares': 50, 'price': 543.22},
            {'name': 'FB', 'shares': 200, 'price': 21.09},
            {'name': 'HPQ', 'shares': 35, 'price': 31.75},
            {'name': 'YHOO', 'shares': 45, 'price': 16.35},
            {'name': 'ACME', 'shares': 75, 'price': 115.65}
            ]
cheap = heapq.nlargest(3, portfolio, key=lambda s:s['price'])
expensive = heapq.nsmallest(3, portfolio, key=lambda s:s['price'])
# 上面代码在对每个元素进行对比的时候，会以 price 的值进行比较。
print('最便宜的3家:')
for i in cheap:
    print(i.get('name'))

print('最贵的3家:', expensive[0].get('name'), expensive[1].get('name'), expensive[2].get('name'),)