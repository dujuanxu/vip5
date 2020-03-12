#
# # 求10阶乘
# h = 1
# i = 1
# while i <= 10:
#     h *= i
#     i += 1
#
# print(h)
# # 求100以内能被3整除的数，并将作为列表输出
# l = []
# i = 3
# while i < 100:
#     if i % 3 == 0:
#         l.append(i)
#     i += 1
# print(l)
#
# # 列表[1,2,3,4,3,4,2,5,5,8,9,7],将此列表去重，得到一个唯一元素的列表
# l_new = []
# l = [1,2,3,4,3,4,2,5,5,8,9,7]
# for i in l:
#    if l[i] not in l_new:
#        l_new.append(l[i])
# print(l_new)

# 求斐波那契数列 1 1 2 3 5 8 13 ……

# 求100以内的质数（只能被1和它本身整除）
# i = 2
# while i < 100:
#     j = 2
#     while j < i:
#         if i % j == 0:
#             break
#         j += 1
#     if j == i:
#         print(i)
#     i += 1
#
# # 计算1+2+3+4……+100的和
# sum = 0
#
# i = 1
# while i <= 100:
#     sum += i
#     i += 1
#
# print('1+2+...+100的和是{}'.format(sum))
#

# 出100以内偶数中能整除3的所有数字
# l = [i for i in range(1,100) if i%3==0]

# ###上课示例
# example4 = [[1,2,3],[4,5,6],[7,8,9],[10]]
# exmaple5 = [j**2 for i in example4 if len(i)>1 for j in i if j%2 == 0]
# print(exmaple5)
#
# #上面推导式的等价代码
# exmaple6 = []
# for i in example4:
#     if len(i) > 1:
#         for j in i:
#             if j%2 == 0:
#                 exmaple6.append(j**2)
# print(exmaple6)

