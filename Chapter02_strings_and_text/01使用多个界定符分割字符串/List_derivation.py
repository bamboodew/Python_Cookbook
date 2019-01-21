'''
Created on 2018年7月10日
列表推导式提供了从序列创建列表的简单途径。通常应用程序将一些操作应用于某个序列的每个元素，用其获得的结果作为生成新列表的元素，或者根据确定的判定条件创建子序列。

每个列表推导式都在 for 之后跟一个表达式，然后有零到多个 for 或 if 子句。返回结果是一个根据表达从其后的 for 和 if 上下文环境中生成出来的列表。如果希望表达式推导出一个元组，就必须使用括号。

这里我们将列表中每个数值乘三，获得一个新的列表：
@author: Administrator
'''
vec = [2, 4, 6]
print([3 * x for x in vec])
print([[x, x ** 2] for x in vec])

freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
print([weapon.strip() for weapon in freshfruit])

print([3 * x for x in vec if x > 3])

vec2 = [4, 3, -9]
print([x*y for x in vec for y in vec2])
print([x+y for x in vec for y in vec2])
print([vec[i]*vec2[i] for i in range(len(vec))])

print([str(round(355/113, i)) for i in range(1, 6)])

