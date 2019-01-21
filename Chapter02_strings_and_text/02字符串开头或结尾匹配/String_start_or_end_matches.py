'''
Created on 2018年7月18日

@author: Administrator
'''
# 问题
# 你需要通过指定的【文本模式】去检查字符串的开头或者结尾，比如文件名后缀，URL
# Scheme 等等。
# 解决方案
# 检查字符串开头或结尾的一个简单方法是使用 str.startswith() 或者是 str.
# endswith() 方法。比如：
filename = 'spam.txt'
print(filename.endswith('.txt'))
print(filename.startswith('file:'))

url = 'http://www.python.org'
print(url.startswith('http:'))

# 如果你想检查多种匹配可能，只需要将所有的匹配项放入到一个元组中去，然后传
# 给 startswith() 或者 endswith() 方法：
import os
filenames = os.listdir('.')  # 当前文件夹下的所有文件的文件名
print(filenames)
print([name for name in filenames if name.endswith(('.c', '.py'))])
print(any(name.endswith('.py') for name in filenames))
