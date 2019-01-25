'''
Created on 2018年7月10日
将列表当作队列使用
也可以把列表当做队列用，只是在队列里第一加入的元素，第一个取出来；但是拿列表用作这样的目的效率不高。在列表的最后添加或者弹出元素速度快，然而在列表里插入或者从头部弹出速度却不快（因为所有其他的元素都得一个一个地移动）。
@author: Administrator
'''
from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry") # 队列增加元素
queue.append("Graham") # 队列增加元素
print(queue) 
print(queue.popleft()) # 移除列表中的左侧一个元素，且返回该元素的值
print(queue)
print(queue.popleft())
print(queue)