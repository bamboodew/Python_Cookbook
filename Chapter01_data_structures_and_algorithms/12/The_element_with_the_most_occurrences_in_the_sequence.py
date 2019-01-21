'''
Created on 2018年3月18日
怎样找出一个序列中出现次数最多的元素呢？
@author: Administrator
'''
# collections.Counter 类就是专门为这类问题而设计的，
# 它甚至有一个有用的most_common() 方法直接给了你答案。
# 为了演示，先假设你有一个单词列表并且想找出哪个单词出现频率最高。
# 你可以这样做：
words = ['look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
         'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
         'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
         'my', 'eyes', "you're", 'under'
        ]
from collections import Counter
word_counts = Counter(words)
# 出现频率最高的 3个单词
top_three = word_counts.most_common(3)
print(top_three)

# 作为输入，Counter 对象可以接受任意的由可哈希（hashable）元素构成的【序列】对象。
# 在底层实现上，一个 Counter 对象就是一个字典，将元素映射到它出现的次数上。比如：
print('not出现的次数：', word_counts['not'])
print('eyes出现的次数：', word_counts['eyes'])

# 如果你想手动增加计数，可以简单的用加法：
morewords = ['why', 'are', 'you', 'not', 'looking', 'in', 'my', 'eyes']
for word in morewords:
    word_counts[word] += 1
print('eyes的最新累积出现次数是：', word_counts['eyes'])
print('not的最新累积出现次数是：', word_counts['not'])

# 或者你可以使用 update() 方法：
word_counts.update(morewords)
print('eyes的最新累积出现次数是：', word_counts['eyes'])
print('not的最新累积出现次数是：', word_counts['not'])

