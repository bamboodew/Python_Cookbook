'''
Created on 2018年3月9日
怎样从一个集合中获得最大或者最小的 N 个元素列表？
@author: Administrator
'''

# 如果你想在一个集合中查找最小或最大的 N 个元素，并且 N 小于集合元素数量，
# 那么这些函数提供了很好的性能。因为在底层实现里面，首先会先将集合数据进行堆排
# 序后放入一个列表中：
import heapq
nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
heap=list(nums) # 将【列表】转换为【堆】
heapq.heapify(heap)
print(heap)
print(heapq.heappop(heap))
print(heapq.heappop(heap))
print(heapq.heappop(heap))