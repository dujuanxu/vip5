# 练习：
# 1. 分别定义一个集合和字典
s = {1,2,3}
d = {'a':4, 'b':5, 'c':6}
print(s)
print(d)

# 2. 为集合和字典分别插入元素：55
s.add(55)
print(s)

d['d'] = 55
print(d)

# 3.分别删除集合和字典内的一个元素
s.remove(55)
print(s)

del d['d']
print(d)
# 4.取出除字典内所有值和集合组成一个列表
l = []
l.extend(list(d.values()))
l.extend(list(d.keys()))
print(l)

# 5.集合和字典的区别