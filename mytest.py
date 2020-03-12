# 练习：定义一个1-9的元组，1、输出倒数第3个元素；
s = (1, 2, 3, 4, 5, 6, 7, 8, 9)
print('倒数第3个是{}'.format(s[-3]))

# 2、输出值468
print(s[3:8:2])

# 思考：如何定义1-999的元组？
s = tuple(range(1, 999 + 1))
print(s)
print(s[-1])

# 思考：如何定义1-999中偶数组成的元组,？
s = tuple(range(2, 1000, 2))
print(s)
print(s[-1])

# 练习：列表[11,13,5,7,0,56,23,34,72]，
#  求该列表中的最大值，最小值及列表中一共有几个元素
l = [11, 13, 5, 7, 0, 56, 23, 34, 72]
print('列表:', l)
print('最大值:{}, 最小值：{}， 一共{}个元素'.format(max(l), min(l), len(l)))

# 获取56元素在列表的位置
pos = l.index(56)
print('元素56在列表位置是：{}'.format(pos))

# 追加元素7
l.append(7)
print(l)
# 删除元素0
l.remove(0)
print(l)

# 排序列表（由大到小）
l.sort()
print(l)

# 将列表[66,67,68]与原列表组合
l_new = [66, 67, 68]
l.extend(l_new)
print(l)



