'''
Created on 2018年7月10日
几乎所有有用的程序都会涉及到某些文本处理，不管是解析数据还是产生输出。
这一章将重点关注文本的操作处理，比如提取字符串，搜索，替换以及解析等。
大部分的问题都能简单的调用字符串的内建方法完成。
但是，一些更为复杂的操作可能需要正则表达式或者强大的解析器，
所有这些主题我们都会详细讲解。
并且在操作 Unicode 时候碰到的一些棘手的问题在这里也会被提及到。
@author: Administrator
'''
# 问题：
# 你需要将一个字符串分割为多个字段，但是分隔符 (还有周围的空格) 并不是固定的。
# 解决方案：
# string 对象的 split() 方法只适应于非常简单的字符串分割情形，它并不允许有
# 多个分隔符或者是分隔符周围不确定的空格。当你需要更加灵活的切割字符串的时候，
# 最好使用 re.split() 方法：
line = 'asdf fjdk;  afed, fjek,asdf, foo'
import re
l = re.split(r'[;,\s]\s', line)
print(l)

field = re.split(r'(;|,|\s)\s*', line)
print(field)